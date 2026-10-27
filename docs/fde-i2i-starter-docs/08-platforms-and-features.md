# 08 — Agentic platforms + must / should / could features

## What a platform gives you

An **agentic platform** (framework or product) helps you avoid rebuilding:

- Agent loop / workflow engine
- Tool registration
- State & memory hooks
- UI or APIs to run agents
- Sometimes: evals, tracing, deployment

Examples you may hear (names change over time): **LangGraph**, **Flowise**, **Letta**, and similar. Learn by **capability**, not brand loyalty.

---

## How to compare platforms (FDE lens)

Ask:

1. Graph/workflow control or free-form agents?
2. Memory model depth?
3. Tooling / MCP support?
4. Observability & evals built-in?
5. Deploy story (local, cloud, enterprise SSO)?
6. Team skill fit (code-first vs low-code)?

---

## Feature tiers from the starter guide mindset

### Must-have (do not ship without)

| Feature | Why |
|---------|-----|
| Tool calling with schemas | Agents that cannot act are demos |
| AuthN/AuthZ for tools & data | Enterprise baseline |
| Logging / tracing of runs | You cannot debug blind |
| Guardrails on high-risk actions | Prevent irreversible harm |
| Error handling / timeouts | Agents loop and fail |

### Should-have (serious production)

| Feature | Why |
|---------|-----|
| Persistent memory (as needed) | Better UX across sessions |
| Human-in-the-loop gates | Approvals for sensitive actions |
| Evaluation harness | Catch regressions when prompts change |
| Cost/latency controls | Budget runaway agents |
| Versioning of prompts/graphs | Rollback when quality drops |

### Could-have (advanced / scale)

| Feature | Why |
|---------|-----|
| Multi-agent / A2A | Cross-team or specialist collaboration |
| MCP tool mesh | Reusable enterprise connectors |
| Advanced adaptive planning | Hard open-ended tasks |
| Rich analytics / simulation | Portfolio of agents at scale |

**Rule:** Ship must-haves first. Do not start with exotic multi-agent if a single agent + tools solves the use case.

---

## Choosing workflow style on a platform

| Need | Lean toward |
|------|-------------|
| Auditable business process | Explicit graph / workflow-driven |
| Open research / exploration | More autonomous planner |
| Regulated + flexible UX | Hybrid |

---

## Practical build order (recommended)

1. One use case, clear success metric  
2. Tools + schemas + auth  
3. Simple workflow or agent loop  
4. Guardrails + HITL for writes  
5. Observability + golden eval set  
6. Memory only if pain is real  
7. Multi-agent / MCP / A2A when integration needs force it  

---

## Study checklist

- [ ] List 5 must-have features without looking
- [ ] Explain should-have vs could-have with examples
- [ ] Compare two platforms using the FDE questions above
- [ ] Recite a sane build order for a first enterprise agent
