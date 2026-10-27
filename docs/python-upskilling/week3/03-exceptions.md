# Week3.3) Exception handling

```python
class LeaveError(Exception):
    pass

def submit(days: int):
    if days <= 0:
        raise LeaveError("days must be positive")
    return "pending"

try:
    submit(-1)
except LeaveError as e:
    print("business error", e)
except Exception as e:
    print("unexpected", e)
else:
    print("no error path")
finally:
    print("always runs cleanup")
```

## Exception chaining
```python
raise RuntimeError("failed") from e
```

## Best practices
- Catch specific exceptions
- Don't swallow errors silently
- Convert low-level errors into domain errors for APIs

## Java comparison
No checked exceptions. Still use try/except carefully.

## Mini practice
Write `parse_days(text)` that raises `ValueError` for non-integers.
