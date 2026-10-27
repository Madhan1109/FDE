# Week3.7) Async / await

## Plain English
Async lets one thread handle many waiting tasks efficiently (like non-blocking I/O).

```python
import asyncio

async def get_balance(emp_id: str) -> str:
    await asyncio.sleep(0.1)  # fake I/O
    return f"{emp_id}: OK"

async def main():
    results = await asyncio.gather(
        get_balance("E1001"),
        get_balance("E1002"),
    )
    print(results)

asyncio.run(main())
```

## Words
- `async def` → coroutine function
- `await` → wait without blocking the event loop
- event loop schedules coroutines (`asyncio`)

## Async vs thread vs process
| | Best for |
|--|----------|
| async | many network waits in one app (APIs) |
| threads | blocking I/O libs not async-ready |
| processes | CPU-bound |

## Real scenario
FastAPI endpoints calling multiple downstream services concurrently.

## Mini practice
Write two async functions and run them with `asyncio.gather`.
