# 8) Generators

## Plain English
A generator gives values one-by-one (lazy), instead of building a full list in memory.

## yield
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(3):
    print(x)  # 3 2 1
```

## Generator expression
```python
gen = (x * x for x in range(5))
print(next(gen))  # 0
```

## next()
```python
g = countdown(2)
print(next(g))  # 2
print(next(g))  # 1
```

## Generator vs list
| List | Generator |
|------|-----------|
| All values in memory now | One value at a time |
| Can reuse / index freely | Mostly one-pass |
| Good for small data | Good for large/streaming data |

## Real scenario
Reading a huge audit log file line-by-line with a generator avoids loading the whole file into RAM — useful in customer environments with large logs.

## Mini practice
Write `def even_numbers(limit):` yielding even numbers up to `limit`.
