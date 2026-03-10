# Legal AI Prompt Library — Analysis & Improvement Guide

*Prepared for The Legal Prompts Library | Based on "The Complete Legal AI Prompt Library 2025"*

---

## Overview

The existing library is a strong foundational resource. It covers 19 sections, 78 prompts, and gives practitioners a broad starting point for AI-assisted legal work. The ABCDE framework in Section 1 is genuinely useful, and the safety warnings throughout show professional awareness of the risks. However, several patterns recur that limit the library's depth, specificity, and usability — especially for a Singapore/APAC audience and for in-house teams. This guide maps what is working well, identifies the weakest areas, and provides concrete recommendations for every section.

---

## What Is Working Well

**The ABCDE framework (Section 1)** is the strongest single element in the library. It gives non-technical lawyers a memorable, repeatable structure. The weak vs. strong prompt comparison is excellent pedagogy — the side-by-side example makes the difference tangible.

**The confidentiality warnings** are placed well throughout the document and strike the right tone. They are specific enough to be actionable (mentioning enterprise versions, zero data retention) rather than vague disclaimers.

**Prompt 2.1-A (Plain-English Contract Summary)** is correctly identified as the most-used legal AI prompt, and the four-part structure (summary, obligations table, unusual clauses, missing clauses) is well-designed. This is the gold standard for how prompts in this library should look.

**Section 5 (Depositions & Discovery)** is one of the fuller sections and reflects genuinely sophisticated use of AI — preparing deposition outlines, analysing discovery documents, and identifying inconsistencies are real high-value tasks that lawyers will recognise.

**The "TIP" callouts** throughout the prompts add valuable meta-instruction. They help lawyers understand not just what the prompt does, but when to use it and what to do next.

**Section 19 (Ethics)** is appropriately placed at the end as a capstone and includes the hallucination warning concretely. The ABA rule references give it credibility, though these need a Singapore-specific counterpart.

---

## What Needs Improvement — Section by Section

### Section 1: Prompt Engineering Basics

**Current strength:** The ABCDE framework and weak/strong examples are excellent.

**What is missing:**
- No explanation of system prompts vs. user prompts for tools that support them (Claude, ChatGPT with Custom Instructions, Copilot)
- No guidance on multi-turn conversations — the library treats AI as a one-shot tool when chaining prompts is actually the highest-value skill
- No guidance on how to handle hallucinations mid-session (e.g. asking the AI to cite the source or flag uncertainty)
- The framework is US-centric (no mention of Singapore law, PDPA, SICC, or SGCA citations)

**Recommended additions:**
- A "Prompt Chaining" tutorial with a worked legal example (e.g. research → memo → client email as a chain)
- A "Red Flags in AI Output" checklist lawyers can use before using any AI-generated content
- A jurisdiction customisation tip: "Always append 'under Singapore law / [JURISDICTION] law' to any research prompt"

---

### Section 2: Contract Drafting & Review

**Current strength:** Best-populated section with 11 prompts across drafting, review, and clause generation. Prompt 2.1-C (Red Flags) is particularly strong.

**What is missing:**
- No prompt for comparing two versions of a contract (redline analysis)
- No prompt for vendor/supplier standard-form pushback (extremely common in practice)
- No SaaS or technology agreement specific prompts beyond Prompt 2.2-D
- No prompt for a closing checklist or conditions precedent tracker
- Prompts assume the user pastes the full contract text, but most enterprise contracts are 50-100 pages; no guidance on how to chunk documents

**Recommended additions:**
- Prompt: "Compare these two contract versions and summarise all material changes"
- Prompt: "We received a supplier's standard terms. Identify the top 10 deviations from market standard and our preferred positions"
- A note on document chunking: paste section by section with context carried forward

---

### Section 3: Legal Research & Case Law

**Current strength:** The framework prompt (3.1-A) is well-structured. The memo drafting and statutory interpretation prompts are useful.

**Critical gap:** The hallucination warning is present but the prompts do not embed self-checking mechanisms. If the AI hallucinates a case, a lawyer following these prompts verbatim has no in-prompt instruction to verify.

**Recommended improvement:** Every research prompt should end with: *"For each case you cite, state: (1) the full citation, (2) your confidence level (High/Medium/Low), and (3) a note if you cannot verify this from your training data."*

**What is missing:**
- No prompt for Singapore case law specifically (SGCA, SGHC, SICC)
- No prompt for comparative jurisdiction research (e.g. how Singapore courts treat a concept vs. English courts)
- No prompt for legislative history or parliamentary debates (Hansard)
- No prompt for secondary sources (law review articles, textbooks)

---

### Section 4: Litigation & Court Documents

**Current strength:** Covers the core trilogy of demand letters, pleadings, and written submissions.

**What is missing:**
- No prompt for Case Management Conferences (CMC) — extremely common in Singapore Supreme Court
- No prompt for Summons or Originating Applications (Singapore procedure)
- No prompt for skeleton arguments or opening statements
- No prompt for cost submissions or taxation of bills
- Letter of demand prompt (4.1-A) is good but does not flag the pre-action protocol requirements common in Singapore and UK

**Recommended additions:**
- Prompt: "Draft a Without Prejudice letter proposing settlement on the following terms"
- Prompt: "Prepare a list of issues for a Case Management Conference in [JURISDICTION] court"
- Prompt: "Draft a Bill of Costs summary for party-and-party taxation under [JURISDICTION] rules"

---

### Section 5: Depositions & Discovery

**Assessment:** One of the stronger sections. The deposition outline and document review prompts reflect real legal workflow.

**What is missing:**
- Singapore context: Singapore uses Affidavits of Evidence-in-Chief (AEICs) rather than depositions; no AEIC drafting prompt exists
- No prompt for drafting interrogatories (written questions)
- No prompt for privilege log preparation

**Recommended addition:**
- Prompt: "Draft an Affidavit of Evidence-in-Chief (AEIC) for a witness in Singapore civil proceedings. Witness: [NAME]. Key facts to cover: [LIST]. The AEIC must follow the format required by Order 15 of the Rules of Court 2021."

---

### Section 6: Corporate, M&A & Due Diligence

**Assessment:** Reasonable coverage of due diligence and M&A checklists.

**What is missing:**
- No prompt for a deal timeline or transaction roadmap
- No prompt for regulatory approval mapping (MAS, CCCS in Singapore)
- No prompt for a data room index or organisation
- No shareholder agreement or shareholders' resolution prompts

---

### Section 7: Employment Law

**Assessment:** Covers termination and workplace investigation — both important. Thin at only 5 prompts.

**What is missing:**
- Singapore-specific employment law: Employment Act, MOM requirements, CPF contributions, fair consideration framework
- No prompt for employment pass / work visa advice
- No prompt for retrenchment procedures (Singapore MOM notification requirements)
- No prompt for tripartite guidelines or advisories

---

### Sections 8, 9, 10, 11: Family, Estate, Immigration, Criminal

**Overall assessment:** These sections are functionally serviceable but very thin (2-4 prompts each). They feel like placeholder sections rather than practice-ready tools.

**Core problem:** These sections are jurisdiction-agnostic in a way that actually makes them weaker. Family law, estate planning, immigration, and criminal law vary so dramatically by jurisdiction that generic prompts are of limited value.

**Recommended approach:** Either (a) create Singapore-specific versions of each section, or (b) add prominent jurisdiction customisation instructions at the top of each section explaining what variables the lawyer must customise.

---

### Section 12: Intellectual Property

**Assessment:** Only 3 prompts for an entire practice area. IP is one of the most active AI use-case areas (patent claim drafting, trademark clearance, copyright analysis) and deserves a much fuller treatment.

**What is missing:**
- Trade secrets protection prompt
- Copyright fair use / fair dealing analysis
- IP licensing negotiation playbook
- Design rights / registered design analysis
- Domain name dispute (UDRP) prompt

---

### Section 13: Real Estate & Property Law

**Assessment:** Only 2 prompts. Real estate is a high-volume practice area, especially in Singapore's active property market.

**What is missing:**
- Option to Purchase (OTP) review — Singapore-specific, extremely common
- HDB transaction prompts
- Strata title / MCST issues
- Conveyancing checklist prompt

---

### Section 14: Compliance & Regulatory

**Assessment:** Only 3 prompts for what should be one of the most comprehensive sections, especially given Singapore's sophisticated regulatory environment (MAS, PDPA, ACRA, etc.).

**What is missing:** See "New Section: Singapore Regulatory & Compliance" below for the full expansion.

---

### Section 15: Personal Injury & Tort

**Assessment:** 3 prompts, adequate as a baseline.

**What is missing:**
- Motor accident protocol (specific to Singapore — NIMA process)
- Medical negligence analysis prompt
- Damages assessment / quantum calculation framework

---

### Section 16: In-House Counsel

**Assessment:** Only 4 prompts for what is identified as a key underserved audience (per the Substack article you shared). This is the most critical gap relative to the stated audience.

**What is missing:** See the dedicated "In-House Counsel Expanded Prompt Pack" document.

---

### Section 17: Client Communication & Intake

**Assessment:** Good prompts for emails and letters. The plain-English commitment is well-placed.

**What is missing:**
- Client intake questionnaire generator
- Engagement letter / fee agreement drafting
- File closure letter
- Difficult conversation scripts (e.g. advising on weak prospects, fee disputes)

---

### Section 18: Legal Marketing

**Assessment:** 3 prompts. Marketing is not a core legal skill, and including it is a nice-to-have. The content calendar prompt is useful.

**What is missing:**
- Bio / profile drafting for firm website
- Award submission / legal directory entry prompt (Chambers, Legal 500)
- Thought leadership article outline

---

### Section 19: Ethics & AI Best Practices

**Assessment:** Solid ethical framework. The ABA rule references give it credibility.

**What is missing:**
- Singapore Law Society Professional Conduct Rules equivalents
- PDPC (Personal Data Protection Commission) guidance on AI
- Singapore courts' emerging position on AI-generated content
- A practical "AI Use Policy" template for law firms

---

## The Biggest Structural Gap: Singapore Context

The library is written almost entirely from a US/UK legal perspective. Given the target audience and the MinLaw guidance context, a Singapore-specific supplement is the single highest-value addition you can make. Key areas where Singapore law diverges meaningfully from the US/UK framework include:

- **Civil procedure:** Rules of Court 2021 (completely reformed in 2022), SICC, SGCA procedure
- **Employment law:** MOM, Employment Act, CPF, fair consideration framework, work pass conditions
- **Data protection:** PDPA and PDPC advisory guidelines (not GDPR)
- **Property law:** HDB, OTP, strata titles
- **Company law:** Companies Act (Cap. 50), ACRA filings
- **Regulatory:** MAS licensing, CCCS competition law, SGX listing rules

---

## Cross-Cutting Improvement: Embed Self-Checking in Every Prompt

The single highest-value improvement across all 78 prompts is adding a self-verification instruction. Research shows that asking AI to flag its own uncertainty dramatically reduces hallucination risk. Recommend adding this sentence to every research or analysis prompt:

*"After completing your response, add a section headed 'Confidence & Caveats' identifying: (1) any facts or legal positions you are less than highly confident about, (2) any areas where you recommend the lawyer independently verify, and (3) any jurisdiction-specific points you could not confirm."*

---

## Summary Scorecard

| Section | Depth (1-5) | Singapore Relevance (1-5) | Priority to Improve |
|---|---|---|---|
| 1 – Prompt Engineering | 4 | 3 | Medium |
| 2 – Contracts | 4 | 3 | Medium |
| 3 – Legal Research | 3 | 2 | High |
| 4 – Litigation | 3 | 2 | High |
| 5 – Depositions/Discovery | 4 | 2 | High (AEIC gap) |
| 6 – Corporate/M&A | 3 | 3 | Medium |
| 7 – Employment | 2 | 2 | High |
| 8–11 – Family/Estate/Immigration/Criminal | 2 | 1 | High (jurisdiction-specific) |
| 12 – IP | 2 | 3 | High |
| 13 – Real Estate | 1 | 2 | High |
| 14 – Compliance | 2 | 2 | Critical |
| 15 – Personal Injury | 2 | 2 | Medium |
| 16 – In-House | 2 | 3 | Critical |
| 17 – Client Comms | 3 | 4 | Low |
| 18 – Marketing | 2 | 3 | Low |
| 19 – Ethics | 3 | 2 | Medium |

---

*This analysis accompanies the following prompt library documents: In-House Counsel Expanded Pack, Singapore & APAC Supplement, Compliance & Regulatory Deep Dive, and Prompt Workflow Examples.*
