# 10 — Quick revision cheatsheet

## Definitions

| Term | One-liner |
|------|-----------|
| **AI agent** | LLM-driven system that can decide and act (often via tools) |
| **Agentic AI** | Agents with planning, dynamic tool use, memory, adaptation (spectrum) |
| **Multi-agent** | Multiple agents collaborating with roles |
| **Workflow** | Structured steps + state + routing |
| **MCP** | Protocol for agent ↔ tools/context |
| **A2A** | Protocol for agent ↔ agent |
| **Guardrail** | Hard check keeping behavior safe/valid |
| **HITL** | Human approval step inside the flow |
| **ReAct** | Reason → Act (tool) → Observe → repeat |

## Spectrum reminder

`Scripted bot → tool-using agent → agentic planner → multi-agent system`

## Orchestration

- **Workflow-driven:** predictable paths  
- **Autonomous:** LLM chooses next step  
- **Hybrid:** rails + freedom (usual enterprise choice)

## Must remember

1. Tools + schemas ≈ product quality  
2. Security ≠ system prompt alone  
3. Memory is optional until needed; privacy matters  
4. MCP ≠ A2A  
5. More agents ≠ better  
6. Ship: tools → guardrails → observability → evals → then fancy multi-agent  

## Interview 30-second pitch

“We build hybrid agentic systems: deterministic workflows for compliance-critical steps, LLM agents for flexible reasoning, narrow authenticated tools (optionally via MCP), guardrails and HITL on writes, and traces plus golden evals so changes don’t silently regress. Multi-agent or A2A only when specialist ownership truly requires it.”
