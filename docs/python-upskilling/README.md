# Python Upskilling (for Java developers)

This folder follows your org PDF: **`docs/Python Upskilling plan.pdf`**.

Everything here is written in **plain English**, with:
- Java comparisons (so your muscle memory helps)
- tiny code examples
- real-life scenarios you can remember

## How to study

1. Read one file per sitting (30–60 min)
2. Type the examples yourself in a Python file / notebook
3. Say out loud: “In Java I do X → in Python I do Y”
4. Do the mini practice at the bottom of each file

## Folder map (matches the PDF)

### Week 1 — Python Fundamentals
| # | Topic | Doc |
|---|-------|-----|
| 1 | Introduction & advantages | [week1/01-intro-and-advantages.md](./week1/01-intro-and-advantages.md) |
| 2 | PEP standards / PEP 8 | [week1/02-pep-standards.md](./week1/02-pep-standards.md) |
| 3 | Datatypes & built-ins | [week1/03-datatypes.md](./week1/03-datatypes.md) |
| 4 | Typing | [week1/04-typing.md](./week1/04-typing.md) |
| 5 | Operators | [week1/05-operators.md](./week1/05-operators.md) |
| 6 | Conditional flow / loops | [week1/06-control-flow.md](./week1/06-control-flow.md) |
| 7 | Comprehensions | [week1/07-comprehensions.md](./week1/07-comprehensions.md) |
| 8 | Generators | [week1/08-generators.md](./week1/08-generators.md) |
| 9 | Functions | [week1/09-functions.md](./week1/09-functions.md) |
| 10 | Built-in functions | [week1/10-builtin-functions.md](./week1/10-builtin-functions.md) |

### Week 2 — Data modeling, OOP & internals
| # | Topic | Doc |
|---|-------|-----|
| 1 | Collections | [week2/01-collections.md](./week2/01-collections.md) |
| 2 | Dataclass | [week2/02-dataclass.md](./week2/02-dataclass.md) |
| 3 | Enum / IntEnum | [week2/03-enum.md](./week2/03-enum.md) |
| 4 | Memory & GC | [week2/04-memory-and-gc.md](./week2/04-memory-and-gc.md) |
| 5 | Pydantic | [week2/05-pydantic.md](./week2/05-pydantic.md) |
| 6 | OOP | [week2/06-oop.md](./week2/06-oop.md) |
| 7 | Dunder / magic methods | [week2/07-dunder-methods.md](./week2/07-dunder-methods.md) |
| 8 | Descriptors | [week2/08-descriptors.md](./week2/08-descriptors.md) |

### Week 3 — Advanced Python
| # | Topic | Doc |
|---|-------|-----|
| 1 | Decorators | [week3/01-decorators.md](./week3/01-decorators.md) |
| 2 | Monkey patching | [week3/02-monkey-patching.md](./week3/02-monkey-patching.md) |
| 3 | Exception handling | [week3/03-exceptions.md](./week3/03-exceptions.md) |
| 4 | Multithreading | [week3/04-multithreading.md](./week3/04-multithreading.md) |
| 5 | Multiprocessing | [week3/05-multiprocessing.md](./week3/05-multiprocessing.md) |
| 6 | GIL | [week3/06-gil.md](./week3/06-gil.md) |
| 7 | Async / await | [week3/07-async-await.md](./week3/07-async-await.md) |
| 8 | Logging | [week3/08-logging.md](./week3/08-logging.md) |
| 9 | Unit testing | [week3/09-unit-testing.md](./week3/09-unit-testing.md) |
| 10 | Regular expressions | [week3/10-regex.md](./week3/10-regex.md) |
| 11 | File handling | [week3/11-file-handling.md](./week3/11-file-handling.md) |

### Next (from PDF)
- FastAPI & SQLAlchemy bridge notes: [next-fastapi-sqlalchemy.md](./next-fastapi-sqlalchemy.md)

### Extra for Java people
- [00-java-to-python-cheatsheet.md](./00-java-to-python-cheatsheet.md)

## Setup (5 minutes)

```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
python --version
```

Create a file `hello.py`:

```python
print("Hello from Python")
```

Run:

```bash
python hello.py
```

## Mindset shift (Java → Python)

| Java habit | Python habit |
|------------|--------------|
| Compile then run | Run directly (interpreted) |
| `public class App { ... }` | Just write statements / functions |
| `;` everywhere | Indentation matters; almost no `;` |
| `ArrayList` / `HashMap` | `list` / `dict` |
| Checked exceptions | Exceptions are mostly unchecked |
| Verbose getters/setters | Properties / dataclasses / Pydantic |
| Interfaces + boilerplate | Duck typing + protocols + type hints |

You are not “starting from zero.” You already know programming. You are learning a **new dialect**.
