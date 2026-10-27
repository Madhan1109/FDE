# Week2.4) Memory management & garbage collection

## Plain English
Python objects live in a heap. Variables are **names/references**, not the object itself.

```python
a = [1, 2]
b = a
b.append(3)
print(a)  # [1,2,3]  same object
print(id(a), id(b))  # same id
```

## Reference counting + GC
- Each object has a refcount
- When refcount hits 0, memory can be reclaimed
- Circular references handled by `gc` module

```python
import gc
gc.collect()
```

## Mutable vs immutable reminder
Changing a mutable via two names affects both. Immutable rebinding creates new objects.

## Java comparison
Similar to object references in Java. Python also has GC; you rarely free memory manually.

## Real scenario
Accidentally sharing one mutable default config dict across requests can leak state between users. Use `default_factory` / copy.

## Mini practice
Create two variables pointing to same list, modify one, observe the other.
