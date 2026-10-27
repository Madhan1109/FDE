# 06 — MCP (Model Context Protocol) — plain English

## One-sentence definition

**MCP** is a standard way for AI apps/agents to connect to **tools and context sources** (files, APIs, DBs, SaaS) without inventing a custom integration format every time.

**Analogy:** USB for tools — plug in a “server” that offers capabilities; the agent (client) discovers and uses them.

---

## The problem MCP tries to solve

Without a shared protocol:

- Every agent framework invents its own tool JSON
- Every data source needs a bespoke connector
- Teams cannot reuse the same tool layer across products

MCP aims for **interoperable tool/context access**.

---

## Main roles

| Role | Plain English |
|------|----------------|
| **MCP Host** | The app that embeds the agent (IDE, chat app, orchestrator) |
| **MCP Client** | Component inside the host that speaks MCP |
| **MCP Server** | Exposes tools/resources/prompts to clients |

Flow:

```
User → Host/Agent → MCP Client → MCP Server → real system (API/DB/files)
```

---

## What an MCP server can expose

Typically:

1. **Tools** — callable actions (like functions)
2. **Resources** — readable context (docs, records)
3. **Prompts** — reusable prompt templates (when supported)

The agent does not hardcode every API shape; it **discovers** what the server offers.

---

## Why FDEs should care

- Faster to add enterprise systems behind a clean tool boundary
- Clearer security review: control what each server exposes
- Easier multi-agent platforms: shared tool catalog
- Better separation: **reasoning** (LLM) vs **capabilities** (servers)

---

## MCP vs “just write a Python tool”

| Approach | When it is fine |
|----------|-----------------|
| Local function tools | Small demos, one app, few tools |
| MCP servers | Many tools, multiple hosts, reuse across teams |

MCP is not mandatory for a first prototype. It becomes valuable as **integration surface area** grows.

---

## Security notes (do not skip)

- Treat MCP servers like APIs: auth, least privilege, audit logs
- Tool allowlists matter — do not expose admin delete by accident
- Validate arguments server-side (never trust the LLM alone)
- Be careful with servers that can read local files or secrets

---

## MCP is *not* A2A

| | MCP | A2A |
|--|-----|-----|
| Connects | Agent ↔ tools/context | Agent ↔ agent |
| Main unit | Tools/resources | Agent capabilities / tasks |
| Analogy | USB peripherals | Team collaboration protocol |

You often use **both**: agents talk via A2A; each agent uses tools via MCP.

---

## Study checklist

- [ ] Define MCP in one sentence
- [ ] Name host / client / server roles
- [ ] List what servers expose (tools, resources, prompts)
- [ ] Explain when MCP beats ad-hoc Python tools
- [ ] Contrast MCP vs A2A
