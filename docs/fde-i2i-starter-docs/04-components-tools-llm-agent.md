# 04 — App components, tools, LLM role, agent internals

## Big picture: what makes an agentic app

Think of layers:

```
User / Channel (chat, API, Slack…)
        ↓
Orchestration (workflow / planner)
        ↓
Agent(s)  ←→  Memory
        ↓
Tools / MCP servers / other agents (A2A)
        ↓
Systems of record (HRIS, CRM, DB, search…)
```

Plus cross-cutting: **guardrails, observability, evals, auth**.

---

## Core components (plain list)

| Component | Job in plain English |
|-----------|----------------------|
| **Interface** | How humans/systems send requests |
| **LLM** | Reasons, plans, writes, chooses tools |
| **Agent runtime** | Runs the think→act→observe loop |
| **Tools** | Real-world actions and data access |
| **Memory** | Remembers context beyond one prompt |
| **Orchestration** | Routes work across steps/agents |
| **Guardrails** | Blocks unsafe/invalid behavior |
| **Observability** | Traces, logs, metrics for each run |
| **Evals** | Tests quality before/after changes |

---

## Tools (critical FDE topic)

A **tool** is a function the agent can call, usually with:

- **Name** (e.g., `get_leave_balance`)
- **Description** (when to use it — the LLM reads this)
- **Parameters schema** (types, required fields)
- **Implementation** (API/DB call)
- **Permissions** (who/what may call it)

### Why schemas matter

Bad description → wrong tool chosen.  
Missing required field → failed call.  
No auth check → security incident.

### Tool categories (examples)

| Category | Examples |
|----------|----------|
| Read data | Search FAQ, get employee profile |
| Write data | Create ticket, submit leave |
| Compute | Calculate prorated days |
| Communicate | Send email, notify manager |
| Retrieve knowledge | RAG / BM25 / vector search |

**Rule of thumb:** Prefer **narrow, reliable tools** over one giant “do anything” tool.

---

## What the LLM actually does

The LLM is not the database. Typical roles:

1. **Understand** the user intent
2. **Plan** next steps
3. **Select** tools / agents
4. **Fill** tool arguments from conversation
5. **Synthesize** final answer from observations
6. **Decide** stop / continue / ask user

Sometimes you use **different models** for different jobs (cheap classifier vs strong planner).

---

## Agent internals (simple mental model)

```
while not done:
  reason with LLM (given goal + state + tool list)
  if LLM wants a tool:
      validate args + guardrails
      run tool
      add result to state / messages
  else:
      return final answer
```

This is the same idea as **ReAct** (Reason + Act), even if your framework hides the loop.

---

## Prompts vs policies vs code

| Layer | Holds |
|-------|-------|
| System prompt | Role, style, high-level rules |
| Policies / guardrails | Hard constraints (block PII leak, force approval) |
| Application code | Auth, transactions, retries, idempotency |

**Do not** put critical security only in the prompt. Prompts can be ignored; code and gateways enforce.

---

## Study checklist

- [ ] Draw the component stack from memory
- [ ] Explain why tool *description* quality matters
- [ ] List 3 LLM roles besides “write text”
- [ ] Explain why security cannot live only in the prompt
