# 7) Comprehensions

## Plain English
A short way to build lists/sets/dicts from loops. Like a compact Java stream mapping.

## List comprehension
```python
nums = [1, 2, 3, 4]
squares = [n * n for n in nums]             # [1,4,9,16]
evens = [n for n in nums if n % 2 == 0]     # [2,4]
```

## Set comprehension
```python
unique_lens = {len(word) for word in ["hi", "hey", "hi"]}
```

## Dict comprehension
```python
names = ["Alice", "Bob"]
ids = {name: name.lower() for name in names}
```

## Generator expression
```python
total = sum(n * n for n in nums)  # lazy, no full list in memory
```

## Nested
```python
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
```

## Real scenario
Normalize leave codes:
```python
raw = ["pl", "SL", " cl "]
clean = [x.strip().upper() for x in raw if x.strip()]
# ["PL", "SL", "CL"]
```

## Mini practice
From `[5, 12, 7, 20]`, make a list of values greater than 10.
