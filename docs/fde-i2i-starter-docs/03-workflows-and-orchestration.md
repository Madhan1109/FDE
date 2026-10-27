# 03 — Workflows and orchestration (plain English)

## What is a workflow here?

A **workflow** is a structured way to move from user request → done.

It usually has:

- **Nodes / steps** (classify, retrieve, call tool, ask human, reply)
- **State** (what we know so far: user id, partial results, flags)
- **Edges / routes** (what happens next: always-next, if/else, LLM chooses)
- **Start / end** conditions

**Plain analogy:** A flowchart that can call AI and tools at some boxes.

---

## Two big orchestration styles

### A) Workflow-driven (graph / state machine first)

You design the path (or limited branches) ahead of time.

| Pros | Cons |
|------|------|
| Predictable, easier audit | Less flexible for weird requests |
| Good for compliance | Can feel rigid |
| Easier testing of paths | New intents may need graph changes |

**Example:** Leave request must always: authenticate → validate dates → check policy → submit → confirm.

### B) Autonomous / LLM-orchestrated

The LLM (or planner agent) decides the next tool/agent at runtime.

| Pros | Cons |
|------|------|
| Flexible for open tasks | Harder to guarantee path |
| Less hardcoding of every branch | Needs strong guardrails + evals |
| Good for research / exploration | Cost and latency can spike |

**Example:** “Prepare a competitor brief” — agent decides which sources and how many loops.

### C) Hybrid (most enterprise builds)

- **Rails** for safety-critical steps (auth, PII, payments, approvals)
- **LLM freedom** inside safe zones (drafting, ranking, research)

**Takeaway:** Hybrid is not a compromise — it is usually the **right** design.

---

## Orchestrator role

An **orchestrator** (often an agent or graph node) is the “conductor”:

- Breaks the goal into steps
- Calls tools or specialist agents
- Merges results
- Decides when to stop or escalate to a human

Specialists stay focused (e.g., “policy lookup agent”, “ticket writer agent”).

---

## State and control flow (why FDEs care)

If you cannot answer these, production will hurt:

1. What is in **state** after each step?
2. What happens on **tool failure**?
3. When do we **retry** vs escalate?
4. When is a **human** required (HITL)?
5. How is the run **logged** for debugging?

---

## Mapping to common stacks (intuition only)

| Idea | Often seen as |
|------|----------------|
| Explicit graph + state | LangGraph-style |
| Visual low-code flows | Flowise-style |
| Memory-centric agents | Letta-style |
| Prompt + tools loop | Classic agent frameworks |

Platform names change; **graph vs free planner vs hybrid** stays useful.

---

## Study checklist

- [ ] Explain workflow-driven vs autonomous in plain words
- [ ] Give one reason enterprises prefer hybrid
- [ ] Describe what an orchestrator does
- [ ] List failure handling questions you should ask in a design review
