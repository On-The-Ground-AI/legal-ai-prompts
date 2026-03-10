# Multi-Step AI Prompt Workflows for Legal Teams
### How to Chain Prompts for Complex Legal Tasks

---

> **What is prompt chaining?**
> Instead of asking AI one big question and hoping for a perfect answer, you break the task into steps. Each step's output feeds into the next prompt. This produces much more accurate, structured, and useful results — especially for complex legal work.
>
> This document contains ready-to-use multi-step workflows for the most common complex legal tasks.

---

## Workflow 1: Contract Review — Full Cycle (5 Steps)

Use this workflow when you receive a contract from a counterparty and need to brief the client and negotiate.

---

**Step 1 — Initial Risk Scan (2 minutes)**

Paste into Copilot / Claude / ChatGPT:

"Act as a contract review specialist. I am pasting a contract below. Read it and give me: (1) the type of contract it is, (2) the parties and their roles, (3) a RAG risk rating (Red/Amber/Green) overall, and (4) the 3 most concerning clauses. [PASTE CONTRACT]"

*What you get: A quick orientation before deep reading.*

---

**Step 2 — Clause-by-Clause Issues List**

"Based on your initial review, now go through the contract clause by clause and identify every clause that: (a) deviates from market standard, (b) creates unusual liability or risk, or (c) is missing but should be standard. Present as a table: [Clause No. | Topic | Issue | Severity (High/Medium/Low) | Recommended Fix]."

*What you get: The raw material for your redline.*

---

**Step 3 — Redline Drafting**

"For each High and Medium issue you identified, draft the replacement clause language I should propose. For each redline: (a) state the current clause language, (b) state our proposed replacement, and (c) give a one-sentence business justification for the change."

*What you get: Draft redline language ready for the lawyer to review and refine.*

---

**Step 4 — Client Summary**

"Now draft a plain-English summary of this contract for my client, who is a [DESCRIBE — e.g. small business owner / finance director]. Cover: (1) what the contract requires them to do, (2) the key risks we have identified, (3) the changes we are proposing and why, and (4) our recommendation (sign as-is / negotiate / reject). Maximum 400 words. No legal jargon."

*What you get: A client-ready briefing note.*

---

**Step 5 — Negotiation Preparation**

"Finally, help me prepare for the negotiation. The counterparty is likely to resist the following redlines: [LIST YOUR KEY CHANGES]. For each point of resistance: (a) predict the counterparty's argument, (b) suggest our response, and (c) identify our fallback position if they won't accept our preferred position."

*What you get: A negotiation strategy brief.*

---

## Workflow 2: Legal Research → Memo → Client Advice (4 Steps)

Use this workflow when a client asks a novel legal question you need to research.

---

**Step 1 — Framework Research**

"Act as a senior legal research assistant. I need to research the following legal question: [DESCRIBE THE QUESTION] under [JURISDICTION] law. Provide: (1) the key statutory framework, (2) the leading cases (name, year, key holding — mark confidence as High/Medium/Low), (3) the current legal standard, and (4) any unresolved areas or recent developments. Flag any cases I must verify independently."

---

**Step 2 — Applying the Law to the Facts**

"Now apply the legal framework you have outlined to the following facts: [DESCRIBE YOUR CLIENT'S SITUATION]. For each element of the legal test, assess: (a) how our facts map to it, (b) whether it is likely satisfied or not, and (c) what additional facts or evidence would strengthen or weaken our position."

---

**Step 3 — Draft Research Memo**

"Draft a formal legal research memorandum on this question in the following structure: (1) Issue, (2) Short Answer, (3) Facts, (4) Legal Analysis — one section per legal issue, with relevant authorities cited, (5) Application to Our Facts, (6) Conclusion and Recommended Next Steps. Length: 600-900 words."

---

**Step 4 — Client Advice Letter**

"Using the memo as your source material, now draft a client advice letter in plain English explaining: what the law says, how it applies to their situation, what their options are, our recommendation, and what we need them to decide or provide. Maximum 500 words. Tone: clear, confident, and accessible to a non-lawyer. Avoid citing cases in the client letter — refer to 'current case law' instead."

---

## Workflow 3: Employee Complaint — Investigation to Outcome (5 Steps)

---

**Step 1 — Initial Triage**

"Act as an employment lawyer. I have received the following complaint from an employee: [DESCRIBE]. Assess: (1) what legal issues this complaint potentially involves (harassment / discrimination / misconduct / whistleblowing), (2) how urgently I need to act, (3) any immediate steps required (suspend the respondent? separate the parties?), and (4) who should conduct the investigation."

---

**Step 2 — Investigation Plan**

"Create a step-by-step workplace investigation plan for this complaint. Include: (1) documents to gather, (2) witnesses to interview in what order, (3) interview questions for the complainant, (4) interview questions for the respondent, (5) timeline for completing the investigation, and (6) how to maintain confidentiality throughout."

---

**Step 3 — Interview Questions**

"Draft detailed interview questions for: (a) the complainant, (b) the respondent, and (c) each key witness: [LIST NAMES / ROLES]. For each set of questions: start with open questions to get the person's account, follow with clarifying questions, and end with any specific allegations they need to respond to. Note what documents to put to them during the interview."

---

**Step 4 — Investigation Report**

"Draft a workplace investigation report template covering: (1) Executive Summary, (2) Background and Scope, (3) Methodology, (4) Summary of Evidence — complainant's account, respondent's account, witness evidence, documentary evidence, (5) Findings of Fact — what did and did not happen, (6) Credibility Assessment, (7) Conclusions — is the complaint substantiated, partially substantiated, or unsubstantiated?, (8) Recommended Outcomes, (9) Appendices."

---

**Step 5 — Outcome Letters**

"Draft two letters: (a) a letter to the complainant informing them of the investigation outcome [SUBSTANTIATED / UNSUBSTANTIATED — choose one], and (b) a letter to the respondent informing them of the outcome and any disciplinary consequences. Both letters should: be professional and sensitive, state the conclusion clearly, not reveal more than is appropriate about the other party's evidence, and comply with [JURISDICTION] employment law."

---

## Workflow 4: New Regulatory Change — Impact to Action Plan (3 Steps)

Use this when a new regulation or law is announced that may affect your organisation.

---

**Step 1 — Regulation Summary**

"Act as a regulatory lawyer. The following new regulation has been announced: [NAME OR DESCRIBE IT]. Summarise: (1) the key new obligations, (2) who is affected and from what date, (3) the penalties for non-compliance, and (4) any transitional provisions or exemptions."

---

**Step 2 — Business Impact Assessment**

"Now assess the impact on my organisation: [DESCRIBE — industry, size, operations, current practices]. For each key obligation: (a) do we currently comply? (b) what changes do we need to make to our policies, contracts, processes, or systems? (c) what is the risk if we do not comply? Present as a table: [Obligation | Current Status | Gap | Action Required | Priority]."

---

**Step 3 — Compliance Action Plan**

"Based on the gap analysis, create a compliance action plan with: (1) a prioritised list of actions (Critical / High / Medium), (2) a suggested owner for each action (Legal / HR / IT / Operations / Finance), (3) a realistic timeline, and (4) a brief description of what 'done' looks like for each action. Format as a project plan table."

---

## Quick Tips for Better Chaining

**Carry context forward.** Start each follow-up prompt with "Based on your previous response..." so the AI remembers what it told you.

**Correct mistakes early.** If Step 2's output is wrong, correct it before moving to Step 3. Bad outputs compound.

**Split the task if it gets too long.** If the AI's response gets truncated or loses quality, start a new chat for Step 3 and paste in the best outputs from Steps 1 and 2 as context.

**Save each step's output.** Copy each step's output into your Word document as you go. This gives you a full audit trail and lets you edit at each stage.

**Always do a final review.** After all steps are complete, re-read the full output as a whole. AI-chained outputs can have inconsistencies between steps that only show up when you read the whole thing together.

---

*This workflow guide is part of The Legal Prompts Library.*
