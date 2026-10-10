#!/usr/bin/env python3
"""
start.py — one call from URL to cleaned transcript.

    python3 start.py <url|video_id> [outdir]      # outdir defaults to cwd (use the scratchpad)

1. Duplicate check: exits 3 if research-data/ already holds this video id.
2. Metadata via yt-dlp --print (title|channel|date), best effort.
3. Transcript: yt-dlp auto-captions, falling back to fetch_transcript_api.py on 429 / failure.
4. Cleans to <id>.en.txt; clean_transcript.py flags sponsor-looking paragraphs and a cut-off ending.

Read the printed .txt path; nothing is deleted from it (flags are for you to skip, not removed).
"""
import glob
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.realpath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))  # skill/yt-stocks-brain/scripts -> repo root


def video_id(arg):
    m = re.search(r"(?:v=|youtu\.be/|shorts/)([\w-]{11})", arg) or re.fullmatch(r"([\w-]{11})", arg)
    if not m:
        sys.exit(f"error: no video id in {arg!r}")
    return m.group(1)


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    vid = video_id(sys.argv[1])
    out = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.getcwd()
    os.makedirs(out, exist_ok=True)

    hit = glob.glob(os.path.join(REPO, "research-data", "*", "*.json"))
    for f in hit:
        if vid in open(f, encoding="utf-8", errors="replace").read(4000):
            print(f"EXISTS: {os.path.dirname(f)}")
            sys.exit(3)

    url = f"https://www.youtube.com/watch?v={vid}"
    meta = run(["yt-dlp", "--skip-download", "--print", "%(id)s|%(title)s|%(channel)s|%(upload_date)s", url])
    print("meta:", (meta.stdout.strip() or "unavailable (yt-dlp failed; take title/channel/date from the page)"))

    srt = os.path.join(out, f"{vid}.en.srt")
    if not os.path.exists(srt):
        run(["yt-dlp", "--skip-download", "--write-auto-sub", "--sub-lang", "en", "--convert-subs", "srt",
             "--no-warnings", url, "-o", os.path.join(out, "%(id)s.%(ext)s")])
    if not os.path.exists(srt):
        print("yt-dlp captions failed (likely 429); using transcript API")
        r = run([sys.executable, os.path.join(HERE, "fetch_transcript_api.py"), vid], cwd=out)
        if not os.path.exists(srt):
            sys.exit(f"no captions: {r.stderr.strip()}\nTry the local-whisper skill.")

    r = run([sys.executable, os.path.join(HERE, "clean_transcript.py"), srt, "--stats"])
    print(r.stdout.strip())
    txt = os.path.splitext(srt)[0] + ".txt"
    print("transcript:", txt)


if __name__ == "__main__":
    main()
