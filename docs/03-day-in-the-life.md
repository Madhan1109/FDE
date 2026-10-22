# What an FDE does every day (plain English)

No two days are identical. This is a realistic picture.

## Morning

- Check production / staging health for the customer deployment
- Read messages from customer stakeholders (ops lead, IT, business owner)
- Triage: is this a bug, a data issue, a training issue, or a new requirement?

## Midday

- Join a short discovery call (“show me how you do this today”)
- Map the current workflow on a whiteboard
- Decide smallest useful next slice to ship this week
- Write or change code:
  - API connector
  - data cleanup script
  - auth / SSO fix
  - agent tool / prompt / guardrail
  - dashboard or workflow UI
- Deploy to customer environment (or approved sandbox)

## Afternoon

- Test with one real user
- Fix what broke
- Write a short note: what changed, how to use it, known limits
- Sync with internal product team: “this pattern is repeating across customers”

## End of day

- Update tracker (ticket / milestone)
- Leave the system in a safe state
- Plan tomorrow’s riskiest unknown

## Weekly rhythm

1. **Discover** — understand the mission and constraints  
2. **Design** — pick a thin vertical slice  
3. **Build** — code + integrate  
4. **Deploy** — put it where users can touch it  
5. **Measure** — did it reduce time / errors / manual work?  
6. **Productize** — feed reusable pieces back to core engineering  

## People an FDE talks to

- Business owner (“what does success mean?”)
- End users (“what do you click today?”)
- IT / security (“what are we allowed to do?”)
- Data owners (“where is the truth?”)
- Internal PM / SWE (“what should become product?”)

## Soft skills that matter as much as code

- Asking clear questions
- Saying “no” to scope that cannot ship
- Explaining tradeoffs without jargon
- Staying calm when demos break
- Writing short, useful documentation

## Hard skills that show up daily

- Debugging across systems
- Reading logs
- SQL / APIs / auth
- Cloud basics
- Scripting
- For AI FDEs: prompts, tools, evals, guardrails, RAG

## What “good” looks like after 30 days with a customer

- One painful workflow is clearly better
- Users trust the tool for that workflow
- Ops knows how to restart / monitor it
- There is a backlog of next slices, not chaos
