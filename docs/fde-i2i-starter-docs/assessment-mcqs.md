# Assessment — Medium to Complex MCQs (with answers)

Source: I2I Agentic AI Starter Guide concepts (study pack 01–10).

For the DOCX **prerequisites** (LLMs, APIs/tools, Python), use [`assessment-prerequisites-mcqs.md`](./assessment-prerequisites-mcqs.md) first.

**How to use:** Cover the **Answer** lines. Score yourself. Aim for ≥80% before claiming the guide is “understood.”

Legend: **(M)** medium · **(C)** complex

---

## Section A — Nuances, agents, agentic AI

**Q1 (M).** Why is “We use Agentic AI” often a weak statement in an architecture review?  
A. Agentic AI is illegal in enterprises  
B. Agentic capability is a spectrum; the statement does not specify autonomy, planning, tools, or collaboration  
C. Agentic AI only means multi-agent  
D. Agentic AI cannot use LLMs  

**Answer:** B

---

**Q2 (M).** Which best separates *agent*, *workflow*, and *platform*?  
A. They are synonyms  
B. Agent decides/acts; workflow structures steps/state; platform helps build/run them  
C. Platform is always the LLM vendor; workflow is the prompt  
D. Agent is only the UI  

**Answer:** B

---

**Q3 (C).** A team says their system is agentic because “the prompt says you are an autonomous agent.” What is the strongest critique?  
A. Prompts cannot mention agents  
B. Agency requires observable capabilities (planning, tool use, memory/adaptation, etc.), not wording alone  
C. Only multi-agent systems can be agentic  
D. They must use MCP to be agentic  

**Answer:** B

---

**Q4 (M).** A single tool-using chatbot that always follows: classify → FAQ search → answer is best described as:  
A. Strong multi-agent A2A mesh  
B. Relatively low on the agentic spectrum (mostly fixed workflow)  
C. Pure autonomous orchestration  
D. An MCP server  

**Answer:** B

---

**Q5 (C).** When is adding a second agent *least* justified?  
A. Legal and finance skills need separate ownership and systems  
B. Vendor agent must stay in another trust boundary  
C. One agent with three well-scoped tools already completes the task reliably  
D. Specialists need independent release cycles  

**Answer:** C

---

## Section B — Workflows and orchestration

**Q6 (M).** Workflow-driven orchestration primarily optimizes for:  
A. Maximum surprise in paths  
B. Predictability, auditability, and testable branches  
C. Eliminating the need for tools  
D. Removing the LLM entirely  

**Answer:** B

---

**Q7 (M).** Autonomous LLM orchestration is most appropriate when:  
A. Every step is legally prescribed and identical  
B. The task space is open-ended and useful paths cannot all be pre-encoded  
C. You must never call tools  
D. You need zero observability  

**Answer:** B

---

**Q8 (C).** An enterprise leave system must: verify identity, enforce blackout dates, submit to HRIS, then optionally draft a manager note. Best pattern?  
A. Fully free planner with no fixed steps  
B. Hybrid: deterministic rails for identity/policy/submit; LLM optional for drafting  
C. Three A2A agents with no schemas  
D. Memory-only system with no tools  

**Answer:** B

---

**Q9 (M).** An orchestrator agent’s main job is to:  
A. Replace all specialist tools with one megaprompt  
B. Decompose goals, delegate, merge results, decide stop/escalate  
C. Store API keys in the prompt  
D. Train the base model weekly  

**Answer:** B

---

**Q10 (C).** Which design-review question most directly reduces production incidents for agent workflows?  
A. Which font does the chat UI use?  
B. What is in state after each step, and what happens on tool failure / retry / HITL?  
C. Can we rename the agent to sound more autonomous?  
D. How many emojis should the agent use?  

**Answer:** B

---

## Section C — Components, tools, LLM role

**Q11 (M).** Which statement about tools is most accurate?  
A. Tool descriptions are unused by the LLM  
B. Name, description, and parameter schema heavily influence tool selection and call success  
C. One “do_everything” tool is always best  
D. Tools cannot perform write operations  

**Answer:** B

---

**Q12 (C).** A production incident shows the LLM called `delete_user` with a guessed id. Which control is *least* sufficient alone?  
A. Server-side authz + allowlist + confirmation/HITL for destructive tools  
B. Stronger wording in the system prompt only  
C. Schema validation and typed ids from trusted session context  
D. Audit logging of tool calls  

**Answer:** B  
*(Prompt-only control is insufficient; B is the weak/insufficient option.)*

---

**Q13 (M).** In a ReAct-style loop, “Observe” means:  
A. Looking at the user only once  
B. Incorporating tool results (or environment feedback) into the next reasoning step  
C. Retraining the model  
D. Deleting memory  

**Answer:** B

---

**Q14 (C).** Why might a system use a small model for routing and a larger model for planning?  
A. It is required by MCP  
B. Cost/latency tradeoffs: cheap classification vs stronger multi-step reasoning  
C. Small models cannot call tools  
D. Large models cannot follow schemas  

**Answer:** B

---

**Q15 (M).** Critical authorization for “submit leave” should live primarily in:  
A. Only the system prompt  
B. Application/tool layer with real authn/authz checks  
C. The marketing website  
D. The model card PDF  

**Answer:** B

---

## Section D — Memory and guardrails

**Q16 (M).** LLMs need external memory because:  
A. They automatically remember all users forever  
B. They are effectively stateless across calls unless context is provided/stored  
C. Memory replaces tools  
D. Memory removes the need for guardrails  

**Answer:** B

---

**Q17 (M).** Storing a user’s medical leave reason in long-term free-text memory without retention controls is mainly a risk to:  
A. CSS layout  
B. Privacy/compliance  
C. TCP window size  
D. Font licensing  

**Answer:** B

---

**Q18 (C).** Which guardrail placement best prevents a disallowed tool call even if the model requests it?  
A. Output style guide only  
B. Tool gateway enforcing allowlist, authz, and schema validation before execution  
C. Increasing temperature  
D. Longer system prompt with more adjectives  

**Answer:** B

---

**Q19 (M).** HITL is best described as:  
A. Proof the agent failed  
B. An intentional pause for human approval on high-impact actions  
C. A replacement for all tools  
D. Only used in demos  

**Answer:** B

---

**Q20 (C).** A support agent may draft emails freely but must get approval before sending externally. This is an example of:  
A. No guardrails  
B. Risk-tiered control: loose on reversible drafts, strict on irreversible side effects  
C. Autonomous A2A swarm  
D. Semantic memory  

**Answer:** B

---

**Q21 (M).** “Max tool calls / timeout” primarily guards against:  
A. Better UX fonts  
B. Runaway loops and cost/latency blowups  
C. MCP versioning  
D. Vector index rebuilds  

**Answer:** B

---

## Section E — MCP

**Q22 (M).** MCP’s primary purpose is:  
A. Training new foundation models  
B. Standardizing how agents/apps connect to tools and context sources  
C. Replacing all databases with prompts  
D. Agent-to-agent negotiation only  

**Answer:** B

---

**Q23 (M).** In MCP terminology, the component that exposes tools/resources is the:  
A. MCP Server  
B. Vector only store  
C. Browser cookie  
D. A2A card  

**Answer:** A

---

**Q24 (C).** Which statement is most accurate?  
A. Every prototype must start with MCP  
B. Ad-hoc local tools can be fine early; MCP value grows with reuse and multi-host integration  
C. MCP eliminates the need for auth  
D. MCP servers should trust all LLM-provided arguments without validation  

**Answer:** B

---

**Q25 (C).** An MCP server that can read arbitrary local files is exposed to a general employee chatbot. Biggest immediate concern?  
A. Color contrast  
B. Over-broad capability / data exfiltration risk without least privilege  
C. Lack of multi-agent  
D. Missing emoji reactions  

**Answer:** B

---

**Q26 (M).** MCP is *not*:  
A. A way to expose tools/resources  
B. A substitute for A2A agent collaboration protocol  
C. Useful for reusable enterprise connectors  
D. Something that can sit under an agent host  

**Answer:** B

---

## Section F — A2A and multi-agent

**Q27 (M).** A2A primarily addresses:  
A. Pixel rendering  
B. Agent-to-agent discovery, messaging, and collaboration  
C. GPU kernel fusion  
D. CSS animations  

**Answer:** B

---

**Q28 (C).** Correct complementary use of MCP and A2A:  
A. A2A for DB access; MCP for agent chat only  
B. A2A between agents; each agent uses MCP (or tools) to reach systems of record  
C. Never use both  
D. MCP replaces orchestrators entirely  

**Answer:** B

---

**Q29 (M).** An “agent card” concept is closest to:  
A. A credit card for tokens  
B. A public profile of an agent’s identity and capabilities  
C. A Docker image of PostgreSQL  
D. A UI theme  

**Answer:** B

---

**Q30 (C).** Two agents keep delegating the same task to each other indefinitely. Best mitigation set?  
A. Remove all schemas and hope  
B. Max hop count, clear ownership, structured task contracts, timeouts  
C. Increase temperature and parallelism  
D. Disable logging  

**Answer:** B

---

**Q31 (M).** Fan-out multi-agent pattern means:  
A. Only one agent may ever run  
B. Multiple agents work (often in parallel) and results are merged  
C. Deleting MCP servers  
D. Disabling HITL forever  

**Answer:** B

---

## Section G — Platforms and feature tiers

**Q32 (M).** Which is the best *must-have* before production tool-writing agents?  
A. Fancy multi-agent debate UI  
B. Authn/authz, tracing, timeouts, and guardrails on high-risk tools  
C. Ten memory types on day one  
D. Custom LLM pretrained from scratch  

**Answer:** B

---

**Q33 (C).** A team wants A2A + adaptive multi-agent planning before they have tool auth, traces, or evals. What should you recommend?  
A. Approve — protocols first always  
B. Reorder: secure tools + observability + evals first; add multi-agent when use case forces it  
C. Skip tools and only do A2A  
D. Replace evals with more prompt adjectives  

**Answer:** B

---

**Q34 (M).** “Should-have” production features typically include:  
A. Ignoring failures  
B. HITL gates, eval harness, cost controls, versioning  
C. Unauthenticated admin tools  
D. No logging  

**Answer:** B

---

**Q35 (C).** Choosing a low-code visual flow builder vs code-first graph library should mainly depend on:  
A. Which logo looks nicer  
B. Team skills, need for complex logic/testability, and enterprise constraints — not hype  
C. Whether MCP forbids low-code  
D. Whether A2A requires Python  

**Answer:** B

---

## Section H — Production stack

**Q36 (M).** An AI gateway’s main job is closest to:  
A. Centralizing model access: routing, keys, rate limits, fallbacks  
B. Storing employee salaries in prompts  
C. Drawing workflow diagrams only  
D. Replacing databases  

**Answer:** A

---

**Q37 (C).** RAG (retrieval) vs agent — which is correct?  
A. RAG alone is always a full agentic system  
B. RAG grounds answers with fetched knowledge; agents add planning/tool actions; they often combine  
C. Agents cannot use retrieval  
D. RAG replaces guardrails  

**Answer:** B

---

**Q38 (M).** Observability and evals differ because:  
A. They are the same thing  
B. Observability inspects live/historical runs; evals systematically score quality/regressions  
C. Evals only measure CPU temperature  
D. Observability forbids traces of tool calls  

**Answer:** B

---

**Q39 (C).** Which kill-switch design is most practical for a runaway agent?  
A. Hope the model stops  
B. Enforce max steps/tool calls, timeouts, budget caps, and admin cancel  
C. Delete the company wiki  
D. Disable HTTPS  

**Answer:** B

---

**Q40 (M).** Channel adapters (Slack/Teams/web) should ideally:  
A. Each reimplement business logic separately  
B. Reuse the same agent core behind different fronts  
C. Bypass auth for convenience  
D. Store secrets in chat messages  

**Answer:** B

---

## Section I — Scenario / synthesis (complex)

**Q41 (C).** You must design an HR assistant that answers policy questions and can submit leave. Stakeholders demand auditability. Which architecture statement is strongest?  
A. One unconstrained autonomous agent with file-system MCP and no logs  
B. Hybrid graph: retrieval for policy Q&A; deterministic validated path for leave submit with authz, HITL if needed, full traces + golden evals  
C. Five A2A agents debating every FAQ  
D. Prompt-only with no tools  

**Answer:** B

---

**Q42 (C).** A vendor provides an external “benefits specialist agent.” Your orchestrator should call it for niche questions. Which pairing fits the guide’s protocol split?  
A. Call vendor via A2A; your agent still uses MCP/tools for internal HRIS  
B. Put HRIS passwords in the vendor agent card  
C. Use only MCP to talk to the vendor agent (as if it were a person) and never authenticate  
D. Avoid schemas for cross-org calls  

**Answer:** A

---

**Q43 (C).** After a prompt tweak, tool-choice accuracy drops 20% but chat “sounds nicer.” What did the team skip?  
A. Font review  
B. Evaluation harness / regression checks on tool selection and task success  
C. Adding more agents immediately  
D. Removing observability  

**Answer:** B

---

**Q44 (C).** Which memory design is most appropriate for a bank’s agent?  
A. Save raw card PANs into semantic memory forever  
B. Prefer minimal retention, purpose-limited memory, encryption/access control, and avoid storing secrets; re-fetch sensitive data from systems of record when needed  
C. Mirror production DB into the prompt weekly  
D. Disable all session memory so fraud cannot be discussed  

**Answer:** B

---

**Q45 (C).** Deterministic vs non-deterministic: approving a wire transfer above threshold should be:  
A. Fully free-form LLM creativity  
B. Deterministic policy + authz (+ HITL), with LLM maybe drafting rationale — not inventing approval  
C. Random specialist agent vote without logs  
D. MCP resource read of a poem  

**Answer:** B

---

## Answer key (quick)

| Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|---|-----|
| 1 | B | 10 | B | 19 | B | 28 | B | 37 | B |
| 2 | B | 11 | B | 20 | B | 29 | B | 38 | B |
| 3 | B | 12 | B | 21 | B | 30 | B | 39 | B |
| 4 | B | 13 | B | 22 | B | 31 | B | 40 | B |
| 5 | C | 14 | B | 23 | A | 32 | B | 41 | B |
| 6 | B | 15 | B | 24 | B | 33 | B | 42 | A |
| 7 | B | 16 | B | 25 | B | 34 | B | 43 | B |
| 8 | B | 17 | B | 26 | B | 35 | B | 44 | B |
| 9 | B | 18 | B | 27 | B | 36 | A | 45 | B |

## Scoring guide

| Score | Meaning |
|-------|---------|
| 40–45 | Ready to explain the guide in reviews/interviews |
| 32–39 | Re-read weak sections (match Q → study file 01–09) |
| &lt; 32 | Do 01→10 in order again, then retry missed section |

### Map questions → study files

| Questions | Study file |
|-----------|------------|
| 1–5 | 01, 02 |
| 6–10 | 03 |
| 11–15 | 04 |
| 16–21 | 05 |
| 22–26 | 06 |
| 27–31 | 07 |
| 32–35 | 08 |
| 36–40 | 09 |
| 41–45 | 10 + all (synthesis) |
