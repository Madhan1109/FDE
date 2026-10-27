# 00c — Programming fundamentals (Python for agents) — deep dive

**Guide prerequisite:** *Programming fundamentals — familiarity with Python or similar for implementing agents (hands-on).*

This is **not** a full Python course. It is the slice you need to **build and read agent code**. For a broader Java→Python path, use [`../python-upskilling/README.md`](../python-upskilling/README.md).

---

## 1. Why the guide asks for programming

Conceptual slides are not enough. Hands-on agent work means you will:

- Define tools as functions  
- Call LLM APIs  
- Parse JSON  
- Keep conversation/tool state  
- Run a web API or CLI  
- Log failures and write tests  

Python is the most common language in agent demos and frameworks (LangGraph, FastAPI, etc.). The ideas transfer to Java/TypeScript.

---

## 2. Mental model of a minimal agent in code

```text
messages = [system, user]
while True:
    decision = call_llm(messages, tools=tool_schemas)
    if decision is a tool_call:
        result = run_tool(decision.name, decision.args)  # your Python
        messages.append(tool_result)
    else:
        return decision.final_text
```

Everything fancy (LangGraph, MCP, A2A) still sits on this loop.

---

## 3. Python pieces you will actually use

### 3.1 Functions = tools

```python
def get_leave_balance(employee_id: str) -> dict:
    """Return remaining annual leave days for an employee."""
    # call HR API here
    return {"employee_id": employee_id, "days_remaining": 12}
```

- **Name + docstring** help the LLM choose the tool  
- **Type hints** help you and schema generators  
- **Return dict/JSON-serializable data**, not huge opaque objects  

### 3.2 Dictionaries & JSON

Agents speak JSON constantly.

```python
import json

payload = {"start_date": "2026-11-10", "end_date": "2026-11-12"}
text = json.dumps(payload)      # dict → string
data = json.loads(text)         # string → dict
```

You must be comfortable reading nested dicts: `data["result"]["id"]`.

### 3.3 Lists for message history

```python
messages = [
    {"role": "system", "content": "You are an HR assistant."},
    {"role": "user", "content": "What is my leave balance?"},
]
```

Appending tool results keeps state for the next LLM call.

### 3.4 `if` / `for` / early returns

Routing, retries, and guardrails are mostly boring control flow — that is good.

```python
if days > balance:
    return {"ok": False, "error": "Insufficient leave balance"}
```

### 3.5 Exceptions

```python
try:
    result = client.get_balance(user_id)
except TimeoutError:
    return {"ok": False, "error": "HR system timeout; try again"}
```

Never let a raw stack trace become the only agent reply in production.

### 3.6 Modules & virtual environments (basics)

| Idea | Why |
|------|-----|
| `venv` / poetry | Isolate project dependencies |
| `requirements.txt` / `pyproject.toml` | Reproducible installs |
| Packages | `httpx`, `pydantic`, `fastapi`, framework SDKs |

---

## 4. Calling an HTTP API from Python

```python
import httpx

def get_leave_balance(employee_id: str) -> dict:
    r = httpx.get(
        f"https://hr.example.com/api/leave/{employee_id}",
        headers={"Authorization": f"Bearer {TOKEN}"},
        timeout=10.0,
    )
    r.raise_for_status()
    return r.json()
```

Connects directly to prerequisite **00b** (APIs).

---

## 5. Validating inputs (Pydantic pattern)

LLMs invent bad arguments. Validate before side effects.

```python
from pydantic import BaseModel, Field

class LeaveRequest(BaseModel):
    employee_id: str
    start_date: str  # or date type
    end_date: str
    leave_type: str = Field(pattern="^(annual|sick|unpaid)$")

def submit_leave(raw: dict) -> dict:
    req = LeaveRequest.model_validate(raw)  # throws if invalid
    # call API with req...
    return {"ok": True, "id": "LR-1"}
```

This is the programming twin of **schemas + guardrails**.

---

## 6. Async basics (why you see `async def`)

Many agent servers are async (FastAPI, streaming).

```python
async def get_leave_balance(employee_id: str) -> dict:
    async with httpx.AsyncClient(timeout=10.0) as client:
        r = await client.get(...)
        r.raise_for_status()
        return r.json()
```

You do not need to master every concurrency detail on day one — but know:

- `await` waits for I/O without blocking the whole server the same way sync would  
- Do not call blocking `time.sleep` / sync HTTP inside async hot paths  

Deeper: `python-upskilling` week3 async lesson.

---

## 7. Structuring a small agent project

```text
app/
  main.py           # API entry (FastAPI)
  agent.py          # LLM loop / graph
  tools/
    leave.py        # tool functions
    search.py
  schemas.py        # Pydantic models
  config.py         # env vars
tests/
  test_tools.py
```

**Habit:** Keep tools testable without the LLM (unit test `submit_leave` with fake HTTP).

---

## 8. Environment variables & secrets

```python
import os
api_key = os.environ["LLM_API_KEY"]  # do not hardcode
```

Never commit keys. Never put keys in prompts.

---

## 9. Logging (agent debugging)

```python
import logging
log = logging.getLogger("agent")
log.info("tool_call", extra={"tool": "submit_leave", "user": user_id})
```

When the agent misbehaves, logs/traces beat guessing. (Connects to observability in file `09`.)

---

## 10. Minimal “hello agent” learning path

Do these in order (even as tiny scripts):

1. Call an LLM chat API; print the reply  
2. Add one local Python tool; run a manual tool loop  
3. Validate tool args with Pydantic  
4. Wrap tools behind FastAPI endpoints  
5. Add a max-steps guard in the loop  
6. Write 3 unit tests for tools (no LLM)  
7. Only then introduce a framework graph (LangGraph, etc.)  

---

## 11. Java developer cheat mapping

| Java | Python (agent world) |
|------|----------------------|
| `class` / methods | `class` / `def` |
| `Optional` / null checks | `None`, often Pydantic |
| Jackson JSON | `json` / Pydantic |
| Spring Controller | FastAPI route |
| Interface + impl for ports | Tool functions + protocol/MCP later |
| JUnit | `pytest` |

---

## 12. How this maps to later I2I topics

| Later topic | Programming angle |
|-------------|-------------------|
| Tools | Functions + schemas |
| Memory | Store/load dicts or DB rows |
| Guardrails | `if` checks + validators around tools |
| MCP | Servers implemented in Python/TS exposing tools |
| Platforms | Libraries you import and configure in code |
| Evals | Scripts that run cases and score outputs |

---

## Study checklist

- [ ] Write a tool as a typed Python function returning JSON-safe data  
- [ ] Parse and build message lists  
- [ ] Call an HTTP API with timeout and error handling  
- [ ] Validate model-produced args before a write  
- [ ] Explain the while-loop agent mentally in code terms  
- [ ] Keep secrets in env vars  

## Self-check questions

1. Why unit-test tools without calling the LLM?  
2. What happens if you skip validation on `employee_id`?  
3. Where does the “tool description” the model reads often come from in code?

## Related deeper practice

- Full Python upskilling track: [`../python-upskilling/README.md`](../python-upskilling/README.md)  
- After 00a–00c, continue I2I files `01` → `10`
