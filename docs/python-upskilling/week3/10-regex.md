# Week3.10) Regular expressions

```python
import re

text = "emp E1001 and E2002"
print(re.findall(r"E\d{4}", text))  # ['E1001','E2002']

m = re.search(r"E(\d{4})", text)
if m:
    print(m.group(1))  # 1001

print(re.sub(r"\s+", " ", "a   b"))  # 'a b'
print(re.split(r",", "a,b,c"))
```

## Basics to remember
- `\d` digit, `\w` word char, `.` any (except newline)
- `* + ? {n}` quantifiers
- `^ $` anchors
- `(...)` groups
- `match` from start, `search` anywhere, `findall` all

## Real scenario
Validate employee IDs like `E1001` before login.

## Mini practice
Write regex that validates email-like `name@company.com` (simple version).
