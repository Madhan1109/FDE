# 01 — Intro and Agentic AI nuances (plain English)

## What this guide is for

The I2I Agentic AI Starter Guide is a **shared language** for building agent systems at work. It covers:

- What agents and agentic systems are
- How workflows and orchestration work
- Core pieces: LLM, tools, memory, guardrails
- Protocols: **MCP** (agent ↔ tools) and **A2A** (agent ↔ agent)
- Platforms and production features

You do **not** need to memorize every product name. Focus on the **ideas**.

---

## Nuance 1 — Agentic AI is not one fixed thing

“Agentic AI” is a **spectrum**, not a checkbox.

| Level | What it feels like | Example |
|-------|--------------------|---------|
| Low | Fixed steps, little choice | A script that always: classify → search FAQ → reply |
| Medium | Some planning + tool choice | Agent picks which tool based on the question |
| High | Multi-step planning, memory, other agents | Orchestrator plans, calls specialist agents, retries, remembers user |

**Takeaway:** Saying “we use Agentic AI” is vague. Say *how much autonomy, planning, and collaboration* you have.

---

## Nuance 2 — Agent vs Workflow vs Platform

People mix these words. Keep them separate:

| Word | Plain meaning |
|------|----------------|
| **Agent** | Software that uses an LLM to decide and act (often with tools) |
| **Workflow** | Ordered steps (graph/state machine) that may include agents |
| **Platform** | Product/framework that helps you build agents/workflows (LangGraph, Flowise, Letta, etc.) |

An agent can sit *inside* a workflow. A platform can run many workflows.

---

## Nuance 3 — Deterministic vs non-deterministic

| Style | Behavior | When useful |
|-------|----------|-------------|
| **Deterministic** | Same inputs → same path | Compliance, payments, regulated steps |
| **Non-deterministic** | LLM chooses path; can vary | Research, open-ended support, creative tasks |

Most real systems are **hybrid**: fixed rails for safety + LLM flexibility where it helps.

---

## Nuance 4 — Tools are not “magic”

An agent is only as useful as:

1. **What tools it can call** (APIs, DB, search, email…)
2. **How clearly tools are described** (name, inputs, outputs — the *schema*)
3. **Whether calls are allowed** (permissions + guardrails)

Without good tools and schemas, the LLM just chatters.

---

## Nuance 5 — Protocols matter at scale

When you grow beyond one agent + a few tools:

- **MCP** = standard way for agents to discover and use tools/context
- **A2A** = standard way for agents to talk to other agents

You can build without them (custom APIs). Protocols help when many teams and vendors must interoperate.

---

## Study checklist

- [ ] I can explain agentic AI as a **spectrum**
- [ ] I can separate agent / workflow / platform in one sentence each
- [ ] I know why hybrid (deterministic + LLM) is common
- [ ] I know tools + schemas are as important as the model
- [ ] I know MCP ≈ tools, A2A ≈ agents (preview; detail in 06–07)
