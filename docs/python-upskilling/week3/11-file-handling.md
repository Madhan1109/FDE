# Week3.11) File handling

```python
from pathlib import Path
import json, csv

# Context manager auto-closes file
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("hello\n")

with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Append
with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("line2\n")

# JSON
data = {"emp": "E1001", "days": 2}
Path("leave.json").write_text(json.dumps(data), encoding="utf-8")

# CSV
with open("emps.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["id", "name"])
    w.writerow(["E1001", "Alice"])

# Paths
p = Path("data") / "emps.csv"
print(p.exists())
```

## Real scenario
Export leave audit for a customer pilot as CSV/JSON using `with` blocks so files always close.

## Mini practice
Write a dict to `out.json` and read it back.
