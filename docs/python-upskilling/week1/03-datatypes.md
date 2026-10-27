# 3) Datatypes & built-in collections

## Plain English
Python has simple built-in types. You use them constantly.

## Primitive-like types
```python
age = 30          # int
salary = 10.5     # float
name = "Bob"      # str
active = True     # bool
```

## Core containers (know these cold)
```python
leaves = ["PL", "SL", "CL"]           # list  (like ArrayList) - mutable, ordered
point = (10, 20)                      # tuple (like immutable array) - immutable, ordered
employee = {"id": "E1001", "name": "Alice"}  # dict (like HashMap)
skills = {"python", "java"}           # set  (unique items)
```

## Type conversion
```python
int("42")
str(42)
float("3.14")
list("abc")   # ['a','b','c']
```

## Mutable vs immutable (very important)
- **Immutable:** cannot change in place → `int`, `float`, `str`, `tuple`, `bool`
- **Mutable:** can change in place → `list`, `dict`, `set`

```python
s = "hi"
# s[0] = "H"  # error: strings immutable

nums = [1, 2]
nums.append(3)  # ok: list mutable
```

## Java map
| Python | Closest Java |
|--------|--------------|
| `list` | `ArrayList` |
| `tuple` | unmodifiable list / record-like fixed values |
| `dict` | `HashMap` |
| `set` | `HashSet` |

## Real scenario
Leave balances:
```python
balance = {"PL": 12, "SL": 5, "pending": 2}
balance["pending"] += 1
```
A `dict` is perfect for key/value HR fields.

## Mini practice
Create a dict for one employee with `id`, `name`, `department`. Print the name.
