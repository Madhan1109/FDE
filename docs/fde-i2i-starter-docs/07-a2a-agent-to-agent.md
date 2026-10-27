# 07 — A2A (Agent-to-Agent) + using MCP together

## One-sentence definition

**A2A** is a way for **agents to discover, communicate, and collaborate** with other agents — often across products or vendors — using a shared protocol instead of one-off HTTP hacks.

**Analogy:** Agents exchanging business cards and work orders, not just calling each other’s private APIs in random formats.

---

## Why multi-agent needs a protocol

When Agent A wants Agent B to do something, they must agree on:

- Who are you and what can you do? (**capabilities / card**)
- How do I send a task?
- How do you report progress / results?
- How do we handle auth and errors?

Without standards, every pair of agents needs custom glue.

---

## Typical A2A ideas (conceptual)

| Concept | Plain English |
|---------|----------------|
| **Agent card / profile** | Public description: name, skills, endpoints |
| **Task / message** | Work request from one agent to another |
| **Artifacts / results** | Outputs returned (text, files, structured data) |
| **Streaming / updates** | Progress while long work runs |
| **Auth** | Prove identity and permission to call |

Exact field names vary by spec version; learn the **roles**, not every JSON key.

---

## Multi-agent patterns with A2A

1. **Delegate:** Orchestrator sends subtask to specialist agent  
2. **Ask:** Agent queries another agent for domain expertise  
3. **Handoff:** Conversation ownership moves to another agent  
4. **Parallel fan-out:** Several agents work, orchestrator merges  

---

## MCP + A2A together (important)

They solve different seams:

```
┌─────────────┐   A2A    ┌─────────────┐
│ Agent Alpha │◄────────►│ Agent Beta  │
└──────┬──────┘          └──────┬──────┘
       │ MCP                    │ MCP
       ▼                        ▼
  Tool servers               Tool servers
```

- **A2A:** who collaborates with whom  
- **MCP:** how each agent reaches systems of record  

**Interview-ready line:**  
“A2A coordinates agents; MCP supplies tools and context to each agent.”

---

## When you need multi-agent / A2A

Good reasons:

- Clear specialist skills (legal vs finance vs IT)
- Different owners/systems of record
- Separate scaling or release cycles
- Organizational boundaries (vendor agents)

Weak reasons:

- “Sounds cooler than one agent”
- One agent could do it with 3 tools

---

## Failure modes to watch

| Risk | Mitigation |
|------|------------|
| Infinite agent ping-pong | Max hops, clear ownership |
| Ambiguous task contracts | Structured schemas for requests/results |
| Security gaps | Auth between agents, audit trail |
| Latency/cost explosion | Budgets, caching, narrower tasks |

---

## Study checklist

- [ ] Define A2A in one sentence
- [ ] Explain agent card / task / result at a high level
- [ ] Draw MCP + A2A together
- [ ] Give one good and one bad reason to use multi-agent
- [ ] Name 2 multi-agent failure modes
