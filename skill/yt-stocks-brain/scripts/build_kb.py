"""Build kb/brain.db — a SQLite knowledge base over every brief, rebuilt from scratch on each
generate.py run (called from build_index). Deterministic: same inputs, same db.

Layers:
  research-data/*/*.json   briefs (source of truth, one per video)
  kb/entities.json         permanent entity + speaker identities (entities.Registry)
  kb/claim_outcomes.json   curated claim verdicts, keyed by claim_id
  kb/brain.db              this derived query layer (gitignored, disposable)

Stable ids: brief_id = YouTube video id; claim_id = brief_id + hash(who + claim). Entity keys
come from the registry and never change, so curated state never orphans on a rebuild.

    sqlite3 kb/brain.db "select * from entity_timeline where entity_key='nvidia'"
"""
import calendar
import datetime as dt
import hashlib
import json
import os
import re
import sqlite3

DB_PATH = os.path.join("kb", "brain.db")
OUTCOMES_PATH = os.path.join("kb", "claim_outcomes.json")

SCHEMA = """
CREATE TABLE briefs (id TEXT PRIMARY KEY, slug TEXT, title TEXT, channel TEXT, date TEXT,
                     category TEXT, speakers TEXT, thread_line TEXT, html TEXT, video_url TEXT,
                     schema_version INTEGER);
CREATE TABLE entities (key TEXT PRIMARY KEY, name TEXT, ticker TEXT, kind TEXT);
CREATE TABLE entity_aliases (alias TEXT PRIMARY KEY, key TEXT);
CREATE TABLE themes (brief_id TEXT, theme_id TEXT, title TEXT, color TEXT, badge TEXT,
                     status TEXT, lead TEXT);
CREATE TABLE theme_tags (brief_id TEXT, theme_id TEXT, tag TEXT);
CREATE TABLE mentions (brief_id TEXT, theme_id TEXT, entity_key TEXT, stance TEXT,
                       conviction TEXT, horizon TEXT, blurb TEXT, raw TEXT);
CREATE TABLE claims (claim_id TEXT PRIMARY KEY, brief_id TEXT, who TEXT, who_note TEXT,
                     claim TEXT, metric TEXT, target TEXT, by_when TEXT, due_date TEXT,
                     condition TEXT, entity_raw TEXT,
                     status TEXT, resolved_on TEXT, evidence TEXT);
CREATE TABLE claim_entities (claim_id TEXT, entity_key TEXT);
CREATE TABLE claim_speakers (claim_id TEXT, entity_key TEXT);
CREATE TABLE relations (brief_id TEXT, src_key TEXT, rel TEXT, dst_key TEXT, note TEXT,
                        src_raw TEXT, dst_raw TEXT);
CREATE TABLE takes (brief_id TEXT, take TEXT, cite TEXT);
CREATE INDEX mentions_entity ON mentions(entity_key);
CREATE INDEX claim_entities_key ON claim_entities(entity_key);
CREATE INDEX claim_speakers_key ON claim_speakers(entity_key);

-- every stance on an entity over time, newest first
CREATE VIEW entity_timeline AS
  SELECT m.entity_key, e.name, e.ticker, e.kind, b.date, b.channel, b.title, m.stance,
         m.conviction, m.horizon, m.blurb, b.id AS brief_id
  FROM mentions m JOIN entities e ON e.key = m.entity_key JOIN briefs b ON b.id = m.brief_id
  ORDER BY b.date DESC;

-- entity pairs named in the same brief, with how many briefs they share
CREATE VIEW co_mentions AS
  SELECT a.entity_key AS a, b.entity_key AS b, COUNT(DISTINCT a.brief_id) AS briefs
  FROM (SELECT DISTINCT brief_id, entity_key FROM mentions) a
  JOIN (SELECT DISTINCT brief_id, entity_key FROM mentions) b
    ON a.brief_id = b.brief_id AND a.entity_key < b.entity_key
  GROUP BY a.entity_key, b.entity_key;

-- every claim per speaker with its deadline and verdict (track-record base)
CREATE VIEW speaker_claims AS
  SELECT s.entity_key AS speaker_key, e.name AS speaker, c.claim_id, b.date, c.claim,
         c.target, c.due_date, COALESCE(c.status, 'open') AS status, c.brief_id
  FROM claim_speakers s JOIN claims c ON c.claim_id = s.claim_id
  JOIN entities e ON e.key = s.entity_key JOIN briefs b ON b.id = c.brief_id;
"""

_VIDEO_ID = re.compile(r"(?:v=|youtu\.be/|shorts/|embed/)([\w-]{11})")
_MONTHS = {m.lower(): i for i, m in enumerate(calendar.month_name) if m}
_MONTHS.update({m.lower(): i for i, m in enumerate(calendar.month_abbr) if m})
_UNIT = r"(day|week|month|quarter|year|decade)s?"
_WORDNUM = {"a": 1, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "ten": 10,
            "few": 3, "a few": 3, "couple": 2, "a couple": 2, "couple of": 2, "a couple of": 2,
            "several": 3, "next": 1}


def video_id(url, fallback):
    m = _VIDEO_ID.search(url or "")
    return m.group(1) if m else fallback


def claim_id(brief_id, who, claim):
    return f"{brief_id}-{hashlib.sha1(f'{who}|{claim}'.encode()).hexdigest()[:8]}"


def _eom(y, m):
    return dt.date(y, m, calendar.monthrange(y, m)[1])


def _add(base, n, unit):
    if unit == "day":
        return base + dt.timedelta(days=round(n))
    if unit == "week":
        return base + dt.timedelta(weeks=n)
    months = round(n * {"month": 1, "quarter": 3, "year": 12, "decade": 120}[unit])
    y, m = divmod(base.month - 1 + months, 12)
    return _eom(base.year + y, m + 1)


def due_date(by, brief_date):
    """Free-text `by` ('2026-12', 'Q3 2027', 'end of 2026', '12-18 months', 'next few weeks',
    '~2046') -> ISO deadline (end of the stated period), or None if unparseable."""
    if not by:
        return None
    s = by.lower().replace("–", "-")
    try:
        base = dt.date.fromisoformat(brief_date)
    except (TypeError, ValueError):
        base = None
    if base:  # relative spans first: "next 6 months from mid-July 2026" is about the span
        m = re.search(r"(\d+(?:\.\d+)?)\s*(?:-|to)\s*(\d+(?:\.\d+)?)\s*" + _UNIT, s) \
            or re.search(r"(\d+(?:\.\d+)?)()\s*\+?\s*" + _UNIT, s)
        if m:
            return _add(base, float(m.group(2) or m.group(1)), m.group(3)).isoformat()
        m = re.search(r"\b(a few|few|a couple of|couple of|a couple|couple|several|a|one|two|three|four|five|six|ten|next)\s+" + _UNIT, s)
        if m:
            return _add(base, _WORDNUM[m.group(1)], m.group(2)).isoformat()
        if re.search(r"\bthis year\b|\byear[- ]end\b|\bend of (the )?year\b", s):
            return dt.date(base.year, 12, 31).isoformat()
        if re.search(r"\bend of (the )?decade\b", s):
            return dt.date(base.year // 10 * 10 + 9, 12, 31).isoformat()
    m = re.search(r"\b20\d\d\s*-\s*(20\d\d)\b", s)  # year range: deadline is the later year
    if m:
        return dt.date(int(m.group(1)), 12, 31).isoformat()
    m = re.search(r"\b(20\d\d)-(\d\d)-(\d\d)\b", s)
    if m:
        return dt.date(*map(int, m.groups())).isoformat()
    m = re.search(r"\b(20\d\d)-(\d\d)\b", s)
    if m and 1 <= int(m.group(2)) <= 12:
        return _eom(int(m.group(1)), int(m.group(2))).isoformat()
    m = re.search(r"\bq([1-4])\s*(?:of\s*)?'?(20\d\d)\b", s) or re.search(r"\b(20\d\d)\s*q([1-4])\b", s)
    if m:
        q, y = (m.group(1), m.group(2)) if len(m.group(1)) == 1 else (m.group(2), m.group(1))
        return _eom(int(y), int(q) * 3).isoformat()
    m = re.search(r"\bh([12])\s*(20\d\d)\b", s)
    if m:
        return _eom(int(m.group(2)), 6 * int(m.group(1))).isoformat()
    m = re.search(r"\b([a-z]{3,9})\.?\s+(20\d\d)\b", s)
    if m and m.group(1) in _MONTHS:
        return _eom(int(m.group(2)), _MONTHS[m.group(1)]).isoformat()
    m = re.search(r"\b(20\d\d)s\b", s)
    if m:
        return dt.date(int(m.group(1)) + 9, 12, 31).isoformat()
    m = re.search(r"(early|mid|summer|spring|fall|autumn)?[\s-]*(?:of\s+)?(20\d\d)\b", s)
    if m:
        month = {"early": 3, "spring": 5, "mid": 6, "summer": 8, "fall": 11, "autumn": 11}.get(m.group(1), 12)
        return _eom(int(m.group(2)), month).isoformat()
    return None


def build(briefs, reg, path=DB_PATH):
    """briefs: generate.py brief dicts (entities carry registry "key", source JSON in "_raw").
    reg: the entities.Registry used for the index. Returns warning strings."""
    warnings = []
    try:
        outcomes = json.load(open(OUTCOMES_PATH, encoding="utf-8"))
    except FileNotFoundError:
        outcomes = {}
    outcomes = {k: v for k, v in outcomes.items() if not k.startswith("_")}

    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    if os.path.exists(tmp):
        os.remove(tmp)
    db = sqlite3.connect(tmp)
    db.executescript(SCHEMA)
    seen_claims, seen_briefs = set(), set()
    n_by = n_due = 0

    for b in briefs:
        d = b["_raw"]
        meta = d.get("meta") or {}
        slug = os.path.splitext(b["html"])[0]
        bid = video_id(meta.get("video_url"), slug)
        if bid in seen_briefs:
            warnings.append(f"two briefs share video id {bid} (second: {slug}) — duplicate brief?")
            bid = slug
        seen_briefs.add(bid)
        db.execute("INSERT INTO briefs VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                   (bid, slug, b["title"], b["channel"], b["date"], b["category"], b["speakers"],
                    b["thread_line"], b["html"], meta.get("video_url"), d.get("schema_version", 1)))
        for t in d.get("themes") or []:
            db.execute("INSERT INTO themes VALUES (?,?,?,?,?,?,?)",
                       (bid, t.get("id"), t.get("title"), t.get("color"), t.get("badge"),
                        t.get("status"), t.get("lead")))
            db.executemany("INSERT INTO theme_tags VALUES (?,?,?)",
                           [(bid, t.get("id"), tag) for tag in t.get("tags") or []])
        db.executemany("INSERT INTO mentions VALUES (?,?,?,?,?,?,?,?)",
                       [(bid, e.get("theme_id"), e["key"], e["stance_label"], e["conviction"],
                         e.get("horizon"), e.get("blurb"), e["raw"]) for e in b["entities"]])
        for c in d.get("claims") or []:
            cid = claim_id(bid, c.get("who"), c.get("claim"))
            while cid in seen_claims:
                cid += "+"
            seen_claims.add(cid)
            due = due_date(c.get("by"), b["date"])
            n_by += bool(c.get("by"))
            n_due += bool(due)
            speakers, note = reg.resolve_who(c.get("who"), b["speakers"], b["channel"])
            o = outcomes.get(cid) or {}
            db.execute("INSERT INTO claims VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                       (cid, bid, c.get("who"), note, c.get("claim"), c.get("metric"),
                        c.get("target"), c.get("by"), due, c.get("condition"), c.get("entity"),
                        o.get("status"), o.get("resolved_on"), o.get("evidence")))
            db.executemany("INSERT INTO claim_entities VALUES (?,?)",
                           [(cid, k) for k in dict.fromkeys(reg.resolve_list(c.get("entity")))])
            db.executemany("INSERT INTO claim_speakers VALUES (?,?)",
                           [(cid, k) for k in dict.fromkeys(speakers)])
        for r in d.get("relations") or []:
            for src in reg.resolve_list(r.get("from")):
                for dst in reg.resolve_list(r.get("to")):
                    db.execute("INSERT INTO relations VALUES (?,?,?,?,?,?,?)",
                               (bid, src, r.get("rel"), dst, r.get("note"), r.get("from"), r.get("to")))
        db.executemany("INSERT INTO takes VALUES (?,?,?)",
                       [(bid, h.get("take"), h.get("cite")) for h in d.get("hot_takes") or []])

    db.executemany("INSERT INTO entities VALUES (?,?,?,?)",
                   [(k, e["name"], e.get("ticker"), e.get("kind")) for k, e in sorted(reg.ents.items())])
    db.executemany("INSERT OR IGNORE INTO entity_aliases VALUES (?,?)", sorted(reg.alias.items()))
    db.commit()
    db.close()
    os.replace(tmp, path)

    orphans = sorted(set(outcomes) - seen_claims)
    if orphans:
        warnings.append(f"{len(orphans)} claim ids in {OUTCOMES_PATH} match no claim: {', '.join(orphans[:5])}")
    if n_by and n_due / n_by < 0.9:
        warnings.append(f"only {n_due}/{n_by} claim deadlines ('by') parse to a date — prefer ISO (YYYY-MM-DD / YYYY-MM)")
    return warnings


def _selftest():
    b = "2026-07-15"
    cases = {"2026-12": "2026-12-31", "2026-11 midterms": "2026-11-30", "Q3 2027": "2027-09-30",
             "end of 2026": "2026-12-31", "2030": "2030-12-31", "~2046": "2046-12-31",
             "12-18 months": "2028-01-31", "next 6 months from mid-July 2026": "2027-01-31",
             "next few weeks": "2026-08-05", "September 2026": "2026-09-30", "mid-2027": "2027-06-30",
             "2030s": "2039-12-31", "2030-2032": "2032-12-31", "by 2026-10-30": "2026-10-30", "short order": None, None: None}
    for by, want in cases.items():
        got = due_date(by, b)
        assert got == want, (by, got, want)
    assert video_id("https://youtu.be/ZB0aHLmSdB0?si=x", "s") == "ZB0aHLmSdB0"
    assert video_id(None, "slug") == "slug"
    print("build_kb selftest ok")


if __name__ == "__main__":
    _selftest()
