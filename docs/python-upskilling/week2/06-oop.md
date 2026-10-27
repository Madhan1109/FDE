# Week2.6) Object-Oriented Programming

## Class & object
```python
class Employee:
    company = "Ideas2IT"          # class attribute

    def __init__(self, emp_id, name):   # constructor
        self.emp_id = emp_id            # instance attributes
        self.name = name

    def greet(self):                    # instance method
        return f"Hi {self.name}"

    @classmethod
    def from_dict(cls, data):           # class method
        return cls(data["id"], data["name"])

    @staticmethod
    def is_valid_id(emp_id: str) -> bool:  # static method
        return emp_id.startswith("E")
```

## Inheritance / encapsulation / polymorphism
```python
class Manager(Employee):
    def greet(self):
        return f"Hello Manager {self.name}"

people = [Employee("E1", "A"), Manager("E2", "B")]
for p in people:
    print(p.greet())  # polymorphism
```

Encapsulation: use `_protected` / `__private`-ish naming conventions (not as strict as Java private).

## Abstract classes
```python
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, msg: str) -> None: ...
```

## Java map
| Java | Python |
|------|--------|
| constructor | `__init__` |
| `this` | `self` |
| `static` method | `@staticmethod` |
| abstract class | `ABC` + `@abstractmethod` |

## Real scenario
`LeaveService` class with methods `balance()`, `submit()`, `cancel()`.

## Mini practice
Create `Animal` with `speak()`, and `Dog(Animal)` overriding it.
