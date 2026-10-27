# 10) Important built-in functions

```python
nums = [3, 1, 2]

list(map(lambda x: x * 2, nums))     # [6,2,4]
list(filter(lambda x: x > 1, nums))  # [3,2]
list(zip(["a", "b"], [1, 2]))        # [('a',1),('b',2)]

from functools import reduce
reduce(lambda a, b: a + b, nums)     # 6

for i, v in enumerate(nums):         # index + value
    print(i, v)

type(nums)      # <class 'list'>
id(nums)        # object identity number
list(range(3))  # [0,1,2]
sorted(nums)    # [1,2,3]
max(nums), min(nums)
```

## Real scenario
Pair employees with managers:
```python
emps = ["Alice", "Bob"]
mgrs = ["M1", "M2"]
for emp, mgr in zip(emps, mgrs):
    print(emp, "->", mgr)
```

## Mini practice
Use `enumerate` to print `1. Alice`, `2. Bob` (1-based).
