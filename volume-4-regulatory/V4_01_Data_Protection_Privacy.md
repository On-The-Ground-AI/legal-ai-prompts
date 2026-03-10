# Data Protection & Privacy AI Prompt Library
## Comprehensive Resource for Legal Professionals
**Version 4.01** | Updated March 2026

---

## SECTION A: PRIVACY COMPLIANCE ASSESSMENT (8 PROMPTS)

### PROMPT 1 — PDPA GAP ANALYSIS
Review the following PDPA (Personal Data Protection Act – Singapore) compliance documentation and identify specific gaps: [ATTACH/DESCRIBE CURRENT PRIVACY POLICY, DATA HANDLING PROCEDURES, AND CONSENT MECHANISMS]. Based on the 10 Personal Data Protection Principles (PPPs) under the PDPA, create a detailed gap analysis that lists: (1) which PPPs are not adequately addressed, (2) specific operational practices that violate each PPP, (3) risk level for each gap (critical/high/medium/low), and (4) recommended remediation steps with timeline. Focus on consent, accuracy, protection, and retention principles which are most frequently non-compliant. Generate this as a structured audit report that the organization can present to the PDPC if requested.

**Context:** Use when auditing Singapore-based organizations or those handling Singaporean personal data; required before implementing privacy improvements; especially valuable when organizations claim PDPA compliance but haven't conducted formal review

**Difficulty:** Intermediate

**Follow-up:** PROMPT 2 (Multi-jurisdiction mapping) if organization operates internationally; PROMPT 5 (Privacy maturity assessment) to understand overall compliance posture

---

### PROMPT 2 — GDPR GAP ANALYSIS
I need to assess GDPR compliance for [ORGANIZATION TYPE/JURISDICTION]. Please review the following documents: [PRIVACY POLICY], [CURRENT DATA PROCESSING PRACTICES], [CONSENT MECHANISMS], [VENDOR CONTRACTS]. Identify gaps against GDPR requirements across: (1) lawful basis for processing (Article 6), (2) special category safeguards (Article 9), (3) data subject rights implementation (Articles 15-22), (4) data protection officer requirements (Articles 37-39), (5) DPIA requirements (Article 35), (6) data breach notification procedures (Articles 33-34), and (7) international data transfer mechanisms (Chapter 5). For each gap, specify the GDPR article(s), practical consequences of non-compliance, and remediation priority. Present findings in a confidential executive summary suitable for board review.

**Context:** Essential for EU organizations or those processing EU resident data; required before GDPR compliance certification; critical for organizations planning European expansion

**Difficulty:** Advanced

**Follow-up:** PROMPT 3 (CCPA gap analysis) if US operations exist; PROMPT 6 (ROPA creation) to document findings; PROMPT 7 (Legitimate interest assessment) if relying on legitimate interest basis

---

### PROMPT 3 — CCPA GAP ANALYSIS
Analyze the following California Consumer Privacy Act (CCPA/CPRA) compliance status: [DESCRIBE CURRENT PRIVACY PRACTICES, DATA COLLECTION METHODS, CONSUMER DISCLOSURE MECHANISMS, AND DELETION PROCEDURES]. Evaluate compliance against: (1) definitions of personal information and consumer (including inferred information), (2) disclosure requirements (notice at collection, privacy policy), (3) consumer rights (access, deletion, opt-out, correction), (4) sale/sharing/profiling restrictions, (5) opt-in requirements for minors, (6) service provider and contractor obligations, (7) CPRA updates including sensitive personal information, and (8) verification procedures. Identify specific non-compliance areas with business risk implications and create a phased remediation roadmap that prioritizes consumer rights implementation. Note any conflicting obligations with GDPR or other frameworks.

**Context:** Mandatory for organizations serving California residents; required before 2025 CPRA full compliance deadline; critical for e-commerce, SaaS, and marketing-intensive businesses

**Difficulty:** Advanced

**Follow-up:** PROMPT 4 (Multi-jurisdiction compliance) for organizations in multiple states/countries; PROMPT 9 (DPA drafting) if working with service providers

---

### PROMPT 4 — MULTI-JURISDICTION COMPLIANCE MAPPING
Our organization operates in [LIST JURISDICTIONS: e.g., Singapore, UK, EU, California, Canada]. Using the following summary of our data practices: [DESCRIBE DATA FLOWS, CATEGORIES, AND PROCESSING ACTIVITIES], create a comprehensive compliance matrix that maps requirements across all applicable privacy regimes. For each jurisdiction, identify: (1) applicable laws (PDPA, GDPR, CCPA, PIPEDA, etc.), (2) definitions of personal data unique to that jurisdiction, (3) requirements for lawful basis/consent, (4) data subject rights, (5) international transfer rules, (6) breach notification timelines, and (7) enforcement authority and penalty structure. Highlight conflicts or contradictions between jurisdictions and recommend an integrated compliance approach that satisfies the strictest requirements. Identify which regimes apply to which data flows and provide implementation priority sequence.

**Context:** Essential for multinational organizations; required before implementing global privacy program; critical for understanding compliance hierarchy and resource allocation

**Difficulty:** Advanced

**Follow-up:** PROMPT 5 (Privacy maturity assessment) to build implementation roadmap; PROMPT 1-3 to deep-dive into specific jurisdictions

---

### PROMPT 5 — PRIVACY MATURITY ASSESSMENT
Evaluate our organization's privacy maturity across the five capability domains. Please assess the following organization: [ORGANIZATION NAME AND INDUSTRY] with [NUMBER] employees operating in [JURISDICTIONS]. For each domain—(1) Governance (policies, accountability, budget), (2) People (training, roles, expertise), (3) Processes (procedures, controls, testing), (4) Technology (tools, systems, infrastructure), and (5) Risk Management (compliance, breach response, vendor management)—assign maturity level (Ad-hoc/Defined/Managed/Measured/Optimized) based on [DESCRIBE CURRENT STATE]. Create a detailed assessment report with: maturity scores, gaps in each domain, industry benchmarks, capability progression roadmap, resource investment requirements, and 12/24-month implementation timeline. Prioritize initiatives based on risk exposure and regulatory deadline.

**Context:** Use at start of privacy program implementation or major restructuring; helps secure stakeholder buy-in for privacy investment; guides phased improvement strategy

**Difficulty:** Intermediate

**Follow-up:** PROMPT 6 (ROPA creation) for quick compliance wins; PROMPT 20 (Privacy requirements for product team) to define specific process improvements

---

### PROMPT 6 — RECORDS OF PROCESSING ACTIVITIES (ROPA) CREATION
Create a comprehensive Records of Processing Activities (ROPA) document for our organization: [ORGANIZATION NAME], [INDUSTRY], [JURISDICTIONS]. Based on our data mapping showing [DESCRIBE DATA CATEGORIES, SOURCES, RECIPIENTS, RETENTION, AND TECHNICAL MEASURES], generate ROPA entries covering all processing activities under Articles 30 and 30a (GDPR). For each processing activity, include: (1) name/ID and department responsible, (2) categories of personal data and data subjects, (3) purpose(s) of processing, (4) categories of recipients, (5) retention period with justification, (6) description of technical and organizational measures (including transfers/sub-processors), and (7) risk assessment reference. Format in tabular format suitable for GDPR article 30(1) and 30(2) documentation. Ensure ROPA references back to legitimate interest assessments and DPIAs where applicable. Include guidance for maintaining/updating this document.

**Context:** Legally required under GDPR Article 30 for controllers; best practice for PDPA and CCPA compliance; demonstrates compliance readiness to regulators

**Difficulty:** Intermediate

**Follow-up:** PROMPT 7 (Legitimate interest assessment) for processing activities where consent is not the lawful basis

---

### PROMPT 7 — LEGITIMATE INTEREST ASSESSMENT
Our organization relies on [DESCRIBE PROCESSING ACTIVITY/CONTEXT] as the lawful basis. Please conduct a detailed Legitimate Interest Assessment (LIA) for [SPECIFIC PROCESSING ACTIVITY] that: (1) clearly identifies the organization's legitimate interest (be specific—not just "business purposes"), (2) assesses whether this interest is lawful and reasonable, (3) analyzes the necessity of the processing for achieving this interest, (4) evaluates data subject rights and reasonable expectations, (5) identifies those with direct interest (children, vulnerable persons, etc.), (6) balances the interest against data subject rights using a three-step test, and (7) documents all mitigating measures and safeguards. Conclude with a clear recommendation: legitimate interest is established, needs conditions/safeguards, or cannot be used. Present in format suitable for regulatory demonstration. Include specific factors that would make this assessment fail or require alternative lawful basis.

**Context:** Required whenever legitimate interest is relied upon instead of consent; critical for marketing, analytics, and business analytics; must be documented to demonstrate GDPR compliance

**Difficulty:** Intermediate

**Follow-up:** PROMPT 6 (ROPA creation) to document the assessment in processing records

---

### PROMPT 8 — CONSENT MECHANISM REVIEW
Analyze our current consent mechanisms: [DESCRIBE CONSENT IMPLEMENTATION—ONLINE FORMS, BANNERS, CHECKBOXES, THIRD-PARTY TOOLS, EMAIL FLOW]. Evaluate compliance against GDPR Article 7 and CCPA/CPRA consent requirements, assessing: (1) clarity of language and layered information, (2) granularity (separate consent for separate purposes), (3) technical implementation (freely given—no dark patterns, pre-checked boxes, or consent walls), (4) proof of consent (timestamp, version, data collected), (5) withdrawal mechanism availability, (6) compliance with "silence as consent" prohibition, and (7) special handling of sensitive categories. Identify specific areas of non-compliance with practical examples from your website/app. Recommend design changes, alternative consent tool implementations, and governance process for consent management. Include template language for consent declarations that meets current regulatory expectations.

**Context:** Use when refreshing privacy compliance or after receiving regulatory guidance on consent; critical for any customer-facing consent interaction; relevant for cookie policies and marketing consent

**Difficulty:** Intermediate

**Follow-up:** PROMPT 23 (Cookie policy and consent banner) for specific technical implementation; PROMPT 38 (Privacy policies & notices) for baseline privacy notice

---

## SECTION B: DATA PROCESSING AGREEMENTS (8 PROMPTS)

### PROMPT 9 — DPA REVIEW AGAINST GDPR ARTICLE 28
Please review the following Data Processing Agreement (DPA) between [DATA CONTROLLER NAME] and [DATA PROCESSOR NAME]: [ATTACH DPA]. Evaluate compliance with GDPR Article 28(3) and Article 28(4) requirements by checking: (1) processor's commitment to only process personal data on controller's instructions, (2) confidentiality and security obligations, (3) adequate technical and organizational measures per Article 32, (4) sub-processor authorization and oversight process, (5) data subject rights assistance mechanisms, (6) data return/deletion upon termination, (7) audit and inspection rights, (8) international transfer mechanisms if applicable, and (9) liability allocation. For each requirement, indicate: compliant/non-compliant/partially compliant with specific clause references. Identify critical gaps that expose the controller to regulatory risk and provide recommended contract language to remediate. Indicate whether DPA is suitable for signature or requires renegotiation.

**Context:** Required for all controller-processor relationships under GDPR; essential governance document; use when onboarding new service providers

**Difficulty:** Intermediate

**Follow-up:** PROMPT 13 (SCC review) if processor transfers data internationally; PROMPT 10 (DPA review against PDPA) if operating in Singapore

---

### PROMPT 10 — DPA REVIEW AGAINST PDPA
Review the following Data Processing Agreement (DPA) from the perspective of PDPA (Singapore Personal Data Protection Act) compliance: [ATTACH DPA]. Assess whether the agreement adequately addresses: (1) appointment of data processor under PDPA Schedule 1 Obligation 1.6, (2) processor's obligation to protect personal data using "generally accepted security standards," (3) processor's commitment to comply with all PDPA Personal Data Protection Principles (PPPs), (4) consent management and data subject request procedures, (5) sub-contractor authorization process and liability chain, (6) data retention and destruction obligations, (7) audit rights and inspection mechanisms, (8) liability allocation between controller and processor, and (9) termination and data handling. Note that PDPA places primary responsibility on the organization, so ensure processor agreement doesn't inappropriately shift obligations. Identify gaps and provide remedial language specifically addressing PDPA requirements. Indicate whether DPA can be executed or requires renegotiation.

**Context:** Essential for all Singapore-based organizations using external data processors; required for PDPC compliance demonstrations

**Difficulty:** Intermediate

**Follow-up:** PROMPT 4 (Multi-jurisdiction mapping) if processor handles data across multiple jurisdictions

---

### PROMPT 11 — DPA DRAFTING FROM SCRATCH
Please draft a comprehensive Data Processing Agreement (DPA) between [CONTROLLER ENTITY] and [PROCESSOR ENTITY] that governs processing of [DATA CATEGORIES] for [SPECIFIED PURPOSES]. The DPA must comply with GDPR Article 28 and PDPA requirements and should include: (1) defined terms and relationship confirmation, (2) scope of processing (categories of data, subjects, purposes, duration), (3) processor's processing instructions and confidentiality obligations, (4) security and technical/organizational measures framework, (5) sub-processor authorization process with prior notice and objection rights, (6) data subject rights assistance (access, deletion, portability, correction), (7) controller audit and inspection rights, (8) data return/certification of destruction at termination, (9) international data transfer mechanisms if applicable, (10) liability and indemnification, (11) term and termination, and (12) governing law. Include appendices for: Standard Contractual Clauses (if needed), list of approved sub-processors, and security measures schedule. Ensure language is clear, legally defensible, and suitable for immediate execution.

**Context:** Use when establishing new controller-processor relationship; when existing DPA is insufficient; when bringing processors in-house; required for vendor onboarding

**Difficulty:** Advanced

**Follow-up:** PROMPT 13 (SCC review) if international data transfers required; PROMPT 15 (Data transfer impact assessment) for transfer impact analysis

---

### PROMPT 12 — SUB-PROCESSOR ASSESSMENT
Our main data processor [PROCESSOR NAME] has proposed the following sub-processors to process our customer personal data: [LIST SUB-PROCESSORS AND THEIR FUNCTIONS]. Please assess these sub-processor arrangements against: (1) GDPR Article 28(2) and 28(4) requirements for explicit or general authorization with prior notice and objection rights, (2) PDPA processor obligations requiring similar controls, (3) adequacy of security measures given sub-processor's industry and geography, (4) specific risk factors (location of sub-processor, data category sensitivity, regulatory environment), (5) whether data subject consent/notification is required, and (6) audit and liability mechanism for multi-party chain. For each sub-processor, assign risk level (critical/high/medium/low) and recommend: approval, approval with conditions, or rejection. Provide template notice/objection language if required to inform data subjects. Create process for ongoing sub-processor monitoring and amendment procedures.

**Context:** Use when processor adds sub-processors; required to maintain GDPR compliance; important governance activity for controller

**Difficulty:** Intermediate

**Follow-up:** PROMPT 11 (DPA drafting) to ensure DPA includes adequate sub-processor authorization language

---

### PROMPT 13 — STANDARD CONTRACTUAL CLAUSES (SCC) REVIEW
Please review the following Standard Contractual Clauses (SCCs) for [TRANSFER MECHANISM: e.g., exporting personal data from EU to [DESTINATION COUNTRY]]: [ATTACH SCC AND TRANSFER AGREEMENT]. Evaluate against: (1) current SCCs authorized by European Commission (post-Schrems II decision of June 2021), (2) incorporation of SCCs in data processing agreement, (3) supplementary measures for [DESTINATION COUNTRY] based on adequacy assessment, (4) identification of any legal obstacles to SCC enforcement in destination country, (5) necessity and appropriateness of supplementary technical measures (encryption, data access controls), (6) data subject rights mechanisms (objection, redress), (7) clauses for data return/deletion, and (8) compatibility with GDPR Chapter 5 requirements. Assess whether current SCCs remain valid given legal/political changes. If Schrems II supplementary measures are needed, provide specific recommendations for technical/organizational additions. Indicate compliance status and any required updates or alternative transfer mechanisms.

**Context:** Critical for any EU-to-third-country data transfers; required for GDPR compliance; must be reviewed following any Schrems II updates

**Difficulty:** Advanced

**Follow-up:** PROMPT 15 (Data transfer impact assessment) for supplementary measures analysis

---

### PROMPT 14 — DATA TRANSFER IMPACT ASSESSMENT
Our organization intends to transfer [DATA CATEGORIES] from [SOURCE JURISDICTION] to [DESTINATION JURISDICTION/CLOUD PROVIDER]. Please conduct a Data Transfer Impact Assessment that: (1) evaluates the destination country's adequacy level (adequate/standard contractual clauses/binding corporate rules/derogations), (2) identifies specific legal or regulatory risks in the destination (government access laws, surveillance, data localization), (3) assesses the sensitivity of the data being transferred and impact of unauthorized access, (4) reviews current transfer mechanism(s) and identifies gaps, (5) evaluates necessity and effectiveness of supplementary technical measures (encryption, key management, anonymization), (6) assesses data subject rights and redress mechanisms in destination country, and (7) recommends optimal transfer mechanism(s) with implementation timeline. Include specific considerations for [DESTINATION COUNTRY] legal/surveillance environment based on recent guidance (EDPB, courts, regulators). Conclude with risk assessment and go/no-go recommendation for transfer.

**Context:** Essential before transferring data outside home jurisdiction; required for Schrems II compliance; critical for cloud migration or international expansion

**Difficulty:** Advanced

**Follow-up:** PROMPT 13 (SCC review) to implement recommended transfer mechanism

---

### PROMPT 15 — BINDING CORPORATE RULES ANALYSIS
Evaluate whether our multinational organization should implement Binding Corporate Rules (BCRs) given: [ORGANIZATION STRUCTURE—number of entities, jurisdictions, volume of intra-group data transfers]. Analyze: (1) GDPR Chapter 5 requirements for BCRs as alternative transfer mechanism, (2) cost-benefit vs. Standard Contractual Clauses (implementation, approval timeline, ongoing compliance), (3) jurisdictional coverage (whether BCRs meet transfer needs for all operations), (4) whether organization's data governance maturity supports BCRs, (5) EDPB guidelines on adequate BCR content, (6) implementation timeline and resource requirements, and (7) approval process with data protection authorities. Provide preliminary assessment of whether BCRs are necessary or whether SCCs are sufficient for current data transfer needs. If BCRs are recommended, outline drafting roadmap and EDPB approval process. If not recommended, explain why SCCs or other mechanisms are adequate.

**Context:** Use for large multinational organizations with significant intra-group data flows; relevant when SCCs are insufficient or too complex to manage

**Difficulty:** Advanced

**Follow-up:** PROMPT 13 (SCC review) if SCCs are recommended instead; PROMPT 11 (DPA drafting) to implement transfer mechanisms in contracts

---

### PROMPT 16 — INTRA-GROUP DATA SHARING AGREEMENT
Please draft an Intra-Group Data Sharing Agreement for [PARENT COMPANY] and its subsidiaries/affiliates: [LIST ENTITIES AND JURISDICTIONS]. The agreement should govern sharing of [DATA CATEGORIES] among group entities for [SPECIFIED PURPOSES] and must include: (1) clear identification of data controller roles for each entity, (2) lawful basis for sharing (including legitimate interest assessments if applicable), (3) categories of personal data and data subjects covered, (4) purposes of sharing and prohibition on secondary use, (5) security and confidentiality obligations for each entity, (6) data subject rights procedures (who responds to requests), (7) retention and deletion protocols, (8) sub-processor authorization if non-group processors are involved, (9) each entity's liability and indemnification obligations, (10) dispute resolution and governance, and (11) audit and compliance verification mechanisms. Ensure compliance with GDPR, PDPA, and other applicable regimes. Include data transfer mechanisms (SCCs if needed). Make agreement suitable for ROPA documentation and regulatory demonstration.

**Context:** Essential for multinational groups sharing data internally; required for GDPR compliance; important governance document for related entity transactions

**Difficulty:** Advanced

**Follow-up:** PROMPT 14 (Data transfer impact assessment) if intra-group transfers cross jurisdictions; PROMPT 4 (Multi-jurisdiction mapping) for governance questions

---

## SECTION C: DATA BREACH RESPONSE (8 PROMPTS)

### PROMPT 17 — BREACH SEVERITY ASSESSMENT
Our organization has experienced a data breach involving [DESCRIBE INCIDENT: type of breach, data categories, estimated number of individuals affected, cause/mechanism]. Please conduct an urgent Breach Severity Assessment that: (1) quantifies the scope (number and categories of individuals, data categories, systems affected), (2) evaluates the breach characteristics (accessibility of data, sensitive categories, identifiability of individuals), (3) assesses likelihood and severity of harm to data subjects (financial, reputational, discrimination risks), (4) identifies regulatory notification requirements and timelines for [JURISDICTION], (5) determines whether breach is likely to result in "high risk" to data subject rights requiring notification, (6) estimates operational/financial impact, (7) assesses likelihood of regulatory investigation or enforcement action, and (8) recommends immediate actions (notification, public statement, law enforcement notification). Present as priority-ranked action log with immediate/24-hour/72-hour timeline. Include data subject notification assessment and required content. Conclude with go/no-go recommendation for regulatory notification.

**Context:** Use immediately upon breach discovery; time-critical for GDPR (72-hour notification requirement) and other regimes; determines notification and response obligations

**Difficulty:** Advanced

**Follow-up:** PROMPT 18-21 for specific jurisdiction notifications and response procedures

---

### PROMPT 18 — PDPC NOTIFICATION DRAFT (SINGAPORE)
We must notify the Personal Data Protection Commission (PDPC) Singapore of a data breach affecting [NUMBER] individuals: [DESCRIBE INCIDENT, DATA CATEGORIES, CAUSE]. Based on PDPA Schedule 1 Obligation 4 requirements and PDPC guidance, please draft the required breach notification message to PDPC that includes: (1) organization and incident details, (2) description of the breach and its impact, (3) categories of personal data affected and estimated number of individuals, (4) timing of discovery and cause analysis, (5) steps taken to mitigate impact and prevent recurrence, (6) data subject notification plan and timeline, (7) relevant contact person for PDPC inquiries, and (8) copies of data subject notification letters. Ensure notification meets PDPC's expectations for urgency (generally expect notification shortly after discovery) and demonstrates reasonable breach response measures. Note that while PDPA doesn't mandate 72-hour notification, PDPC expects prompt notification and good-faith disclosure. Format notification for immediate transmission to PDPC via [CONTACT METHOD].

**Context:** Required for breaches affecting Singapore residents; necessary for demonstrating PDPA compliance; critical to establish cooperative relationship with regulator

**Difficulty:** Intermediate

**Follow-up:** PROMPT 19 (Affected individual notification) to prepare data subject notifications

---

### PROMPT 19 — ICO NOTIFICATION DRAFT (UK)
Our organization must notify the Information Commissioner's Office (ICO) regarding a data breach affecting [NUMBER] UK residents: [DESCRIBE INCIDENT, DATA CATEGORIES, IMPACT]. Please draft the required ICO breach notification that includes: (1) organization details and incident summary, (2) date breach was discovered and when reported to ICO, (3) whether breach is likely to result in "high risk" to rights/freedoms, (4) categories of personal data involved and number of individuals affected, (5) breach cause and investigation findings, (6) measures implemented to mitigate impact and prevent recurrence, (7) statement of whether data subject notification is being issued, (8) details of any law enforcement notification, and (9) contact details for ICO inquiries. Under UK GDPR (post-Brexit), notification is required without undue delay and no later than 72 hours of discovering the breach (Article 33). If no high-risk determination, explain reasons for not notifying individuals. Format notification for submission to ICO breach notification portal or email. Include supporting documentation (breach investigation summary, sample data subject notification).

**Context:** Mandatory for breaches affecting UK residents; required to meet UK GDPR 72-hour deadline; establishes compliance with ICO regulatory requirements

**Difficulty:** Intermediate

**Follow-up:** PROMPT 20 (Affected individual notification) to prepare subject notification; PROMPT 22 (Breach post-mortem report) for detailed investigation analysis

---

### PROMPT 20 — AFFECTED INDIVIDUAL NOTIFICATION
Please draft notification letters to individuals affected by [DESCRIBE DATA BREACH: categories, data types, incident date]. Create notifications that comply with GDPR Article 34 (or equivalent requirements in CCPA, PDPA, PIPEDA as applicable) and include: (1) clear statement that a breach occurred and acknowledgment of responsibility, (2) description of data compromised (what personal data, not unnecessary technical details), (3) timing of breach and discovery, (4) likely consequences for affected individuals (financial, identity theft, discrimination risks), (5) technical/organizational measures in place to prevent recurrence, (6) recommended mitigation steps individuals should take, (7) contact details for individuals with questions, (8) information about available remedies/compensation, and (9) reference to organization's privacy policy/rights information. Provide versions suitable for: (a) high-risk breaches requiring immediate notification, (b) lower-risk breaches notified after investigation, and (c) vulnerable populations (children, elderly). Include consideration for translation and accessibility. Prepare notification delivery plan (email, postal mail, public notice) based on breach characteristics and contact data availability.

**Context:** Required for high-risk breaches under GDPR and many other regimes; essential to mitigate individual harm and regulatory backlash; must balance transparency with avoiding unnecessary alarm

**Difficulty:** Intermediate

**Follow-up:** PROMPT 17 (Breach severity assessment) for risk determination; PROMPT 22 (Breach post-mortem report) for detailed investigation findings

---

### PROMPT 21 — BREACH RESPONSE ACTION LOG (72-HOUR PLAN)
Following discovery of data breach affecting [DESCRIBE INCIDENT], please create a detailed action log tracking all response activities across the critical first 72 hours. For each action item, specify: (1) action description, (2) responsible party/department, (3) deadline (within 4/24/48/72 hours), (4) status (pending/in-progress/complete), (5) evidence/documentation of completion, and (6) who authorized action. Organize by category: (a) Incident containment (stop ongoing access, preserve evidence, isolate affected systems), (b) Investigation (root cause analysis, scope assessment, forensic investigation initiation), (c) Notification (PDPC/ICO/regulators, affected individuals, law enforcement), (d) Remediation (credit monitoring, breach response services, system hardening), (e) Communication (internal team notification, public statement, media response), and (f) Documentation (preserve all records, attorney-client privilege protections). Create this as dynamic document for real-time tracking. Assign accountability and escalation procedures for missed deadlines. Include checkpoints for regulatory notification decision and evidence preservation protocol. Format for presentation to executive team and legal counsel.

**Context:** Essential crisis management tool for breach response; required to demonstrate GDPR 72-hour compliance and timely response; helps coordinate complex multi-party response

**Difficulty:** Intermediate

**Follow-up:** PROMPT 22 (Breach post-mortem report) after 72 hours for detailed findings

---

### PROMPT 22 — FORENSIC INVESTIGATION BRIEF
Our organization has experienced a data breach and requires independent forensic investigation. Please prepare an Investigation Brief for [FORENSIC INVESTIGATOR/FIRM] that specifies: (1) scope of investigation (systems affected, data categories involved, time period relevant), (2) investigation objectives (determine scope, root cause, identify compromise, assess impact), (3) key questions to be answered (how was access gained, what data was accessed, for how long, by whom), (4) systems, logs, and data to be preserved and analyzed, (5) timeline expectations and reporting format, (6) confidentiality and privilege expectations (work should be subject to attorney-client privilege), (7) chain of custody and evidence handling protocols, (8) credentials and system access required, (9) coordination with internal IT and legal teams, and (10) final report requirements (technical findings, risk assessment, remediation recommendations, evidence supporting conclusions). Include specific reference to regulatory requirements for investigation documentation. Ensure investigation is designed to support PDPC/ICO notification and potential litigation defense. Include request for interim findings if 72-hour regulatory notification deadline requires urgent reporting.

**Context:** Essential for serious breaches requiring evidence analysis; supports regulatory notification and potential litigation defense; must preserve attorney-client privilege

**Difficulty:** Intermediate

**Follow-up:** PROMPT 23 (Breach post-mortem report) to document findings and recommendations

---

### PROMPT 23 — BREACH POST-MORTEM REPORT
Following completion of breach investigation and immediate response, please prepare a comprehensive Breach Post-Mortem Report documenting: (1) Executive summary of incident, response, and key findings, (2) Detailed timeline of breach discovery, response actions, and notifications, (3) Investigation findings (root cause, scope, affected systems/data), (4) Regulatory notifications issued and responses received, (5) Individual notifications issued and response rates, (6) Financial and operational impact assessment, (7) Analysis of prior controls that failed or were inadequate, (8) Detailed remediation plan (system improvements, security hardening, process changes, timeline), (9) Preventive measures to reduce recurrence likelihood, and (10) Recommendations for policy, technology, and process improvements. Include appendices with: breach investigation report summary, notification copies, regulatory correspondence, forensic investigation findings, cost analysis. Structure report for PDPC/ICO submission if requested and for board governance review. Ensure all findings support regulatory compliance narrative and business continuity. Identify lessons learned and budget requirements for remediation.

**Context:** Required after breach resolution for regulatory compliance and organizational learning; supports PDPC/ICO investigations if they occur; essential for board reporting and breach insurance claims

**Difficulty:** Intermediate

**Follow-up:** PROMPT 25 (Breach remediation plan) for implementation of recommendations

---

### PROMPT 24 — BREACH REMEDIATION PLAN
Based on the following breach incident: [DESCRIBE BREACH AND INVESTIGATION FINDINGS], please develop a comprehensive Breach Remediation Plan that addresses: (1) immediate actions (already taken and follow-up items), (2) root cause remediation (fixes addressing the specific failure that led to breach), (3) detective controls enhancement (systems to identify similar incidents faster), (4) preventive controls strengthening (measures to prevent recurrence), (5) data protection improvements (encryption, access controls, pseudonymization), (6) process and policy updates required, (7) technology/infrastructure upgrades needed with cost estimates, (8) vendor/third-party changes required, (9) staff training and capability building, (10) implementation timeline and phasing strategy, (11) resource requirements and budget, and (12) success metrics for measuring remediation effectiveness. Prioritize actions based on: (a) regulatory requirements and deadlines, (b) risk level and likelihood of recurrence, (c) cost and feasibility, and (d) business impact. Format as detailed roadmap with responsible parties, milestones, and governance checkpoints. Include contingency plans if primary remediation approach faces obstacles. Prepare executive summary suitable for board approval and audit committee oversight.

**Context:** Critical after breach resolution; required to demonstrate remediation commitment to regulators; essential for breach insurance coverage and litigation defense

**Difficulty:** Advanced

**Follow-up:** Regular progress tracking against plan; PROMPT 5 (Privacy maturity assessment) to assess systemic improvements needed

---

## SECTION D: DATA SUBJECT REQUESTS (6 PROMPTS)

### PROMPT 25 — DSAR ACKNOWLEDGEMENT LETTER
An individual has submitted a Data Subject Access Request (DSAR) dated [DATE] to our organization. Please draft an acknowledgement letter that: (1) confirms receipt of the request and date received, (2) provides unique reference number for tracking, (3) states the timeline for response (30 days under GDPR, [X] days under PDPA/CCPA), (4) explains what information we will provide (categories of data, how it will be formatted), (5) outlines the verification process to confirm requester identity, (6) identifies any additional information needed from requester (proof of identity, clarification of scope), (7) provides contact details for questions or concerns, (8) explains appeal/escalation procedures if request is denied, and (9) confirms organization's commitment to timely and complete response. Keep tone professional but accessible. Include statement about requester's rights under applicable privacy laws. If request requires more time (complex, voluminous), indicate this and explain reasons per GDPR Article 12(3). Send via method used by requester (email, portal, postal mail). Maintain records of acknowledgement for compliance documentation.

**Context:** Required for any DSAR under GDPR, PDPA, CCPA, and similar regimes; establishes compliance timeline and sets expectations; creates documented record of request receipt

**Difficulty:** Beginner

**Follow-up:** PROMPT 26 (DSAR fulfillment checklist) for response preparation; PROMPT 27 (DSAR response letter) for final response

---

### PROMPT 26 — DSAR FULFILLMENT CHECKLIST
We have received a DSAR from [INDIVIDUAL] requesting access to [SCOPE OF REQUEST]. Please create a detailed Fulfillment Checklist for our response that includes: (1) Identification and verification (confirm requester identity through verification process), (2) Scope confirmation (clarify what data categories are in scope, any limitations on request), (3) Data location identification (identify all systems, databases, applications, archives containing requested data), (4) Data collection and assembly (retrieve data from all sources, including backups and archived data), (5) Claim evaluation (identify any exemptions, trade secrets, third-party information requiring redaction or refusal), (6) Compilation and formatting (organize data logically, provide in commonly used format, consider readability and usability), (7) Verification review (internal team review to ensure complete and accurate response), (8) Delivery mechanism (email, encrypted portal, postal mail, or in-person review), (9) Timing verification (confirm response meets 30/45/60-day deadline per jurisdiction), (10) Documentation (maintain records of what data was provided, verification steps, exemptions claimed). Include specific checkpoints for: sensitive data handling, third-party data, employee/contractor data, metadata and file versions. Assign responsible parties and timeline for each step. Flag any complexity or potential delays immediately.

**Context:** Essential for any complex DSAR to ensure complete and timely response; helps identify data location and scope issues; reduces risk of incomplete responses

**Difficulty:** Intermediate

**Follow-up:** PROMPT 27 (DSAR response letter) for actual response delivery

---

### PROMPT 27 — DSAR RESPONSE LETTER (FULL DISCLOSURE)
Based on the DSAR from [INDIVIDUAL] received [DATE], please draft a comprehensive response letter that: (1) confirms the request has been processed within the required timeframe, (2) provides the requested personal data in organized, understandable format (with brief explanation of what each data element is), (3) explains the categories of data provided and why each category is included, (4) identifies all recipients with whom data has been shared (processors, controllers, third parties) with dates, (5) explains any additional information derived from raw data (inferences, profiling results, decisions made), (6) references the lawful basis for collecting and processing each data category, (7) explains retention periods and how data is handled, (8) advises on rights available (correction, erasure, portability, objection), (9) provides contact details for exercising additional rights, (10) explains appeal procedures if requester believes response is incomplete or inaccurate. Keep language clear and accessible (avoid jargon). Provide data in structured format (PDF, spreadsheet, or suitable alternative). Include cover letter plus data attachments. Send via secure method. Maintain records of response including what was disclosed, dates, delivery method. Consider providing brief plain-language guide explaining the data provided.

**Context:** Required for all DSARs under GDPR, PDPA, CCPA when requester has legitimate access; essential for demonstrating data subject transparency; must be complete and accurate

**Difficulty:** Intermediate

**Follow-up:** If requester disputes response or claims incompleteness, escalate to PROMPT 28 (Partial denial letter) if denial warranted or re-compile response

---

### PROMPT 28 — DSAR PARTIAL DENIAL LETTER (WITH EXEMPTIONS)
The DSAR from [INDIVIDUAL] dated [DATE] has requested access to [SCOPE], but we are unable to provide certain categories of data. Please draft a response letter that: (1) confirms we received and processed the request, (2) provides all data we can disclose in full, (3) clearly identifies data categories we are withholding or partially redacting, (4) for each withheld category, specifies the legal exemption or reason for withholding (trade secret, attorney-client privilege, third-party information, etc.) under [APPLICABLE JURISDICTION], (5) explains why the exemption applies to that specific information, (6) indicates what portions (if any) can be disclosed even within withheld categories, (7) provides contact information for appealing the denial, and (8) explains any alternative mechanisms to access information (e.g., through third party, in redacted form, or upon passage of time). Cite specific legal authorities for each exemption. Keep tone respectful and explain reasoning in accessible language. Include copy of access denial under GDPR Article 12(4) or equivalent provision if fully refusing portions. Warn that providing misleading reasons for denial could undermine compliance credibility. Maintain detailed records of what was withheld and why. Be prepared for appeal/escalation to regulator if denial is challenged.

**Context:** Use when DSAR cannot be fully satisfied due to legal exemptions; requires careful legal analysis to justify withholding; must document reasoning for regulatory scrutiny

**Difficulty:** Advanced

**Follow-up:** Prepare for potential regulatory complaint if requester escalates denial; document exemption analysis carefully

---

### PROMPT 29 — RIGHT TO ERASURE ASSESSMENT
An individual has requested erasure of their personal data: [DESCRIBE REQUEST SCOPE]. Please conduct a Right to Erasure Assessment under GDPR Article 17 (or equivalent PDPA/CCPA provisions) that: (1) confirms whether erasure request falls within Article 17 grounds (data no longer necessary, consent withdrawn, processing unlawful, legal obligation to erase, legitimate interest balance fails, child's data), (2) identifies all systems and locations where data is stored, (3) evaluates whether any grounds for refusing erasure apply (legal obligation to retain, exercise of freedom of expression, public interest, legal claim defense, etc.), (4) assesses the impact of erasure on business operations and other data subjects, (5) determines if data can be fully deleted or only pseudonymized, (6) creates deletion procedure (immediate systems, backups, archives), (7) identifies third parties with whom data has been shared who must also be notified of erasure request, (8) estimates timeline for completion and any required follow-up steps, (9) documents the final decision (grant/refuse/delay). Conclude with clear recommendation: fully erase, erase with exceptions, refuse with explanation, or delay (explaining grounds). Maintain detailed records for regulatory accountability. Indicate how requester will be notified of decision.

**Context:** Required for any right to erasure request under GDPR and similar regimes; common requests from customers; must balance rights against legitimate retention needs

**Difficulty:** Intermediate

**Follow-up:** If erasure is granted, execute deletion and confirm; if refused, prepare response letter explaining grounds

---

### PROMPT 30 — DATA PORTABILITY RESPONSE
An individual has requested data portability of their personal data: [DESCRIBE REQUEST]. Under GDPR Article 20 (or equivalent CCPA/PDPA provisions), please prepare a Data Portability Response that: (1) confirms whether the data falls within scope of Article 20 (data provided by individual, processing based on consent/contract, processed by automated means), (2) identifies all data elements covered by the request, (3) determines the appropriate technical format for portability (CSV, JSON, XML, or format commonly used by competing services if identifiable), (4) compiles data from all sources and systems in machine-readable format, (5) ensures data is accurate and complete as of request date, (6) creates a data transfer mechanism (email, secure download, API integration with alternative provider if feasible), (7) specifies any limitations on portability (e.g., trade secrets, third-party data, inferred information), (8) confirms timeline compliance (30 days or extended per GDPR Article 12(3)), (9) determines whether direct transmission to alternative provider is feasible and appropriate. Prepare practical guidance for requester on using the data with alternative services. Document the portability provision and format selected. If direct transmission to third party is requested, ensure appropriate security and verification of third party identity. Maintain records of data portability response.

**Context:** Increasing requests under GDPR and similar regimes; important for individual data autonomy; requires technical solution to transfer data between systems

**Difficulty:** Intermediate

**Follow-up:** If direct transmission to third party requested, verify third party identity and obtain additional consent/authorization as needed

---

## SECTION E: PRIVACY IMPACT ASSESSMENTS (5 PROMPTS)

### PROMPT 31 — DPIA FOR NEW PRODUCT/SERVICE
Our organization is launching [NEW PRODUCT/SERVICE DESCRIPTION], which will process [CATEGORIES OF PERSONAL DATA] from [IDENTIFIED DATA SUBJECTS]. Please conduct a Data Protection Impact Assessment (DPIA) as required by GDPR Article 35 (or equivalent privacy impact assessment requirements) that includes: (1) Summary of processing (purposes, categories of data, expected volume, retention period), (2) Necessity assessment (whether this processing is necessary for product/service delivery), (3) Proportionality assessment (is processing proportionate to business objectives), (4) Legitimate interest analysis if applicable, (5) Identification of data subjects (who is affected, any vulnerable populations), (6) Data subject rights (how will individuals exercise access, correction, erasure, portability), (7) Risk analysis: identify risks to data subjects (data breach, unauthorized access, discrimination, profiling, etc.), (8) Risk mitigation measures (technical/organizational controls to reduce identified risks), (9) Data protection by design and default assessment (privacy embedded in product from outset), (10) Consultation with third parties (DPA, processors, regulators if required). Conclude with risk determination (high-risk requiring consultation with authority; moderate-risk manageable with safeguards; low-risk acceptable). Include detailed Annex with risk/mitigation matrix. Format as document suitable for regulatory inspection. Identify any issues requiring resolution before product launch.

**Context:** Mandatory for new products/services involving large-scale systematic processing; important to embed privacy early in product development; required for GDPR compliance

**Difficulty:** Advanced

**Follow-up:** If high-risk identified, conduct PROMPT 32 (DPIA for AI/ML) if applicable, or escalate to DPA for consultation

---

### PROMPT 32 — DPIA FOR AI/ML SYSTEM
Our organization is implementing [DESCRIBE AI/ML SYSTEM: purpose, input data, decision-making impact]. Please conduct a comprehensive DPIA for this AI/ML system that covers: (1) System overview (how it works, decision types it makes, why individuals matter), (2) Data categories used (training, inference), (3) Processing purposes and legal basis, (4) Individuals affected (how AI decisions impact them), (5) Data quality assessment (representativeness, bias, accuracy), (6) Automated decision-making implications (whether system makes autonomous decisions under GDPR Article 22), (7) Potential bias and discrimination risks (protected characteristics in training data, algorithmic bias, impact disparities across populations), (8) Transparency and explainability (can decision-making be explained to individuals), (9) Data subject rights (access to decision logic, correction, challenge), (10) Security and access controls (who can access/modify model, outputs, training data), (11) Monitoring and oversight mechanisms (how will ongoing model performance be monitored, bias detected, decisions audited), (12) High-risk determination and mitigation measures. Assess whether model requires high-risk AI classification under emerging AI regulations. Document assumptions, limitations, and human oversight requirements. Consider external audit or certification of AI system. Present findings with clear recommendations for deployment, restrictions, or redesign.

**Context:** Critical for AI/ML systems involving personal data or significant decision impact; increasingly required under emerging AI regulations; essential for GDPR Article 22 compliance

**Difficulty:** Advanced

**Follow-up:** If high-risk AI identified, consider PROMPT 40 (AI training data compliance review) and PROMPT 41 (Automated decision-making assessment)

---

### PROMPT 33 — DPIA FOR EMPLOYEE MONITORING
Our organization intends to implement [DESCRIBE MONITORING SYSTEM: cameras, keystroke monitoring, location tracking, email monitoring, etc.] for [STATED PURPOSE]. Please conduct a DPIA specific to employee monitoring that addresses: (1) Necessity and proportionality (is monitoring necessary/proportionate to stated purpose, could less intrusive alternatives achieve purpose), (2) Legal basis assessment (likely employee consent, legal obligation, or legitimate interest—which applies and is it valid), (3) Categories of employees affected (all employees, specific department, specific roles), (4) Scope of monitoring (what is monitored, frequency, retention of monitoring data), (5) Risks to employee rights (privacy, dignity, discrimination, chilling effect on freedoms), (6) Vulnerable populations (if any—remote workers, health conditions, union representatives), (7) Technical safeguards (encryption, access controls, audit logs), (8) Data subject notification and transparency (will employees know they're monitored, can they access monitoring data), (9) Employee rights (correction, objection, inspection, deletion), (10) Third parties (IT vendors, outsourced monitoring providers requiring DPA), (11) Risk determination and mitigation. Assess against emerging employee privacy standards and regulatory guidance. Consider cultural and reputational impact on employee relations. Provide clear recommendation on whether monitoring is justified or should be modified/rejected.

**Context:** Important for organizations implementing employee monitoring; high sensitivity area with significant employee rights implications; required for GDPR compliance

**Difficulty:** Advanced

**Follow-up:** If monitoring approved, ensure DPA execution with vendors; conduct ongoing compliance monitoring

---

### PROMPT 34 — DPIA FOR CROSS-BORDER DATA TRANSFER
Our organization intends to transfer [DATA CATEGORIES] from [SOURCE COUNTRY] to [DESTINATION COUNTRY] for [PROCESSING PURPOSE]. Please conduct a DPIA specific to cross-border transfers that evaluates: (1) Transfer volume and scope (categories of data, number of individuals, frequency), (2) Data sensitivity assessment (sensitive categories requiring additional protection), (3) Destination country adequacy (does destination country have adequate legal framework—EU adequacy decision, equivalence finding, etc.), (4) Legal risks in destination (surveillance laws, government access, data localization requirements, political instability), (5) Transfer mechanism evaluation (whether adequate legal basis exists—adequate country, SCCs, BCRs, derogations), (6) Supplementary measures necessity (encryption, pseudonymization, access controls to compensate for legal gaps), (7) Data subject rights enforcement (can individuals exercise rights in destination country, what redress mechanisms exist), (8) Recourse mechanisms (EDPB complaints, court jurisdiction, alternative remedies), (9) Risk assessment (likelihood and severity of unauthorized access, government surveillance, data loss), (10) High-risk determination and mitigation plan. If high-risk identified, recommend transfer denial or additional safeguards. Reference recent regulatory guidance (EDPB, Schrems II, etc.). Provide clear go/no-go recommendation for transfer with conditions if needed.

**Context:** Essential before any international data transfer; required for GDPR compliance with Schrems II considerations; critical for cloud migration and outsourcing

**Difficulty:** Advanced

**Follow-up:** If proceeding with transfer, implement PROMPT 14 (Data transfer impact assessment) or PROMPT 13 (SCC review) for specific mechanism

---

### PROMPT 35 — DPIA FOR MARKETING ACTIVITIES
Our organization is implementing [DESCRIBE MARKETING ACTIVITY: email campaigns, targeted advertising, retargeting, profiling, segmentation, etc.] targeting [CUSTOMER SEGMENT]. Please conduct a DPIA specific to marketing activities that covers: (1) Processing purposes (direct marketing, profiling for segmentation, decision-making impact on individuals), (2) Data categories collected (what personal data is collected, inferred, or derived), (3) Data sources (where data comes from—first-party collection, third-party providers, brokers), (4) Profiling and segmentation mechanisms (how are individuals categorized and targeted), (5) Decision-making impact (does activity result in adverse decisions or exclusion from benefits), (6) Consent mechanisms (is opt-in consent being used or relying on other basis), (7) Legitimate interest assessment (if not consent-based, what is organization's legitimate interest), (8) Data subject transparency (are individuals aware of data collection and profiling), (9) Exclusion and discrimination risks (do profiling mechanisms create adverse impact on protected groups), (10) Cookie and tracking technologies (are cookies/pixels compliant with ePrivacy Directive), (11) Third-party data providers and data brokers (due diligence on data sources), (12) Risk assessment (profiling harms, automated decision-making, scope creep). Determine if high-risk marketing activity requiring additional safeguards. Provide specific recommendations for consent, transparency, fairness, and opt-out mechanisms.

**Context:** Important for data-driven marketing organizations; increasing regulatory scrutiny of profiling and targeted advertising; required for GDPR and ePrivacy compliance

**Difficulty:** Advanced

**Follow-up:** If profiling or automated decision-making identified, conduct PROMPT 41 (Automated decision-making assessment)

---

## SECTION F: PRIVACY POLICIES & NOTICES (6 PROMPTS)

### PROMPT 36 — WEBSITE PRIVACY POLICY (MULTI-JURISDICTION)
Please draft a comprehensive website Privacy Policy for [ORGANIZATION NAME AND INDUSTRY] that serves customers in [LIST JURISDICTIONS: EU, UK, Singapore, California, Canada, etc.] and addresses requirements of GDPR, UK GDPR, PDPA, CCPA, PIPEDA, and applicable local laws. The policy must clearly explain: (1) Organization identification (controller, contact details, DPA if applicable), (2) What personal data we collect (categories, whether required or optional), (3) How we collect data (direct from you, third parties, inferred), (4) Purposes of processing and legal basis for each purpose (separate basis if different jurisdictions apply), (5) Recipients (processors, sub-contractors, third parties, law enforcement), (6) Data retention periods (with justification for each category), (7) Your rights (access, correction, erasure, portability, restriction, objection, automated decision-making rights—detailed for each jurisdiction), (8) How to exercise rights (contact process, timeline, appeal procedures), (9) Cookie policy reference (link to separate cookie policy), (10) Transfers outside home jurisdiction (if applicable, explanation of mechanism and safeguards), (11) Children's data (if applicable), (12) Updates to privacy policy, (13) Complaint process (right to complain to regulator). Ensure language is clear, accessible, organized in sections, and jurisdiction-specific sections clearly marked. Include plain-language summary in addition to full policy. Make policy available in multiple languages if serving non-English jurisdictions. Ensure policy is technically accurate and legally defensible.

**Context:** Fundamental privacy law requirement; must be clear, accurate, and jurisdiction-specific; required for GDPR, CCPA, and most privacy regimes

**Difficulty:** Advanced

**Follow-up:** PROMPT 37 (Employee privacy notice) for workforce policy; PROMPT 38 (Cookie policy) for cookie-specific disclosure

---

### PROMPT 37 — EMPLOYEE PRIVACY NOTICE
Please draft a comprehensive Employee Privacy Notice for [ORGANIZATION NAME] that is required under GDPR Article 14 (information for employees) and similar provisions in other regimes. The notice must clearly explain: (1) Controller identification and DPA contact information, (2) Purposes of processing employee data (recruitment, employment management, payroll, benefits, performance management), (3) Legal basis for each processing activity (employment contract, legal obligation, legitimate interest, consent if applicable), (4) Categories of personal data collected (name, contact, identification, health, performance data, etc.), (5) Data sources (application, recruitment agencies, background check providers, performance systems), (6) Recipients of employee data (HR team, management, external providers, payroll processors), (7) Retention periods for each data category, (8) Employee rights (access, correction, erasure limitations due to employment law, objection to processing), (9) How to exercise rights and appeal process, (10) Automated decision-making (if any performance systems use automated decisions), (11) Right to lodge complaint with DPA, (12) Consequences of not providing data (whether provision is mandatory or optional), (13) Monitoring activities (workplace monitoring, email monitoring, etc. if applicable), (14) Updates to notice. Provide to employees: before hiring (in offer letter), at hire (in handbook), and annually (in updates). Ensure notice is clear, accessible to non-native speakers, and compliant with employment law. Keep tone professional and transparent.

**Context:** Legally required privacy disclosure to employees; increasingly emphasized by regulators; demonstrates employee transparency commitment

**Difficulty:** Intermediate

**Follow-up:** PROMPT 33 (DPIA for employee monitoring) if employee monitoring is mentioned in notice; PROMPT 36 (Website privacy policy) for customer-facing equivalent

---

### PROMPT 38 — COOKIE POLICY AND CONSENT BANNER
Please draft a comprehensive Cookie Policy and Consent Banner for [ORGANIZATION WEBSITE/APP] serving users in [JURISDICTIONS: EU, UK, etc.]. Provide: (1) COOKIE POLICY covering: (a) what cookies are and how they work, (b) types of cookies used (essential, analytics, marketing, social media), (c) purposes of each cookie type, (d) retention periods, (e) third parties setting cookies (vendors, partners), (f) how users can control cookies (browser settings, opt-out mechanisms, (g) list of specific cookies with purposes and retention, (h) links to third-party privacy policies for vendor cookies. (2) CONSENT BANNER specifying: (a) clear disclosure that cookies are used, (b) purposes of each cookie category, (c) separate consent options for each category (essential cannot be optional, others must be separately consentable), (d) no dark patterns (pre-checked boxes, forced consent), (e) plain language accessible to general users, (f) clear Accept/Reject buttons in equal prominence, (g) option to manage preferences in detail, (h) easy withdrawal of consent mechanism. Ensure compliance with ePrivacy Directive (EU) and equivalent requirements. Make policy and banner mobile-friendly and keyboard-accessible. Include technical implementation guidance for consent management platform. Provide testing checklist to ensure implementation meets legal requirements. Reference EDPB guidelines on cookie consent and avoid common non-compliance patterns.

**Context:** Critical for GDPR and ePrivacy Directive compliance; high regulatory scrutiny on cookie practices; increasingly important for user trust

**Difficulty:** Intermediate

**Follow-up:** PROMPT 36 (Website privacy policy) for broader privacy framework; ensure cookie policy cross-referenced in main policy

---

### PROMPT 39 — MOBILE APP PRIVACY NOTICE
Please draft a Privacy Notice for [MOBILE APP NAME/FUNCTION] that complies with GDPR, CCPA, App Store requirements, and other applicable regimes. The notice must clearly explain: (1) Organization identification and contact information, (2) What personal and device data the app collects (location, contacts, camera, microphone, device identifiers, usage data), (3) How data is collected (direct from user, app permissions, third-party SDKs, device sensors), (4) Purposes of data collection (functionality, analytics, marketing, improvement), (5) Legal basis for each processing activity, (6) Recipients of data (vendors, analytics providers, marketing platforms, sub-contractors), (7) Retention periods for data, (8) Whether data is shared or sold (California requirement), (9) User rights (access, deletion, opt-out of marketing/analytics), (10) How to exercise rights and contact information, (11) Security measures (encryption, access controls), (12) Children's data (if applicable—COPPA in US, GDPR for EU), (13) Third-party services (SDKs, analytics, ad networks with links to their privacy policies), (14) Permission requirements by platform (iOS, Android), (15) How to modify app permissions through device settings. Ensure notice is accessible within app (Settings > Privacy or equivalent), not buried in T&Cs. Make notice concise but complete. Provide in app store listing and welcome screens. Keep language clear for general users. Reference app permissions requested and explain why each is necessary.

**Context:** Important for app-based services; high user sensitivity to mobile privacy; critical for compliance with app store requirements and privacy laws

**Difficulty:** Intermediate

**Follow-up:** PROMPT 36 (Website privacy policy) for web-based equivalent or companion web service

---

### PROMPT 40 — CUSTOMER PRIVACY NOTICE
Please draft a Privacy Notice for customers of [BUSINESS TYPE/SERVICE] that clearly explains our data practices. The notice must address: (1) Organization identification (name, contact, location), (2) Categories of personal data collected about customers (name, contact, transaction history, preferences, browsing behavior, etc.), (3) How we collect data (directly from customer, from transactions, from third parties, from cookies/analytics), (4) Purposes for processing customer data (service delivery, customer service, marketing, analytics, fraud prevention, etc.), (5) Legal basis for each purpose, (6) Who we share data with (payment processors, fulfillment partners, analytics vendors, marketing partners), (7) How long we keep data (transaction records, customer history), (8) Customer rights (access, correction, marketing opt-out, deletion), (9) How to exercise rights (contact form, email, procedure, timeline), (10) Cookies and tracking (reference to cookie policy), (11) Data security measures, (12) Data transfers (if applicable, explanation of mechanisms), (13) Right to lodge complaint with DPA, (14) Changes to notice. Ensure notice is: (a) clearly visible (privacy policy link in website footer, reference in contracts), (b) accessible (clear language, not buried in long T&Cs), (c) actionable (with specific contact info and process for exercising rights), (d) up-to-date (reflecting current practices). Version notice for different customer types (online, in-store, subscription, etc.) if data practices differ. Keep tone professional but customer-friendly.

**Context:** Fundamental privacy law requirement for customer-facing businesses; critical for transparency and building customer trust

**Difficulty:** Intermediate

**Follow-up:** PROMPT 25 (DSAR acknowledgement letter) when customers exercise rights identified in notice

---

### PROMPT 41 — VENDOR/SUPPLIER PRIVACY NOTICE
Please draft a Privacy Notice for vendors and suppliers of [ORGANIZATION NAME] regarding how we process vendor personal data: [VENDOR CONTACT NAMES, BUSINESS DATA, PAYMENT INFORMATION, ETC.]. The notice must explain: (1) Organization identification (data controller), (2) Categories of vendor/supplier data collected (contact information, business details, tax ID, banking information, performance data), (3) Purposes of processing vendor data (vendor management, procurement, payment, compliance, due diligence), (4) Legal basis for processing (contract, legal obligation, legitimate business interest), (5) Recipients of vendor data (procurement team, finance, legal, external advisors), (6) Retention periods (varies by purpose and legal obligation), (7) Vendor rights (access to their data, correction, objection), (8) Security measures for protecting vendor data, (9) Data transfers (if applicable, international transfers with safeguards), (10) Sub-processors and external service providers (payment processors, accounting systems), (11) How vendors can exercise rights (contact process, response timeline), (12) Right to lodge complaint with DPA, (13) Consequences of not providing required data (whether provision is mandatory), (14) Policy updates. Provide notice to: (a) new vendors at onboarding, (b) existing vendors periodically (annually or with policy updates), (c) in procurement contracts and vendor agreements. Keep tone professional and appropriate for business-to-business context. Include clear contact person for privacy questions. Reference vendor DPA if separate from notice.

**Context:** Best practice for vendor management; demonstrates privacy commitment to business partners; may be required by procurement contracts or regulations

**Difficulty:** Intermediate

**Follow-up:** PROMPT 10 (DPA review against PDPA) or PROMPT 9 (DPA review against GDPR) to ensure vendor data sharing agreements are in place

---

## SECTION G: PRIVACY BY DESIGN (5 PROMPTS)

### PROMPT 42 — PRIVACY REQUIREMENTS FOR PRODUCT TEAM
We are building [DESCRIBE PRODUCT/SERVICE AND DATA FLOWS]. Please develop a comprehensive Privacy Requirements Document for the product development team that specifies: (1) Business requirements review (what personal data is truly necessary for product function—data minimization principle), (2) Legal basis identification (what lawful basis applies, is consent required), (3) Data collection requirements (minimum necessary data types, sources, frequency), (4) User consent mechanisms (how will privacy be explained, consent obtained, managed, withdrawn), (5) Data retention requirements (how long data must be kept, automatic deletion procedures), (6) Data security requirements (encryption at rest/transit, access controls, audit logging), (7) Data subject rights mechanisms (how will individuals exercise access, deletion, portability, correction rights), (8) International transfer requirements (if cross-border, what transfer mechanism is needed), (9) Third-party integrations (where third parties process data, DPA required), (10) Privacy-enhancing technologies (consider anonymization, pseudonymization, differential privacy where appropriate), (11) User transparency mechanisms (privacy notices, in-product disclosures, settings), (12) Testing and compliance (how will privacy be verified before launch), (13) Incident response (data breach handling procedures). Format as detailed specification document with sections for architects, developers, product managers, designers. Include specific privacy checklist for each development phase (design, development, testing, launch). Provide non-technical explanation of privacy concepts for product teams. Make requirements binding on development teams.

**Context:** Essential for embedding privacy in product development from outset; supports privacy by design principle; reduces post-launch compliance issues

**Difficulty:** Advanced

**Follow-up:** PROMPT 31 (DPIA for new product/service) to validate that privacy requirements are being met

---

### PROMPT 43 — DATA MINIMISATION AUDIT
Please conduct a Data Minimisation Audit of [ORGANIZATION/PRODUCT] evaluating whether we collect and retain only personal data necessary for our specified purposes. For each data category: [LIST DATA TYPES COLLECTED], assess: (1) whether data is necessary for primary purpose, (2) whether necessity could be achieved with less personal data or less sensitive alternatives, (3) whether data is retained longer than necessary, (4) whether data collection is legally required or voluntary, (5) whether data is used for secondary purposes (assess necessity for each), (6) whether aggregated or anonymized data would satisfy requirements, (7) impact on individuals if data were deleted (would service still function), (8) risk to individuals from retaining unnecessary data. For each identified unnecessary data collection: recommend deletion, anonymization, or restricted retention. Create data minimisation roadmap with: (a) immediate deletions (clearly unnecessary data), (b) planned deletions (data where retention rationale expires), (c) data reduction strategies (collect less sensitive alternative), (d) retention policy updates. Estimate resource effort for implementation. Include governance process for preventing unnecessary data collection in future. Provide to product/business teams with explanation of business benefit (reduced storage, regulatory compliance, reduced breach exposure).

**Context:** Important for GDPR Article 5 compliance (data minimization principle); reduces organizational risk; often reveals unnecessary data collection

**Difficulty:** Intermediate

**Follow-up:** PROMPT 44 (Retention schedule creation) to formalize deletion timelines

---

### PROMPT 44 — RETENTION SCHEDULE CREATION
Based on our documented processing activities and [REGULATORY/BUSINESS REQUIREMENTS], please create a comprehensive Data Retention Schedule that specifies: (1) For each data category collected by organization [LIST CATEGORIES], identify: (a) retention period justified by each purpose, (b) legal/regulatory requirements mandating retention, (c) business justification for retention period, (d) automatic deletion procedures and timeline, (e) exception procedures (if legal claim is pending, retention extends). (2) Format schedule as table with columns: data category, purpose(s), retention period, justification, deletion method, responsible party. (3) For data with multiple purposes, apply longest retention period necessary across all purposes. (4) For regulated data (financial, employment), identify regulatory minimum retention (e.g., 7 years for tax records). (5) Include secure deletion procedures (complete deletion from systems and backups, documentation of deletion). (6) Create implementation procedure: who is responsible for deletion monitoring, how deletions are triggered, how deletion is documented. (7) Establish governance: annual review of schedule, updating when purposes/regulations change, exception management when deletion is deferred due to legal dispute. (8) Template for adding new data types with retention analysis. Format as living document that can be shared with regulators (ROPA requirement). Include guidance for business teams on determining appropriate retention periods. Make retention schedule binding on all teams handling personal data.

**Context:** Required for GDPR Article 5 compliance (storage limitation); essential for ROPA documentation; supports data minimization and reduces storage costs

**Difficulty:** Intermediate

**Follow-up:** PROMPT 43 (Data minimisation audit) to identify unnecessary data for deletion

---

### PROMPT 45 — ANONYMISATION/PSEUDONYMISATION ASSESSMENT
We process [DATA CATEGORY] and are considering applying [anonymization/pseudonymization] to reduce privacy risk. Please conduct an Anonymisation/Pseudonymisation Assessment that: (1) Distinguishes between anonymisation (irreversible removal of identifiability, not considered personal data) vs. pseudonymisation (replacement of identifying data with token, still personal data but reduces linking), (2) For anonymisation: assess whether [TECHNIQUE PROPOSED] actually achieves irreversible de-identification (risk of re-identification through combination with other data), (3) Evaluate specific anonymisation techniques (aggregation, generalization, differential privacy, noise injection) for [YOUR DATA] and their effectiveness/data utility tradeoffs, (4) Assess whether re-identification is possible (either theoretically or practically given context), (5) For pseudonymisation: assess whether mapping between identifier and pseudonym can be protected sufficiently (encryption key management, access controls, separation from raw data), (6) Evaluate whether pseudonymisation achieves meaningful risk reduction vs. raw data storage, (7) Assess whether pseudonymised data remains subject to privacy rights (typically yes—still personal data), (8) For regulatory purposes, document whether data is truly anonymized (exempt from GDPR) or only pseudonymized (still regulated), (9) Recommend appropriate technique for your use case and data sensitivity, (10) Estimate implementation effort and cost for application. Provide practical guidance for product/engineering teams on correct implementation. Warn against false anonymisation claims that don't withstand EDPB scrutiny.

**Context:** Important for reducing privacy risk where full data is unnecessary; growing regulatory focus on proper anonymization vs. pseudonymization distinction; critical for secondary data use

**Difficulty:** Advanced

**Follow-up:** PROMPT 31 (DPIA for new product/service) to incorporate anonymization as risk mitigation measure

---

### PROMPT 46 — PRIVACY-ENHANCING TECHNOLOGY EVALUATION
Our organization is considering implementing [PRIVACY-ENHANCING TECHNOLOGY: e.g., differential privacy, homomorphic encryption, federated learning, privacy-preserving analytics, etc.] to [STATED PURPOSE]. Please conduct an evaluation that: (1) Explains the technology in accessible terms (what it does, how it works, relevant parameters), (2) Assesses whether technology actually achieves the privacy goals claimed (independent assessment, not vendor claims), (3) Evaluates whether technology is suitable for [YOUR SPECIFIC USE CASE] given your data types and analysis needs, (4) Assesses data utility tradeoffs (privacy/utility curve—what accuracy/insights are lost for privacy gain), (5) Evaluates implementation complexity and organizational capability (do we have expertise, or does this require external partnership), (6) Estimates cost and timeline for implementation, (7) Assesses vendor maturity and reliability (if using third-party technology/vendor), (8) Evaluates whether technology is regulatory-accepted (do regulators recognize this as achieving privacy goals), (9) Identifies residual risks even with technology (does technology eliminate all privacy risk or merely reduce it), (10) Provides recommendation: implement, pilot, defer, or reject with reasoning. Include assessment of realistic privacy gains vs. organizational effort/cost. Provide to business teams with honest assessment of tradeoffs. Distinguish between technologies that truly achieve privacy (e.g., differential privacy with appropriate noise) vs. technologies that merely provide security (encryption—protects against some risks but not all). Consider regulatory acceptability and audit trail.

**Context:** Growing organizational interest in privacy-enhancing technologies; important to evaluate realistic effectiveness vs. hype; supports privacy by design implementation

**Difficulty:** Advanced

**Follow-up:** PROMPT 31 (DPIA for new product/service) to incorporate evaluation findings into risk assessment

---

## SECTION H: AI & PRIVACY (5 PROMPTS)

### PROMPT 47 — AI SYSTEM PRIVACY IMPACT ASSESSMENT
Our organization is implementing [AI SYSTEM DESCRIPTION: model type, input data, decision/output, business purpose]. Please conduct a comprehensive Privacy Impact Assessment for this AI system covering: (1) System overview (architecture, data flows, inputs/outputs, decision scope), (2) Personal data in AI pipeline: (a) training data sources (is personal data used—what categories, from where), (b) inference data (does model process personal data for predictions), (c) output data (does model generate personal information about individuals). (3) Data subject impacts: (a) who is affected by system (individuals in training data, individuals subject to predictions, individuals impacted by decisions), (b) what decisions or actions does system influence, (c) is this automated decision-making under GDPR Article 22. (4) Lawful basis assessment (what is legal basis for training data, inference data, can consent be obtained or is legitimate interest appropriate). (5) Data quality and bias assessment: (a) is training data representative and unbiased, (b) are there protected characteristics in data creating discrimination risk, (c) what is accuracy/precision on different population subsets. (6) Transparency and explainability (can system decisions be explained to individuals, are explanations meaningful). (7) Data subject rights (how will individuals exercise access to training data, correction, objection to predictions, challenge automated decisions). (8) Privacy risks (data breaches exposing training data, model inversion/membership inference attacks, extraction of training data from model). (9) Retention of training/inference data (how long is data kept, is deletion possible). (10) Third parties (if using third-party AI platform, evaluate their data practices and DPA). (11) Monitoring and oversight (how will model performance be monitored over time, how will bias be detected and remediated, what is human oversight process). Present findings with specific privacy risks and mitigation measures. Provide clear recommendation on deployment, restrictions, or redesign.

**Context:** Critical for responsible AI development; increasingly required by emerging AI regulations; essential for GDPR Article 22 compliance if automated decision-making involved

**Difficulty:** Advanced

**Follow-up:** PROMPT 48 (AI training data compliance review) to detail-examine training data privacy compliance

---

### PROMPT 48 — AI TRAINING DATA COMPLIANCE REVIEW
Our AI model has been trained on [DESCRIBE TRAINING DATA SOURCE: dataset name, size, source, data categories]. Please conduct an AI Training Data Compliance Review assessing: (1) Data source verification (is source documented, legitimate, with clear provenance), (2) Personal data identification (does training data contain personal data—what categories, of whom), (3) Lawful basis for training data collection (when original data was collected, was consent obtained or legitimate basis established for that collection), (4) Lawful basis for AI training use (is training data use the same purpose as original collection—if not, is it compatible under GDPR Article 6(4) repurposing test), (5) Data subject notification (were individuals told their data might be used for AI training—is this explicitly disclosed), (6) Intellectual property and licensing (does data source allow use for AI training without additional licensing), (7) Third-party data rights (if training data was licensed from third parties, review license terms for AI use permissions). (8) Sensitive data handling (if training data contains sensitive categories—health, biometric, special categories—are enhanced safeguards in place), (9) Accuracy and representativeness (is training data accurate, up-to-date, representative of populations model will be applied to), (10) Data minimization (is all training data necessary for model performance or could training be done on less personal data/anonymized data), (11) Retention and deletion (when will training data be deleted, can deletion be verified from model). Present findings with specific compliance gaps. If data use is not compliant, recommend: (a) seek retroactive consent from data subjects if feasible, (b) cease model training on non-compliant data, (c) use alternative compliant training data, (d) anonymize training data if possible. Provide remediation roadmap for addressing identified issues.

**Context:** Critical for organizations using personal data to train AI models; common compliance gap in AI development; required for GDPR and similar regimes

**Difficulty:** Advanced

**Follow-up:** PROMPT 47 (AI system privacy impact assessment) for broader system assessment; PROMPT 41 (Automated decision-making assessment) if model makes autonomous decisions

---

### PROMPT 49 — AUTOMATED DECISION-MAKING (ARTICLE 22 GDPR) ASSESSMENT
Our organization uses [AI/ALGORITHMIC SYSTEM] to make or significantly influence decisions affecting individuals: [DESCRIBE DECISIONS: hiring, lending, credit scoring, fraud detection, content recommendation, etc.]. Please conduct an Automated Decision-Making Assessment under GDPR Article 22 and similar provisions that: (1) Determines whether system is "automated decision-making" (fully automated without human involvement) vs. "profiling" (automated analysis of characteristics that may inform human decision). (2) If automated decision-making, identifies whether it produces "legal effect" or "significantly affects" individuals (creates obligation, limits choice, adversely impacts individual). (3) If Article 22 applies, assesses compliance requirements: (a) lawful basis for automated decision-making (cannot be consent alone—must be contract performance or vital interest or public task; legitimate interest does not allow Article 22 processing), (b) safeguards and rights (right to explanation, human review/intervention, ability to contest decision), (c) special categories prohibition (cannot make Article 22 decisions based on sensitive data unless specific exception applies). (4) For each decision type, evaluate: whether full automation is necessary, whether human review is feasible, whether individuals can contest decisions, what remedies exist if decision is wrong. (5) Assess decision accuracy and fairness (test whether system discriminates against protected groups, whether accuracy varies by demographic). (6) Documents safeguards in place (human review procedures, audit mechanisms, individual notification). (7) Provides recommendation: compliant, compliant with conditions (e.g., mandatory human review), or non-compliant. If non-compliant, recommend changes (human review requirement, use of different lawful basis, individual consent verification). Present findings suitable for regulatory accountability and audit.

**Context:** Important for any organization using AI/algorithms for consequential decisions about individuals; high regulatory scrutiny; critical for GDPR Article 22 compliance

**Difficulty:** Advanced

**Follow-up:** PROMPT 31 (DPIA for new product/service) to incorporate Article 22 findings; PROMPT 47 (AI system privacy impact assessment) for broader AI assessment

---

### PROMPT 50 — AI VENDOR PRIVACY DUE DILIGENCE
Our organization is evaluating using [THIRD-PARTY AI VENDOR/SERVICE] for [SPECIFIED PURPOSE]. Please conduct comprehensive AI Vendor Privacy Due Diligence assessing: (1) Vendor data practices: (a) what personal data does vendor collect from/about our organization and users, (b) what are vendor's purposes for collecting this data, (c) how long does vendor retain data, (d) does vendor share data with third parties. (2) Training data use: (a) does vendor use customer data for AI model training, (b) are our customers' data used to train models used by other customers, (c) what opt-out or consent mechanisms exist. (3) Vendor data security (encryption, access controls, breach notification procedures). (4) Data transfer mechanisms (if vendor is in different jurisdiction, what transfer safeguards are in place—adequacy decision, SCCs, other). (5) Contractual framework: (a) does vendor have appropriate DPA/data processing agreement in place, (b) does DPA address AI-specific obligations (training data handling, sub-processor use, model transparency). (6) Vendor policies: (a) review vendor privacy policy for data use disclosures, (b) assess transparency of how AI models use data, (c) evaluate mechanisms for users to understand how their data affects model decisions. (7) Regulatory compliance: (a) is vendor compliant with privacy laws in relevant jurisdictions, (b) has vendor received regulatory complaints or enforcement actions regarding privacy. (8) Red flags: (a) vendor uses customer data for model training without explicit consent, (b) vendor has history of data breaches, (c) vendor's data security practices are inadequate, (d) vendor is unclear about data use. Provide recommendation: approved, approved with conditions (require specific DPA terms, audit rights, opt-out mechanisms), or rejected. Include DPA revisions needed before contract execution.

**Context:** Critical for organizations considering AI/ML vendor adoption; important to understand vendor data practices before committing; increasingly important as AI services are widely available

**Difficulty:** Advanced

**Follow-up:** PROMPT 9 (DPA review against GDPR) to review vendor DPA terms; PROMPT 48 (AI training data compliance review) if vendor uses data for model training

---

### PROMPT 51 — GENERATIVE AI ACCEPTABLE USE POLICY FOR PERSONAL DATA
Our organization is implementing [GENERATIVE AI TOOL: e.g., ChatGPT, Claude, other LLM] and needs to establish acceptable use policies for employee/customer interaction with personal data. Please develop a Generative AI Acceptable Use Policy that: (1) Clearly prohibits uploading or disclosing personal data to public generative AI systems without controls (public systems may retain data for training). (2) Permits use of generative AI only with: (a) internal/proprietary systems where data retention is controlled, or (b) vendor systems with DPA confirming data is not used for model training/improvement. (3) Specifies data categories strictly prohibited in generative AI: (a) sensitive categories (health, financial, biometric, genetic data), (b) customer personal data (must not disclose customer information to generative AI), (c) employee data (limited use for HR purposes with safeguards). (4) Permits limited internal use of generative AI for: (a) drafting generic policy templates (not containing actual personal data), (b) processing aggregated/anonymized data, (c) internal research/analysis. (5) Requires approval process for use of generative AI with any personal data (even limited use requires privacy review). (6) Establishes controls: (a) use only from approved accounts, (b) audit logging of AI system use, (c) DPA review before vendor AI systems are used, (d) training on risks. (7) Specifies liability allocation (user/department responsible for compliance if they violate policy). (8) Requires vendors using generative AI (consultants, service providers) to comply with policy. (9) Includes clear examples of prohibited use (uploading customer database, disclosing employee SSNs, sharing patient health data). (10) Provides guidance on appropriate redaction before using generative AI (remove identifying information where possible). Present policy as binding governance document. Include training materials for employees. Provide to legal, HR, product teams with specific guidance on their use cases.

**Context:** Critical for organizations adopting generative AI tools; high risk of inadvertent personal data disclosure to public AI systems; essential governance framework

**Difficulty:** Intermediate

**Follow-up:** PROMPT 9 (DPA review against GDPR) to review any vendor generative AI systems for data use terms

---

## FINAL NOTES FOR PRACTITIONERS

This prompt library is designed to be comprehensive, detailed, and immediately actionable for privacy lawyers and compliance professionals. Each prompt:

- Is formatted for easy copy-paste into AI tools (Claude, ChatGPT, etc.)
- Contains clear bracketed placeholders for your specific organizational context
- Provides multiple use cases and follow-up pathways
- Scales from beginner to advanced complexity
- References specific legal regimes (GDPR, PDPA, CCPA, UK GDPR, PIPEDA)
- Produces work product suitable for regulatory inspection and audit

**Usage Tips:**

1. Copy the full prompt text (excluding the ID/title) into your AI tool
2. Replace [BRACKETED PLACEHOLDERS] with your specific facts and context
3. Review and edit AI output for accuracy—AI is advisory, not definitive legal guidance
4. Maintain records of prompts used and responses for file documentation
5. Use follow-up prompts to deepen analysis or conduct adjacent compliance reviews
6. Combine prompts for comprehensive compliance programs (e.g., PROMPT 5 → PROMPT 1-3 → PROMPT 6 → PROMPT 20)

**Disclaimer:** These prompts are tools for generating working drafts and compliance analysis. All AI-generated output requires attorney review for legal accuracy and applicability to your specific jurisdiction and circumstances. Do not rely on AI output without independent legal verification.

---

**Document Version:** V4.02
**Last Updated:** March 2026
**Applicable Law:** GDPR, UK GDPR, PDPA (Singapore), CCPA/CPRA (California), PIPEDA (Canada), and emerging AI regulations

---

## SECTION G: SAL-MICROSOFT SINGAPORE DATA PROTECTION PROMPTS

*The following prompts are adapted from the **Prompt Engineering for Lawyers (2nd Edition)** guide, published by the **Singapore Academy of Law (SAL)** in collaboration with **Microsoft Singapore** (2025). Developed by Singapore data protection practitioners. Source: https://sal.org.sg/wp-content/uploads/2025/10/Prompt-Engineering-Guide-2025-2nd-Edition.pdf*

---

### PROMPT SAL-1 — PDPA DATA BREACH NOTIFICATION PACKAGE (SINGAPORE)

*Source: SAL Guide, New Prompts (2nd Edition)*

I am a data protection counsel supporting a Singapore organisation. Using only the attached incident log and timeline, prepare the following three documents:

1. **Internal incident report**
2. **Data subject notification**
3. **Regulator-facing summary** compliant with the Personal Data Protection Act 2012 (Singapore)

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

For the **PDPC notification**, include mandatory particulars under Regulation 5: date of awareness, chronology of containment steps, number of affected individuals, types of data, potential harm, remedial actions, contact person.

For **notifications to individuals** (Regulation 6), include: circumstances, types of data, potential harm, remedial steps by the organisation, and steps individuals can take to mitigate misuse.

Do not speculate on root cause or impact; state what is known, what is suspected, and what remains unknown. Maintain consistency with defined terms across all three documents.

Use only these materials:
- Incident timeline and data categories
- Containment actions and impact assessment
- Personal Data Protection Act 2012 Part 6A (Notification of Data Breaches)
- Personal Data Protection (Notification of Data Breaches) Regulations 2021
- PDPC Advisory Guidelines on Key Concepts

Where attachments are referenced, restrict analysis to those materials and provide pinpoint references.

**Context:** Singapore PDPA data breach response
**Difficulty:** Advanced
**Best AI tool:** Claude (document attachment required)
**Follow-up:** Chain with a communications prompt to draft the press statement and employee briefing

---

### PROMPT SAL-2 — NRIC COLLECTION COMPLIANCE ANALYSIS (SINGAPORE PDPA)

*Source: SAL Guide, Regulatory Compliance section*

Analyse the references provided to assess if we can stop collecting NRIC numbers of our customers. My company provides [DESCRIBE SERVICES] in Singapore. Before [DESCRIBE PROCESS], customers are asked to fill up a questionnaire. I am the data protection officer, and I have been asked whether we can stop collecting NRIC numbers.

Ensuring compliance with Singapore law, provide your assessment objectively with a clear justification. Think through this step-by-step. Analyse the following:
- Personal Data Protection Act
- Personal Data Protection Regulations
- Advisory Guidelines on Key Concepts
- Advisory Guidelines on Selected Topics
- NRIC Guidelines

Restrict the analysis to the references above and cite applicable sections of the legislative or regulatory provisions.

**Context:** Singapore PDPA — NRIC collection compliance
**Difficulty:** Intermediate
**Best AI tool:** Claude
**Tips:** Attach the relevant PDPC guidelines as documents for better accuracy. Cite specific provisions in your follow-up questions.

---

### PROMPT SAL-3 — ESG / SUSTAINABILITY REGULATORY CHANGE IMPACT ASSESSMENT (SINGAPORE)

*Source: SAL Guide, New Prompts (2nd Edition)*

I am a compliance adviser at a Singapore organisation. A regulator or standards body has issued updated requirements on ESG reporting (e.g., sustainability disclosures under ACRA's reporting framework). I need to prepare a Regulatory Change Impact Assessment for internal approval.

The memorandum shall follow this structure:
1. Background & Scope
2. Summary of Regulatory Change
3. Applicability to the Organisation (entities, functions, products/services, locations)
4. Gap Analysis (current state vs new requirements)
5. Risk Assessment (legal/compliance, conduct, data protection/privacy, operational/technology, financial/reputation, health & safety)
6. Remediation Plan (measures, owners, dependencies)
7. Implementation Timeline & Milestones
8. Approvals, Assurance & Ongoing Monitoring

The analysis should map each new requirement to a concrete control (policy, procedure, system/configuration, training/communications, contracts/third-party oversight) and identify areas requiring legal interpretation or regulator engagement.

Draft language must be precise, neutral, and decision-oriented, with clear asks for management approval of resources and timelines. Do not create obligations not present in the source documents; where ambiguity exists, set out conservative options with pros/cons and a recommended position. Maintain a traceability table linking each clause/section to the proposed control and evidence.

Use only these materials:
- The ACRA Sustainability Reporting requirements and official FAQs/circulars
- The organisation's current policies, procedures, control inventories, contracts/templates, and risk assessments for the impacted area
- Any prior governance papers and action trackers relevant to this topic

Where attachments are referenced, restrict analysis to those materials with pinpoint references.

**Context:** Singapore ACRA/MAS ESG regulatory compliance
**Difficulty:** Advanced
**Best AI tool:** Claude (document attachment required)

