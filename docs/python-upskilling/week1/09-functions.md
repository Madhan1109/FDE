# 9) Functions

## Define + return
```python
def add(a, b):
    return a + b
```

## Positional / keyword / default
```python
def apply_leave(emp_id, days, leave_type="PL"):
    return f"{emp_id}:{leave_type}:{days}"

apply_leave("E1001", 2)                 # positional
apply_leave("E1001", days=2, leave_type="SL")  # keyword
```

## *args and **kwargs
```python
def demo(*args, **kwargs):
    print(args)    # tuple of extra positional
    print(kwargs)  # dict of extra keywords

demo(1, 2, x=3)
```

## lambda (anonymous)
```python
square = lambda n: n * n
```

## Scope: local / global / nonlocal
```python
counter = 0

def bump():
    global counter
    counter += 1

def outer():
    x = 1
    def inner():
        nonlocal x
        x += 1
    inner()
    return x
```

## Recursion
```python
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
```

## Java comparison
- Python `self` is explicit in methods
- Overloading by signature is not Java-style; use defaults / `*args` instead

## Real scenario
```python
def submit_leave(emp_id: str, days: int, leave_type: str = "PL") -> str:
    if days <= 0:
        return "invalid"
    return "pending"
```

## Mini practice
Write `greet(name, prefix="Hello")` supporting default + keyword calls.
