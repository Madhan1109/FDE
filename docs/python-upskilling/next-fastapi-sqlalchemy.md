# Next in your PDF: FastAPI & SQLAlchemy

Your upskilling PDF ends with:
1. InProject - FastAPI Upskilling plan
2. CDP - FastAPI Upskilling plan

## Why this comes after core Python
FastAPI apps use almost everything you just learned:
- type hints
- pydantic models
- async endpoints (often)
- exceptions + logging
- OOP / services
- unit tests

## Tiny mental preview (do not stress yet)
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LeaveIn(BaseModel):
    emp_id: str
    days: int

@app.post("/leave")
def create_leave(body: LeaveIn):
    return {"status": "pending", "emp_id": body.emp_id}
```

SQLAlchemy = Python ORM (like JPA/Hibernate idea) for talking to databases with classes.

## Suggested order after Week 3
1. Finish Week 1–3 drills
2. Ask your org for the FastAPI Upskilling plan PDF(s)
3. Build a tiny leave API with FastAPI + SQLite
