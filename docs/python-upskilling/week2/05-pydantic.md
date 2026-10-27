# Week2.5) Pydantic

## Plain English
Pydantic validates data using type hints. Extremely common in FastAPI.

```python
from pydantic import BaseModel, Field
from typing import Optional

class LeaveIn(BaseModel):
    emp_id: str
    days: int = Field(gt=0)
    leave_type: str = "PL"
    note: Optional[str] = None

payload = LeaveIn(emp_id="E1001", days=2)
print(payload.model_dump())          # dict (serialize)
obj = LeaveIn.model_validate({"emp_id": "E1001", "days": 1})  # deserialize
```

## Nested models
```python
class Employee(BaseModel):
    id: str
    name: str

class Ticket(BaseModel):
    employee: Employee
    reason: str
```

## Pydantic vs dataclass
- dataclass: convenience structure
- Pydantic: validation + parsing + JSON-friendly APIs

## Real scenario
Reject bad leave requests before DB write (`days=-1` fails validation).

## Mini practice
Make a `User` model with `email: str` and `age: int` (age > 0).
