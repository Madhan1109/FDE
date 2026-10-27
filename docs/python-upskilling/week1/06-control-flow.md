# 6) Conditional flow control

## if / elif / else
```python
days = 3
if days <= 0:
    print("invalid")
elif days > 5:
    print("needs manager")
else:
    print("auto approve path")
```

## Nested conditions
Possible, but prefer early returns for clarity.

## while
```python
n = 3
while n > 0:
    print(n)
    n -= 1
```

## for
```python
for day in ["Mon", "Tue", "Wed"]:
    print(day)

for i in range(3):  # 0,1,2
    print(i)
```

## break / continue / pass
```python
for x in items:
    if x == "skip":
        continue
    if x == "stop":
        break
    print(x)

def todo():
    pass  # placeholder (like empty method body)
```

## Java map
| Java | Python |
|------|--------|
| `else if` | `elif` |
| `for (i=0;i<n;i++)` | `for i in range(n)` |
| enhanced for | `for item in collection` |

## Real scenario
Route leave requests:
```python
status = "pending"
if status == "pending":
    print("waiting approval")
elif status == "approved":
    print("done")
else:
    print("check request")
```

## Mini practice
Loop 1..10, print only even numbers (`continue` for odds).
