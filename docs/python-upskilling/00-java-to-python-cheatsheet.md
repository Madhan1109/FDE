# Java → Python cheatsheet (keep this open)

## Everyday syntax

| Need | Java | Python |
|------|------|--------|
| Print | `System.out.println(x);` | `print(x)` |
| Variable | `int n = 5;` | `n = 5` |
| String | `String s = "hi";` | `s = "hi"` |
| List | `List<String> a = new ArrayList<>();` | `a = []` |
| Map | `Map<String,Integer> m = new HashMap<>();` | `m = {}` |
| Null | `null` | `None` |
| True/False | `true` / `false` | `True` / `False` |
| If | `if (x > 0) { ... }` | `if x > 0:\n    ...` |
| For-each | `for (String s : list)` | `for s in list:` |
| Method | `void foo(int x)` | `def foo(x):` |
| Class | `class User { ... }` | `class User:\n    ...` |
| Inheritance | `class A extends B` | `class A(B):` |
| Interface-ish | `implements` | duck typing / Protocol |
| Package import | `import com.x.Y;` | `from x import Y` / `import x` |
| Equals value | `.equals()` for objects | `==` compares values for many types |
| Same object | `==` for objects | `is` |
| Length | `.size()` / `.length` | `len(x)` |
| This | `this` | `self` |

## Mental model

- Python uses **indentation** instead of `{ }`.
- Types exist, but are often optional until you add type hints.
- Almost everything is an **object** (including functions).
- “Pythonic” means clear and simple, not clever one-liners only experts understand.

## Real scenario to remember

You are writing an HR leave helper.
- In Java you create `LeaveService.java`, interfaces, DTOs, builders.
- In Python you often start with functions + a `dict` / dataclass, then grow into classes/Pydantic when needed.
