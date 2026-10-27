# Week2.2) Dataclass

## Plain English
`@dataclass` auto-creates `__init__`, `__repr__`, etc. Like a Java record / Lombok `@Data`, but simpler.

```python
from dataclasses import dataclass, field

@dataclass
class LeaveRequest:
    emp_id: str
    days: int
    leave_type: str = "PL"
    tags: list[str] = field(default_factory=list)

req = LeaveRequest("E1001", 2)
print(req)
```

## Useful options
- `frozen=True` → immutable instance
- `field(default_factory=list)` → safe mutable defaults
- compare dataclass vs normal class: less boilerplate
- vs namedtuple: dataclass can be mutable and richer

## Real scenario
Model API payloads before full Pydantic validation.

## Mini practice
Create `@dataclass class Employee` with `id`, `name`, `department`.
