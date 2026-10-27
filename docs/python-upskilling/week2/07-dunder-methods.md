# Week2.7) Dunder / magic methods

## Plain English
Methods with `__name__` customize object behavior (`len(x)`, `print(x)`, `x+y`).

```python
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

    def __str__(self):
        return f"Team({len(self)})"

    def __repr__(self):
        return f"Team({self.members!r})"

    def __eq__(self, other):
        return self.members == other.members

    def __getitem__(self, idx):
        return self.members[idx]
```

Also useful: `__lt__`, `__add__`, `__setitem__`, `__iter__`, `__next__`, `__call__`.

## Real scenario
Make a `LeaveBalance` object printable and comparable for reports.

## Mini practice
Write a class where `len(obj)` returns number of items stored.
