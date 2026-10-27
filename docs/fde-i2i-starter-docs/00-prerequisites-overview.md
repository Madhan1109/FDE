# 00 — Prerequisites (from the I2I guide)

The starter guide says that to benefit fully, you should already understand these **three** topics at a basic level:

| # | Prerequisite (exact idea from the guide) | Deep-dive file |
|---|------------------------------------------|----------------|
| 1 | **Large Language Models (LLMs)** — role as reasoning engines and decision-makers in AI agents | [00a-llm-fundamentals.md](./00a-llm-fundamentals.md) |
| 2 | **APIs and external tools** — how AI systems talk to outside data and services | [00b-apis-and-external-tools.md](./00b-apis-and-external-tools.md) |
| 3 | **Programming fundamentals** — Python (or similar) for hands-on agent work | [00c-python-for-agents.md](./00c-python-for-agents.md) |

## How to use

1. Finish **00a → 00c** before (or alongside) files `01`–`10`
2. If you already know one topic well, skim that file and focus on the others
3. For broader Java→Python practice, also use [`../python-upskilling/README.md`](../python-upskilling/README.md) — **00c** is the agent-focused slice

## Why the guide lists them

| Without this… | You will struggle with… |
|---------------|-------------------------|
| LLMs | Prompts, tool choice, hallucinations, token limits, model roles |
| APIs / tools | Schemas, auth, errors, MCP-style tool servers |
| Programming | Implementing loops, calling APIs, wiring LangGraph/FastAPI demos |

**These three were not covered as separate deep files in the first study pack.** That gap is what `00a`–`00c` fix.
