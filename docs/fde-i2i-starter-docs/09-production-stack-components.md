# 09 — Production stack plug-ins (plain English)

Beyond “LLM + tools”, real deployments add supporting pieces. The starter guide’s OSS/stack tables map to ideas like these:

## Gateway / AI gateway

**What:** Central place for model calls (routing, keys, rate limits, fallbacks).  
**Why:** Do not scatter API keys and model names across every service.

## Orchestration / workflow engine

**What:** Runs graphs, state, retries, human gates.  
**Why:** Control and visibility over multi-step work.

## Tool layer / MCP servers

**What:** Controlled actions into enterprise systems.  
**Why:** Clean boundary for security and reuse.

## Memory store

**What:** DB/vector/kv store for session or long-term memory.  
**Why:** Continuity without stuffing huge history every time.

## Retrieval (RAG or search)

**What:** Fetch knowledge (vector DB, BM25, hybrid).  
**Why:** Ground answers in approved content. (RAG ≠ agent by itself.)

## Guardrail / policy engine

**What:** Filters and rules around inputs, outputs, tools.  
**Why:** Enforce what prompts cannot guarantee.

## Observability (traces / logs / metrics)

**What:** Per-run timeline: prompts, tool calls, latencies, errors.  
**Why:** Debug “why did the agent do that?”

## Evaluation harness

**What:** Automated tests on golden questions, tool-choice accuracy, safety cases.  
**Why:** Prompt/model changes break things silently.

## HITL / approval UI

**What:** Human review queue for risky actions.  
**Why:** Safe autonomy for enterprise.

## Identity & secrets

**What:** SSO, service accounts, secret managers.  
**Why:** Agents act *as someone* — that must be explicit.

## Channel adapters

**What:** Slack, Teams, web chat, API.  
**Why:** Same agent core, many fronts.

---

## How pieces connect (simple)

```
Channels → API → Orchestrator/Agent
                    ├─ LLM via Gateway
                    ├─ Memory store
                    ├─ Retrieval
                    ├─ Tools / MCP
                    ├─ Guardrails
                    └─ HITL queue
         Observability + Evals wrap the whole path
```

---

## FDE design review checklist

- [ ] Where do model keys live?
- [ ] Which tools are write vs read?
- [ ] What is logged (and is PII redacted)?
- [ ] What is the eval set before release?
- [ ] What requires human approval?
- [ ] What is the kill switch / max-step limit?

---

## Study checklist

- [ ] Explain gateway vs orchestrator in one line each
- [ ] Differentiate RAG and agenting
- [ ] Name observability vs evals (different jobs)
- [ ] List identity concerns for tool-calling agents
