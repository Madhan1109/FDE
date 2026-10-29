"""Generate professional I2I summary + 50-MCQ PDFs (fpdf2)."""
from pathlib import Path
from fpdf import FPDF

OUT = Path(__file__).resolve().parent


class DocPDF(FPDF):
    def __init__(self, title: str):
        super().__init__(format="Letter")
        self.doc_title = title
        self.set_auto_page_break(auto=True, margin=18)
        self.set_margins(16, 16, 16)

    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(90, 90, 90)
        self.cell(0, 6, self.doc_title, align="L")
        self.ln(8)
        self.set_draw_color(200, 200, 200)
        self.line(16, self.get_y(), 200, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-14)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, f"Page {self.page_no()}/{{nb}}", align="C")

    def _mc(self, h: float, text: str, **kwargs):
        self.set_x(self.l_margin)
        self.multi_cell(0, h, text, new_x="LMARGIN", new_y="NEXT", **kwargs)

    def h1(self, text: str):
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(20, 40, 70)
        self._mc(8, text)
        self.ln(2)

    def h2(self, text: str):
        self.ln(2)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(30, 60, 100)
        self._mc(6, text)
        self.ln(1)

    def h3(self, text: str):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(40, 40, 40)
        self._mc(5, text)
        self.ln(0.5)

    def body(self, text: str):
        self.set_font("Helvetica", "", 9.5)
        self.set_text_color(30, 30, 30)
        self._mc(5, text)
        self.ln(1)

    def bullet(self, text: str, indent: float = 4):
        self.set_font("Helvetica", "", 9.5)
        self.set_text_color(30, 30, 30)
        self.set_x(self.l_margin + indent)
        w = self.w - self.r_margin - self.l_margin - indent
        self.multi_cell(w, 5, f"- {text}", new_x="LMARGIN", new_y="NEXT")

    def bold_line(self, label: str, text: str):
        self.set_font("Helvetica", "B", 9.5)
        self.set_text_color(30, 30, 30)
        self._mc(5, f"{label} {text}")
        self.set_font("Helvetica", "", 9.5)

    def rule(self):
        self.ln(1)
        self.set_draw_color(180, 180, 180)
        y = self.get_y()
        self.line(16, y, 200, y)
        self.ln(3)


def build_summary() -> Path:
    pdf = DocPDF("I2I Agentic AI Starter Guide - Executive Summary")
    pdf.alias_nb_pages()
    pdf.add_page()

    # Cover block
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(20, 40, 70)
    pdf._mc(9, "I2I Agentic AI Starter Guide")
    pdf.set_font("Helvetica", "B", 13)
    pdf._mc(7, "Executive Study Summary")
    pdf.ln(1)
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(80, 80, 80)
    pdf._mc(
        5,
        "A concise reference distilled from the I2I Agentic AI Starter Guide (FDE). "
        "Intended for quick revision and shared learning across the team.",
    )
    pdf.rule()

    pdf.h2("1. Purpose and Prerequisites")
    pdf.body(
        "The starter guide provides a shared language for designing and building agentic systems: "
        "single agents, multi-agent collaboration, workflows, tools, memory, guardrails, and protocols "
        "(MCP and A2A). Before deep implementation work, readers should understand three foundations:"
    )
    pdf.bullet("Large Language Models (LLMs) as reasoning and decision engines inside agents.")
    pdf.bullet("APIs and external tools - how agents reach live systems of record.")
    pdf.bullet("Programming fundamentals (typically Python) for hands-on agent loops and integrations.")

    pdf.h2("2. Core Distinctions (Agentic Nuances)")
    pdf.bold_line("AI Agent:", "A single LLM-driven system that can decide and act, usually via tools.")
    pdf.bold_line(
        "Agentic AI:",
        "A capability style/spectrum: planning, dynamic tool or agent choice, memory, adaptation, "
        "and often collaboration - not merely a fixed script.",
    )
    pdf.bold_line(
        "Multi-agent workflow:",
        "Multiple agents with roles (orchestrator + specialists, pipeline, hierarchical). "
        "More agents are not automatically more intelligent.",
    )
    pdf.body(
        "Important nuance: a fixed A->B->C multi-agent pipeline without autonomous decision-making "
        "is workflow automation, not true agentic intelligence. Use a single agent for linear tasks "
        "(FAQ, one-step API). Use agentic designs for multi-step, open-ended, cross-domain work. "
        "Avoid over-engineering simple problems."
    )
    pdf.body(
        "Spectrum: Scripted bot -> tool-using agent -> agentic planner -> multi-agent system."
    )

    pdf.h2("3. Orchestration Styles")
    pdf.bullet(
        "Workflow-driven: predefined graph/state machine - predictable, auditable, easier to test."
    )
    pdf.bullet(
        "Autonomous / LLM-orchestrated: the model chooses next tools or agents at runtime - flexible, harder to guarantee."
    )
    pdf.bullet(
        "Hybrid (usual enterprise choice): deterministic rails for identity, policy, and writes; "
        "LLM freedom for drafting, ranking, and research."
    )
    pdf.body(
        "An orchestrator decomposes goals, delegates to tools or specialists, merges results, "
        "and decides when to stop or escalate (including human-in-the-loop)."
    )

    pdf.h2("4. Application Building Blocks")
    pdf.body(
        "Typical stack: Channel/UI -> Orchestration -> Agent(s) <-> Memory -> Tools/MCP/other agents (A2A) "
        "-> Systems of record. Cross-cutting concerns: guardrails, observability, evaluations, and identity."
    )
    pdf.bullet(
        "LLM roles: understand intent, plan, select tools, fill arguments, synthesize answers, stop/continue/ask."
    )
    pdf.bullet(
        "Tools: name, description, parameter schema, implementation, permissions. Narrow reliable tools beat one mega-tool."
    )
    pdf.bullet(
        "ReAct-style loop: Reason -> Act (tool) -> Observe -> repeat until final answer or escalation."
    )
    pdf.bullet(
        "Critical security rule: authorization and irreversible actions must be enforced in code/tool layers, "
        "not only in the system prompt."
    )

    pdf.h2("5. Memory and Guardrails")
    pdf.body(
        "LLMs are effectively stateless across calls. Memory types include short-term/working context, "
        "episodic session history, semantic long-term facts, procedural playbooks, and shared team memory. "
        "Start with session memory; add long-term only when clearly valuable - and protect privacy/retention."
    )
    pdf.body(
        "Guardrails constrain unsafe or invalid behavior: input filters, output filters, tool allowlists and AuthZ, "
        "business policy checks, scope limits, and cost/loop limits (max tool calls, timeouts). "
        "HITL (human-in-the-loop) is intentional for high-impact actions - not a failure of autonomy. "
        "Prefer risk-tiered autonomy: freer on read/draft; stricter on write/send/pay."
    )

    pdf.add_page()
    pdf.h2("6. MCP (Model Context Protocol)")
    pdf.body(
        "MCP standardizes how AI hosts/agents connect to tools and context sources (files, APIs, databases, SaaS) "
        "without inventing a custom integration format every time. Analogy: USB for capabilities."
    )
    pdf.bullet("Roles: Host (app), Client (speaks MCP), Server (exposes tools/resources/prompts).")
    pdf.bullet("Local function tools are fine for small prototypes; MCP value grows with reuse across teams and hosts.")
    pdf.bullet(
        "Security: treat MCP servers like APIs - authentication, least privilege, server-side validation, audit logs."
    )

    pdf.h2("7. A2A (Agent-to-Agent) and Combined Use")
    pdf.body(
        "A2A addresses discovery, messaging, and collaboration between agents (capabilities/cards, tasks, results, "
        "progress updates, auth). Use multi-agent/A2A when specialist skills, system ownership, or organizational "
        "boundaries require it - not because it sounds advanced."
    )
    pdf.bold_line(
        "Complementary split:",
        "A2A coordinates agents; MCP (or equivalent tools) supplies each agent with systems access.",
    )
    pdf.bullet("Failure modes: agent ping-pong, ambiguous contracts, auth gaps, latency/cost explosion.")
    pdf.bullet("Mitigations: max hops, clear ownership, structured schemas, timeouts, budgets.")

    pdf.h2("8. Platforms and Feature Tiers")
    pdf.body(
        "Compare platforms by workflow control, memory depth, tool/MCP support, observability/evals, "
        "deployment/SSO fit, and team skill (code-first vs low-code) - not by brand alone."
    )
    pdf.h3("Must-have before production")
    pdf.bullet("Tool calling with schemas; AuthN/AuthZ; logging/tracing; guardrails on high-risk actions; timeouts/error handling.")
    pdf.h3("Should-have")
    pdf.bullet("Appropriate memory; HITL gates; evaluation harness; cost/latency controls; versioning of prompts/graphs.")
    pdf.h3("Could-have / scale")
    pdf.bullet("Multi-agent/A2A, MCP tool mesh, advanced adaptive planning, richer analytics.")
    pdf.body(
        "Recommended build order: one use case and metric -> tools + auth -> simple loop/workflow -> "
        "guardrails/HITL -> observability + golden evals -> memory if needed -> multi-agent/MCP/A2A when forced by integration needs."
    )

    pdf.h2("9. Production Stack Essentials")
    pdf.bullet("AI gateway: centralized model access, keys, rate limits, fallbacks.")
    pdf.bullet("Orchestration engine: graphs, state, retries, human gates.")
    pdf.bullet("Retrieval (RAG/search): grounds answers in approved content - RAG alone is not a full agent.")
    pdf.bullet("Observability: per-run traces of prompts, tools, latency, errors.")
    pdf.bullet("Evals: regression checks on task success, tool choice, safety - distinct from live tracing.")
    pdf.bullet("Identity and secrets: agents act as someone; make that explicit and auditable.")

    pdf.h2("10. Key Takeaways for Design Reviews")
    pdf.bullet("Say how much autonomy you have - do not stop at 'we use Agentic AI'.")
    pdf.bullet("Prefer hybrid rails for compliance-critical steps.")
    pdf.bullet("Tool/schema quality and AuthZ often matter more than model upgrades.")
    pdf.bullet("MCP != A2A; more agents != better.")
    pdf.bullet("Ship tools, guardrails, observability, and evals before exotic multi-agent designs.")

    pdf.h2("11. Quick Reference Glossary")
    pdf.bold_line("ReAct:", "Reason -> Act (tool) -> Observe -> repeat.")
    pdf.bold_line("HITL:", "Human-in-the-loop approval for high-impact actions.")
    pdf.bold_line("Guardrail:", "Hard check that keeps behavior safe and valid (input, output, tool, policy, cost).")
    pdf.bold_line("ACI:", "Agent-Computer Interface - treat tool design like clear API design for the model.")
    pdf.bold_line(
        "Hallucination:",
        "Model invents facts; mitigate with tools for live data, retrieval for approved docs, schemas, and evals.",
    )

    pdf.h2("12. One-Paragraph Design Pitch")
    pdf.body(
        "We build hybrid agentic systems: deterministic workflows for compliance-critical steps, "
        "LLM agents for flexible reasoning, narrow authenticated tools (optionally via MCP), "
        "guardrails and HITL on writes, and traces plus golden evals so changes do not silently regress. "
        "Multi-agent or A2A is introduced only when specialist ownership or trust boundaries truly require it."
    )

    pdf.rule()
    pdf.set_font("Helvetica", "I", 8.5)
    pdf.set_text_color(90, 90, 90)
    pdf._mc(
        4.5,
        "Source: I2I Agentic AI Starter Guide (FDE). This summary is a learning aid for internal study and discussion; "
        "refer to the original guide for full detail and platform tables.",
    )

    out = OUT / "I2I-Agentic-AI-Executive-Summary.pdf"
    pdf.output(out)
    return out


# --- 50 complex MCQs ---
MCQS = [
    (
        "A team states 'we use Agentic AI' in an architecture review but cannot describe autonomy, planning, or tool choice. What is the strongest critique?",
        [
            "Agentic AI is not a recognized term",
            "Agentic capability is a spectrum; the claim lacks architectural specificity",
            "Only multi-agent systems may use the term",
            "LLMs cannot participate in agentic systems",
        ],
        "B",
    ),
    (
        "Which statement best separates agent, workflow, and platform?",
        [
            "They are interchangeable synonyms",
            "Agent decides/acts; workflow structures steps and state; platform helps build and run them",
            "Platform always means the LLM vendor only",
            "Workflow is only the UI theme",
        ],
        "B",
    ),
    (
        "A multi-agent pipeline always executes Agent A then B then C with no runtime decision-making. How should this be classified?",
        [
            "Strongly agentic AI by definition",
            "Primarily workflow automation, even though multiple agents exist",
            "Pure A2A mesh",
            "An MCP host",
        ],
        "B",
    ),
    (
        "When is adding a second agent least justified?",
        [
            "Legal and finance need separate ownership and systems",
            "A vendor agent must remain in another trust boundary",
            "One agent with a few well-scoped tools already completes the task reliably",
            "Specialists require independent release cycles",
        ],
        "C",
    ),
    (
        "For an enterprise leave system that must authenticate, enforce blackout dates, submit to HRIS, then optionally draft a manager note, which pattern fits best?",
        [
            "Fully free planner with no fixed steps",
            "Hybrid: deterministic rails for identity/policy/submit; LLM optional for drafting",
            "Five debating A2A agents with no schemas",
            "Memory-only design with no tools",
        ],
        "B",
    ),
    (
        "What is the primary advantage of workflow-driven orchestration?",
        [
            "Maximum path surprise",
            "Predictability, auditability, and testable branches",
            "Eliminating all tools",
            "Removing the need for AuthZ",
        ],
        "B",
    ),
    (
        "Autonomous LLM orchestration is most appropriate when:",
        [
            "Every step is legally prescribed and identical",
            "The task space is open-ended and useful paths cannot all be pre-encoded",
            "Tools must never be called",
            "Observability is intentionally disabled",
        ],
        "B",
    ),
    (
        "An orchestrator's main responsibility is to:",
        [
            "Replace all tools with one megaprompt",
            "Decompose goals, delegate, merge results, and decide stop or escalate",
            "Store API keys in the system prompt",
            "Retrain the base model weekly",
        ],
        "B",
    ),
    (
        "Which design-review question most directly reduces production incidents?",
        [
            "Which emoji should the agent use?",
            "What is in state after each step, and what happens on tool failure, retry, or HITL?",
            "Can we rename the agent to sound more autonomous?",
            "Which font does the chat UI use?",
        ],
        "B",
    ),
    (
        "Why do tool descriptions and parameter schemas matter so much?",
        [
            "They are ignored by modern models",
            "They heavily influence tool selection and argument correctness",
            "One do-everything tool is always superior",
            "Schemas replace authentication",
        ],
        "B",
    ),
    (
        "A model requests delete_user with a guessed id. Which control is least sufficient alone?",
        [
            "Server-side AuthZ, allowlists, and HITL for destructive tools",
            "Stronger wording in the system prompt only",
            "Schema validation and trusted identity from session context",
            "Audit logging of tool calls",
        ],
        "B",
    ),
    (
        "In a ReAct-style loop, 'Observe' means:",
        [
            "Looking at the user only once at start",
            "Incorporating tool or environment results into the next reasoning step",
            "Retraining the foundation model",
            "Deleting all memory",
        ],
        "B",
    ),
    (
        "Why might a system use a small model for routing and a larger model for planning?",
        [
            "MCP requires dual models",
            "Cost and latency tradeoffs: cheap classification vs stronger multi-step reasoning",
            "Small models cannot call tools",
            "Large models cannot follow schemas",
        ],
        "B",
    ),
    (
        "Critical authorization for submit_leave should primarily live in:",
        [
            "Only the system prompt",
            "The application/tool layer with real AuthN/AuthZ checks",
            "The marketing site copy",
            "The model card PDF alone",
        ],
        "B",
    ),
    (
        "LLMs need external memory primarily because:",
        [
            "They automatically remember all users forever",
            "They are effectively stateless across calls unless context is provided or stored",
            "Memory replaces tools",
            "Memory removes the need for guardrails",
        ],
        "B",
    ),
    (
        "Storing sensitive medical leave reasons in long-term free-text memory without retention controls mainly risks:",
        [
            "CSS layout breakage",
            "Privacy and compliance exposure",
            "TCP window sizing",
            "Font licensing",
        ],
        "B",
    ),
    (
        "Which placement best prevents a disallowed tool call even if the model requests it?",
        [
            "Output style guide only",
            "Tool gateway enforcing allowlist, AuthZ, and schema validation before execution",
            "Increasing temperature",
            "Longer system prompt with more adjectives",
        ],
        "B",
    ),
    (
        "HITL is best described as:",
        [
            "Proof the agent failed",
            "An intentional pause for human approval on high-impact actions",
            "A replacement for all tools",
            "Only suitable for demos",
        ],
        "B",
    ),
    (
        "An agent may draft external emails freely but must get approval before sending. This illustrates:",
        [
            "No guardrails",
            "Risk-tiered control: looser on reversible drafts, stricter on irreversible side effects",
            "Mandatory A2A swarming",
            "Semantic memory only",
        ],
        "B",
    ),
    (
        "Max tool-call and timeout limits primarily protect against:",
        [
            "Better typography",
            "Runaway loops and cost/latency blowups",
            "MCP versioning conflicts",
            "Vector index rebuilds",
        ],
        "B",
    ),
    (
        "MCP's primary purpose is to:",
        [
            "Train new foundation models",
            "Standardize how agents/apps connect to tools and context sources",
            "Replace databases with prompts",
            "Provide only agent-to-agent negotiation",
        ],
        "B",
    ),
    (
        "In MCP terminology, which component exposes tools and resources?",
        [
            "MCP Server",
            "Vector-only store",
            "Browser cookie jar",
            "A2A agent card exclusively",
        ],
        "A",
    ),
    (
        "Which statement about adopting MCP is most accurate?",
        [
            "Every prototype must start with MCP",
            "Ad-hoc local tools can be fine early; MCP value grows with reuse and multi-host integration",
            "MCP eliminates authentication needs",
            "MCP servers should trust all LLM arguments without validation",
        ],
        "B",
    ),
    (
        "An MCP server exposing arbitrary local file reads to a general employee chatbot creates which immediate concern?",
        [
            "Color contrast",
            "Over-broad capability and data exfiltration risk without least privilege",
            "Lack of multi-agent debate",
            "Missing emoji reactions",
        ],
        "B",
    ),
    (
        "MCP is not:",
        [
            "A way to expose tools and resources",
            "A substitute for an agent-to-agent collaboration protocol",
            "Useful for reusable enterprise connectors",
            "Something that can sit under an agent host",
        ],
        "B",
    ),
    (
        "A2A primarily addresses:",
        [
            "Pixel rendering",
            "Agent-to-agent discovery, messaging, and collaboration",
            "GPU kernel fusion",
            "CSS animations",
        ],
        "B",
    ),
    (
        "Correct complementary use of MCP and A2A is:",
        [
            "A2A for database rows; MCP only for agent chat",
            "A2A between agents; each agent uses MCP or tools to reach systems of record",
            "Never combine them",
            "MCP fully replaces orchestrators",
        ],
        "B",
    ),
    (
        "An 'agent card' concept is closest to:",
        [
            "A payment card for tokens",
            "A public profile of an agent's identity and capabilities",
            "A Docker image of PostgreSQL",
            "A UI theme pack",
        ],
        "B",
    ),
    (
        "Two agents keep delegating the same task indefinitely. Best mitigation set?",
        [
            "Remove schemas and hope",
            "Max hop count, clear ownership, structured task contracts, timeouts",
            "Increase temperature and parallelism",
            "Disable logging",
        ],
        "B",
    ),
    (
        "Fan-out multi-agent pattern means:",
        [
            "Only one agent may ever run",
            "Multiple agents work (often in parallel) and results are merged",
            "Deleting MCP servers",
            "Disabling HITL permanently",
        ],
        "B",
    ),
    (
        "Which set is the strongest must-have before production tool-writing agents?",
        [
            "Fancy multi-agent debate UI first",
            "AuthN/AuthZ, tracing, timeouts, and guardrails on high-risk tools",
            "Ten memory types on day one",
            "Custom foundation model pretrained from scratch",
        ],
        "B",
    ),
    (
        "A team wants A2A multi-agent planning before tool auth, traces, or evals. What should you recommend?",
        [
            "Approve - protocols always come first",
            "Reorder: secure tools, observability, and evals first; add multi-agent when the use case forces it",
            "Skip tools and only do A2A",
            "Replace evals with more prompt adjectives",
        ],
        "B",
    ),
    (
        "Should-have production features typically include:",
        [
            "Ignoring failures",
            "HITL gates, eval harness, cost controls, and versioning",
            "Unauthenticated admin tools",
            "No logging by policy",
        ],
        "B",
    ),
    (
        "Choosing low-code visual flows vs code-first graphs should mainly depend on:",
        [
            "Which logo looks nicer",
            "Team skills, need for complex logic/testability, and enterprise constraints",
            "Whether MCP forbids low-code",
            "Whether A2A requires Python",
        ],
        "B",
    ),
    (
        "An AI gateway's main job is closest to:",
        [
            "Centralizing model access: routing, keys, rate limits, fallbacks",
            "Storing salaries in prompts",
            "Drawing diagrams only",
            "Replacing operational databases",
        ],
        "A",
    ),
    (
        "Which statement correctly relates RAG and agents?",
        [
            "RAG alone is always a full agentic system",
            "RAG grounds answers with fetched knowledge; agents add planning and tool actions; they often combine",
            "Agents cannot use retrieval",
            "RAG replaces guardrails",
        ],
        "B",
    ),
    (
        "Observability and evals differ because:",
        [
            "They are identical",
            "Observability inspects runs; evals systematically score quality and regressions",
            "Evals only measure CPU temperature",
            "Observability forbids tool-call traces",
        ],
        "B",
    ),
    (
        "Which kill-switch design is most practical for a runaway agent?",
        [
            "Hope the model stops",
            "Enforce max steps/tool calls, timeouts, budget caps, and admin cancel",
            "Delete the company wiki",
            "Disable HTTPS",
        ],
        "B",
    ),
    (
        "Channel adapters (Slack/Teams/web) should ideally:",
        [
            "Each reimplement business logic separately",
            "Reuse the same agent core behind different fronts",
            "Bypass auth for convenience",
            "Store secrets in chat messages",
        ],
        "B",
    ),
    (
        "You must design an HR assistant for policy Q&A and leave submit with strong audit needs. Strongest architecture statement?",
        [
            "One unconstrained autonomous agent with filesystem MCP and no logs",
            "Hybrid graph: retrieval for policy; deterministic validated path for leave submit with AuthZ, optional HITL, traces, and golden evals",
            "Five A2A agents debating every FAQ",
            "Prompt-only with no tools",
        ],
        "B",
    ),
    (
        "A vendor provides an external benefits specialist agent. Your orchestrator should call it for niche questions. Best protocol pairing?",
        [
            "Call vendor via A2A; your agent still uses MCP/tools for internal HRIS",
            "Put HRIS passwords in the vendor agent card",
            "Use only MCP to talk to the vendor agent as if it were a person, with no auth",
            "Avoid schemas for cross-org calls",
        ],
        "A",
    ),
    (
        "After a prompt tweak, tool-choice accuracy drops 20% but chat 'sounds nicer.' What was most likely skipped?",
        [
            "Font review",
            "Evaluation/regression checks on tool selection and task success",
            "Immediately adding more agents",
            "Removing observability",
        ],
        "B",
    ),
    (
        "Which memory design is most appropriate for a regulated financial agent?",
        [
            "Save raw card PANs into semantic memory forever",
            "Minimal retention, purpose-limited memory, access control; re-fetch sensitive data from systems of record when needed",
            "Mirror production DB into the prompt weekly",
            "Disable all session memory so fraud cannot be discussed",
        ],
        "B",
    ),
    (
        "Approving a wire transfer above threshold should be:",
        [
            "Fully free-form LLM creativity",
            "Deterministic policy and AuthZ (plus HITL), with LLM maybe drafting rationale - not inventing approval",
            "Random specialist agent vote without logs",
            "MCP resource read of a poem",
        ],
        "B",
    ),
    (
        "A leave bot answers 'You have 14 days left' without any API/tool call. Primary failure mode?",
        [
            "Correct tool grounding",
            "Hallucination / ungrounded answer instead of live system data",
            "Perfect AuthZ",
            "Deterministic HRIS write",
        ],
        "B",
    ),
    (
        "For structured tool-argument generation, which setting is usually safer?",
        [
            "Very high temperature for creativity",
            "Lower temperature for more stable structured outputs",
            "No schema, only free prose",
            "Disable all validation",
        ],
        "B",
    ),
    (
        "Soft policy text in the system prompt is insufficient for 'cannot approve own expenses' because:",
        [
            "Prompts are illegal",
            "Models can ignore or be manipulated; enforcement belongs in code and tool AuthZ",
            "Expenses never need rules",
            "Only A2A can enforce policy",
        ],
        "B",
    ),
    (
        "Submitting leave twice creates two records. Which concept was missing?",
        [
            "Temperature tuning",
            "Idempotency and/or duplicate detection for write operations",
            "Vector embeddings",
            "Agent cards",
        ],
        "B",
    ),
    (
        "Why unit-test tools without calling the LLM?",
        [
            "LLMs are always free",
            "Tools are deterministic business logic; tests catch contract bugs cheaply and stably",
            "Unit tests replace AuthZ",
            "Frameworks forbid LLM tests forever",
        ],
        "B",
    ),
    (
        "Which interview-ready summary best reflects mature enterprise practice?",
        [
            "Always maximize agent count and autonomy on day one",
            "Build hybrid systems: rails for compliance-critical steps, LLM agents for flexible reasoning, narrow authenticated tools, guardrails/HITL on writes, traces plus golden evals; multi-agent/A2A only when specialist ownership requires it",
            "Put all security rules only in prompts and skip evals",
            "Prefer one mega-tool with admin rights for speed",
        ],
        "B",
    ),
]


def build_mcq() -> Path:
    pdf = DocPDF("I2I Agentic AI - Complex MCQ Assessment (50)")
    pdf.alias_nb_pages()
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(20, 40, 70)
    pdf._mc(8, "I2I Agentic AI Starter Guide")
    pdf.set_font("Helvetica", "B", 12)
    pdf._mc(6, "Complex Multiple-Choice Assessment (50 Questions)")
    pdf.ln(1)
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(80, 80, 80)
    pdf._mc(
        5,
        "Instructions: Choose the single best answer for each question. "
        "Answers and a quick key appear at the end of this document. "
        "Recommended pass bar: 40/50 (80%) before claiming readiness for design discussions.",
    )
    pdf.rule()

    letters = ["A", "B", "C", "D"]
    for i, (q, opts, _ans) in enumerate(MCQS, start=1):
        # Keep questions from orphaning badly
        if pdf.get_y() > 245:
            pdf.add_page()
        pdf.set_font("Helvetica", "B", 9.5)
        pdf.set_text_color(25, 25, 25)
        pdf._mc(5, f"Q{i}. {q}")
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(40, 40, 40)
        for L, opt in zip(letters, opts):
            pdf._mc(4.8, f"    {L}. {opt}")
        pdf.ln(2)

    # Answers section
    pdf.add_page()
    pdf.h1("Answer Key")
    pdf.body(
        "Review only after attempting the full set. Each item lists the correct option."
    )
    pdf.ln(1)

    # Compact grid-like listing
    pdf.set_font("Helvetica", "", 9.5)
    answers = [a for _, _, a in MCQS]
    line = ""
    for i, a in enumerate(answers, start=1):
        line += f"Q{i}:{a}   "
        if i % 5 == 0:
            pdf._mc(5.5, line.strip())
            line = ""
    if line.strip():
        pdf._mc(5.5, line.strip())

    pdf.ln(4)
    pdf.h2("Brief rationale themes (for discussion)")
    pdf.bullet("Prefer architectural specificity over buzzwords; agentic is a spectrum.")
    pdf.bullet("Hybrid orchestration is the usual enterprise fit for compliance + flexibility.")
    pdf.bullet("Enforce AuthZ and irreversible actions in the tool layer, not prompts alone.")
    pdf.bullet("MCP connects agents to tools/context; A2A connects agents to agents.")
    pdf.bullet("Ship tools, guardrails, traces, and evals before exotic multi-agent designs.")
    pdf.bullet("Ground live facts with tools; use evals to catch regressions after prompt changes.")

    pdf.rule()
    pdf.set_font("Helvetica", "I", 8.5)
    pdf.set_text_color(90, 90, 90)
    pdf._mc(
        4.5,
        "Source basis: I2I Agentic AI Starter Guide (FDE) study pack. "
        "For internal learning use.",
    )

    out = OUT / "I2I-Agentic-AI-Complex-MCQs-50.pdf"
    pdf.output(out)
    return out


if __name__ == "__main__":
    assert len(MCQS) == 50, len(MCQS)
    s = build_summary()
    m = build_mcq()
    print(s)
    print(m)
    # page counts
    from pypdf import PdfReader

    for p in (s, m):
        try:
            n = len(PdfReader(str(p)).pages)
            print(f"{p.name}: {n} pages")
        except Exception as e:
            print("pagecount skip", e)
