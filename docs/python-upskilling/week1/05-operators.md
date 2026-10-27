# 5) Operators

## Arithmetic
`+ - * / // % **`
- `/` always float division (`5/2 == 2.5`)
- `//` floor division (`5//2 == 2`) — like Java integer division feel
- `**` power (`2**3 == 8`)

## Comparison
`== != < <= > >=`

## Assignment
`= += -= *= /=` etc.

## Logical
`and or not` (Java: `&& || !`)

```python
if active and balance > 0:
    print("can apply")
```

## Bitwise
`& | ^ ~ << >>` (same idea as Java)

## Membership
```python
"PL" in ["PL", "SL"]      # True
"X" not in {"A", "B"}     # True
```

## Identity
```python
a = [1, 2]
b = a
c = [1, 2]
a is b        # True (same object)
a is not c    # True (different objects)
a == c        # True (same values)
```
Remember: `==` value, `is` identity (like Java `==` for object refs).

## Walrus `:=` (assign + use)
```python
if (n := len(errors)) > 0:
    print(f"{n} errors")
```

## Real scenario
```python
leave_type = "PL"
allowed = {"PL", "SL", "CL"}
if leave_type in allowed and balance.get(leave_type, 0) > 0:
    print("eligible")
```

## Mini practice
Explain why `a == b` can be True while `a is b` is False for two lists.
