# FDE YouTube Video Notes (1–2 pages)

**Purpose:** Org task — watch FDE YouTube videos and capture key learnings in short bullet points.  
**Branch:** `docs/fde-study-guide`  
**Also available as Word doc:** [`FDE-YouTube-Video-Notes.docx`](./FDE-YouTube-Video-Notes.docx)

---

## YouTube videos used

1. **What is a Forward Deployed Engineer? (with Founding Rippling FDE)**  
   https://www.youtube.com/watch?v=Ck-LeYlAVbY

2. **How to Become a Forward Deployed Engineer in 2026**  
   https://www.youtube.com/watch?v=vLlIBT0HSSc

3. **I gave 15 Forward Deployed Engineer Interviews. Here's what they ask.**  
   https://www.youtube.com/watch?v=VnIDWlOzb6s

4. **How Shyam Sankar Created Palantir's Forward Deployed Engineers**  
   https://www.youtube.com/watch?v=LkX_J_rX2x4

5. **Palantir's Forward Deployed Software Engineer — Revolution or Rebrand? (AA218)**  
   https://www.youtube.com/watch?v=SGvJK-aruJ8

---

## Key takeaways (from the videos)

### What FDE means
- FDE = engineer placed **close to the customer** (“forward”), not only at HQ.
- Job is to make a complex product work in the customer’s **real environment**.
- Invented / popularized at **Palantir**; now used by many AI and enterprise companies.
- Core idea: powerful software alone is not enough — someone must wire it into messy real systems.

### Why the role exists
- Demos work; customer reality is hard (legacy systems, bad data, compliance, process).
- Especially important when the **product is technical** but the **buyer/users are not**.
- In AI era, models are strong; the bottleneck is **production deployment and adoption**.
- FDE lives in the gap between “cool demo” and “paid business value.”

### What FDE is / is not
- **Is:** customer-facing software engineer with end-to-end ownership (discover → plan → build → deliver).
- **Is not:** only sales engineering / pre-sales demos.
- **Is not:** only classic product SWE building one feature for thousands of customers.
- **Is not:** consulting that ends in slides; output should be **working software**.
- Often described as wearing **3 hats:** consultant + product manager + software engineer.

### How FDEs work day to day
- Start by **listening** (main communication skill), not pitching.
- Customer’s first statement is often a **symptom**, not the real business goal.
- Example from video: “dashboard is slow” may really mean “conversion / sales is down.”
- Pick highest-impact problem that is also **feasible** with current platform/time.
- Ship a small first version fast, then iterate (customer will dislike v1; plan for that).
- Own completeness: build, demo, gather feedback, get acceptance — not just merge a PR.
- Growth is by **scope**: one slice → one customer → industry / geography.

### Skills highlighted in the videos
- **Engineering:** Python, APIs, SQL/DB, testing, debugging, system design.
- **AI (for AI FDE roles):** LLM APIs, prompts, RAG, agents, evals, observability.
- **Customer skills:** clarify vague asks, explain tradeoffs in business language, ownership when things break.
- Technical skills get you in the door; **customer skills often decide the offer**.

### Interview / hiring patterns from the videos
- DSA still exists, but weight has shifted toward judgment and delivery.
- Common patterns: OOP in Python, take-home assignments, live Python coding.
- Ambiguous **case study** rounds: vague customer problem → scoped plan in ~45 minutes.
- Agentic system design + AI security (prompt injection, PII, jailbreaks, failure handling).
- Strong signal: clarify before solving, think out loud, speak in business outcomes.
- Resume tip: end-to-end projects with **measurable impact**, not tutorial apps.

### Origin story (Palantir / Shyam Sankar clip)
- Early insight: sales-only customer interaction is not enough.
- Need technical people co-located with customers to learn what product must exist.
- First hard deployments required extreme ownership beyond “out of the box” software.
- Lessons from the field should be **fed back** into the core product (“back propagation”).

---

## One-line summary for org submission

FDE is a customer-embedded engineering role that turns complex products (especially AI) into real production value by listening deeply, scoping tightly, shipping software end-to-end, and feeding field lessons back into the product.
