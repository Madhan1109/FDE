# Week3.6) GIL — Global Interpreter Lock

## Plain English
In CPython, the GIL allows only one thread to execute Python bytecode at a time.

## What that means
- Threads help **I/O-bound** tasks (waiting on network/disk)
- Threads do **not** give true parallel CPU speedup for pure Python CPU work
- Use **multiprocessing** (or native libs) for CPU-bound parallelism

## Real scenario
- Downloading 50 URLs → threads/async good
- Heavy number crunching in pure Python → processes / numpy / pypy alternatives

## Mini practice
Classify: "parse 1GB CSV CPU-heavy" vs "call 50 REST APIs" → process or thread?
