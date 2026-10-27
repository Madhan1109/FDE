# 00b — APIs and external tools — deep dive (plain English)

**Guide prerequisite:** *APIs and external tools — how AI systems interact with external data and services (basic level).*

Agents are useless in enterprises if they only chat. They must **read and write real systems**. This file builds that foundation before MCP/tools chapters.

---

## 1. What “external” means

Anything outside the LLM’s brain:

| External thing | Example |
|----------------|---------|
| HTTP API | HRIS leave API, ServiceNow, weather API |
| Database | Employee table, ticket store |
| Search / docs | FAQ index, SharePoint, Confluence |
| Files | PDF policy, CSV export |
| SaaS | Slack, email, calendar |
| Another agent | Benefits specialist service |

**Tool** (in agent language) = a controlled function your agent is allowed to call that reaches one of the above.

---

## 2. API basics (enough for agents)

### Request / response

```
Your agent runtime  →  HTTP request  →  External service
Your agent runtime  ←  HTTP response ←
```

Common pieces:

| Piece | Meaning |
|-------|---------|
| **URL / endpoint** | Where to call (`GET /employees/{id}/leave-balance`) |
| **Method** | GET (read), POST (create), PUT/PATCH (update), DELETE |
| **Headers** | Auth token, content type, request id |
| **Body** | JSON payload for create/update |
| **Status code** | 200 OK, 400 bad input, 401/403 auth, 404 missing, 500 server error |
| **Response body** | JSON data or error message |

### Why agents care about status codes

The LLM should not “guess success.” Your **code** checks:

- 2xx → pass result back to the model  
- 4xx/5xx → pass a clear error (or retry/escalate), do not invent data  

---

## 3. Authentication & authorization (non-negotiable)

| Term | Plain English |
|------|----------------|
| **Authentication (AuthN)** | Prove who is calling (login / token / API key) |
| **Authorization (AuthZ)** | Prove they are allowed to do *this* action |

Agent-specific gotchas:

1. **Whose identity?** The end user vs a service account  
2. **Never put secrets in prompts** or tool descriptions the model can echo  
3. **Least privilege** — read-only tools vs write tools  
4. **Do not trust the LLM** to enforce permissions — check in the API/tool layer  

Example: Model asks to cancel a coworker’s leave → tool layer must reject if the user is not allowed.

---

## 4. JSON and schemas (why tool calling works)

Most tools exchange **JSON**:

```json
{
  "employee_id": "E123",
  "start_date": "2026-11-10",
  "end_date": "2026-11-12",
  "leave_type": "annual"
}
```

A **schema** describes allowed fields and types. Agent stacks use schemas so the model knows what arguments to fill.

| Bad tool design | Better |
|-----------------|--------|
| Free-text “do something in HR” | Narrow functions with clear params |
| Optional everything | Required fields for safe writes |
| Vague description | “Use when user asks for remaining annual leave days” |

**MCP** (later) standardizes how such tools/resources are exposed — but the *idea* is still API + schema.

---

## 5. Sync vs async, timeouts, retries

| Concept | Why it matters for agents |
|---------|---------------------------|
| **Timeout** | External API hangs → agent loop freezes without limits |
| **Retry** | Transient 503 → retry with backoff; do not retry unsafe POSTs blindly |
| **Idempotency** | Submitting leave twice should not create two requests |
| **Async jobs** | Long tasks return a job id; agent polls or waits |

Production agents need failure paths: retry → fallback → HITL → user-friendly error.

---

## 6. Read tools vs write tools

| Type | Risk | Examples |
|------|------|----------|
| **Read** | Privacy leak if over-broad | Get balance, search FAQ |
| **Write** | Irreversible side effects | Submit leave, send email, create ticket |

Design pattern:

- Allow reads more freely (still authz)  
- Gate writes with validation + sometimes **HITL**  

---

## 7. How the LLM “uses” an API (important mental model)

The LLM does **not** magically speak HTTP.

Your runtime does:

1. Model outputs: `submit_leave(start=..., end=...)`  
2. Your code validates args + auth  
3. Your code calls the real HTTP API  
4. Your code returns a short result string/JSON to the model  

So: **LLM chooses → code executes → LLM reads result.**

---

## 8. Common integration patterns in agent apps

| Pattern | Plain English |
|---------|----------------|
| **Direct SDK/API tools** | Python functions wrapping REST calls |
| **Gateway** | One place for auth, rate limits, logging |
| **MCP server** | Reusable tool/resource endpoint for many hosts |
| **Event / queue** | Agent enqueues work; workers finish later |
| **RAG retrieval** | Search docs, then LLM answers with snippets |

---

## 9. Error messages the model can use

Return tool errors that are **actionable**:

- Bad: `"Error"`  
- Better: `"Blackout period: leave not allowed 2026-12-24 to 2026-12-26. Suggest alternate dates."`

Good errors help the agent recover or ask the user a smart follow-up.

---

## 10. Security checklist for tool/API design

- [ ] Secrets in env/secret manager, not prompts  
- [ ] AuthZ on every write (and sensitive read)  
- [ ] Input validation (dates, ids, amounts)  
- [ ] Allowlist of tools per agent/role  
- [ ] Audit log: who triggered what tool when  
- [ ] Rate limits / budgets  
- [ ] PII minimization in logs and memory  

---

## 11. Tiny end-to-end example

**User:** “Book annual leave next Monday to Wednesday.”

1. LLM extracts dates → calls `validate_leave_request`  
2. API returns OK / blackout conflict  
3. If OK, LLM calls `submit_leave` (maybe after user confirm)  
4. API returns request id `LR-9081`  
5. LLM answers: “Submitted LR-9081 for Mon–Wed.”

Every valuable step after “understanding English” is an **API/tool**.

---

## How this maps to later I2I topics

| Later topic | API/tools connection |
|-------------|----------------------|
| Agent components | Tools are first-class parts of the app |
| Guardrails | Wrap tool execution |
| MCP | Standard tool/context protocol |
| A2A | Sometimes the “external system” is another agent |
| Production stack | Gateways, observability on each call |

---

## Study checklist

- [ ] Explain request/response and why status codes matter  
- [ ] Separate AuthN vs AuthZ with an agent example  
- [ ] Explain why the LLM never “directly” hits HTTP without your runtime  
- [ ] Contrast read vs write tool risk  
- [ ] List timeout/retry/idempotency concerns  
- [ ] Write one good tool error message example  

## Self-check questions

1. Where should permission checks live — prompt or tool layer? Why?  
2. What is a schema and why do agents need it?  
3. What goes wrong if a write tool is not idempotent?
