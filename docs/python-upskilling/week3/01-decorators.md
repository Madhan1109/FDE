# Week3.1) Decorators

## Plain English
A decorator wraps a function to add behavior (logging, auth, timing) without changing the function body. Like Java annotations + interceptors idea.

```python
import functools
import time

def timing(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        print("took", time.time() - start)
        return result
    return wrapper

@timing
def work(n):
    return sum(range(n))
```

## Why functools.wraps
Keeps original function name/doc for debugging.

## Decorator with arguments / multiple decorators
You can stack `@auth` then `@timing`. Order matters (bottom runs first inward).

## Real scenario
`@require_login` before leave APIs.

## Mini practice
Write `@shout` that uppercases a function's string return.
