# Legal AI Prompt Engineering Masterclass

A comprehensive guide to writing effective prompts for AI tools in legal practice. Version 1.02

---

## INTRODUCTION

This masterclass teaches lawyers how to extract maximum value from AI tools like Claude, ChatGPT, and specialized legal AI platforms. The difference between mediocre AI output and exceptional results lies entirely in how you ask the question.

**Three Core Principles:**
1. Be specific, not vague
2. Provide context, not assumptions
3. Verify, don't blindly trust

---

## SAL-MICROSOFT FRAMEWORK: GCES

*This framework is drawn from the **Prompt Engineering for Lawyers (2nd Edition)** guide, published by the **Singapore Academy of Law (SAL)** in collaboration with **Microsoft Singapore** (2025). Developed by and for Singapore lawyers, it reflects the SAL's official guidance on responsible AI use in legal practice. Source: https://sal.org.sg/wp-content/uploads/2025/10/Prompt-Engineering-Guide-2025-2nd-Edition.pdf*

The SAL-Microsoft guide introduces a practical four-part framework — **GCES** — which complements the ABCDE framework below. GCES is particularly well-suited to Singapore legal practice.

**GCES = Goal, Context, Expectations, Source**

**G — Goal:** State the task at the very beginning. Use action verbs: *Draft*, *Summarise*, *Analyse*, *Review*, *Compare*. If complex, break into sub-goals and state them in priority order.

**C — Context:** Provide background: who you are, the client, jurisdiction, applicable law, and relevant facts. You can include a few examples of the style you want (few-shot prompting). Include your "Persona" and the intended audience for the output.

**E — Expectations:** Set the output format: tone (formal, plain English), structure (table, bullet points, numbered memo), depth, word limit, and audience. For complex tasks, add "think through this step-by-step" — this is Chain-of-Thought prompting and significantly improves analytical quality.

**S — Source:** Reference or attach the specific documents, clauses, URLs, or legislation the AI should use. Be precise — paste in the relevant paragraph rather than uploading an entire document. Ensure documents shared comply with your firm's confidentiality and data security policies.

---

### SAL Ethics and Professional Responsibility

*From the SAL-Microsoft Prompt Engineering Guide for Lawyers (2025)*

**1. You remain responsible.** Generative AI will not be fully accurate. As the SAL guide puts it: *do not rely on an authority that you have not read.* Always review and verify AI output before using it in your work.

**2. Copilot, not autopilot.** AI helps with fluency and drafts. It should not substitute for developing your own subject matter expertise.

**3. Disclosure.** Your firm's policy, professional conduct rules, or court practice directions may require disclosure of AI use. Check before you use.

**4. Confidentiality.** Free-to-use AI services may use prompt content for training. Enterprise services typically have stronger safeguards. Anonymise prompts appropriately and share only what is necessary.

**5. Data security.** Before attaching any document, confirm the AI service complies with your organisation's data privacy and security policies. Paste specific paragraphs or clauses rather than entire documents.

**The SAL DO / DON'T Checklist:**

| DO | DON'T |
|---|---|
| Use AI to generate comparisons, summaries, and brainstorm ideas from trusted sources | Ask the AI to do too many things at once |
| Start a new chat for each task with clear context | Expect perfect output on a single try |
| Chain related prompts and run them repeatedly to verify results | Assume all output is fully accurate |
| Experiment and iterate to get the results you need | Use output as work product without verification |

---

## HOW TO IMPROVE ANY PROMPT USING SAL PRINCIPLES

*Based on the Singapore Academy of Law's Prompt Engineering for Lawyers (2nd Edition) (2025)*

The SAL guide identified six techniques that consistently improve AI output quality for lawyers. Apply these to every prompt in this library — including the ones below.

**1. Ground the AI in your specific documents.** Add: *"Use only the attached [document name]. Do not reference any external sources or make assumptions beyond its contents."* This prevents the AI from hallucinating case names, statutory provisions, or contract terms that don't exist in your materials.

**2. Use chain-of-thought for complex analysis.** Add: *"Think through this step-by-step"* when asking for legal analysis. This forces the AI to reason explicitly rather than jump to conclusions, and produces more accurate, auditable output.

**3. Set a precise output format.** Tell the AI exactly how to structure the response: *"Present your findings in a table with columns: (1) Clause reference, (2) Issue, (3) Risk rating (HIGH/MEDIUM/LOW), (4) Why it matters, (5) Recommended language."* Structured output is easier to review and harder to misuse.

**4. Specify the audience.** Add: *"This output will be reviewed by [senior partner / client / court / board]."* The AI calibrates tone, depth, and language accordingly.

**5. Set the source boundary explicitly.** For every prompt that involves documents, add: *"Where attachments are referenced, restrict analysis and drafting to those materials and provide pinpoint references where applicable."* This is the SAL guide's standard closing instruction — it prevents scope creep and makes outputs more defensible.

**6. Include a verification reminder for yourself.** Add as a personal note: *"Verify all case citations, statutory references, and legal conclusions before relying on this output."* The SAL guide is explicit: you remain responsible for your work product.

---

### EXAMPLE: BEFORE AND AFTER SAL IMPROVEMENT

**Before (basic prompt):**
> Review this contract and flag any issues.

**After (SAL-improved):**
> **Goal:** Review the attached contract and identify the top 5 legal risks for our client.
>
> **Context:** I am a [Singapore / English law] lawyer acting for [PARTY], the [buyer/licensor/tenant]. This is a [describe agreement] in its [first/second] round of negotiation. The counterparty is [describe].
>
> **Expectations:** Present findings in a table with columns: (1) Clause reference, (2) Issue, (3) Risk rating (HIGH/MEDIUM/LOW), (4) Why it matters to our client, (5) Recommended language change. Think through this step-by-step. Use formal legal language.
>
> **Source:** Use only the attached contract. Do not reference any external sources or make assumptions beyond its contents. Provide pinpoint clause references for every finding.
>
> *[After receiving output: Verify all legal conclusions and statutory references before use.]*

---

## SECTION 1: THE ABCDE FRAMEWORK

The ABCDE Framework is your foundational system for every legal AI prompt. It ensures you provide all necessary context.

**ABCDE = Agent, Background, Clear instructions, Detailed parameters, Evaluation**

---

### PROMPT 1 — ABCDE FRAMEWORK: CONTRACT REVIEW (SIMPLE)

**PROMPT ID:** ABCDE-001

**Agent:** "You are an experienced contract lawyer specializing in commercial agreements."

**Background:** "I'm reviewing a 5-year software licensing agreement between our company (SaaS provider) and a Fortune 500 manufacturing client. The relationship is strategic but we have limited relationship history. The contract is in its second round of negotiation."

**Clear instructions:** "Identify the top 5 financial and operational risks in this agreement from our perspective as the vendor. Think through this step-by-step."

**Detailed parameters:** "Focus on: (1) termination rights and notice periods, (2) indemnification obligations, (3) limitation of liability caps, (4) payment terms and conditions, (5) IP ownership. Flag items that are more onerous than market standard. Present findings in a table with columns: Clause reference | Issue | Risk rating (HIGH/MEDIUM/LOW) | Why it matters | Recommended language change."

**Evaluation:** "For each risk, rate it as HIGH/MEDIUM/LOW based on revenue exposure and operational impact. Use only the attached contract — do not reference external sources or make assumptions beyond its contents. Provide pinpoint clause references for every finding."

**Context:** Corporate/Commercial Law
**Difficulty:** Beginner
**Best AI tool:** Claude (works with document attachments)
**SAL Principles Applied:** Source-grounding, chain-of-thought, structured output format
**Follow-up:** Chain with PROMPT 7 (few-shot prompting) to show examples of balanced language

---

### PROMPT 2 — ABCDE FRAMEWORK: LITIGATION DISCOVERY REQUEST

**PROMPT ID:** ABCDE-002

**Agent:** "You are a senior litigation associate with 8 years of experience in antitrust law and discovery management."

**Background:** "We represent the defendant in a price-fixing class action filed in the Northern District of California. We received a wide-ranging interrogatory set focusing on competitor communications and pricing decisions from 2018-2022. Opposing counsel has been aggressive on scope."

**Clear instructions:** "Draft objections to three specific interrogatories that I will provide. Each objection should use proper legal language and cite applicable discovery rules. Think through this step-by-step."

**Detailed parameters:** "Structure each response as: (1) Full interrogatory text, (2) Our objection, (3) Basis under FRCP 33, (4) Explanation of burden/scope issues, (5) Conditional limited response if any. Keep objections defensible under Eighth Circuit standards. Restrict analysis to the interrogatories I provide — do not assume or invent additional interrogatory text."

**Evaluation:** "Rate each objection's strength as STRONG/MODERATE/WEAK. Flag any interrogatories where we should consider providing a limited response. Verify all FRCP citations before use — AI citations require independent verification."

**Context:** Litigation/Discovery
**Difficulty:** Intermediate
**Best AI tool:** Claude
**SAL Principles Applied:** Source-grounding (restrict to provided interrogatories), chain-of-thought, verification reminder
**Follow-up:** Chain with PROMPT 12 (iterative refinement) to adjust tone and specificity after feedback

---

### PROMPT 3 — ABCDE FRAMEWORK: REGULATORY COMPLIANCE MEMO

**PROMPT ID:** ABCDE-003

**Agent:** "You are the head of regulatory compliance for a healthcare organization with 50+ facilities across 8 states."

**Background:** "The FDA recently issued a guidance document regarding off-label promotion practices in the pharmaceutical device industry. Our company manufactures surgical instruments used in oncology. Last month, we received an inquiry from the SEC's Office of Compliance Inspections and Examinations (OCIE)."

**Clear instructions:** "Create a compliance memo for our sales and marketing teams explaining what we can and cannot do under the new FDA guidance. Think through this step-by-step."

**Detailed parameters:** "The memo should: (1) Summarize the key restrictions in plain language, (2) Provide 5 specific examples of what would violate the guidance, (3) Provide 5 examples of compliant marketing practices, (4) Include a Q&A for the most common questions, (5) Specify documentation requirements. Audience: MBAs and sales professionals without legal training. Use only the FDA guidance document provided — do not reference other guidance documents or make assumptions beyond its contents. Cite specific sections of the guidance for every restriction stated."

**Evaluation:** "Flag any areas where the guidance is ambiguous. Note that the sales team should escalate to compliance counsel before taking action in ambiguous areas. Verify all regulatory citations before distributing this memo."

**Context:** Regulatory/Compliance
**Difficulty:** Intermediate
**Best AI tool:** Claude
**SAL Principles Applied:** Source-grounding (restrict to provided guidance), chain-of-thought, audience specification, verification reminder
**Follow-up:** Chain with PROMPT 9 (temperature control) set to "conservative" for regulatory content

---

### PROMPT 4 — ABCDE FRAMEWORK: DUE DILIGENCE CHECKLIST

**PROMPT ID:** ABCDE-004

**Agent:** "You are a corporate development attorney at a mid-market private equity firm with focus on healthcare IT acquisitions."

**Background:** "We are evaluating acquisition of a health information exchange (HIE) platform. Target company has 15 employees, $8M annual revenue, and operates in 12 states. No venture capital backing. CEO founded the company 5 years ago. The company holds patient health data."

**Clear instructions:** "Create a legal due diligence checklist specific to this transaction. Only include items actually relevant—don't provide a generic 100-item list."

**Detailed parameters:** "Organize by category: (1) Corporate governance (3-5 items), (2) HIPAA and healthcare compliance (4-6 items), (3) Data security and liability (3-4 items), (4) IP and tech stack (3-4 items), (5) Regulatory (2-3 items), (6) Litigation and claims (2-3 items). For each item, explain why it matters and what red flags would be concerning."

**Evaluation:** "Assign risk level to each category: CRITICAL/HIGH/MEDIUM based on deal risk."

**Context:** M&A/Corporate
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Chain with PROMPT 6 (jurisdiction anchoring) if expansion into specific states requires additional regulatory review

---

### PROMPT 5 — ABCDE FRAMEWORK: EMPLOYMENT SETTLEMENT AGREEMENT

**PROMPT ID:** ABCDE-005

**Agent:** "You are employment counsel representing a multinational technology company in a sensitive departure negotiation."

**Background:** "We are settling with our former VP of Engineering after a wrongful termination claim was filed (retaliation allegation under Title VII). The employee's lawyer has submitted a draft settlement. We offered $750K. The underlying claim is weak (we have documentation), but the employee has significant internal communications about prior performance issues that could be problematic if litigated. Executive departure was messy. We want to minimize any ongoing risk or public relations issues."

**Clear instructions:** "Review the draft settlement agreement for gaps and weaknesses. Identify what additional protective language we must add before signing."

**Detailed parameters:** "Critical areas: (1) Scope of release—what claims are actually covered, (2) Confidentiality and NDA—enforceability and scope, (3) Non-disparagement—mutual obligations, (4) Return of property and IP—completeness, (5) References and post-employment conduct—clarity, (6) Dispute resolution—arbitration clause effectiveness, (7) Regulatory and legal hold obligations. Assume Texas law and assume the settlement contemplates a severance package with benefits continuation. DO NOT provide generic advice—focus on specific gaps in THIS agreement."

**Evaluation:** "For each gap, rate its legal risk as CRITICAL/HIGH/MEDIUM and note whether it's likely to create enforcement problems later."

**Context:** Employment Law
**Difficulty:** Advanced
**Best AI tool:** Claude
**Follow-up:** Chain with PROMPT 13 (comparative analysis) to compare with prior settlements your firm has negotiated

---

## SECTION 2: ROLE ASSIGNMENT & PERSONA PROMPTING

Assigning a specific persona dramatically improves AI output quality. Rather than "You are a lawyer," give specific experience level, specialty, and background.

---

### PROMPT 6 — PERSONA: LITIGATION PARTNER PERSPECTIVE

**PROMPT ID:** PERSONA-001

You are a 22-year litigation partner at a 250+ attorney AmLaw 100 firm. You specialize in complex commercial disputes and have tried 35+ cases to jury verdict. You've handled cases involving contract disputes, business torts, and securities litigation. You regularly advise C-suite executives on litigation risk. You're pragmatic about costs and timelines—you know that 90% of cases settle, and you focus on building leverage early.

**Context:** General Litigation
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Use this persona when you need strategic business advice, not just legal analysis

---

### PROMPT 7 — PERSONA: IN-HOUSE GENERAL COUNSEL

**PROMPT ID:** PERSONA-002

You are the General Counsel for a publicly traded retail company with $2B in annual revenue. You oversee a team of 12 lawyers covering corporate, litigation, HR, and compliance. Your CEO requires that you identify risks in plain English and recommend specific action items. You're accountable for the company's legal budget (which is fixed) and you manage relationships with 8 outside counsel firms. You balance legal risk against business opportunity. You've been in-house for 8 years and understand that sometimes "good enough" is better than "perfect" when the business needs to move fast.

**Context:** Corporate Management
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Use this persona when balancing legal perfection against business reality

---

### PROMPT 8 — PERSONA: REGULATORY SPECIALIST

**PROMPT ID:** PERSONA-003

You are a regulatory counsel with 14 years of experience in FDA and FTC compliance. You've worked both at the agency (7 years) and in private practice (7 years). You understand agency guidance documents, warning letters, and enforcement priorities. You know which interpretations are well-settled and which are still evolving. You have relationships with contacts at both agencies. When you identify a compliance issue, you think first about what the agency cares about and second about pure legal doctrine. You're conservative on enforcement matters but pragmatic about gray areas.

**Context:** FDA/FTC/Regulatory
**Difficulty:** Intermediate-Advanced
**Best AI tool:** Claude
**Follow-up:** Use this persona when handling agency compliance or when you need to anticipate enforcement risk

---

### PROMPT 9 — PERSONA: JUNIOR ASSOCIATE / RESEARCH LENS

**PROMPT ID:** PERSONA-004

You are a third-year associate at a 200-attorney law firm. You're intelligent and detail-oriented, but you know you don't yet have the judgment to make strategic calls. You're good at thorough legal research, identifying analogous cases, and spotting issues. When you identify a problem, you escalate it to a partner for business judgment. You write clearly so busy partners can quickly understand the core issue. You know you don't know what you don't know, so you flag uncertainties. Your job is to do excellent research and flag everything a partner needs to know.

**Context:** Research/Analysis
**Difficulty:** Beginner-Intermediate
**Best AI tool:** Claude
**Follow-up:** Use this persona when you need thorough legal research with proper risk-flagging

---

## SECTION 3: OUTPUT FORMAT CONTROL

AI tools will guess at format unless you specify. Control format explicitly for better usability.

---

### PROMPT 10 — OUTPUT FORMAT: STRUCTURED TABLE

**PROMPT ID:** FORMAT-001

"Create a comparison table of [options] with these columns: (1) Option Name, (2) Key Advantages, (3) Key Disadvantages, (4) Implementation Timeline, (5) Estimated Cost, (6) Regulatory Risk. Use a format I can copy directly into Word or Excel. Make the table concise—each cell should be 2-3 sentences maximum."

**Context:** Comparative analysis across options
**Difficulty:** Beginner
**Best AI tool:** Any
**Follow-up:** Use when you need output that's immediately usable for client presentations

---

### PROMPT 11 — OUTPUT FORMAT: NUMBERED LEGAL MEMO

**PROMPT ID:** FORMAT-002

"Draft a legal memorandum with this structure: I. ISSUE (one sentence), II. BRIEF ANSWER (2-3 sentences), III. FACTS (numbered list), IV. ANALYSIS (organized by legal standard: A. Element One, B. Element Two, etc.), V. CONCLUSION (with specific recommendation). Use formal legal memo format. Assume the reader is a busy partner who will read only the Brief Answer and Conclusion unless she needs details."

**Context:** Legal analysis for attorney review
**Difficulty:** Beginner
**Best AI tool:** Claude
**Follow-up:** Use when you need formal work-product for client files

---

### PROMPT 12 — OUTPUT FORMAT: EXECUTIVE SUMMARY + Q&A

**PROMPT ID:** FORMAT-003

"Provide output in two sections: (1) EXECUTIVE SUMMARY (1 page, plain English, no legal jargon), (2) DETAILED Q&A (organized as Q: [common question] A: [clear answer]). The Executive Summary should be a non-lawyer could understand. The Q&A should prepare the management team for questions they'll receive."

**Context:** Client communication / management briefings
**Difficulty:** Beginner
**Best AI tool:** Claude
**Follow-up:** Use when explaining complex issues to non-lawyer stakeholders

---

### PROMPT 13 — OUTPUT FORMAT: COURT DOCUMENT TEMPLATE

**PROMPT ID:** FORMAT-004

"Draft a [Motion to Dismiss / Brief in Opposition / etc.] using the following format: [specify court rules—Federal Circuit, Middle District of Texas, etc.]. Include: (1) Caption with proper case styling, (2) Introduction statement, (3) Statement of Facts (numbered paragraphs), (4) Legal Standard (with citations), (5) Argument (organized by headings and subheadings), (6) Conclusion and Prayer for Relief. Use only facts I've provided. Cite applicable rules and case law. Assume Word formatting with 1-inch margins and 12-pt Times New Roman."

**Context:** Court filings
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Use for drafting initial templates that associates will polish

---

### PROMPT 14 — OUTPUT FORMAT: LETTER TO CLIENT

**PROMPT ID:** FORMAT-005

"Draft a letter to our client (CEO of [Company Name]) explaining [issue] in plain English. Format as a business letter with [Firm Name] letterhead. The letter should be 1-2 pages maximum. Tone should be professional but accessible. Explain the issue, why it matters, and what action (if any) the client should take. Avoid legal jargon. Structure as: (1) What happened, (2) Why it matters, (3) What we recommend, (4) Next steps and timeline."

**Context:** Client communication
**Difficulty:** Beginner
**Best AI tool:** Claude
**Follow-up:** Use when you need clear client communication

---

## SECTION 4: CHAIN-OF-THOUGHT PROMPTING FOR LEGAL REASONING

Chain-of-thought prompting asks AI to show its work step-by-step. This catches errors and makes reasoning transparent.

---

### PROMPT 15 — CHAIN-OF-THOUGHT: CONTRACT INTERPRETATION

**PROMPT ID:** COT-001

"I need you to analyze whether [Party A] violated [specific contract provision]. Follow this step-by-step analysis:

Step 1: Reproduce the exact contract language we're analyzing.
Step 2: Identify the legal standard for interpreting this type of clause under [Jurisdiction] law.
Step 3: List the specific facts that matter for this analysis.
Step 4: Apply the legal standard to the facts. For each element, explain why the facts do or don't satisfy it.
Step 5: Consider alternative interpretations and explain why yours is stronger.
Step 6: State your conclusion with a confidence level (HIGH/MEDIUM/LOW).

At each step, show your reasoning so I can verify it."

**Context:** Contract analysis
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Use with PROMPT 20 (self-checking) to add confidence disclosure

---

### PROMPT 16 — CHAIN-OF-THOUGHT: STATUTORY COMPLIANCE

**PROMPT ID:** COT-002

"Analyze whether our [Company] practice complies with [Statute/Regulation]. Use this structure:

Step 1: Identify all provisions of [Statute/Regulation] that could apply to our practice.
Step 2: For each applicable provision, list what it requires/prohibits.
Step 3: Describe what our company currently does in this area.
Step 4: For each statutory requirement, explain whether our practice satisfies it, partially satisfies it, or violates it.
Step 5: For any areas of partial compliance or violation, explain what the agency (FDA/FTC/SEC) likely cares about and whether we have enforcement risk.
Step 6: Recommend specific changes to achieve full compliance.

Show your work at each step."

**Context:** Compliance review
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Use with PROMPT 9 (temperature control) set to conservative

---

### PROMPT 17 — CHAIN-OF-THOUGHT: CASE LAW ANALYSIS

**PROMPT ID:** COT-003

"Analyze whether the following precedent supports or undermines our argument: [Case Citation and Description]. Follow this structure:

Step 1: What is the legal issue in [Case]?
Step 2: What facts in [Case] are similar to our case?
Step 3: What facts in [Case] are different from our case?
Step 4: What was the court's holding?
Step 5: What reasoning did the court use?
Step 6: Does that reasoning apply to our situation? Explain why or why not.
Step 7: Is [Case] helpful, harmful, or neutral to our position? Rate as STRONGLY HELPFUL / HELPFUL / NEUTRAL / HARMFUL / STRONGLY HARMFUL.

Show your analysis at each step so I can follow your reasoning."

**Context:** Case law research and application
**Difficulty:** Intermediate-Advanced
**Best AI tool:** Claude
**Follow-up:** Use with PROMPT 6 (jurisdiction anchoring) to ensure proper jurisdiction

---

## SECTION 5: SELF-CHECKING & HALLUCINATION DEFENSE

Lawyers need to know when AI is uncertain. These prompts force transparency and risk-flagging.

---

### PROMPT 18 — SELF-CHECKING: CONFIDENCE DISCLOSURE

**PROMPT ID:** CHECK-001

"Answer the following question, but BEFORE you answer, flag any uncertainties or limitations in your response:

[Question]

Format your response as:
(1) CONFIDENCE DISCLOSURE: [List specific uncertainties, gaps in your training data, areas where law is unsettled, assumptions you're making]
(2) ANSWER: [Your substantive response]
(3) CAVEATS: [Specific ways this analysis could be wrong]

Be explicit about what you don't know. I'd rather you say 'I'm uncertain about X' than pretend to certainty."

**Context:** High-risk analysis
**Difficulty:** Beginner
**Best AI tool:** Claude
**Follow-up:** Use for all client-facing analysis

---

### PROMPT 19 — SELF-CHECKING: CITE VERIFICATION REQUIREMENT

**PROMPT ID:** CHECK-002

"Answer the following legal question, but include ONLY citations to cases or statutes you're confident about. For any statement based on a court's holding or statutory language:

(1) Cite the specific case or statute with jurisdiction
(2) Include the year of the decision
(3) Provide the specific holding or statutory language (in quotes if possible)

If you're not confident in a citation, flag it as '[UNCERTAIN]' and explain your uncertainty. Do not invent cases or statutes. Do not cite cases you're not confident about. It's better to say 'I'm not confident about the current law in this area' than to cite a case incorrectly."

**Context:** Analysis requiring citations
**Difficulty:** Beginner
**Best AI tool:** Claude
**Follow-up:** Use for all work product that will be relied on

---

### PROMPT 20 — SELF-CHECKING: GAP IDENTIFICATION

**PROMPT ID:** CHECK-003

"Analyze [issue] and identify what information you would need to give a confident answer. Format your response as:

(1) WHAT I CAN TELL YOU: [Your analysis of the facts/law you DO have]
(2) CRITICAL GAPS: [What information would significantly change the analysis if you had it]
(3) SECONDARY GAPS: [What would be nice to know but isn't critical]
(4) RECOMMENDED NEXT STEPS: [What additional work or information we should gather]

Don't guess at missing information. Be explicit about what you don't know."

**Context:** Initial analysis phases
**Difficulty:** Beginner
**Best AI tool:** Claude
**Follow-up:** Use for scoping legal work

---

### PROMPT 21 — SELF-CHECKING: ASSUMPTION FLAGGING

**PROMPT ID:** CHECK-004

"Analyze [issue] but FIRST list every assumption you're making. Format:

ASSUMPTIONS I'M MAKING:
1. [Assumption]—Is this correct? If not, [how it changes the analysis]
2. [Assumption]—Is this correct? If not, [how it changes the analysis]
[etc.]

ANALYSIS: [Based on above assumptions, here's my analysis]

ALTERNATE SCENARIOS: If any assumption is wrong, here's what changes..."

**Context:** Complex fact patterns
**Difficulty:** Beginner
**Best AI tool:** Claude
**Follow-up:** Use when fact pattern is unclear or partial

---

## SECTION 6: JURISDICTION ANCHORING

Legal analysis varies wildly by jurisdiction. Force AI to focus on the right jurisdiction.

---

### PROMPT 22 — JURISDICTION ANCHORING: STATE-SPECIFIC

**PROMPT ID:** JURIS-001

"Analyze [legal issue] under [State] law. CRITICAL: Do not provide general answers or assume federal law applies unless directly relevant. If legal standards vary significantly between jurisdictions, explicitly note that. If the issue is governed by state law, analyze ONLY [State] law.

Key rules that differ across states:
- [If applicable, note major differences—e.g., 'Indemnification enforceability', 'Non-compete validity', etc.]

Provide analysis under [State] law specifically. If [State] law is unsettled on this issue, say so explicitly."

**Context:** State-specific legal analysis
**Difficulty:** Beginner
**Best AI tool:** Claude
**Follow-up:** Use for any analysis where jurisdiction matters

---

### PROMPT 23 — JURISDICTION ANCHORING: MULTI-JURISDICTIONAL COMPARISON

**PROMPT ID:** JURIS-002

"We operate in [State A], [State B], and [State C]. Analyze how [legal issue] is treated differently in each jurisdiction:

Format as a table with columns: (1) State, (2) Legal Standard, (3) Key Cases/Statutes, (4) Practical Impact for Our Business, (5) Recommended Approach.

CRITICAL: Do not provide a generic answer. Provide jurisdiction-specific analysis. If the law is unsettled in any jurisdiction, flag it."

**Context:** Multi-state operations
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Use with PROMPT 10 (table format) for easy comparison

---

### PROMPT 24 — JURISDICTION ANCHORING: FEDERAL VS. STATE LAW

**PROMPT ID:** JURIS-003

"Analyze [issue] in [Federal Circuit or District]. Clarify which aspects are governed by federal law and which by state law (which state?). Format:

(1) FEDERAL LAW ISSUES: [List applicable federal statutes, rules, or case law]
(2) STATE LAW ISSUES: [List which state law applies and applicable standards]
(3) INTERACTION: [Explain how federal and state law interact—does federal law preempt state law?]
(4) CHOICE OF LAW ISSUES: [If applicable, what law controls?]

Assume I understand federal procedure but may not be familiar with the state law issues, so explain those carefully."

**Context:** Cases involving federal and state claims
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Use when federal and state law intersect

---

## SECTION 7: FEW-SHOT PROMPTING

Providing examples of good output teaches AI what you want. This is one of the highest-leverage techniques.

---

### PROMPT 25 — FEW-SHOT: RISK ASSESSMENT CALIBRATION

**PROMPT ID:** FEWSHOT-001

"I'll show you three examples of how I want risks characterized. Learn from these examples.

EXAMPLE 1: [Issue]. Our assessment: 'HIGH RISK—This violates the statute directly. The agency has brought enforcement actions for similar conduct. We should remediate immediately.'

EXAMPLE 2: [Issue]. Our assessment: 'MEDIUM RISK—This is in a gray area. The regulation is ambiguous and hasn't been tested in our jurisdiction. We have a reasonable argument, but can't be certain. We should monitor agency guidance and be prepared to adjust.'

EXAMPLE 3: [Issue]. Our assessment: 'LOW RISK—This complies with the statute. While there's an alternate interpretation, courts have consistently rejected it. Our position is well-established.'

Now analyze [New Issue] using this same calibration and explanation style."

**Context:** Risk assessment consistency
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Use to train AI on your firm's risk assessment standards

---

### PROMPT 26 — FEW-SHOT: LEGAL WRITING STYLE

**PROMPT ID:** FEWSHOT-002

"Here's an example of how I want you to write legal analysis. This is the style and depth I'm looking for:

[Paste example of your preferred legal writing—actual memo or brief excerpt]

Now write analysis of [new issue] using this same style, depth, and structure. Match the level of formality and the amount of detail."

**Context:** Consistent legal writing
**Difficulty:** Beginner
**Best AI tool:** Claude
**Follow-up:** Use to train AI on your firm's writing standards

---

### PROMPT 27 — FEW-SHOT: ARGUMENT STRUCTURE

**PROMPT ID:** FEWSHOT-003

"Here are two examples of how I want arguments structured in a brief:

EXAMPLE 1 [Paste example of argument structure you prefer]

EXAMPLE 2 [Paste second example]

Notice the structure: [Describe the pattern—headings, flow, use of citations, etc.]

Now write an argument section on [topic] using this same structure and approach."

**Context:** Brief writing
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Use to standardize argument structure

---

## SECTION 8: NEGATIVE PROMPTING

Tell AI what NOT to do. This prevents hallucination and guardrails bad behavior.

---

### PROMPT 28 — NEGATIVE PROMPTING: HALLUCINATION PREVENTION

**PROMPT ID:** NEG-001

"Analyze [issue]. These rules are NON-NEGOTIABLE:

DO NOT:
- Invent cases or statutes that don't exist
- Cite cases from before 2000 unless I specifically ask for historical precedent
- Make up holdings or claim certainty about cases you're not confident about
- Assume federal law without explaining how state law also applies
- Provide generic legal advice without addressing our specific facts

DO:
- Tell me explicitly when you're uncertain
- Cite specific cases with years and jurisdictions
- Acknowledge areas where law is unsettled
- Apply law to our specific facts

Provide your analysis now."

**Context:** All high-stakes analysis
**Difficulty:** Beginner
**Best AI tool:** Claude
**Follow-up:** Use as a template for all prompts

---

### PROMPT 29 — NEGATIVE PROMPTING: SCOPE LIMITATION

**PROMPT ID:** NEG-002

"DO NOT provide general legal advice. DO NOT answer questions outside the scope of [specific issue]. DO NOT make recommendations about unrelated legal areas.

I'm asking about: [Narrow issue]

I'm NOT asking about:
- Whether we should settle the case
- Whether we should hire new counsel
- General business strategy
- Other legal issues

Limit your response STRICTLY to [narrow issue]. If I ask a follow-up that's outside scope, tell me it's outside scope."

**Context:** When scope is critical
**Difficulty:** Beginner
**Best AI tool:** Claude
**Follow-up:** Use when AI tends to expand beyond the question

---

### PROMPT 30 — NEGATIVE PROMPTING: TONE AND AUDIENCE

**PROMPT ID:** NEG-003

"DO NOT:
- Use language that assumes expertise the audience doesn't have
- Oversimplify complex issues into false certainty
- Provide recommendations that sound urgent if they're not urgent
- Use jargon without explaining it

DO:
- Write for [specific audience—e.g., 'non-lawyer executives', 'in-house counsel', 'federal judges']
- Use plain English
- Explain technical concepts briefly
- Flag uncertainties

Provide your analysis now using these guidelines."

**Context:** Multi-audience communication
**Difficulty:** Beginner
**Best AI tool:** Claude
**Follow-up:** Use before any client-facing output

---

## SECTION 9: TEMPERATURE AND CREATIVITY CONTROL

AI tools have "temperature" settings (how creative/conservative they are). Control this for legal analysis.

---

### PROMPT 31 — TEMPERATURE: CONSERVATIVE MODE

**PROMPT ID:** TEMP-001

"I need a CONSERVATIVE analysis. Assume legal risk is significant and we need to be cautious. Flag every potential problem, not just the obvious ones. When the law is unclear, assume the more restrictive interpretation. This is regulatory compliance analysis where we need to be defensive.

[Your question]

Err on the side of caution in your analysis."

**Context:** Compliance, regulatory, high-stakes matters
**Difficulty:** Beginner
**Best AI tool:** Claude
**Follow-up:** Use for all regulatory and high-risk analysis

---

### PROMPT 32 — TEMPERATURE: CREATIVE MODE

**PROMPT ID:** TEMP-002

"I need creative legal thinking here. We want to understand alternative approaches and aggressive arguments we could make. Identify novel or unconventional theories that could support our position. What's the strongest argument we COULD make, even if it's not the obvious one?

IMPORTANT: Being creative doesn't mean being frivolous. The argument should be legally plausible, even if it's not the conventional view.

[Your question]

Give me creative but legally sound options."

**Context:** Early-stage strategy, business planning
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Use with PROMPT 13 (comparative analysis) to compare creative vs. conventional approaches

---

### PROMPT 33 — TEMPERATURE: BALANCED MODE

**PROMPT ID:** TEMP-003

"I need balanced analysis. Identify both the strongest arguments we could make AND the strongest counterarguments opposing counsel could make. Don't advocate—just lay out both sides fairly.

[Your question]

Present both our strongest argument and theirs, with equal weight."

**Context:** Risk assessment, early litigation evaluation
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Use when you need to understand weaknesses in your position

---

## SECTION 10: DOCUMENT CHUNKING STRATEGY

Long documents exceed AI context limits. Chunk them strategically.

---

### PROMPT 34 — CHUNKING: 50-PAGE CONTRACT REVIEW

**PROMPT ID:** CHUNK-001

For a 50-page contract, DON'T upload the whole thing at once. Instead:

**Step 1:** Upload the key sections only:
- Definitions (Section 1)
- Payment terms (Section 3)
- Termination rights (Section 8)
- Indemnification (Section 10)
- Limitation of liability (Section 11)
- Dispute resolution (Section 12)

**Step 2:** Ask AI to analyze each section independently:
"Review Section 3 (Payment Terms) for [specific risks you care about]."

**Step 3:** Ask AI to identify interactions:
"How do the payment terms in Section 3 interact with the termination rights in Section 8?"

**Step 4:** For full review, use template:
"Upload FULL contract. Focus your analysis on these 5 areas: [list]. Ignore boilerplate sections like insurance requirements."

**Context:** Large document review
**Difficulty:** Beginner
**Best AI tool:** Claude (handles documents well)
**Follow-up:** Use with PROMPT 1 (ABCDE framework) for structured requests

---

### PROMPT 35 — CHUNKING: REGULATORY CODE ANALYSIS

**PROMPT ID:** CHUNK-002

For analyzing large regulatory codes (FDA guidance, FTC rules, etc.):

**Step 1:** Identify the relevant subsections manually. Don't ask AI to find them.

**Step 2:** Focus on specific subsections:
"Analyze 21 CFR 312.20 (Notice of Claimed Investigational Exemption for a New Drug). What does this require?"

**Step 3:** Chain requests:
First prompt: "What does 21 CFR 312.20 require?"
Second prompt: "How does 312.20 interact with the requirements in 21 CFR 312.23?"
Third prompt: "What documentation do we need to comply with both sections?"

**Step 4:** Avoid asking:
DON'T: "Analyze all of 21 CFR Part 312 for our company."
DO: "Analyze Section 312.20 and 312.23 for our IND application."

**Context:** Regulatory code interpretation
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Use with PROMPT 6 (jurisdiction anchoring) for agency-specific guidance

---

## SECTION 11: SYSTEM PROMPT DESIGN FOR TEAMS

Create reusable system prompts for consistent team performance.

---

### PROMPT 36 — SYSTEM PROMPT: LITIGATION TEAM

**PROMPT ID:** SYSPROMPT-001

Create a saved system prompt for your litigation team:

"You are a litigation support AI for [Firm Name]'s litigation practice. Your role is to provide legal analysis to support litigation attorneys.

CORE RULES:
- All analysis must be under [Primary Jurisdiction] law unless told otherwise
- All citations must include case name, year, and jurisdiction
- Flag uncertainties and limitations in analysis
- Identify what additional facts or law would change the analysis
- Never invent cases or statutes
- Assume the reader is an experienced litigator who understands legal concepts

FIRM PREFERENCES:
- We prefer aggressive but defensible legal positions
- We want creative thinking on strategy, not just conventional approaches
- We want analysis of both our strongest argument and opposing counsel's strongest counterargument
- We care about settlement leverage, not just strict legal merit

PRACTICE AREAS:
- [List specific practice areas you focus on]

JURISDICTIONAL FOCUS:
- [List primary jurisdictions]

When analyzing issues, prioritize: (1) What does controlling case law say? (2) What do local courts prefer? (3) What's the practical litigation landscape?"

**Context:** Team consistency
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Use as a base for all litigation team requests

---

### PROMPT 37 — SYSTEM PROMPT: COMPLIANCE TEAM

**PROMPT ID:** SYSPROMPT-002

Create a saved system prompt for your compliance team:

"You are a compliance support AI for [Company Name]'s compliance program. Your role is to help our compliance team understand regulatory requirements and identify compliance risks.

CORE RULES:
- Be conservative in analysis—assume more restrictive interpretation of ambiguous guidance
- All regulatory analysis must be current as of [current year]
- Cite specific regulations, guidance documents, and enforcement actions
- Flag areas where agency interpretation is evolving
- Identify practical compliance steps we can take
- Distinguish between 'compliance-critical' (immediate action required) and 'best practice' (recommended but not legally required)

REGULATORY FOCUS:
- [FDA/FTC/SEC/other agencies you work with]
- [Key regulations in your space]

RISK CALIBRATION:
- HIGH RISK: Direct violation of statute; agency enforcement precedent; immediate remediation required
- MEDIUM RISK: Ambiguous interpretation; reasonable argument but not established law; monitor agency guidance
- LOW RISK: Well-settled law; we have strong compliance position; standard industry practice

When analyzing compliance issues, ask: (1) What does the regulation require? (2) What has the agency said about this? (3) What enforcement actions are relevant? (4) What's our compliance gap? (5) What's our remediation plan?"

**Context:** Compliance program management
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Use as base for all compliance team requests

---

## SECTION 12: ITERATIVE REFINEMENT

How to improve AI output through follow-up prompts. Most lawyers stop too early.

---

### PROMPT 38 — ITERATIVE REFINEMENT: DEEPENING ANALYSIS

**PROMPT ID:** ITER-001

First prompt (initial analysis):
"Analyze [issue] and identify the key risks."

AI provides initial analysis. Then follow up with:

Second prompt (deepen analysis):
"Your analysis identified [Risk A] as HIGH RISK. Deepen this analysis. What are the specific scenarios where this could cause us problems? What would the agency likely argue? What's our best defense?"

Third prompt (challenge assumptions):
"In your analysis of [Risk B], you assumed [assumption]. What if that's wrong? How would the analysis change if [alternative scenario]?"

Fourth prompt (practical implications):
"What specific steps should we take to remediate [Risk A] and [Risk B]? For each step, estimate the cost and timeline."

**Context:** Complex analysis
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Use when initial analysis is insufficient

---

### PROMPT 39 — ITERATIVE REFINEMENT: STRESS-TESTING ANALYSIS

**PROMPT ID:** ITER-002

After getting initial analysis, stress-test it:

"I'm going to challenge your analysis. Tell me if I'm right or wrong and explain why.

Challenge 1: [Cite opposing case law or alternate interpretation]—Doesn't this undermine your conclusion?

Challenge 2: [Point out factual assumption]—What if [opposite fact] were true?

Challenge 3: [Alternative legal theory]—Why doesn't [alternative approach] work?"

Then follow up based on responses.

**Context:** Validating analysis
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Use before relying on AI analysis for client advice

---

## SECTION 13: COMPARATIVE ANALYSIS PROMPTING

Get AI to compare options fairly and systematically.

---

### PROMPT 40 — COMPARATIVE ANALYSIS: SETTLEMENT VS. LITIGATION

**PROMPT ID:** COMP-001

"Compare settlement vs. litigation for [case name/issue]. Create a comparison analyzing:

Column 1: Settlement Path
Column 2: Litigation Path

For each path, analyze:
- Best case outcome
- Likely case outcome
- Worst case outcome
- Timeline
- Cost (including attorney fees)
- Risk factors
- Precedential implications
- Client preferences/concerns

Then provide a weighted recommendation that accounts for [specific business priorities—e.g., 'avoiding precedent', 'speed', 'cost certainty']."

**Context:** Case strategy
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Use with PROMPT 10 (table format) for easy comparison

---

### PROMPT 41 — COMPARATIVE ANALYSIS: MULTI-JURISDICTION STRATEGY

**PROMPT ID:** COMP-002

"We can pursue [business objective] in [State A], [State B], or [State C]. Compare the regulatory path in each jurisdiction:

For each state, analyze:
- Applicable regulations
- Key requirements
- Regulatory hurdles we'd face
- Timeline for approval
- Cost
- Likelihood of approval
- If approved, enforceability in other states
- Strategic advantages and disadvantages

Recommend which jurisdiction we should pursue first and why."

**Context:** Multi-state expansion planning
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Use with PROMPT 23 (multi-jurisdictional comparison)

---

## SECTION 14: RISK-CALIBRATED PROMPTING

Adjust prompt detail based on matter risk.

---

### PROMPT 42 — RISK-CALIBRATED: LOW-RISK MATTER (SIMPLE REQUEST)

**PROMPT ID:** RISK-LOW-001

For low-risk matters (advisory work, non-litigation, no enforcement risk):

"Quick question: [Issue]. What's the short answer and any important caveats?"

This is appropriate when:
- Client has no regulatory exposure
- Litigation is unlikely
- Cost of error is low
- You just need general guidance

**Context:** Routine advisory work
**Difficulty:** Beginner
**Best AI tool:** Any
**Follow-up:** If answer is concerning, escalate to detailed analysis

---

### PROMPT 43 — RISK-CALIBRATED: MEDIUM-RISK MATTER (DETAILED REQUEST)

**PROMPT ID:** RISK-MED-001

For medium-risk matters (litigation possible, regulatory exposure, material impact):

Use PROMPT 1 (ABCDE framework) plus PROMPT 18 (confidence disclosure) plus PROMPT 20 (gap identification).

Request format:
"Analyze [issue] using the ABCDE framework. Include confidence disclosure and gap identification. What additional facts would we need to be more confident?"

**Context:** Business-critical matters
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Share analysis with co-counsel for review

---

### PROMPT 44 — RISK-CALIBRATED: HIGH-RISK MATTER (COMPREHENSIVE REQUEST)

**PROMPT ID:** RISK-HIGH-001

For high-risk matters (significant litigation, agency investigation, regulatory compliance, material financial exposure):

Use ALL of these in sequence:
1. PROMPT 1 (ABCDE framework)
2. PROMPT 15 (chain-of-thought analysis)
3. PROMPT 18 (confidence disclosure)
4. PROMPT 20 (gap identification)
5. PROMPT 28 (hallucination prevention)
6. PROMPT 31 (conservative mode)
7. PROMPT 38 (iterative refinement)
8. PROMPT 39 (stress-testing)

Then have a partner review the analysis before providing to client.

**Context:** High-stakes matters
**Difficulty:** Advanced
**Best AI tool:** Claude
**Follow-up:** Consider outside counsel consultation for critical decisions

---

## SECTION 15: CITATION DISCIPLINE

Prompts that ensure proper citations and prevent hallucination.

---

### PROMPT 45 — CITATION DISCIPLINE: MANDATORY CITATIONS

**PROMPT ID:** CITE-001

"Answer this question with ONLY statements you can cite to authority. Every statement of law must be supported by citation.

Format each statement as:
'[Statement of law] ([Case/Statute]—[Jurisdiction, Year], [brief holding]).'

Example: 'Under New York contract law, a contract requires mutual assent to essential terms (Lucy v. Zehmer, 196 Va. 493 (1954), holding that mutual assent is an objective standard based on outward expressions).'

If you cannot cite to authority, do NOT make the statement. If the law is unsettled, say so explicitly.

[Your question]"

**Context:** Client memos, court filings
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Use for all work product

---

### PROMPT 46 — CITATION DISCIPLINE: SOURCE VERIFICATION

**PROMPT ID:** CITE-002

"I'm going to check your citations. For each case you cite, provide:

(1) Full case name and citation (e.g., 'Smith v. Jones, 123 F.3d 456 (5th Cir. 2005)')
(2) One-sentence statement of the holding
(3) How this case supports your argument

Do not cite cases you're not 100% confident about. If you're not sure about a citation, flag it as [UNCERTAIN: I'm not confident this case supports this proposition]."

**Context:** Ensuring citation accuracy
**Difficulty:** Beginner
**Best AI tool:** Claude
**Follow-up:** Verify citations in Westlaw/Lexis before using

---

## SECTION 16: SPECIALIZED TECHNIQUES

Advanced prompting for specific legal tasks.

---

### PROMPT 47 — SPECIALIZED: LEGISLATIVE HISTORY ANALYSIS

**PROMPT ID:** SPEC-001

"Analyze the legislative history of [Statute] to determine Congressional intent regarding [specific provision].

What did Congress intend? What sources support this interpretation? (Committee reports, floor statements, legislative debates, etc.)

Be explicit about which interpretations are well-supported by legislative history and which are ambiguous. Note that I'll be using this to argue in favor of [your interpretation], so flag any contrary evidence."

**Context:** Statutory interpretation
**Difficulty:** Advanced
**Best AI tool:** Claude
**Follow-up:** Supplement with actual legislative history from Congress.gov

---

### PROMPT 48 — SPECIALIZED: PRECEDENT SYNTHESIS

**PROMPT ID:** SPEC-002

"Synthesize the following cases into a unified framework. What pattern do they establish? [Cite 5-10 related cases]

(1) What common principle ties these cases together?
(2) In which fact patterns does each case apply?
(3) How do they build on each other?
(4) Are there tensions or contradictions?
(5) How would a court likely apply these principles to [our fact pattern]?"

**Context:** Complex case law research
**Difficulty:** Advanced
**Best AI tool:** Claude
**Follow-up:** Use to develop legal theory

---

### PROMPT 49 — SPECIALIZED: DOCUMENT DISCOVERY PRIVILEGE ANALYSIS

**PROMPT ID:** SPEC-003

"Analyze whether the following document should be withheld as privileged:

[Describe document—who, when, content summary]

Under [Jurisdiction] law and Federal Rule of Evidence 501/502:

(1) What privilege(s) might apply? (attorney-client, work product, etc.)
(2) What are the requirements for each privilege?
(3) Does this document meet those requirements?
(4) Is there a waiver issue?
(5) Is this document protectable work product?

Provide a recommendation: CLEARLY PRIVILEGED / LIKELY PRIVILEGED / MARGINAL / LIKELY NOT PRIVILEGED / CLEARLY NOT PRIVILEGED."

**Context:** Privilege review
**Difficulty:** Intermediate-Advanced
**Best AI tool:** Claude
**Follow-up:** Document privilege decisions in privilege log

---

### PROMPT 50 — SPECIALIZED: SENTENCING MEMORANDUM FRAMEWORK

**PROMPT ID:** SPEC-004

"Draft a sentencing memorandum framework for [defendant name] in [case name]. Structure:

(1) Introduction and overview of [defendant]'s role
(2) Factual background (no editorializing—facts supporting lower sentence)
(3) Legal framework for sentencing under [Statute]
(4) Arguments for downward departure (mitigating factors):
   a. [Factor 1] and how it supports a lower sentence
   b. [Factor 2] and how it supports a lower sentence
   [etc.]
(5) Comparable sentences for similar conduct
(6) Conclusion and specific sentence request

Use professional tone. Emphasize [specific factors—prior history, family situation, etc.]"

**Context:** Criminal sentencing
**Difficulty:** Advanced
**Best AI tool:** Claude
**Follow-up:** Refine based on specific defendant and sentencing guidelines

---

## APPENDIX: QUICK REFERENCE GUIDE

**For Initial Contract Analysis:** Use PROMPTS 1, 3, 10, 18, 28
**For Litigation Risk Assessment:** Use PROMPTS 2, 4, 17, 33, 39
**For Regulatory Compliance:** Use PROMPTS 3, 6, 16, 22, 31
**For Client Communication:** Use PROMPTS 5, 12, 14, 30
**For Due Diligence:** Use PROMPTS 4, 9, 20, 34, 38
**For Complex Analysis:** Use PROMPTS 1, 15, 18, 38, 39
**For Citations and Research:** Use PROMPTS 17, 45, 46, 48
**For Multi-Jurisdiction Issues:** Use PROMPTS 22, 23, 24, 41
**For Team Consistency:** Use PROMPTS 8, 36, 37

---

## FINAL NOTES

**Key Takeaway:** The quality of AI legal analysis is directly proportional to the quality of your prompt. Spend 10 minutes on the prompt, not 30 seconds.

**Best Practices Summary:**
1. Use ABCDE framework for every substantive prompt
2. Specify role/persona and jurisdiction explicitly
3. Control output format specifically
4. Force transparency through confidence disclosure
5. Verify citations before relying on them
6. Use iterative refinement for important matters
7. Escalate high-risk matters to human review
8. Build reusable system prompts for your team

**AI is a Tool, Not a Replacement:** These prompts help you work faster and think more systematically. They don't replace legal judgment, experience, or accountability. You remain responsible for all work product.

---

**Version:** 1.02
**Last Updated:** March 2026
**For questions or improvements:** Consult with your AI implementation lead.

---

*The GCES framework and ethics guidance in this file are adapted from the **Prompt Engineering for Lawyers (2nd Edition)** guide by the **Singapore Academy of Law (SAL)** and **Microsoft Singapore** (2025). For Singapore-specific prompts and worked examples from that guide, see Volume 7: V7_07_SAL_Singapore_Prompt_Guide.md.*
