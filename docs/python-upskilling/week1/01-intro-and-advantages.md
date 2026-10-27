# 1) Introduction to Python and its advantages

## Plain English
Python is a high-level language made to be readable. You write less ceremony than Java and run files directly.

## Why companies use it
- Fast to prototype (great for FDE pilots)
- Huge libraries (data, AI, web APIs)
- Easy for mixed teams to read
- Strong ecosystem: FastAPI, pandas, LangChain, etc.

## Java comparison
| | Java | Python |
|--|------|--------|
| Style | Verbose, strict types by default | Concise, optional types |
| Run | Compile to bytecode, then run | Interpret / run script |
| Common use | Large enterprise backends | APIs, scripting, AI, automation |

## Tiny example
```python
name = "Alice"
days = 2
print(f"{name} requested {days} leave days")
```

## Real scenario
An FDE needs a quick script to read a customer CSV of employees and print who has zero leave balance. In Python this can be a short script the same day. In Java it often needs more project setup first.

## Mini practice
Write a script that asks for your name and prints: `Welcome, <name>`.
Hint: `input("Your name: ")`
