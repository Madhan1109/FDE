# 05 — Memory and Guardrails (plain English)

## Why memory exists

LLMs are **stateless** by default: each call only sees what you put in the prompt.

**Memory** is how the system keeps useful information across turns or sessions so the agent does not re-ask everything or forget decisions.

---

## Common memory types

| Type | Plain English | Example |
|------|----------------|---------|
| **Short-term / working** | Current conversation + scratchpad | Last 10 messages, current tool results |
| **Episodic** | What happened in past sessions | “Last week user asked about parental leave” |
| **Semantic / long-term facts** | Stable knowledge about user or domain | Preferred language, team, role |
| **Procedural** | How this agent should work | Preferred tool order, playbooks |
| **Shared / team memory** | Facts multiple agents can read | Case id, approved budget |

Not every product needs all types. Start with **session memory**, add long-term only when it clearly helps.

---

## Memory design questions

1. What must be remembered vs recomputed?
2. How long do we keep it? (TTL / retention)
3. Who can read it? (privacy)
4. How do we **update or forget** wrong memories?
5. Is memory injected into the prompt, retrieved on demand, or both?

**Risk:** Storing sensitive HR/health data in free-text memory without controls.

---

## Guardrails — what they are

**Guardrails** are checks that keep the agent inside safe and useful bounds.

Think: seatbelts + traffic rules, not the engine.

---

## Guardrail categories

| Category | Stops / enforces | Example |
|----------|------------------|---------|
| **Input** | Bad/unsafe user input | Block prompt-injection patterns, jailbreaks |
| **Output** | Bad model text | Redact secrets, block toxic content |
| **Tool** | Dangerous actions | Require manager approval before cancel leave |
| **Policy / business** | Domain rules | Cannot approve own expenses |
| **Scope** | Off-topic / unauthorized | HR bot refuses payroll admin for non-admins |
| **Cost / loop** | Runaway agents | Max tool calls, max tokens, timeouts |

---

## Where guardrails sit

Often in layers:

1. **Before LLM** — validate/sanitize input
2. **Around tools** — authz, schema validation, allowlists
3. **After LLM** — filter output, groundedness checks
4. **In workflow** — mandatory human steps for high risk

---

## HITL (Human-in-the-loop)

For high-impact actions, the agent **pauses** and asks a human:

- Approve refund > $X
- Send external email
- Change production config

This is a **feature**, not a failure of autonomy.

---

## Balance: safety vs usefulness

Too few guardrails → incidents.  
Too many → agent that cannot do anything useful.

Good design: **strict on irreversible actions**, looser on draft/read-only tasks.

---

## Study checklist

- [ ] Name 3 memory types with examples
- [ ] Explain why LLMs need external memory
- [ ] List input / output / tool guardrail examples
- [ ] Explain when HITL is the right design
