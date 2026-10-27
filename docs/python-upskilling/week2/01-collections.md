# Week2.1) Collections module

## Plain English
`collections` adds specialized containers beyond list/dict/set.

```python
from collections import Counter, OrderedDict, defaultdict, namedtuple, deque
```

## Counter
```python
votes = Counter(["PL", "PL", "SL"])
print(votes["PL"])  # 2
```

## defaultdict
```python
by_dept = defaultdict(list)
by_dept["Engineering"].append("Alice")
```
No KeyError on missing keys — auto-creates default.

## OrderedDict
Preserves order (modern `dict` also preserves insertion order, but OrderedDict has extra order helpers).

## namedtuple
```python
Employee = namedtuple("Employee", ["id", "name"])
e = Employee("E1001", "Alice")
print(e.name)
```
Like a lightweight immutable record.

## deque
Fast appends/pops from both ends (useful queues).

## Real scenario
Count leave types in a month of requests with `Counter`.

## Mini practice
Use `Counter` on `"banana"` and print count of `a`.
