# Week3.4) Multithreading

```python
import threading

def fetch(url):
    print("fetching", url)

threads = [threading.Thread(target=fetch, args=(u,)) for u in ["a", "b"]]
for t in threads:
    t.start()
for t in threads:
    t.join()
```

## Sync with Lock
```python
lock = threading.Lock()
with lock:
    shared += 1
```

## Race conditions
Two threads update shared data without locks → corrupt results.

## Thread pool
```python
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=4) as pool:
    list(pool.map(fetch, ["a", "b", "c"]))
```

## Real scenario
Call 10 customer APIs concurrently for I/O wait (network), not heavy CPU math.

## Mini practice
Start 3 threads that print their names.
