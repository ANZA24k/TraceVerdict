"""Recompute a recorded final decision hash without network access."""
import hashlib
import json
import sys
from pathlib import Path

address, path = sys.argv[1:]
record = json.loads(Path(path).read_text())
expected = record.pop("decision_hash")
encoded = json.dumps({"domain": "TraceVerdict/decision/v1", "contract": address,
                      "record": record}, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
actual = hashlib.sha256(encoded).hexdigest()
assert actual == expected, (actual, expected)
assert record["state"] == "FINAL"
print(f"FINAL {record['result']['outcome']} decision_hash={actual}")
