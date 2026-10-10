"""A one-word claim `who` that the brief also names must resolve to that firm, not a channel-scoped
first name ('Stifel @ GYW'). Run: python3 test_canonicalize.py"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import entities  # noqa: E402
import generate  # noqa: E402

p = os.path.join(tempfile.mkdtemp(), "entities.json")
generate.Registry = lambda: entities.Registry(p)
brief = {"speakers": "Valentin Dragu", "channel": "GYW", "entities": [{"raw": "Stifel"}],
         "_raw": {"claims": [{"who": "Stifel (cited by Valentin Dragu)", "entity": "AMD"}], "relations": []}}
keys = sorted(generate._canonicalize_entities([brief]).ents)
assert keys == ["amd", "stifel"], keys
print("ok")
