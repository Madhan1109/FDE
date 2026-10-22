# Practice questions for FDE (with short answers)

Practice out loud. Keep answers concrete.

## Role understanding

**Q: What is an FDE?**  
A: An engineer who works close to the customer and ships working software in their environment so the product creates real value.

**Q: How is FDE different from SWE?**  
A: SWE optimizes the core product for many customers. FDE optimizes a customer outcome first, then feeds patterns back to product.

**Q: How is FDE different from Solutions Engineer?**  
A: Solutions Engineer often focuses on demos and winning the deal. FDE stays through deployment and adoption.

**Q: How is FDE different from support?**  
A: Support reacts to tickets. FDE builds systems that remove repeated pain.

## Delivery

**Q: How do you start with a new customer?**  
A: Discover the mission, constraints, data, and success metric. Then ship the smallest useful vertical slice.

**Q: What if the customer wants everything in two weeks?**  
A: Agree on one workflow that proves value. Put the rest on a sequenced backlog.

**Q: How do you know you succeeded?**  
A: Adoption + outcome metric (time saved, errors reduced, tickets avoided), not just “demo worked.”

**Q: What do you hand off?**  
A: Working system, runbook, owners, known limits, and next backlog.

## Technical

**Q: What is integration work?**  
A: Connecting the product to customer systems (APIs, auth, data stores, workflows).

**Q: What are guardrails in an AI deployment?**  
A: Rules that prevent unsafe or wrong behavior: auth, privacy, policy limits, grounded answers, tool restrictions.

**Q: Do all RAG systems need a vector DB?**  
A: No. Some use keyword retrieval like BM25. Vector DBs help with semantic similarity when needed.

**Q: What is agentic AI?**  
A: Software that can plan steps and call tools to complete a goal, not only generate text.

## Behavioral

**Q: Tell me about ambiguity.**  
A: Use a story where requirements were unclear, you chose a thin slice, shipped, learned, and iterated.

**Q: Tell me about a failure.**  
A: Demo/integration broke, you diagnosed, fixed, added a check/runbook, and prevented repeat.

**Q: Tell me about conflict with a stakeholder.**  
A: They wanted a big feature; you proposed a smaller path that still hit their metric, and got agreement.

## Stretch questions

**Q: When should custom FDE work become product?**  
A: When the same pattern appears across customers and can be maintained centrally.

**Q: When should it stay custom?**  
A: When it is deeply unique, regulated, or not worth generalizing yet.

**Q: What makes a bad FDE engagement?**  
A: Endless one-off scripts, no metrics, no handoff, no feedback to product.
