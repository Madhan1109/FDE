# 00a — Large Language Models (LLMs) — deep dive (plain English)

**Guide prerequisite:** *LLMs — their role as reasoning engines and decision-makers in AI agents.*

This file goes deeper than “ChatGPT answers questions.” You need this to understand everything after file `01`.

---

## 1. What an LLM actually is

An LLM is a model trained to predict the **next token** (roughly: next piece of text) given previous text.

It does **not** “know the truth” or “run your company systems.” It generates plausible text based on patterns from training + whatever you put in the prompt/context.

| Myth | Reality |
|------|---------|
| “The model remembers our last chat forever” | Only if *your app* stores and resends history |
| “The model can call our HR database by itself” | Only if *you* give it a tool/API and allow the call |
| “If it sounds confident, it is correct” | Confidence ≠ correctness (**hallucination**) |

**Plain analogy:** A very skilled intern who writes and reasons from notes you hand them — but invents details if notes are missing.

---

## 2. Why agents treat the LLM as a “reasoning engine”

In agent systems, the LLM is often used to:

1. **Understand** the user request (intent)
2. **Plan** steps (“first check leave balance, then submit”)
3. **Decide** which tool to call and with what arguments
4. **Interpret** tool results
5. **Write** the final answer or next question

That is the “decision-maker” role the guide mentions — **not** because the model is a database, but because it chooses among actions when given options (tools, policies, state).

```
User message + system rules + tool list + memory
                    ↓
                 LLM
                    ↓
     “call tool X with args…”  OR  “final answer…”
```

---

## 3. Tokens, context window, and cost

| Term | Plain meaning |
|------|----------------|
| **Token** | Chunk of text the model reads/writes (not always one word) |
| **Context window** | Max tokens the model can see at once (prompt + history + tool results) |
| **Input / output tokens** | What you send vs what the model generates (both cost money) |

**Agent implication:** Long chats + big tool dumps fill the window. You must truncate, summarize, or retrieve only what matters (this connects to **memory** and **RAG** later).

---

## 4. Temperature and “determinism”

| Setting | Effect |
|---------|--------|
| **Low temperature** | More repeatable, safer for tool JSON / classification |
| **Higher temperature** | More varied wording; worse for strict schemas |

For tool calling and routing, teams often prefer **lower temperature**. For creative drafting, higher can be fine.

Even at temperature 0, behavior can still vary slightly across providers/versions — do not assume bit-identical runs.

---

## 5. Prompts that matter for agents

| Layer | Purpose |
|-------|---------|
| **System prompt** | Role, rules, style, high-level policy |
| **Developer / tool schemas** | Exact tool names, params, descriptions |
| **User message** | The request |
| **Conversation / tool history** | What already happened this run |

**Critical:** Soft rules in the prompt can be ignored. Hard rules (auth, money moves) belong in **code/guardrails**, not only in the prompt.

Good tool descriptions are as important as the system prompt — the model uses them to decide *when* to call a tool.

---

## 6. Tool calling / function calling (core for agents)

Modern APIs let the model return a structured “I want to call function F with args …” instead of only chat text.

Typical cycle:

1. App sends messages + tool definitions  
2. Model returns a **tool call**  
3. App **executes** the real API/DB function  
4. App sends the **result** back as a message  
5. Model continues until it produces a final answer  

Without this loop, you mostly have a chatbot, not an acting agent.

---

## 7. Hallucinations and grounding

**Hallucination** = model invents facts, ids, policy text, or tool results.

Mitigations used in agentic apps:

- Retrieve approved docs (**RAG** / search) before answering
- Prefer tool results over model memory for live data
- Cite sources
- Validate structured outputs against schemas
- Eval sets that catch made-up answers

---

## 8. Model roles in a real stack

You often use **more than one** model:

| Role | Typical job | Why |
|------|-------------|-----|
| Router / classifier | Detect intent, language | Cheap & fast |
| Planner / main agent | Multi-step reasoning + tools | Stronger model |
| Draft rewriter | Tone / summary | Medium |
| Embeddings model | Vectors for search | Not a chat LLM |

The guide’s “LLM as decision-maker” often means the **planner/agent** model, not every model in the system.

---

## 9. Limits you must design around

1. **No private live data** unless retrieved or tool-fetched  
2. **Context length** — cannot paste entire company wiki every turn  
3. **Latency** — each reasoning/tool round trip costs time  
4. **Cost** — agent loops multiply token usage  
5. **Non-determinism** — same prompt can yield different plans  
6. **Safety** — prompt injection can try to override instructions  

---

## 10. How this maps to later I2I topics

| Later topic | LLM connection |
|-------------|----------------|
| Agent vs agentic | LLM plans and chooses tools/agents |
| Workflows | LLM may sit inside graph nodes or drive routing |
| Memory | Extra context fed into the LLM each turn |
| Guardrails | Filters before/after the LLM and around tools |
| MCP | Standardized way to offer tools/context *to* the LLM host |
| Evals | Measure whether the LLM picks right tools and answers |

---

## Mini examples (mental models)

**Good agent use of LLM**  
User: “What’s my leave balance?”  
LLM decides → call `get_leave_balance(user_id)` → answer from tool result.

**Bad use**  
User asks balance → LLM invents “12 days” from training patterns with no tool call.

---

## Study checklist

- [ ] Explain LLM as next-token predictor in one sentence  
- [ ] List 4 jobs an LLM does inside an agent  
- [ ] Explain context window impact on agents  
- [ ] Describe one tool-call round trip  
- [ ] Name 3 ways to reduce hallucinations  
- [ ] Explain why auth must not live only in the system prompt  

## Self-check questions

1. Why can a confident answer still be wrong?  
2. What does the app do between two LLM calls in a tool loop?  
3. When would you use a small model vs a large one?
