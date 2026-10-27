# Prerequisites assessment — Medium to Complex MCQs (with answers)

Covers the three DOCX prerequisites: **LLMs**, **APIs/tools**, **Python for agents** (`00a`–`00c`).

Legend: **(M)** medium · **(C)** complex

---

## Section P1 — LLMs

**P1 (M).** An LLM is best described as:  
A. A live company database  
B. A model that predicts next tokens and can be used to reason/decide when given context and tools  
C. A guaranteed source of truth  
D. A replacement for AuthZ  

**Answer:** B

---

**P2 (M).** Why do agent apps store chat history outside the model?  
A. Models permanently remember every user by default  
B. Models are effectively stateless unless the app resends or retrieves context  
C. History cannot be stored in databases  
D. MCP forbids prompts  

**Answer:** B

---

**P3 (C).** A leave bot answers “You have 14 days left” without calling any API. Main failure mode?  
A. Correct grounding via tools  
B. Hallucination / ungounded answer instead of tool-fetched data  
C. Perfect AuthZ  
D. Deterministic HRIS write  

**Answer:** B

---

**P4 (C).** For tool-argument JSON generation, which setting is usually safer?  
A. Very high temperature for creativity  
B. Lower temperature for more stable structured outputs  
C. No schema, only poetry  
D. Disable all validation  

**Answer:** B

---

**P5 (M).** In a tool-calling loop, after the model requests `get_leave_balance`, the application must:  
A. Ignore it and answer from training data  
B. Execute the real function/API and return the result to the model  
C. Retrain the foundation model  
D. Delete the system prompt  

**Answer:** B

---

**P6 (C).** Soft policy text in the system prompt is not enough for “cannot approve own expenses” because:  
A. Prompts are illegal  
B. Models can ignore or be manipulated; enforcement belongs in code/tool AuthZ  
C. Expenses never need rules  
D. Only A2A can enforce policy  

**Answer:** B

---

## Section P2 — APIs and external tools

**P7 (M).** In agent systems, a “tool” is typically:  
A. Only the GPU  
B. A controlled function that reaches external data or services  
C. The system font  
D. The marketing website  

**Answer:** B

---

**P8 (M).** AuthN vs AuthZ:  
A. Same thing  
B. AuthN = who you are; AuthZ = what you are allowed to do  
C. AuthZ = proving identity only  
D. AuthN = schema validation only  

**Answer:** B

---

**P9 (C).** The LLM outputs a tool call with an employee id. Where must permission be enforced?  
A. Only in the model’s “personality”  
B. In the tool/API layer (and identity context), not trusting the model alone  
C. Only in the CSS  
D. Nowhere if temperature is 0  

**Answer:** B

---

**P10 (C).** Submitting leave twice creates two records. Which concept was missing?  
A. Temperature  
B. Idempotency (and/or duplicate detection) for write operations  
C. Vector embeddings  
D. Agent cards  

**Answer:** B

---

**P11 (M).** Why return a detailed tool error like “blackout dates …” instead of “Error”?  
A. It uses more GPU  
B. It helps the agent recover or ask a useful follow-up  
C. MCP requires poetry  
D. It disables AuthN  

**Answer:** B

---

**P12 (C).** Which design is most appropriate?  
A. One tool: `do_anything(command: str)` with admin rights  
B. Narrow tools with schemas; stricter gates on write/destructive actions  
C. No timeouts ever  
D. Put API keys in tool descriptions for convenience  

**Answer:** B

---

## Section P3 — Python for agents

**P13 (M).** The core agent loop in code is closest to:  
A. Only training a new model from scratch each request  
B. Call LLM → if tool call, run tool and append result → repeat until final answer  
C. Only CSS rendering  
D. Only static HTML  

**Answer:** B

---

**P14 (M).** Why are type hints + docstrings on tool functions valuable?  
A. They increase temperature  
B. They help humans and often feed clearer tool schemas/descriptions for the model  
C. They replace HTTPS  
D. They store secrets safely in git  

**Answer:** B

---

**P15 (C).** Before `submit_leave` hits HRIS, Pydantic validation fails on `leave_type`. Best next step?  
A. Call HRIS anyway with raw model text  
B. Return a validation error to the agent/user; do not perform the write  
C. Disable validation permanently  
D. Store the API key in the error message  

**Answer:** B

---

**P16 (C).** Why unit-test tools without calling the LLM?  
A. LLMs are free  
B. Tools are deterministic business logic; tests catch API/contract bugs cheaply and stably  
C. Unit tests replace AuthZ  
D. Frameworks forbid LLM tests forever  

**Answer:** B

---

**P17 (M).** Secrets for LLM/HTTP clients should live in:  
A. Committed source code  
B. Environment / secret manager  
C. System prompts shared with users  
D. Public agent cards  

**Answer:** B

---

**P18 (C).** A Java developer maps Spring controllers to agent apps most closely as:  
A. Pygame sprites  
B. FastAPI (or similar) routes wrapping agent/tools  
C. JVM garbage collector tuning only  
D. CSS grids  

**Answer:** B

---

## Answer key

| Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|
| P1 | B | P7 | B | P13 | B |
| P2 | B | P8 | B | P14 | B |
| P3 | B | P9 | B | P15 | B |
| P4 | B | P10 | B | P16 | B |
| P5 | B | P11 | B | P17 | B |
| P6 | B | P12 | B | P18 | B |

## Map → study files

| Questions | File |
|-----------|------|
| P1–P6 | [00a-llm-fundamentals.md](./00a-llm-fundamentals.md) |
| P7–P12 | [00b-apis-and-external-tools.md](./00b-apis-and-external-tools.md) |
| P13–P18 | [00c-python-for-agents.md](./00c-python-for-agents.md) |

**Pass bar:** 15/18 before moving hard into `01`–`10` if these topics are new to you.
