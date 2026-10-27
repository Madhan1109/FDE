# 02 — AI Agent vs Agentic AI vs Multi-agent (plain English)

## The three ideas (keep them straight)

### 1) AI Agent (single agent)

A **single** system that:

- Takes a goal or user message
- Uses an **LLM** to reason
- May call **tools** (search, APIs, DB)
- Returns an answer or takes an action

**Plain analogy:** One smart employee with a toolkit.

**Typical loop (ReAct-style):**

1. Think (“I need the leave balance”)
2. Act (call `get_leave_balance`)
3. Observe (tool result)
4. Repeat or answer

---

### 2) Agentic AI (capability style)

**Agentic** means the system behaves with more **agency**:

- **Plans** multi-step work (not one shot)
- **Chooses** tools or next steps dynamically
- **Remembers** useful context (session / long-term)
- **Adapts** when something fails (retry, different tool)
- May **delegate** to other agents

**Plain analogy:** Not just answering questions — owning the job until done (within rules).

So: every agentic system uses agents, but not every “chatbot with one tool” is strongly agentic.

---

### 3) Multi-agent workflow

Several agents (or agent roles) cooperate:

| Pattern | Plain English |
|---------|----------------|
| **Orchestrator + specialists** | Manager agent breaks work; specialists do pieces |
| **Pipeline** | Agent A → Agent B → Agent C in order |
| **Peer / swarm** | Agents discuss or vote (less common in enterprise) |
| **Hierarchical** | Supervisors manage worker agents |

**Plain analogy:** A team with roles, not one person doing everything.

---

## Side-by-side comparison

| | Single AI agent | Strongly agentic system | Multi-agent |
|--|-----------------|-------------------------|-------------|
| Actors | One agent | One or many | Many |
| Planning | Simple / short | Multi-step, dynamic | Often split across agents |
| Tools | Own tools | Tools + maybe other agents | Each may have tools |
| Memory | Optional | Usually important | Shared + private memory |
| Hard part | Tool design | Control + reliability | Coordination + contracts |

---

## What “good” looks like in demos / interviews

Say clearly:

1. **Who decides** the next step? (fixed graph vs LLM planner)
2. **What can it call?** (tools / other agents)
3. **What must stay fixed?** (policy, approvals, audit)
4. **How do you know it worked?** (evals, logs, traces)

---

## Common confusion to avoid

| Wrong shorthand | Better |
|-----------------|--------|
| “We have Agentic AI” | “We have a LangGraph workflow with an orchestrator agent and two tool-using specialists” |
| “Multi-agent = smarter” | More agents can mean more failure modes; use them when roles truly differ |
| “LLM alone = agent” | Agent usually implies **action** via tools or environment, not only text |

---

## Study checklist

- [ ] Define AI agent in one sentence
- [ ] List 3 traits that make a system more *agentic*
- [ ] Give one multi-agent pattern with a business example
- [ ] Explain why more agents ≠ automatically better
