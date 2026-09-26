#!/usr/bin/env python3
"""Fallback transcript fetch when yt-dlp is missing or rate-limited (HTTP 429).
Usage: fetch_transcript_api.py VIDEO_ID_OR_URL [lang]   -> writes VIDEO_ID.<lang>.srt in cwd
Then run clean_transcript.py on it as usual. Needs: pip install youtube-transcript-api"""
import re, sys
from youtube_transcript_api import YouTubeTranscriptApi

arg, lang = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else "en")
vid = re.search(r"(?:v=|youtu\.be/|shorts/)([\w-]{11})", arg)
vid = vid.group(1) if vid else arg

def ts(s):
    return f"{int(s//3600):02}:{int(s%3600//60):02}:{int(s%60):02},{int(s%1*1000):03}"

segs = YouTubeTranscriptApi().fetch(vid, languages=[lang])
with open(f"{vid}.{lang}.srt", "w") as f:
    f.write("\n".join(f"{i}\n{ts(s.start)} --> {ts(s.start+s.duration)}\n{s.text}\n"
                      for i, s in enumerate(segs, 1)))
print(f"Wrote {vid}.{lang}.srt ({len(segs)} segments)")
