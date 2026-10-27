# 4) Typing (type annotations)

## Plain English
Python can run without types. Type hints make code safer and clearer (like optional Java types).

```python
def add(a: int, b: int) -> int:
    return a + b
```

## Common annotations
```python
from typing import Optional, Union, Any, List, Dict, Tuple, Set

name: str = "Alice"
age: int = 30
score: float = 9.5
ok: bool = True
tags: list[str] = ["hr", "leave"]
data: dict[str, int] = {"PL": 10}
pair: tuple[str, int] = ("E1001", 10)
ids: set[str] = {"E1001"}

maybe_name: Optional[str] = None      # str or None
id_or_num: Union[str, int] = "E1001"  # either
anything: Any = 123                   # escape hatch (use rarely)
```

## Type aliases
```python
EmployeeId = str
Balance = dict[str, float]
```

## Java comparison
- Java: types required
- Python: types optional, checked by tools (`mypy`, Pyright), not by runtime (normally)

## Real scenario
FastAPI uses type hints to validate request bodies automatically. Good typing = better APIs.

## Mini practice
Write a function `days_left(entitled: int, used: int) -> int`.
