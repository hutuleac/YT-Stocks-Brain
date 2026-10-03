"""Build kb/brain.db — a SQLite knowledge base over every brief, rebuilt from scratch on each
generate.py run (called from build_index). Deterministic: same research-data in, same db out.

Source of truth stays the per-brief JSON in research-data/; this db is a derived, disposable
query layer (gitignored). Entity strings in names/claims/relations all go through the same
entities.Resolver, so `entity_key` joins across every table.

    sqlite3 kb/brain.db "select * from entity_timeline where entity_key='NVDA'"
"""
import os
import sqlite3

DB_PATH = os.path.join("kb", "brain.db")

SCHEMA = """
CREATE TABLE briefs (id TEXT PRIMARY KEY, title TEXT, channel TEXT, date TEXT, category TEXT,
                     speakers TEXT, thread_line TEXT, html TEXT, video_url TEXT);
CREATE TABLE entities (key TEXT PRIMARY KEY, name TEXT, ticker TEXT);
CREATE TABLE entity_aliases (raw TEXT PRIMARY KEY, key TEXT);
CREATE TABLE themes (brief_id TEXT, theme_id TEXT, title TEXT, color TEXT, badge TEXT,
                     status TEXT, lead TEXT);
CREATE TABLE theme_tags (brief_id TEXT, theme_id TEXT, tag TEXT);
CREATE TABLE mentions (brief_id TEXT, theme_id TEXT, entity_key TEXT, stance TEXT,
                       conviction TEXT, horizon TEXT, blurb TEXT, raw TEXT);
CREATE TABLE claims (brief_id TEXT, who TEXT, claim TEXT, metric TEXT, target TEXT,
                     by_when TEXT, condition TEXT, entity_key TEXT, entity_raw TEXT);
CREATE TABLE relations (brief_id TEXT, src_key TEXT, rel TEXT, dst_key TEXT, note TEXT,
                        src_raw TEXT, dst_raw TEXT);
CREATE TABLE takes (brief_id TEXT, take TEXT, cite TEXT);
CREATE INDEX mentions_entity ON mentions(entity_key);
CREATE INDEX claims_entity ON claims(entity_key);

-- every stance on an entity over time, newest first
CREATE VIEW entity_timeline AS
  SELECT m.entity_key, e.name, e.ticker, b.date, b.channel, b.title, m.stance, m.conviction,
         m.horizon, m.blurb, b.id AS brief_id
  FROM mentions m JOIN entities e ON e.key = m.entity_key JOIN briefs b ON b.id = m.brief_id
  ORDER BY b.date DESC;

-- entity pairs named in the same brief, with how many briefs they share
CREATE VIEW co_mentions AS
  SELECT a.entity_key AS a, b.entity_key AS b, COUNT(DISTINCT a.brief_id) AS briefs
  FROM (SELECT DISTINCT brief_id, entity_key FROM mentions) a
  JOIN (SELECT DISTINCT brief_id, entity_key FROM mentions) b
    ON a.brief_id = b.brief_id AND a.entity_key < b.entity_key
  GROUP BY a.entity_key, b.entity_key;
"""


def build(briefs, resolver, path=DB_PATH):
    """briefs: generate.py brief dicts with canonicalized entities and the source JSON in "_raw"."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    if os.path.exists(tmp):
        os.remove(tmp)
    db = sqlite3.connect(tmp)
    db.executescript(SCHEMA)
    ents = {}

    def key(raw):
        c = resolver.resolve(raw)
        if not c:
            return None
        ents[c["key"]] = (c["name"], c["ticker"])
        db.execute("INSERT OR IGNORE INTO entity_aliases VALUES (?,?)", (raw.strip(), c["key"]))
        return c["key"]

    for b in briefs:
        d = b["_raw"]
        bid = os.path.splitext(b["html"])[0]
        db.execute("INSERT INTO briefs VALUES (?,?,?,?,?,?,?,?,?)",
                   (bid, b["title"], b["channel"], b["date"], b["category"], b["speakers"],
                    b["thread_line"], b["html"], (d.get("meta") or {}).get("video_url")))
        for t in d.get("themes") or []:
            db.execute("INSERT INTO themes VALUES (?,?,?,?,?,?,?)",
                       (bid, t.get("id"), t.get("title"), t.get("color"), t.get("badge"),
                        t.get("status"), t.get("lead")))
            db.executemany("INSERT INTO theme_tags VALUES (?,?,?)",
                           [(bid, t.get("id"), tag) for tag in t.get("tags") or []])
        for e in b["entities"]:
            db.execute("INSERT INTO mentions VALUES (?,?,?,?,?,?,?,?)",
                       (bid, e.get("theme_id"), key(e["raw"]), e["stance_label"], e["conviction"],
                        e.get("horizon"), e.get("blurb"), e["raw"]))
        for c in d.get("claims") or []:
            db.execute("INSERT INTO claims VALUES (?,?,?,?,?,?,?,?,?)",
                       (bid, c.get("who"), c.get("claim"), c.get("metric"), c.get("target"),
                        c.get("by"), c.get("condition"), key(c.get("entity")), c.get("entity")))
        for r in d.get("relations") or []:
            db.execute("INSERT INTO relations VALUES (?,?,?,?,?,?,?)",
                       (bid, key(r.get("from")), r.get("rel"), key(r.get("to")), r.get("note"),
                        r.get("from"), r.get("to")))
        db.executemany("INSERT INTO takes VALUES (?,?,?)",
                       [(bid, h.get("take"), h.get("cite")) for h in d.get("hot_takes") or []])

    db.executemany("INSERT INTO entities VALUES (?,?,?)", [(k, n, t) for k, (n, t) in sorted(ents.items())])
    db.commit()
    db.close()
    os.replace(tmp, path)
    return path
