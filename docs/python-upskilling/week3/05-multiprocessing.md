# Week3.5) Multiprocessing

## Processes vs threads
- Threads: shared memory, good for I/O
- Processes: separate memory, better for CPU-heavy work in CPython

```python
from multiprocessing import Process, Pool

def square(n):
    return n * n

if __name__ == "__main__":
    with Pool(4) as pool:
        print(pool.map(square, [1, 2, 3, 4]))
```

## IPC
Queues/pipes share data between processes carefully.

## Real scenario
Batch re-encrypting large files on multiple CPU cores.

## Mini practice
Explain when you choose process pool over thread pool.
