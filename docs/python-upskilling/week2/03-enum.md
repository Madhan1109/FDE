# Week2.3) Enum / IntEnum

```python
from enum import Enum, IntEnum, auto

class LeaveType(Enum):
    PL = "privilege"
    SL = "sick"
    CL = "casual"

class Priority(IntEnum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()

print(LeaveType.PL.value)  # privilege
print(Priority.HIGH > Priority.LOW)  # True
```

## Why use Enum
Avoid magic strings like `"PL"` everywhere. Safer refactors.

## Real scenario
```python
if leave_type is LeaveType.SL:
    print("medical docs maybe required")
```

## Mini practice
Make `Status(Enum)` with PENDING, APPROVED, CANCELLED.
