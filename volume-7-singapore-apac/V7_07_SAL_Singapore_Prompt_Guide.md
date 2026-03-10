# SAL-Microsoft Prompt Engineering Guide for Singapore Lawyers

*This file is based on and adapted from the **Prompt Engineering for Lawyers (2nd Edition)** guide, published by the **Singapore Academy of Law (SAL)** in collaboration with **Microsoft Singapore** (2025). The prompts, frameworks, and worked examples in this file draw directly from that guide. Full credit to SAL, Microsoft Singapore, and the Singapore legal professionals who contributed, including competition winners Mr Rodney Yap (PwC NewLaw / SMU), Mr Jerome Tay (NUS Law), and other practitioner contributors. Source: https://sal.org.sg/wp-content/uploads/2025/10/Prompt-Engineering-Guide-2025-2nd-Edition.pdf*

---

## Overview

The Singapore Academy of Law (SAL), in collaboration with Microsoft Singapore, developed this prompt engineering guide specifically for Singapore lawyers. It is grounded in real-world Singapore legal practice and features prompts tested by Singapore practitioners across litigation, corporate, in-house, regulatory, and compliance work.

This volume captures the key frameworks, use-case prompts, and competition-winning examples from that guide, adapted and extended for use in The Legal Prompts Library.

---

## SECTION 1: THE SAL GCES FRAMEWORK

The SAL guide teaches a four-part framework for structuring legal prompts. Think of it as the "what, why, how, and where" of a good prompt.

---

### THE GCES FRAMEWORK EXPLAINED

**G — Goal**
State the task at the very beginning of your prompt. Use action verbs: *Draft*, *Summarise*, *Analyse*, *Review*, *Compare*. If the task is complex, break it into sub-goals and state them in order of priority.

**C — Context**
Provide the background: who you are, who the client is, the jurisdiction, the applicable law, and any relevant facts. You can also include a few examples of the style or format you want (this is called "few-shot prompting").

**E — Expectations**
Set out how you want the output: tone (formal, plain language), format (table, bullet points, numbered list), depth (one paragraph, full memo), word limit, and audience (client, senior partner, court).

**S — Source**
Attach or reference the specific documents, clauses, URLs, or legislation the AI should use. Be precise — paste in the relevant paragraph rather than uploading an entire contract. Always ensure documents shared comply with your firm's confidentiality and data security policies.

---

### PROMPT 1 — GCES FRAMEWORK: CONTRACT REVIEW (SINGAPORE LAW)

**Context:** Singapore-governed commercial agreement

**Goal:** Review the attached contract and identify the top 5 risks for our client.

**Context:** I am a lawyer acting for [PARTY], the [buyer/seller/licensor/licensee], in a [describe transaction] governed by Singapore law. The counterparty is [describe]. The deal is in its [first/second] round of negotiation.

**Expectations:** For each risk, rate it HIGH/MEDIUM/LOW. Present findings in a table with columns: (1) Clause reference, (2) Issue, (3) Risk rating, (4) Why it matters, (5) Recommended language change. Use formal legal language.

**Source:** Use only the attached contract. Do not reference any external sources.

**Difficulty:** Beginner
**Best AI tool:** Claude, Copilot (with document attachment)
**Follow-up:** Chain with a redlining prompt to generate specific revised clause language

---

### PROMPT 2 — GCES FRAMEWORK: LEGAL RESEARCH (SINGAPORE COURTS)

**Goal:** [State your research question clearly, e.g. "Identify the legal test for striking out a claim under Order 9 Rule 16 of the Rules of Court 2021."]

**Context:** I am a lawyer acting for [plaintiff/defendant] in a Singapore [High Court/District Court/State Courts] matter. The key issue is [describe]. The claim involves [area of law].

**Expectations:** Provide a structured legal analysis covering: (1) the applicable rule or statute, (2) the leading Singapore case(s) and their facts, (3) the legal test distilled from the cases, (4) how the test applies to the facts I will describe, (5) any recent developments or conflicting cases. Present in formal legal language suitable for inclusion in a legal memorandum.

**Source:** Use SG Courts at [insert URL] and Singapore Statutes Online at [insert URL] as primary sources. Provide detailed citations.

**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Ask the AI to identify weaknesses in the analysis and potential counter-arguments

---

### PROMPT 3 — GCES FRAMEWORK: CLIENT EMAIL FOLLOW-UP (MEETING RECAP)

*Adapted from the SAL Guide's practical use case examples.*

**Goal:** Summarise the key points from the attached meeting minutes and draft a follow-up email to the client.

**Context:** I am a lawyer who attended a meeting with [CLIENT NAME] on [DATE] regarding [MATTER]. The meeting was attended by [LIST ATTENDEES].

**Expectations:** The email should include:
- Date, time, and location of the meeting, with a list of persons in attendance
- A list of the topics discussed
- Key decisions and actions, with a summary of the main points agreed upon
- A detailed action plan with responsibilities assigned to specific team members with deadlines for each action item

Use plain language and be concise. The email is addressed to [CLIENT NAME] and will be sent by [LAWYER NAME].

**Source:** Restrict your summary to materials within the attached meeting minutes only.

**Difficulty:** Beginner
**Best AI tool:** Copilot (Teams/Outlook), Claude
**Follow-up:** Ask the AI to shorten the email to a maximum of 200 words

---

### PROMPT 4 — GCES FRAMEWORK: REGULATORY COMPLIANCE CHECKLIST (SINGAPORE)

*Adapted from the SAL Guide.*

**Goal:** Generate a list of obligations for an employer during a retrenchment exercise.

**Context:** My company is closing a department. I am the in-house counsel, and I need a list of obligations that I can refer to when briefing internal teams.

**Expectations:** Produce a checklist that includes references, arranged according to the areas that the Human Resource, Finance, Corporate Communications, and Legal departments must be briefed on. Additionally, identify the conditions for proper termination and any additional considerations. Format as a table.

**Source:** Limit your analysis to the Singapore Employment Act, the Tripartite Guidelines on Fair Employment Practices, and Ministry of Manpower guidelines and advisories. Cite applicable provisions.

**Difficulty:** Intermediate
**Best AI tool:** Claude
**Follow-up:** Ask the AI to flag any areas where your company's practices may fall short

---

## SECTION 2: SINGAPORE-SPECIFIC USE CASES (SAL GUIDE)

The following prompts are drawn directly from the SAL Guide's worked use cases, adapted for general library use.

---

### PROMPT 5 — CONTRACT DRAFTING: IP INDEMNITY CLAUSE

*Source: SAL Guide, Contract Review and Drafting section.*

Draft an IP indemnity clause in favour of the licensor. I am a lawyer acting for a licensor in a negotiation on a software IP licensing agreement. Ensure that the clauses are in formal legal language using the active voice and concise. Base your drafts on these samples: [sample 1] and [sample 2].

**Context:** Singapore-governed IP licensing agreement
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Tips:** Paste in your sample clauses directly in the prompt. This "few-shot" approach significantly improves relevance and quality.

---

### PROMPT 6 — CONTRACT DRAFTING: REPRESENTATIONS AND WARRANTIES (LICENSOR)

*Source: SAL Guide, Contract Review and Drafting section.*

Draft a clause that outlines representations and warranties for a software IP licensing agreement. I am a lawyer acting for the licensor. The clause should strongly favour the licensor, ensuring that:
- The licensor's ownership of the IP is clearly affirmed
- There are no existing infringement claims
- The software meets defined performance standards

The language must be formal and legally robust, appropriate for inclusion in a legal contract. Base the clause on [sample A] and [sample B], ensuring that the licensor's interests are thoroughly protected.

**Context:** Singapore-governed software licensing
**Difficulty:** Intermediate
**Best AI tool:** Claude

---

### PROMPT 7 — CONTRACT DRAFTING: MSA CLEAN DRAFT FROM NEGOTIATION RECORD

*Source: SAL Guide, New Prompts (2nd Edition).*

I am a lawyer advising on a transaction governed by Singapore law. I want to update the attached Master Services Agreement (MSA) to incorporate all negotiated changes reflected in the accompanying email chain/summary, and produce a clean, execution-ready draft.

The deliverable is a clean, revised version of the MSA that accurately reflects these agreed amendments. You must ensure that:
- All defined terms are used correctly
- The revisions do not result in internal contradictions within the agreement
- No new substantive legal terms are introduced or clauses modified that were not subject to negotiation
- The original formatting and clause numbering is maintained, unless specific changes require re-numbering

Use only these materials:
- Base document: original MSA (.docx)
- Negotiation record: email chain or a summary document listing each agreed change

Where attachments are referenced, restrict analysis and drafting to those materials and provide pinpoint references where applicable.

**Context:** Singapore law commercial contracts
**Difficulty:** Advanced
**Best AI tool:** Claude (document attachment required)
**Tips:** Break this into two steps if the MSA is long — first ask the AI to list all the changes it identified from the email chain, verify them, then proceed to produce the clean draft.

---

### PROMPT 8 — REAL ESTATE: TENANCY AGREEMENT FROM LOI

*Source: SAL Guide, New Prompts (2nd Edition).*

I am a paralegal in a real estate practice group in Singapore. We have received a signed Letter of Intent (LOI) from the landlord and prospective tenant. My task is to draft the first version of the Tenancy Agreement (TA) for the landlord's review based on the agreed terms.

Prepare a complete Tenancy Agreement (TA) from the attached Letter of Intent (LOI), using the firm's TA template provided. Systematically populate the template with the following key details:
- Full names and UEN/NRIC of the Landlord and Tenant
- Address of the demised premises
- Lease term (including commencement and expiry dates)
- Monthly rent and any rent-free period
- Security deposit amount
- Permitted use of the premises
- Any option to renew
- Responsibility for stamp duty and legal costs

At the end of the draft, insert a short section titled **"Review Notes for Solicitor"** to flag:
1. Any terms in the LOI that deviate from the standard template (e.g. an unusual break clause)
2. Any standard clauses in the template that are not addressed in the LOI (e.g. if the LOI is silent on reinstatement obligations)

Do not alter any standard legal clauses in the template unless the LOI specifically requires it. The final output should be a clean, ready-to-review draft of the Tenancy Agreement.

Use only these materials:
- Core Terms: [Attach the signed Letter of Intent (LOI)]
- Base Document: [Attach the firm's standard commercial Tenancy Agreement template]

Where attachments are referenced, restrict analysis and drafting to those materials and provide pinpoint references where applicable.

**Context:** Singapore property / commercial leasing
**Difficulty:** Intermediate
**Best AI tool:** Claude (document attachment required)

---

### PROMPT 9 — LITIGATION: AFFIDAVIT vs. STATEMENT OF CLAIM INCONSISTENCY TABLE

*Source: SAL Guide, Dispute Resolution section.*

Analyse the plaintiff's affidavit against the statement of claim to identify areas of inconsistencies. I am a lawyer acting for the defendant.

The analysis should be presented in a table format with the following columns:
- Item Number
- Statement of Claim Reference (paragraph/section)
- Affidavit Reference (paragraph/section)
- Description of Inconsistency/Discrepancy
- Potential Impact on Case

Prioritise significant inconsistencies that could materially affect the case. Include both factual discrepancies and differences in the characterisation of events or intentions. Be objective, focusing on factual comparisons rather than legal arguments. If you encounter any ambiguities, indicate this in your analysis.

Use only the two documents provided [insert reference files], and do not reference any external sources or make assumptions beyond their contents.

**Context:** Singapore civil litigation, defendant-side
**Difficulty:** Intermediate
**Best AI tool:** Claude (document attachment required)
**Follow-up:** Ask the AI to convert the table into a narrative summary for use in written submissions

---

### PROMPT 10 — LITIGATION: WITNESS CREDIBILITY ANALYSIS

*Source: SAL Guide, Dispute Resolution section.*

Analyse the affidavit of the witness and the transcript of his oral testimony during the trial to identify inconsistencies and discrepancies. I am preparing written submissions after trial. The inconsistencies will be used to attack the witness's credibility.

Think through this step-by-step, focusing on inconsistencies that could materially affect his credibility. Include discrepancies in facts, timelines, event interpretations, and characterisations of key interactions or documents.

Present your findings in a table with the following columns:
- Item Number
- Affidavit (Para/Section)
- Transcript (Page/Line Number)
- Description of Inconsistency
- Impact on Credibility

In the transcript, the witness is labelled "[DW3 / insert label]". Use only the witness's affidavit and the extract of transcript provided. Do not reference any external sources or make assumptions beyond these documents.

**Context:** Singapore civil litigation, post-trial submissions
**Difficulty:** Advanced
**Best AI tool:** Claude (document attachment required)

---

### PROMPT 11 — MOTOR ACCIDENT: ENE SUBMISSION (PART 1 — FACTUAL NARRATIVE)

*Source: SAL Guide, New Prompts (2nd Edition). Applicable to State Courts practice in Singapore.*

I am a lawyer advising on motor accident claims. My firm represents the Claimant in a motor vehicle collision matter scheduled for an Early Neutral Evaluation (ENE) submission at the Singapore State Courts. My task is to draft a compelling submission on liability, arguing for a favourable apportionment in the claimant's favour.

**Part 1:** Prepare the Introduction, Undisputed Facts, Disputed Facts, and The Parties' Positions.

The ENE submission must strictly adhere to the structure in the State Court's Practice Directions Appendix B (Guidelines for Court Dispute Resolution for Non-Injury Motor Accident Claims). The factual summary should present a concise and persuasive narrative, highlighting specific evidence from the case file that supports the Claimant's position.

Use only these materials:
- State Court's Practice Directions Appendix B
- Case file documents (Traffic Police report, accident sketch plan, medical reports, client's statement, any dashcam transcript/summary)
- Any firm template or a past, successful ENE submission for formatting/style reference

The tone must be formal, objective and persuasive, in keeping with the standards expected by the Singapore Courts. All factual assertions must be explicitly grounded in the evidence provided; no facts are to be invented or inferred.

**Difficulty:** Advanced
**Best AI tool:** Claude (document attachment required)
**Follow-up:** Use PROMPT 12 (Part 2) to complete the Submissions on Liability and Conclusion

---

### PROMPT 12 — MOTOR ACCIDENT: ENE SUBMISSION (PART 2 — LIABILITY SUBMISSIONS)

*Source: SAL Guide, New Prompts (2nd Edition).*

Building on the previously prepared factual narrative (Part 1), continue drafting the ENE submission with the remaining sections: Submissions on Liability and Conclusion.

Analyse the factual summary and identify relevant principles and scenarios from the Singapore Motor Accident Guide (MAG) that can be relied upon to substantiate the Claimant's case.

The submission should:
- Critically analyse the available evidence, particularly the sketch plan and photographs
- Highlight any inconsistencies or potential weaknesses in the Defendant's anticipated arguments
- Reference specific MAG sections that support the Claimant's case

Conclude with a clearly reasoned proposal for liability apportionment ([insert proposed percentage, e.g. 90%]). Identify relevant evidence and MAG sections that justify the proposed percentage, with structured and detailed reasons.

Use only these materials:
- State Court's Practice Directions Appendix B
- Case file documents
- Relevant extracts from the latest uploaded copy of the Singapore Motor Accident Guide (MAG)
- Any firm template or a past, successful ENE submission for formatting/style reference

All factual assertions must be grounded in the evidence provided. Restrict analysis and drafting to attached materials with pinpoint references.

**Difficulty:** Advanced
**Best AI tool:** Claude (document attachment required)

---

### PROMPT 13 — M&A DUE DILIGENCE: IP LICENSING IMPACT ANALYSIS

*Source: SAL Guide, Mergers and Acquisitions section.*

Analyse the provided third-party IP licensing contracts in the context of the merger of two companies. I am a corporate lawyer representing the merged entity. I want to identify IP licensed from third parties and analyse the potential impact if these licences are terminated.

Generate a table with information organised according to:
- Name of third-party licensor
- Summary of the licensing clauses
- Permitted use and scope of licensed IP
- Whether licence is exclusive or non-exclusive
- Whether licence is perpetual or renewable
- Whether licence is revocable
- Whether licence is world-wide or limited by region/country
- Whether regular licence fees are payable
- Whether there is a right to sub-license
- Reference link to the source contract

Restrict your analysis to the contracts attached. Do not include any analysis beyond the attached set.

**Context:** Singapore-governed M&A / due diligence
**Difficulty:** Advanced
**Best AI tool:** Claude (document attachment required)

---

### PROMPT 14 — M&A: JOINT VENTURE TERM SHEET FROM MOU

*Source: SAL Guide, New Prompts (2nd Edition).*

I am a corporate lawyer advising on a new Joint Venture (JV) transaction. Our client has signed a high-level Memorandum of Understanding (MOU) with a potential JV partner. I need to draft a comprehensive, non-binding Term Sheet that will form the basis for drafting the definitive JV Agreement.

Prepare a detailed Joint Venture Term Sheet by populating the firm's standard template using the commercial terms set out in the attached MOU. Translate the high-level principles of the MOU into the appropriate detailed clauses of the Term Sheet.

Pay close attention when extracting and inserting the following key elements:
- Names of the JV partners; the business objective of the JV
- Each party's capital contributions (form and amount)
- Proposed ownership percentages
- Governance arrangements including board composition, voting rights, and management appointments
- Any agreed mechanisms for deadlock or dispute resolution

At the end of the document, include a separate section titled **"Points for Discussion"** listing any standard commercial or legal terms not addressed in the MOU, such as IP licensing, dividend policy, exit scenarios, or restrictive covenants.

The Term Sheet must clearly state that it is non-binding, except for specific provisions like Confidentiality and Governing Law. Do not invent or infer commercial terms; missing information should be noted under "Points for Discussion" rather than filled in.

Use only: [MOU, term sheet template, …]

Where attachments are referenced, restrict analysis and drafting to those materials with pinpoint references.

**Context:** Singapore-governed joint ventures / corporate
**Difficulty:** Advanced
**Best AI tool:** Claude (document attachment required)

---

### PROMPT 15 — DATA PROTECTION: PDPA BREACH NOTIFICATION PACKAGE

*Source: SAL Guide, New Prompts (2nd Edition) — Regulatory Compliance section.*

I am a data protection counsel supporting a Singapore organisation. Using only the attached incident log and timeline, prepare:
1. An internal incident report
2. A data subject notification
3. A regulator-facing summary compliant with the Personal Data Protection Act 2012 (Singapore)

**Internal Report Structure:**
- Incident Overview & Timeline (facts-only chronology)
- Affected Personal Data (types, volumes, data subjects)
- Containment & Eradication Actions
- Risk Assessment (likelihood/severity of harm)
- Mitigation Steps
- Notifiability Analysis under PDPA (threshold and rationale)
- Recommendations (actions, owners, timelines)

**Notifiability Thresholds:**
- Significant harm (Regulation 3): whether the breach involves full name/NRIC or other identifiers, or account credentials combined with passwords/security codes/biometric data
- Significant scale (Regulation 4): whether ≥500 individuals are affected

For the PDPC notification, include the mandatory particulars under Regulation 5 (date of awareness, chronology of containment steps, number of affected individuals, types of data, potential harm, remedial actions, contact person).

For notifications to individuals (Regulation 6), include: circumstances, types of data, potential harm, remedial steps by the organisation, and steps individuals can take to mitigate misuse.

Do not speculate on root cause or impact; state what is known, what is suspected, and what remains unknown.

Use only these materials:
- Incident timeline and data categories
- Containment actions and impact assessment
- Personal Data Protection Act 2012 Part 6A
- Personal Data Protection (Notification of Data Breaches) Regulations 2021
- PDPC Advisory Guidelines on Key Concepts

Where attachments are referenced, restrict analysis to those materials with pinpoint references.

**Context:** Singapore PDPA data breach response
**Difficulty:** Advanced
**Best AI tool:** Claude (document attachment required)
**Follow-up:** Chain with a communications prompt to draft the press statement and employee briefing

---

### PROMPT 16 — REGULATORY: ESG / SUSTAINABILITY REPORTING IMPACT ASSESSMENT

*Source: SAL Guide, New Prompts (2nd Edition) — Regulatory Compliance section.*

I am a compliance adviser at a Singapore organisation. A regulator or standards body has issued updated requirements on ESG reporting (e.g., sustainability disclosures under ACRA's reporting framework). I need to prepare a Regulatory Change Impact Assessment for internal approval.

The memorandum shall follow this structure:
1. Background & Scope
2. Summary of Regulatory Change
3. Applicability to the Organisation (entities, functions, products/services, locations)
4. Gap Analysis (current state vs new requirements)
5. Risk Assessment (legal/compliance, conduct, data protection/privacy, operational/technology, financial/reputation, and health & safety where relevant)
6. Remediation Plan (measures, owners, dependencies)
7. Implementation Timeline & Milestones
8. Approvals, Assurance & Ongoing Monitoring

The analysis should map each new requirement to a concrete control (policy, procedure, system/configuration, training/communications, contracts/third-party oversight) and identify any areas requiring legal interpretation or regulator engagement.

Draft language must be precise, neutral, and decision-oriented, with clear asks for management approval of resources and timelines. Do not create obligations not present in the source documents; where ambiguity exists, set out conservative options with pros/cons and a recommended position. Maintain a traceability table linking each clause/section to the proposed control and evidence.

Use only these materials:
- The ACRA Sustainability Reporting requirements and official FAQs/circulars
- The organisation's current policies, procedures, control inventories, contracts/templates, and risk assessments for the impacted area
- Any prior governance papers and action trackers relevant to this topic

**Context:** Singapore ACRA/MAS ESG regulatory compliance
**Difficulty:** Advanced
**Best AI tool:** Claude (document attachment required)

---

## SECTION 3: SAL COMPETITION-WINNING PROMPT TECHNIQUES

The SAL organised a Prompt Engineering Competition in 2024 in collaboration with Microsoft Singapore. The top entries demonstrate advanced prompt engineering techniques for Singapore legal practice. Below are the key techniques extracted from the winning entries.

---

### TECHNIQUE 1: MULTI-ROLE ANALYSIS (ENTRY 1 — MR RODNEY YAP, PwC NewLaw / SMU)

*Winner of the 2024 SAL-Microsoft Legal Prompt Engineering Competition.*

This technique directs the AI to analyse a problem from multiple professional perspectives simultaneously — as M&A lawyers, as business executives, and as a compliance officer — before synthesising the outputs into a unified work product. It is particularly powerful for complex transactions where legal, commercial, and regulatory considerations all intersect.

**Structure:**
1. **Step 1:** Adopt the role of three experienced M&A lawyers and propose legal considerations
2. **Step 2:** Adopt the role of three CEOs and propose business considerations
3. **Step 3:** Adopt the role of a compliance officer and propose compliance considerations
4. **Step 4:** Combine all considerations into a negotiation table
5. **Step 5:** Draft the term sheet incorporating all considerations

**Example Application (M&A Term Sheet):**

Your task is to help me analyse and prepare a term sheet and a negotiation document for the full acquisition of the target company.

Your analysis will come in three steps. In the first step, you shall take on the role of three experienced Mergers and Acquisitions (M&A) lawyers versed in Singapore law. Each will propose a list of legal considerations. In the second step, you shall take on the role of three Chief Executive Officers (CEO) and each will propose a list of business considerations. In the third step, you shall take on the role of a Singapore-trained compliance officer and propose a list of compliance and transaction-related considerations.

Finally, combine all the considerations listed. Using the full list, generate a negotiation table listing: the consideration, the position most favourable to us, the most reasonable position both parties can accept, and the relevant factors we can use to negotiate. Then draft the term sheet.

[Insert context and expectations as per your transaction]

**Context:** Singapore-governed M&A, complex transactions
**Difficulty:** Advanced
**Best AI tool:** Claude

---

### TECHNIQUE 2: LAYERED STRUCTURED PROMPT (ENTRY 2 — MR JEROME TAY, NUS Law)

*Runner-up in the 2024 SAL-Microsoft Legal Prompt Engineering Competition.*

This technique uses a five-part structure — Identity, Context, General Instructions, Specific Instructions, and Further Refinements — to produce legally rigorous, highly structured documents while ensuring Singapore-specific compliance.

**Structure:**
- **Identity:** Define the AI's professional role, jurisdiction, and ethical obligations
- **Context:** Set the factual background precisely
- **General Instructions:** State the overall task and any flagging conventions (e.g. "TO NOTE:")
- **Specific Instructions:** List every section or clause the output must cover
- **Further Refinements:** Add any priority concerns or formatting requirements

**Key Innovation:** Use of the **"TO NOTE:"** marker to flag high-risk or priority items within the output — ensures critical issues are never buried in a long document.

**Example Application:**

**Identity:** Adopt the position of a legal professional in Singapore with a specialisation in mergers and acquisitions. The documents you create should be rigorous, comprehensive, yet succinct. At all times, your terms should be in accordance with the ethical guidelines and frameworks set in Singapore.

**Context:** [Insert your specific transaction facts]

**General Instructions:** Draft a term sheet for [CLIENT]. If a particular term requires special action or attention, flag it by adding "TO NOTE:" before the term.

**Specific Instructions:** Cover the following terms: (1) Parties Involved, (2) Transaction Structure, (3) Conditions Precedent, (4) Representations and Warranties, (5) Covenants, (6) Employee Matters, (7) Closing Details, (8) Post-Merger Integration, (9) Termination, (10) Exclusivity, (11) Confidentiality, (12) Dispute Resolution, (13) Governing Law.

**Further Refinements:** [Add any priority issues, formatting requirements, or stakeholder concerns]

**Context:** Singapore M&A, complex transactions
**Difficulty:** Advanced
**Best AI tool:** Claude

---

## SECTION 4: SAL ETHICS AND PROFESSIONAL RESPONSIBILITY FRAMEWORK

The SAL Guide emphasises that prompt engineering must always align with lawyers' professional obligations. This section captures the key ethics guidance.

---

### CORE PRINCIPLES FROM THE SAL GUIDE

**1. Professionalism — You remain responsible**
You are responsible for your work product, even when using generative AI. Generative AI will not be fully accurate. As the guide puts it: *do not rely on an authority that you have not read*. Review and verify all generated output before incorporating it into your work.

**2. Copilot, not autopilot**
Generative AI works best when you provide substantive content and context. It is helpful for fluency and generating permutations but should not substitute for developing subject matter expertise.

**3. Disclosure obligations**
There may be situations where your firm's policy, codes of professional conduct, or practice directions require disclosure of the use of generative AI to clients or the courts.

**4. Confidentiality — Critical for Singapore lawyers**
Be aware of the terms of the generative AI service you are using to prevent inadvertent disclosure of client information or personal data. Free-to-use services may use prompt content for continuous learning or content moderation. Enterprise services are more likely to have robust confidentiality safeguards. **Anonymise prompts appropriately.** Minimise client-specific information shared with the AI.

**5. Data security — Before attaching any document**
Always ensure that the data being shared with the language model complies with your organisation's data privacy and security policies. When including reference materials, be precise — include specific paragraphs or clauses rather than entire documents.

---

### THE SAL DO / DON'T CHECKLIST

**DO:**
- Use generative AI to generate comparisons, summaries, key issues, and brainstorm ideas based on trusted sources
- Start a new chat for each task and provide clear context for prompts
- Submit related prompts in a chain and run a prompt repeatedly to verify results
- Experiment and iterate to get the results you need

**DON'T:**
- Ask the AI to do too many things at once
- Expect perfect output on a single try
- Assume that all output will be fully accurate and fit for purpose
- Use output as work product without verification

---

## SECTION 5: JUDGMENT ANALYSIS FRAMEWORK (SAL WORKED EXAMPLE)

The SAL Guide demonstrates how to analyse Singapore court judgments using a structured five-question framework. This is applicable to any Singapore High Court or Court of Appeal judgment.

*The framework was demonstrated using Deutsche Bank AG Singapore Branch v ARJ Holding Limited [2025] SGHC 163.*

---

### PROMPT 17 — JUDGMENT ANALYSIS: FIVE-QUESTION FRAMEWORK

Apply this sequence of prompts to any Singapore judgment, attaching the judgment text:

**Question 1 — Issues:**
What are the main issues framed by the Court in this matter?

**Question 2 — Claimant's arguments:**
List the main arguments presented by the claimant. Give a detailed explanation of each argument.

**Question 3 — Defendant's arguments:**
List the main arguments presented by the defendants. Give a detailed explanation of each argument.

**Question 4 — Court's decision and reasoning:**
What decision did the court arrive at? Explain the court's reasoning and analysis for each of the issues in this judgment.

**Question 5 — Precedents:**
Identify and summarise the precedents cited in this judgment. Which precedents did the court rely on in its decision?

**Usage Notes:**
- Attach the full judgment text or paste in the relevant portions
- Work through the questions sequentially — each builds on the previous
- For step 4, ask the AI to "think through this step-by-step" for more analytical depth
- Verify all case citations independently before relying on them in submissions

**Context:** Singapore legal research, precedent analysis, training
**Difficulty:** Beginner to Intermediate
**Best AI tool:** Claude
**Follow-up:** Ask the AI to compare the reasoning in this judgment with an earlier conflicting judgment

---

## ATTRIBUTION AND FURTHER READING

This volume is based on the **Prompt Engineering for Lawyers (2nd Edition)** guide published by the **Singapore Academy of Law (SAL)** in collaboration with **Microsoft Singapore** (2025).

The prompts, frameworks, and competition entries in this file were developed by Singapore legal practitioners and academics, including:
- **Mr Rodney Yap** — Senior Manager, PwC NewLaw; Adjunct Lecturer, Singapore Management University; Winner, 2024 SAL-Microsoft Prompt Engineering Competition
- **Mr Jerome Tay** — Undergraduate, NUS Faculty of Law; Runner-up, 2024 SAL-Microsoft Prompt Engineering Competition
- The broader community of Singapore lawyers who contributed to and piloted the guide

The SAL-Microsoft guide is available at: https://sal.org.sg/wp-content/uploads/2025/10/Prompt-Engineering-Guide-2025-2nd-Edition.pdf

The Legal Prompts Library has adapted and extended these prompts for broader use. All substantive frameworks, prompt structures, and examples originate from the SAL-Microsoft guide and are used with attribution.
