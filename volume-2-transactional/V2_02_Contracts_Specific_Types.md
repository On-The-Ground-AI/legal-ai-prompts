# V2.02 Contracts — Specific Types
## Comprehensive AI Prompt Pack for Drafting & Reviewing Specific Contract Types

**Overview:** This prompt pack contains 50+ detailed, production-ready prompts for drafting, reviewing, and analyzing specific contract types. Each prompt is formatted for direct copy-paste into Claude or other legal AI tools, with clear placeholders, context, difficulty levels, and suggested follow-ups.

---

## A. NON-DISCLOSURE AGREEMENTS (6 prompts)

### PROMPT A1 — MUTUAL NDA DRAFT
Draft a mutual non-disclosure agreement between [PARTY_A_NAME] and [PARTY_B_NAME] for the purpose of [TRANSACTION_PURPOSE: e.g., "evaluating a potential business partnership"]. The agreement should be governed by [JURISDICTION] law and include confidentiality obligations lasting [DURATION: e.g., "3 years"], standard exclusions (including information already public), standard return/destruction of materials clause, and a non-circumvention provision preventing parties from contacting each other's employees or customers without consent. Include a mutual acknowledgment that a breach would cause irreparable harm. The agreement should be approximately 3-5 pages and suitable for [TRANSACTION_TYPE: e.g., "a technology licensing transaction"].

**Context:** Use when two parties are evaluating a potential transaction and need equal confidentiality protections. Mutual NDAs are common in M&A due diligence, technology partnerships, and joint venture discussions.

**Difficulty:** Beginner

**Follow-up:** PROMPT A2 (if you need to make the NDA one-sided instead)

---

### PROMPT A2 — UNILATERAL NDA DRAFT
Draft a unilateral non-disclosure agreement where [DISCLOSING_PARTY] will disclose confidential information to [RECEIVING_PARTY] in connection with [PURPOSE]. The receiving party is the sole obligor. Include provisions covering: (1) definition of confidential information, (2) permitted uses (limited to evaluating the [TRANSACTION_TYPE]), (3) return or destruction of materials, (4) permitted disclosures (only to advisors, limited to [NUMBER] people, under NDAs), (5) no license or obligation to proceed, (6) [DURATION]-year survival clause after termination, (7) equitable remedies language, and (8) integration clause. The agreement should be suitable for [DISCLOSER_CONTEXT: e.g., "a confidential patent license opportunity"] and governed by [JURISDICTION] law. Target length: 2-3 pages.

**Context:** Use when one party (often the more powerful party or the one holding sensitive IP) needs to restrict the other party's use of information. Common in technology licensing, real estate pitches, and confidential business opportunities.

**Difficulty:** Beginner

**Follow-up:** PROMPT A3 (if you need to review the resulting NDA against your actual transaction)

---

### PROMPT A3 — NDA REVIEW & TRIAGE
Review the attached NDA between [PARTY_A] and [PARTY_B] and provide a detailed triage analysis. Identify: (1) any one-sided or ambiguous language favoring one party; (2) gaps in standard protections (e.g., missing exclusions, no employee disclosure limits, undefined "confidential information"); (3) red flags (e.g., perpetual obligations, overly broad definitions, restrictive return-of-materials clauses); (4) jurisdictional concerns if governed by [JURISDICTION]; and (5) alignment with [CONTEXT: e.g., "typical market practice for [TRANSACTION_TYPE]"]. For each issue, assign a risk level (Low/Medium/High) and provide recommended language or a brief comment. Format as a table: Issue | Current Language | Risk | Recommendation. Then provide a 3-5 sentence executive summary and prioritized list of 3-5 key negotiation points.

**Context:** Use before signing an NDA to understand your exposure and identify negotiation opportunities. Particularly useful when you receive an NDA drafted by the counterparty and want to understand what you're agreeing to.

**Difficulty:** Intermediate

**Follow-up:** PROMPT A4 (if you need help negotiating the identified issues)

---

### PROMPT A4 — NDA COMPARISON AGAINST STANDARD FORM
I have two NDAs: a "Market Standard" NDA (provided below) and [COUNTERPARTY_NAME]'s Proposed NDA (provided below). Compare them and identify all material differences. For each difference, explain: (1) what the market-standard version says, (2) what the proposed version says, (3) the practical impact on [MY_ROLE: e.g., "the receiving party"], and (4) whether the proposed change is market-typical. Organize by topic (definitions, permitted use, return of materials, survival, remedies, etc.). Then provide a summary table with columns: Topic | Market Standard | Proposed | Impact on [MY_ROLE] | Recommendation (Accept/Negotiate/Reject). Finally, list the 5 most material deviations and suggest revised language for any you recommend rejecting.

**Context:** Use when you have access to a market-standard NDA template and want to understand how counterparty deviations affect you. Helps prioritize which differences are deal-breakers vs. acceptable variations.

**Difficulty:** Intermediate

**Follow-up:** PROMPT A5 (to draft a negotiation response email)

---

### PROMPT A5 — NDA NEGOTIATION RESPONSE
I received an NDA from [COUNTERPARTY_NAME] dated [DATE] and have identified [NUMBER] issues. Provide me with a professional but firm email to [COUNTERPARTY_CONTACT] requesting specific modifications. Address these issues: [ISSUE_1: e.g., "Definition of confidential information is too broad and includes information that is not confidential"], [ISSUE_2], [ISSUE_3]. For each issue, explain why the proposed change is necessary from [MY_PERSPECTIVE: e.g., "operational"], and suggest revised language or a reasonable compromise. Maintain a collaborative tone while making clear we cannot accept the current version. End with a request for revised language within [TIMEFRAME] and an offer to discuss by phone. Keep the email to 3-4 paragraphs. Then provide 3 revised language snippets that address the key issues.

**Context:** Use after triaging an NDA and identifying specific negotiation points. This generates a diplomatic counterproposal email rather than a point-by-point redline.

**Difficulty:** Intermediate

**Follow-up:** PROMPT A6 (if you need to manage multiple parties' confidentiality rights)

---

### PROMPT A6 — MULTILATERAL NDA FOR CONSORTIUM
Draft a multilateral non-disclosure agreement for a consortium consisting of [PARTY_1], [PARTY_2], [PARTY_3], and [PARTY_4], collectively evaluating [PROJECT_NAME/TRANSACTION]. The agreement should: (1) impose equal confidentiality obligations on all parties toward all other parties (mutual/multilateral structure), (2) allow each party to disclose information to [PERMITTED_RECIPIENTS: e.g., "employees, advisors, and board members"], (3) require confidentiality agreements from all recipients, (4) establish a steering committee chair ([TITLE/PARTY]) who can manage administrative questions, (5) prevent one party from circumventing others via direct contact with their affiliates, (6) include a [DURATION]-year survival clause, and (7) address what happens if the consortium breaks up (ongoing confidentiality obligations remain). Include a schedule identifying each party's key personnel and advisors. The agreement should be neutral (no party favored) and governed by [JURISDICTION] law. Target length: 5-7 pages.

**Context:** Use when three or more parties jointly evaluate a transaction, acquisition, or project and all need equal protection. Common in consortium acquisitions, joint development projects, and syndicated investments.

**Difficulty:** Advanced

**Follow-up:** PROMPT B1 (if the parties then enter a technology partnership requiring a SaaS or IP license agreement)

---

## B. SAAS & TECHNOLOGY AGREEMENTS (6 prompts)

### PROMPT B1 — SAAS SUBSCRIPTION AGREEMENT DRAFT
Draft a SaaS subscription agreement for [SAAS_PROVIDER_NAME] to provide [SAAS_PRODUCT_NAME] to [CUSTOMER_NAME]. The agreement should cover: (1) service scope (describe briefly what the service does and what is included vs. excluded [SCOPE_DETAILS]), (2) subscription term ([DURATION] with auto-renewal unless cancelled [NOTICE_PERIOD] days prior), (3) pricing ([PRICE_PER_MONTH/YEAR] per [UNIT: e.g., "user per month"]), (4) payment terms (net [DAYS], annually in advance or monthly), (5) service levels (uptime SLA of [UPTIME_PERCENTAGE]%, response time of [TIME] for critical issues, credits for missed SLAs), (6) data security (encryption in transit/at rest, GDPR/CCPA compliance, backups [FREQUENCY]), (7) acceptable use policy (no illegal use, no reverse engineering, no excessive bandwidth), (8) intellectual property (Provider retains all IP in the service; Customer retains IP in Customer Data), (9) limitation of liability ([CAP_AMOUNT] or [MULTIPLIER] of annual fees), (10) termination rights (either party, with [NOTICE] days notice; immediately for material breach), and (11) confidentiality. The agreement should be [PAGES] pages and favorable to [PROVIDER/BALANCED]. Include all standard limitations, disclaimers, and indemnities.

**Context:** Use when a SaaS company needs a boilerplate customer agreement. This is a provider-favorable template suitable for SMB customers; enterprise customers typically negotiate materially.

**Difficulty:** Intermediate

**Follow-up:** PROMPT B2 (if you need to draft a software license for a one-time license instead of SaaS)

---

### PROMPT B2 — SOFTWARE LICENCE AGREEMENT DRAFT
Draft a software license agreement for [LICENSOR_NAME] to grant a [SCOPE: "non-exclusive, non-transferable"] license to [LICENSEE_NAME] to use [SOFTWARE_PRODUCT_NAME] [LICENSE_TYPE: e.g., "perpetual, for internal business purposes only"]. The agreement should include: (1) license grant (specify use rights, restrictions on reverse engineering/disassembly, no sublicense rights), (2) installation (number of installations: [NUMBER] or unlimited), (3) maintenance and updates ([PROVIDER] provides [FREQUENCY: e.g., "annual"] updates; [LICENSEE] must apply within [TIMEFRAME]), (4) intellectual property (Licensor retains all IP; license is non-exclusive except [EXCLUSIVITY_DETAILS]), (5) fees ([AMOUNT], payable [TERMS]), (6) term ([DURATION] with renewal options), (7) support ([SUPPORT_LEVEL: e.g., "email support, 24-hour response time"]), (8) warranty disclaimer ([DISCLAIMER_LEVEL: e.g., "AS IS"], except [SPECIFIC_WARRANTIES]), (9) limitation of liability (liability capped at fees paid), (10) indemnity (each party indemnifies the other for IP claims), (11) confidentiality, (12) termination ([TERMINATION_RIGHTS]), and (13) data security ([SECURITY_MEASURES]). Include standard export controls language. Target length: 4-6 pages. Tone: [TONE: e.g., "Balanced but slightly favoring licensor"].

**Context:** Use for perpetual or term-based software licenses (not SaaS). Common for enterprise software, on-premises tools, and standalone applications.

**Difficulty:** Intermediate

**Follow-up:** PROMPT B3 (if you need to define API terms for third-party integrations)

---

### PROMPT B3 — API TERMS OF USE DRAFT
Draft Terms of Use for [COMPANY_NAME]'s Application Programming Interface (API), which allows third-party developers to access [API_CAPABILITIES: e.g., "real-time data, transaction processing"]. The terms should cover: (1) license grant (limited, non-exclusive, non-transferable right to access and use the API for [USE_CASE: e.g., "integrating with Customer's internal systems"]), (2) restrictions (no competitive products, no reverse engineering, no automated scraping beyond [RATE_LIMIT: e.g., "100 requests/minute"]), (3) API credentials (developers receive keys; keys are confidential; misuse results in immediate suspension), (4) rate limits and quotas ([LIMIT_DETAILS]), (5) uptime expectations (API uptime target [PERCENTAGE]%, no SLA promised, maintenance windows [FREQUENCY]), (6) data handling (API returns non-personal data only; developers may not store copies longer than [DURATION]; GDPR compliance), (7) intellectual property (Company retains all IP in the API; Developer retains IP in applications built on API), (8) indemnity (Developer indemnifies Company for claims arising from Developer's use), (9) liability (Company not liable for data loss, interruptions, or indirect damages), (10) termination (Company may terminate access immediately for breach or business reasons with [NOTICE] notice), (11) monitoring ([COMPANY] monitors usage and traffic patterns), and (12) no support ([SUPPORT_LEVEL]). Include attribution requirements if applicable. Target length: 3-4 pages.

**Context:** Use when you operate an API and want terms protecting you from misuse, rate abuse, and competitive copying. Commonly used for data/content platforms, payment processors, and integration services.

**Difficulty:** Intermediate

**Follow-up:** PROMPT B4 (if you need a broader technology services agreement)

---

### PROMPT B4 — TECHNOLOGY SERVICES AGREEMENT DRAFT
Draft a comprehensive Technology Services Agreement between [SERVICE_PROVIDER_NAME] and [CLIENT_NAME] for [SERVICE_DESCRIPTION: e.g., "software development, cloud migration support, and technical consulting"]. The agreement should establish: (1) scope of services (detailed statement of work with deliverables, milestones, and acceptance criteria [SOW_DETAILS]), (2) term ([DURATION], with renewal options), (3) pricing and payment (project-based pricing: [AMOUNT]; time-and-materials pricing: [RATE_DETAILS]; payment terms: net [DAYS]), (4) change management (scope changes require a written change order signed by both parties; additional fees apply), (5) staffing ([PROVIDER] assigns [TEAM_COMPOSITION]; Client may request replacement of underperforming staff), (6) project governance (weekly [MEETING_FREQUENCY] status meetings, reporting structure, escalation procedures), (7) intellectual property (for custom work: Client owns deliverables and IP; Provider retains pre-existing and off-the-shelf IP), (8) warranties (Provider warrants services conform to professional standards; warranty period [DURATION]), (9) confidentiality (both parties keep confidential information secret), (10) limitation of liability ([CAP_AMOUNT] or [MULTIPLIER] of fees), (11) indemnification (each party indemnifies the other), (12) data handling and security ([SECURITY_STANDARDS]), and (13) termination rights ([TERMINATION_TERMS]). Include a detailed statement of work as Schedule A. Target length: 6-8 pages. Tone: [TONE: e.g., "Balanced"].

**Context:** Use for custom software development, IT consulting, cloud migration, or specialized technology services where a detailed SOW is essential.

**Difficulty:** Advanced

**Follow-up:** PROMPT B5 (if the services include cloud hosting)

---

### PROMPT B5 — CLOUD HOSTING AGREEMENT DRAFT
Draft a Cloud Hosting Agreement between [CLOUD_PROVIDER_NAME] and [CLIENT_NAME] for hosting [CLIENT_SYSTEMS/APPLICATIONS: e.g., "web applications, databases, development environments"]. The agreement should cover: (1) service description (hosting infrastructure, compute capacity [SPECS], storage [AMOUNT/TERMS], bandwidth [ALLOWANCE], geographic regions [REGIONS]), (2) term ([DURATION], auto-renew), (3) pricing (monthly: [PRICE_DETAILS]; upfront discount: [DISCOUNT_DETAILS]), (4) service levels (uptime SLA [PERCENTAGE]%, response time [TIME], downtime credits [CREDIT_DETAILS]), (5) access and security (Client provides cloud credentials; Provider implements [SECURITY_MEASURES: e.g., "encryption, firewalls, DDoS protection"]), (6) backup and disaster recovery (backups [FREQUENCY], recovery point objective [HOURS], recovery time objective [HOURS], geographic redundancy [DETAILS]), (7) compliance (GDPR, HIPAA, SOC 2, etc. [CERTIFICATIONS]), (8) data location (data stored in [REGION(S)] only), (9) data deletion (upon termination, Client data deleted within [TIMEFRAME] or securely returned), (10) monitoring and alerts ([MONITORING_DETAILS]), (11) support ([SUPPORT_LEVEL: e.g., "24/7 phone support"]), (12) intellectual property (Provider retains IP in hosting platform), (13) limitation of liability ([CAP_AMOUNT]), (14) incident response and notification ([NOTIFICATION_TIMEFRAME]), and (15) termination ([TERMINATION_RIGHTS]). Include a Service Level Agreement schedule. Target length: 7-10 pages.

**Context:** Use for cloud infrastructure hosting (AWS, Azure, Google Cloud type arrangements). Essential for enterprises handling sensitive data or relying on high availability.

**Difficulty:** Advanced

**Follow-up:** PROMPT B6 (if you need to assess a SaaS vendor's data handling practices)

---

### PROMPT B6 — SAAS VENDOR DUE DILIGENCE QUESTIONNAIRE
Create a comprehensive due diligence questionnaire to evaluate [SAAS_VENDOR_NAME]'s suitability for our organization regarding [USAGE_CONTEXT: e.g., "storing customer data, financial information, healthcare records"]. The questionnaire should include sections on: (1) Company & Background (incorporation, years in business, ownership, key customers), (2) Product & Service (features, uptime history, roadmap, competitive advantages), (3) Data Security (encryption, penetration testing, vulnerability management, incident history), (4) Compliance & Certifications (GDPR, HIPAA, SOC 2, ISO 27001, CCPA, industry-specific certifications), (5) Data Handling & Privacy (data storage location, subprocessors, data retention, deletion processes, GDPR DPA status), (6) Backup & Disaster Recovery (backup frequency, recovery testing, RTO/RPO, geographic redundancy), (7) Support & Service Levels (uptime SLA, support tiers, response times, on-call availability), (8) Financial Stability (audited financials, funding, cash burn, customer concentration), (9) Contractual (liability caps, IP rights, change of control, bankruptcy scenarios), and (10) Other Risks (vendor lock-in, migration difficulty, price escalation history). Format as a table with columns: Question | Importance (Critical/High/Medium) | Vendor Response | Assessment | Follow-up. Include 30-40 targeted questions. Provide guidance on acceptable responses for each category.

**Context:** Use before committing to a new SaaS vendor, especially when storing sensitive, regulated, or business-critical data. Protects against vendor failures, security breaches, and lock-in.

**Difficulty:** Advanced

**Follow-up:** PROMPT C1 (if you need to negotiate a consulting services agreement)

---

## C. PROFESSIONAL SERVICES (5 prompts)

### PROMPT C1 — CONSULTING AGREEMENT DRAFT
Draft a Consulting Agreement between [CONSULTANT_NAME/FIRM] and [CLIENT_NAME] for [CONSULTING_SERVICES: e.g., "business strategy, market analysis, and board-level advisory"]. The agreement should include: (1) scope of services (detailed description of deliverables, frequency of services [FREQUENCY], and any exclusions [EXCLUSIONS]), (2) engagement term ([DURATION], starting [START_DATE]), (3) compensation ([RATE_STRUCTURE: e.g., "monthly retainer of $[AMOUNT] or hourly rate of $[RATE]"], payment terms [PAYMENT_TERMS]), (4) reimbursable expenses (categories and approval process [PROCESS]), (5) confidentiality (each party keeps confidential information secret; [DURATION]-year survival), (6) conflicts of interest (Consultant discloses any conflicts; Client consents to [SPECIFIED_CONFLICTS]), (7) intellectual property (Client owns deliverables and work product; Consultant retains IP in methodologies, tools, and pre-existing materials), (8) independent contractor status (Consultant is not an employee; no benefits; Consultant is responsible for taxes and insurance), (9) termination ([TERMINATION_RIGHTS], with [NOTICE] notice; fees due through end of notice period), (10) limitation of liability ([CAP_AMOUNT]), (11) insurance (Consultant maintains professional liability insurance), and (12) references (Client may reference Consultant with prior approval). Target length: 3-4 pages. Tone: [TONE: e.g., "Balanced but slightly favoring client"]. Include a SOW as Schedule A if applicable.

**Context:** Use for external consultants, advisors, and strategic experts. Common for business consulting, technical strategy, and interim executive roles.

**Difficulty:** Intermediate

**Follow-up:** PROMPT C2 (if you need a formal advisory board agreement)

---

### PROMPT C2 — ADVISORY BOARD AGREEMENT DRAFT
Draft an Advisory Board Member Agreement between [COMPANY_NAME] and [ADVISOR_NAME] for service on the Company's [BOARD_TYPE: e.g., "Technical Advisory Board / Scientific Advisory Board"]. The agreement should define: (1) role and responsibilities ([RESPONSIBILITIES_DETAIL: e.g., "quarterly meetings, strategic input on R&D priorities"]), (2) term ([DURATION], renewable by mutual consent), (3) time commitment ([HOURS_PER_MONTH] hours per month or [FREQUENCY]), (4) compensation ([COMPENSATION_STRUCTURE: e.g., "equity grant of [AMOUNT] shares vesting over [SCHEDULE]"]; or retainer fee [AMOUNT]), (5) confidentiality (strict confidentiality regarding Company information; [DURATION]-year survival post-termination), (6) IP assignment (Advisor agrees that IP created during service is Company IP, except [CARVE_OUTS]), (7) conflicts of interest (Advisor discloses conflicts; Advisor may not advise [RESTRICTED_PARTIES: e.g., "direct competitors"] without written consent), (8) non-disclosure of advisory relationship (Advisor may not publicly reference advisory role without approval except [EXCEPTIONS]), (9) indemnification (Company indemnifies Advisor for claims arising from advisory service), (10) director and officer liability insurance (Company includes Advisor in D&O policy if applicable), (11) independent contractor status (Advisor is not an employee), and (12) termination ([TERMINATION_TERMS]). Include a confidentiality schedule if needed. Target length: 3-4 pages.

**Context:** Use for external technical, scientific, or strategic advisors who provide expertise without formal employment. Common for biotech, deep tech, and hardware companies.

**Difficulty:** Intermediate

**Follow-up:** PROMPT C3 (if you need to outsource ongoing operations)

---

### PROMPT C3 — OUTSOURCING AGREEMENT DRAFT
Draft an Outsourcing Agreement between [CLIENT_COMPANY] and [SERVICE_PROVIDER] for outsourcing [BUSINESS_FUNCTIONS: e.g., "accounts payable processing, HR administration, IT support"]. The agreement should establish: (1) scope of services (detailed description of functions, current volume/baseline [BASELINE_METRICS], staffing levels [STAFFING_DETAILS]), (2) term ([DURATION], with renewal options and termination rights), (3) service levels (quality metrics [METRICS_DETAILS], response times [RESPONSE_TIMES], error rates [ERROR_THRESHOLDS], monitoring and reporting [REPORTING_FREQUENCY]), (4) transition (Provider assumes current operations by [TRANSITION_DATE]; provides [TRANSITION_SUPPORT: e.g., "120 days knowledge transfer"]), (5) pricing (monthly fee [AMOUNT]; volume adjustments [ADJUSTMENT_FORMULA]; inflation escalation [ESCALATION_RATE]), (6) key personnel (Provider assigns named key contacts; Client may request changes for performance issues), (7) data security and compliance ([SECURITY_MEASURES], GDPR/compliance requirements [REQUIREMENTS], audit rights [AUDIT_RIGHTS]), (8) intellectual property (Client retains all IP; Provider retains IP in processes/tools), (9) confidentiality (mutual confidentiality; [DURATION]-year survival), (10) liability and indemnity ([LIABILITY_CAP] for general claims; uncapped for IP infringement and data breaches), (11) termination for convenience (either party, [NOTICE] days notice; wind-down period [DURATION]), (12) transition assistance upon termination ([TRANSITION_DURATION] at [HOURLY_RATE] or fixed fee), and (13) business continuity ([BACKUP_PLANS]). Target length: 8-12 pages.

**Context:** Use for business process outsourcing (accounting, HR, customer service, IT) where ongoing operations are delegated to a third party. Requires detailed SLAs and transition planning.

**Difficulty:** Advanced

**Follow-up:** PROMPT C4 (if you need a simpler managed services arrangement)

---

### PROMPT C4 — MANAGED SERVICES AGREEMENT DRAFT
Draft a Managed Services Agreement between [MSP_NAME] and [CLIENT_NAME] for providing [SERVICES: e.g., "24/7 IT helpdesk, network monitoring, security management"]. The agreement should include: (1) services covered (detailed list of included services [SERVICE_LIST], excluded services [EXCLUSIONS], hours of operation [HOURS]), (2) service levels (average response time [RESPONSE_TIME], resolution time [RESOLUTION_TIME], uptime commitment [UPTIME_PERCENTAGE], credit for missed SLAs [CREDIT_STRUCTURE]), (3) term ([DURATION], auto-renew unless [NOTICE] days notice given), (4) pricing (monthly managed services fee [AMOUNT]; additional services [ADDITIONAL_PRICING]; travel/on-site [ON_SITE_RATES]), (5) staffing (named points of contact [POC_DETAILS]), (6) monitoring and access (Client grants access to systems for monitoring; access credentials [SECURITY_MEASURES]), (7) change management (major changes require [APPROVAL_PROCESS]), (8) security and compliance (GDPR, SOC 2, [SECURITY_STANDARDS]; regular security assessments [FREQUENCY]; vulnerability reporting [TIMELINE]), (9) intellectual property (Provider retains IP in tools, scripts, and methodologies), (10) confidentiality, (11) liability (capped at [MULTIPLIER] of monthly fees; uncapped for security breaches and IP infringement), (12) termination ([TERMINATION_RIGHTS], with [NOTICE] notice; knowledge transfer period [DURATION]), and (13) communication and escalation (weekly check-ins [CADENCE], escalation procedures [PROCEDURES]). Target length: 5-7 pages.

**Context:** Use for ongoing IT support, security monitoring, or helpdesk services where an MSP acts as an extension of your IT function.

**Difficulty:** Intermediate

**Follow-up:** PROMPT C5 (if you need a one-time project SOW)

---

### PROMPT C5 — STATEMENT OF WORK TEMPLATE
Create a detailed Statement of Work (SOW) template for [PROJECT_TYPE: e.g., "software development, consulting project, construction work"]. The SOW should serve as a Schedule A to a Master Services Agreement and include: (1) project overview (project name, brief description, business objectives [OBJECTIVES], success criteria [CRITERIA]), (2) scope of work (detailed deliverables with descriptions [DELIVERABLES], exclusions [EXCLUSIONS], assumptions [ASSUMPTIONS]), (3) timeline (project phases [PHASES] with start/end dates [DATES], key milestones [MILESTONES], critical path [PATH]), (4) deliverables and acceptance (detailed description of each deliverable [SPECIFICATIONS], delivery format/method [METHOD], acceptance criteria [ACCEPTANCE_CRITERIA], acceptance procedure [PROCEDURE]), (5) resource allocation (team composition [COMPOSITION], roles and responsibilities [ROLES], key personnel [PERSONNEL]), (6) governance (project manager [PM_DETAILS], status reports [FREQUENCY], meetings [FREQUENCY/ATTENDEES], escalation [ESCALATION]), (7) change management (scope change process [PROCESS], change order template, fee adjustments [ADJUSTMENT_PROCESS]), (8) testing and quality assurance ([QA_PROCESS], testing phases [PHASES], defect handling [PROCESS]), (9) pricing and payment (total project cost [AMOUNT], payment schedule [SCHEDULE], change order procedures [PROCEDURES]), (10) risks and contingency ([IDENTIFIED_RISKS] and mitigation plans [MITIGATION]), (11) transition and handover ([TRANSITION_PLAN], training [TRAINING_DETAILS], documentation [DOCUMENTATION]), and (12) term and termination (project duration [DURATION], termination for convenience [TERMS], survival clauses [SURVIVALS]). Provide sample language for each section and a template that can be customized. Target length: 6-10 pages.

**Context:** Use for any significant project requiring detailed planning, deliverables, and acceptance criteria. Serves as the operational contract under a broader MSA.

**Difficulty:** Intermediate

**Follow-up:** PROMPT D1 (if you need to define employment relationships)

---

## D. EMPLOYMENT AGREEMENTS (6 prompts)

### PROMPT D1 — EXECUTIVE EMPLOYMENT CONTRACT DRAFT
Draft an Executive Employment Agreement between [COMPANY_NAME] and [EXECUTIVE_NAME] for the position of [POSITION_TITLE: e.g., "Chief Financial Officer"]. The agreement should cover: (1) position and duties (title [TITLE], reporting to [REPORTS_TO], responsibilities [RESPONSIBILITIES]), (2) term ([DURATION] with [RENEWAL_TERMS] or at-will employment [AT_WILL_TERMS]), (3) base compensation (annual salary: $[SALARY], payable [FREQUENCY]), (4) bonus compensation (annual target bonus [PERCENTAGE]% of base, based on [PERFORMANCE_METRICS: e.g., "revenue, profitability, strategic objectives"]; discretionary [DISCRETION_LEVEL]), (5) equity ([EQUITY_GRANT]: [NUMBER] shares/options vesting over [SCHEDULE] with [ACCELERATION_TERMS]), (6) benefits (health insurance [COVERAGE_LEVEL], 401(k) [MATCH_DETAILS], life insurance [COVERAGE], disability insurance [COVERAGE], vacation [DAYS] days, executive perks [PERKS_DETAILS]), (7) severance ([SEVERANCE_AMOUNT]: [MULTIPLE] of base + bonus if terminated without cause; [ACCELERATION_TERMS] for equity; extended benefits [DURATION]), (8) change of control ([CHANGE_OF_CONTROL_PAYMENT]: [MULTIPLE] of base + target bonus, [ACCELERATION_TERMS]), (9) confidentiality and IP assignment (trade secrets, work product, and IP inventions are Company property), (10) non-compete ([SCOPE], [DURATION] post-termination, [GEOGRAPHIC_SCOPE]), (11) non-solicitation of employees ([SCOPE], [DURATION]), (12) non-solicitation of customers ([SCOPE], [DURATION]), (13) representations and warranties (Executive authority, background check results [RESULTS_TERMS]), (14) indemnification (Company indemnifies Executive for official acts), and (15) at-will employment clause if applicable. Target length: 6-10 pages. Include equity grant letter and confidentiality acknowledgment as schedules.

**Context:** Use for C-suite executives, VPs, and senior leaders. Include robust severance, equity, and change-of-control provisions. Common for startups and established companies.

**Difficulty:** Advanced

**Follow-up:** PROMPT D2 (if you need a simpler employee offer letter)

---

### PROMPT D2 — STANDARD EMPLOYMENT CONTRACT DRAFT
Draft a Standard Employment Agreement between [COMPANY_NAME] and [EMPLOYEE_NAME] for the position of [POSITION_TITLE: e.g., "Software Engineer, Senior"]. The agreement should establish: (1) position and duties (title, department, reporting relationship, job description [DESCRIPTION]), (2) employment term (at-will employment unless [TERM_DETAILS]), (3) compensation (annual salary: $[SALARY], payable [FREQUENCY]; overtime treatment [OT_TREATMENT]), (4) benefits (health insurance [ELIGIBILITY/COVERAGE], 401(k) [MATCH], vacation [DAYS] days, sick leave [DAYS] days, holidays [NUMBER], other benefits [BENEFITS]), (5) work schedule ([HOURS], location [LOCATION], remote work policy [POLICY]), (6) probationary period ([DURATION] if applicable), (7) performance reviews (annual reviews [FREQUENCY], performance expectations [EXPECTATIONS]), (8) confidentiality (trade secrets, customer lists, business information), (9) intellectual property assignment (work created within scope of employment or using Company resources belongs to Company; pre-existing IP disclosed by Employee remains Employee's), (10) non-compete ([SCOPE], [DURATION] if enforceable in [JURISDICTION]), (11) non-solicitation of customers ([SCOPE], [DURATION]), (12) compliance (laws, policies, ethics, harassment policies [POLICIES]), (13) at-will employment (either party may terminate at any time for any reason not prohibited by law, with [NOTICE] notice or pay in lieu), (14) grounds for immediate termination (gross misconduct [EXAMPLES], theft, violence, legal violations), (15) severance ([SEVERANCE_AMOUNT] weeks of pay; [SEVERANCE_CONDITIONS]), (16) references ([REFERENCE_TERMS]), and (17) miscellaneous (governing law, integration, dispute resolution [DISPUTE_RESOLUTION]). Target length: 4-6 pages.

**Context:** Use for non-executive employees (individual contributors, managers, specialists). Balances protection of Company IP and confidentiality with fairness to Employee.

**Difficulty:** Intermediate

**Follow-up:** PROMPT D3 (if you need to engage an independent contractor instead)

---

### PROMPT D3 — CONTRACTOR/FREELANCER AGREEMENT DRAFT
Draft a Contractor/Freelancer Agreement between [COMPANY_NAME] and [CONTRACTOR_NAME] for [SERVICES_DESCRIPTION: e.g., "graphic design, copywriting, technical writing, consulting"]. The agreement should include: (1) independent contractor status (Contractor is not an employee; no benefits; Contractor responsible for taxes, insurance, workers' comp), (2) scope of work (detailed services, deliverables [DELIVERABLES], timeline [TIMELINE]), (3) term ([DURATION], project-based [PROJECT_TERMS], or retainer [RETAINER_TERMS]), (4) compensation ([HOURLY_RATE] or [PROJECT_FEE] or [RETAINER_AMOUNT]), (5) payment terms (net [DAYS], invoicing requirements [REQUIREMENTS]), (6) intellectual property (Contractor assigns all IP in deliverables to Company; Contractor may retain pre-existing tools and methodologies), (7) confidentiality (Contractor keeps confidential information secret; [DURATION]-year survival), (8) independent judgment (Contractor has discretion on how to perform services; Company does not control day-to-day methods), (9) no exclusive relationship (Contractor may work for other clients), (10) compliance (Contractor complies with laws, including employment, tax, and IP laws), (11) insurance (Contractor maintains general liability insurance if applicable), (12) liability and indemnity (Contractor indemnifies Company for IP claims; liability capped at fees paid), (13) termination ([TERMINATION_TERMS], with [NOTICE] notice or payment), (14) return of materials (all Company materials and deliverables returned/destroyed upon termination), and (15) dispute resolution ([DISPUTE_MECHANISM]). Target length: 3-4 pages. Include a SOW as Schedule A if appropriate.

**Context:** Use for independent contractors, freelancers, and consultants. Critical to establish independent contractor status to avoid misclassification issues. Protects Company IP while respecting Contractor independence.

**Difficulty:** Intermediate

**Follow-up:** PROMPT D4 (if you need to transfer an employee to another company or location)

---

### PROMPT D4 — SECONDMENT AGREEMENT DRAFT
Draft a Secondment Agreement between [EMPLOYING_COMPANY], [RECEIVING_COMPANY], and [EMPLOYEE_NAME] for the temporary assignment of [EMPLOYEE_POSITION/ROLE]. The agreement should clarify: (1) parties (Employing Company, Receiving Company, and Employee), (2) purpose ([SECONDMENT_PURPOSE: e.g., "knowledge transfer, project support, joint venture"]), (3) term ([START_DATE] to [END_DATE], [DURATION]), (4) position and duties (role [ROLE], responsibilities [RESPONSIBILITIES], reporting relationship [REPORTING_TO]), (5) employment relationship (Employee remains employed by Employing Company; Receiving Company supervises day-to-day work), (6) compensation and benefits (Employing Company continues to pay salary and benefits; Receiving Company may reimburse [REIMBURSEMENT_TERMS]), (7) travel and relocation (Receiving Company covers travel and relocation costs [COST_ALLOCATION]), (8) insurance and liability (Employing Company maintains coverage; Receiving Company insures Employee against workplace injuries [INSURANCE_DETAILS]), (9) performance and discipline (Receiving Company provides performance feedback; Employing Company maintains employment decisions [DECISION_ALLOCATION]), (10) confidentiality and IP (Employing Company IP and confidential information treated as such; IP created during secondment belongs to [IP_OWNER]), (11) early termination ([CONDITIONS_FOR_EARLY_TERMINATION], notice required [NOTICE]), (12) return ([RETURN_LOGISTICS] at end of secondment), (13) post-secondment (Employee returns to Employing Company; no ongoing obligations to Receiving Company), and (14) dispute resolution ([MECHANISM]). Target length: 4-5 pages.

**Context:** Use for temporarily assigning employees to other companies (joint ventures, partnerships, customer engagements, startup incubators). Clarifies employment relationship and cost allocation.

**Difficulty:** Intermediate

**Follow-up:** PROMPT D5 (if you need non-compete/non-solicitation standalone agreements)

---

### PROMPT D5 — NON-COMPETE & NON-SOLICITATION STANDALONE
Draft a standalone Non-Compete and Non-Solicitation Agreement between [COMPANY_NAME] and [EMPLOYEE_NAME] (or [DEPARTING_EMPLOYEE_NAME]). The agreement should include: (1) non-compete (Employee agrees not to engage in competitive activities [COMPETITIVE_ACTIVITY_DEFINITION] within [GEOGRAPHIC_SCOPE] for [DURATION] post-employment [CONSIDERATION]; or [SPECIAL_TERMS] for [SPECIAL_CIRCUMSTANCES]), (2) scope of restriction (defined as [BUSINESS_SCOPE], excluding [EXCLUSIONS], limited to [LIMITATIONS]), (3) permitted activities (Employee may work for [PERMITTED_EMPLOYERS/INDUSTRIES] or perform [PERMITTED_ROLES]), (4) non-solicitation of employees (Employee agrees not to solicit, hire, or recruit Company employees or former employees for [DURATION], except [GENERAL_RECRUITMENT_EXCEPTIONS]), (5) non-solicitation of customers (Employee agrees not to solicit or service [CUSTOMER_DEFINITION: e.g., "customers Employee worked with in past 12 months"]] for [DURATION] after employment ends, except [EXCEPTIONS]), (6) non-disparagement (post-employment, Employee does not publicly disparage Company's reputation or business; [DURATION]), (7) confidentiality reminder (Employee remains bound by confidentiality obligations; trade secrets remain Company property), (8) notice and acknowledgment (Employee acknowledges receipt, understands restrictions, has opportunity to consult counsel), (9) consideration ([CONSIDERATION: e.g., "continued employment, promotion, bonus", "$[AMOUNT] cash payment"]), (10) legality and severability (if any restriction is unenforceable in [JURISDICTION], the remaining restrictions survive), (11) injunctive relief (acknowledging that monetary damages may be inadequate, and Company may seek injunctive relief), and (12) dispute resolution ([MECHANISM], governed by [JURISDICTION]). Target length: 3-4 pages. Include a schedule of restricted customers if applicable.

**Context:** Use when establishing or reinforcing non-compete/non-solicitation restrictions, especially upon departure or promotion. Enforcement varies significantly by jurisdiction; consult local counsel.

**Difficulty:** Advanced

**Follow-up:** PROMPT D6 (if you need to assign employee inventions)

---

### PROMPT D6 — EMPLOYEE INVENTION ASSIGNMENT
Draft an Employee Invention Assignment Agreement between [COMPANY_NAME] and [EMPLOYEE_NAME]. The agreement should establish: (1) scope of assignment (all inventions, discoveries, improvements, and intellectual property created by Employee [TIME_SCOPE: e.g., "during employment"] belong to Company if the invention: (a) is created using Company resources or (b) relates to Company's business or (c) is created during work hours or (d) is suggested by Company or a Company customer [ASSIGNMENT_CRITERIA], with exceptions [EXCEPTIONS]), (2) pre-existing IP (Employee may disclose pre-existing IP [SCHEDULE_A]; pre-existing IP remains Employee's property unless incorporated into Company IP), (3) assignment and cooperation (Employee assigns all rights, title, and interest in covered inventions to Company; Employee cooperates in obtaining patents, trademarks, copyrights [COOPERATION_TERMS]), (4) moral rights (to the extent permitted by law, Employee waives moral rights in Company IP), (5) confidentiality reminder (inventions remain confidential until Company decides to patent or protect), (6) disclosure procedure (Employee discloses inventions to [DISCLOSURE_PROCESS] within [TIMEFRAME]), (7) post-employment inventions ([POST_EMPLOYMENT_TERMS]: inventions created [DURATION] after employment ends using Company resources or relating to Company business may be Company IP), (8) employee benefits ([BENEFIT_STRUCTURE]: Employee receives [BENEFITS: e.g., "recognition, bonuses for patented inventions, equity"], if applicable), (9) legal compliance (complies with [JURISDICTION] law, including [SPECIFIC_LAWS: e.g., "California Labor Code § 2870"]), (10) notice of employee rights (acknowledgment that Employee understands legal rights in [JURISDICTION]), and (11) signature and date. Target length: 2-3 pages. Include as a schedule to the employment agreement or as a standalone agreement. Provide clear examples of covered vs. non-covered inventions.

**Context:** Use at hire or during employment to clarify Company ownership of employee inventions. Critical for tech companies, R&D organizations, and innovators. Enforceability varies by jurisdiction (particularly California).

**Difficulty:** Advanced

**Follow-up:** PROMPT E1 (if you need to create a distribution agreement with a third party)

---

## E. DISTRIBUTION & COMMERCIAL (5 prompts)

### PROMPT E1 — DISTRIBUTION AGREEMENT DRAFT
Draft a Distribution Agreement between [MANUFACTURER/SUPPLIER_NAME] and [DISTRIBUTOR_NAME] for distribution of [PRODUCTS: e.g., "industrial equipment, consumer goods, software"]. The agreement should include: (1) grant of rights (Supplier grants Distributor the right to buy and sell Products in [TERRITORY: e.g., "North America"] [EXCLUSIVITY: "exclusive" or "non-exclusive"]), (2) term ([DURATION], with automatic renewal unless [NOTICE] days notice given; renewal term [RENEWAL_DURATION]), (3) territory ([GEOGRAPHIC_SCOPE], permitted channels [CHANNELS], restrictions [RESTRICTIONS]), (4) products ([PRODUCT_DEFINITION], updates/revisions [UPDATE_TERMS], discontinued products [DISCONTINUATION_TERMS]), (5) ordering and inventory (ordering process [PROCESS], minimum purchase quantities [QUANTITIES], inventory management [INVENTORY_TERMS]), (6) pricing (Supplier's cost [PRICING_STRUCTURE], Distributor's margin [MARGIN_PERCENTAGE], price changes [CHANGE_TERMS], volume discounts [DISCOUNT_TIERS]), (7) payment terms (net [DAYS], payment method [METHOD], late payment penalties [PENALTIES]), (8) marketing and sales (Distributor's marketing obligations [OBLIGATIONS], approved advertising [APPROVAL_PROCESS], trade shows [PARTICIPATION_TERMS], customer support [SUPPORT_LEVEL]), (9) intellectual property (Supplier retains all IP; Distributor may use trademarks under [LICENSE_TERMS]), (10) confidentiality (mutual confidentiality), (11) returns and refunds ([RETURN_POLICY]: defective products [DEFECT_TERMS], restocking fees [FEES], expiration dates [EXPIRATION_TERMS]), (12) warranty (Products warranted by Supplier for [WARRANTY_PERIOD]; Distributor disclaims all other warranties), (13) liability (Supplier liable for defective products; Distributor liable for sales/customer claims), (14) compliance and regulatory (Distributor ensures compliance with [REGULATORY_REQUIREMENTS]), (15) termination (either party, [NOTICE] days notice; immediate termination for material breach; post-termination inventory wind-down [WIND_DOWN_TERMS]), and (16) dispute resolution ([MECHANISM], governed by [JURISDICTION]). Target length: 8-10 pages.

**Context:** Use for manufacturing/supply relationships where a distributor buys products and resells them. Common in consumer goods, industrial products, and technology distribution.

**Difficulty:** Advanced

**Follow-up:** PROMPT E2 (if you need an agency agreement for representation)

---

### PROMPT E2 — AGENCY AGREEMENT DRAFT
Draft an Agency Agreement between [PRINCIPAL_NAME] and [AGENT_NAME] for [AGENCY_PURPOSE: e.g., "sales representation, customer acquisition, business development"]. The agreement should cover: (1) appointment ([AGENT] appointed as [EXCLUSIVE/NON-EXCLUSIVE] agent of [PRINCIPAL] to [AGENCY_SCOPE: e.g., "solicit customers and take orders in [TERRITORY]"]), (2) term ([DURATION], automatic renewal unless [NOTICE] notice given), (3) agent's duties ([DUTIES_DETAIL: e.g., "solicit customers, provide customer support, report on market conditions"]), (4) principal's duties (provide [PRINCIPAL_SUPPORT: e.g., "marketing materials, product information, timely fulfillment"]), (5) territory ([GEOGRAPHIC_SCOPE], non-interference outside territory [TERMS]), (6) compensation (base compensation [AMOUNT/STRUCTURE] and/or commission [COMMISSION_RATE] on sales [SALES_BASIS]), (7) payment and reporting (commission paid [FREQUENCY]; Agent provides [REPORTING_FREQUENCY] sales reports [REPORT_FORMAT]), (8) expenses (Agent covers own expenses [COVERED_EXPENSES]; Principal reimburses [REIMBURSABLE_EXPENSES] if pre-approved [APPROVAL_PROCESS]), (9) independent contractor status (Agent is independent contractor; not Principal's employee; no benefits), (10) authority and representations (Agent acts only within [SCOPE_OF_AUTHORITY]; cannot bind Principal except [EXCEPTIONS]; represents authority and qualifications), (11) intellectual property and confidentiality (Agent uses Principal's IP only for agency purposes; maintains confidentiality), (12) warranty of services (Agent warrants compliance with law [LAWS], no breach of third-party rights [INDEMNITY_TERMS]), (13) liability and indemnity (Agent indemnifies Principal for damages arising from Agent's acts), (14) term and termination (either party may terminate at [NOTICE] days notice or for cause [CAUSE_DEFINITION]), (15) post-termination obligations (Agent ceases use of IP; returns materials; stops representing Principal; knowledge transfer [TERMS]), and (16) dispute resolution ([MECHANISM]). Target length: 5-7 pages.

**Context:** Use for sales representatives, business development agents, and independent contractors working to generate customers or leads. Agent has limited authority and is not an employee.

**Difficulty:** Intermediate

**Follow-up:** PROMPT E3 (if you need a franchise agreement)

---

### PROMPT E3 — FRANCHISE AGREEMENT DRAFT
Draft a Franchise Agreement between [FRANCHISOR_NAME] and [FRANCHISEE_NAME] for [FRANCHISE_CONCEPT: e.g., "quick-service restaurant, fitness studio, retail store"]. The agreement should establish: (1) grant ([FRANCHISOR] grants [FRANCHISEE] a non-exclusive franchise to operate a [FRANCHISE_NAME] business at [LOCATION] using [FRANCHISOR]'s system, trademark, and methods), (2) term ([INITIAL_TERM], with renewal options [RENEWAL_OPTIONS] if Franchisee meets performance standards), (3) franchisor's obligations (provide [FRANCHISOR_SUPPORT: e.g., "initial training, site selection assistance, ongoing support, marketing materials"]), (4) franchisee's obligations ([FRANCHISEE_OBLIGATIONS: e.g., "follow operating manual, maintain quality standards, submit to inspections, use approved suppliers"]), (5) franchise fee (initial franchisee fee: $[AMOUNT], including [FEES_INCLUDE: e.g., "training, supplies, initial inventory"], due [PAYMENT_TERMS]), (6) ongoing fees (royalty fee: [PERCENTAGE]% of gross revenues, paid [FREQUENCY]; marketing fund contribution: [PERCENTAGE]% of gross revenues or $[AMOUNT]; technology fees: $[AMOUNT] per [PERIOD]), (7) operating manual ([MANUAL_REQUIREMENTS]: confidential, provided to Franchisee, updated by Franchisor [UPDATE_FREQUENCY]), (8) location and site [LOCATION_APPROVAL]: Franchisee selects site subject to Franchisor approval; Franchisor may relocate [RELOCATION_TERMS]), (9) equipment and supplies (Franchisor-approved suppliers [APPROVED_SUPPLIERS], pricing [PRICING_TERMS]), (10) training ([TRAINING_DETAILS]: initial training [DURATION], ongoing training [FREQUENCY], certification [CERTIFICATION_TERMS]), (11) trademark and IP (Franchisor retains all IP; Franchisee licenses trademark [LICENSE_SCOPE], permitted use [PERMITTED_USE], quality control [QUALITY_TERMS]), (12) confidentiality ([CONFIDENTIALITY_SCOPE], [DURATION] survival), (13) insurance (Franchisee maintains [INSURANCE_TYPES] insurance, named as additional insured [COVERAGE_AMOUNTS]), (14) accounting and audit (Franchisee maintains books and records [RECORD_TERMS]; Franchisor may audit [AUDIT_FREQUENCY] [AUDIT_PROCESS]), (15) advertising and marketing (Franchisee uses [MARKETING_REQUIREMENTS], national/local advertising fund [FUND_DETAILS]), (16) competition and non-compete ([COMPETITION_RESTRICTIONS], duration [DURATION]), (17) termination ([TERMINATION_GROUNDS], with [NOTICE] notice; immediate termination for [IMMEDIATE_GROUNDS]), (18) post-termination ([POST_TERMINATION_OBLIGATIONS]: cease use of marks, remove signage, return materials, customer non-solicitation [TERMS]), and (19) dispute resolution ([MECHANISM], governed by [JURISDICTION]). Target length: 15-20 pages. Include operating manual, disclosure schedules, and FDD compliance schedules. Note: Franchise agreements are heavily regulated (FDD requirements, state laws); consult franchise counsel.

**Context:** Use for franchisors granting franchise rights to franchisees. Heavily regulated by FTC (Franchise Disclosure Document) and state franchise laws. Requires specialized counsel.

**Difficulty:** Advanced

**Follow-up:** PROMPT E4 (if you need a supply agreement)

---

### PROMPT E4 — SUPPLY AGREEMENT DRAFT
Draft a Supply Agreement between [SUPPLIER_NAME] and [BUYER_NAME] for the supply of [GOODS/MATERIALS: e.g., "raw materials, components, packaging, finished goods"]. The agreement should include: (1) products ([PRODUCT_DESCRIPTION], specifications [SPECIFICATIONS_REFERENCE], approved suppliers/sources [SOURCES]), (2) term ([DURATION], automatic renewal unless [NOTICE] notice given), (3) volume and ordering (estimated annual volume: [VOLUME], ordering procedures [PROCEDURES], lead time [LEAD_TIME], order minimums [MINIMUMS]), (4) pricing and payment (unit price: $[PRICE], pricing schedule [SCHEDULE_REFERENCE], volume discounts [DISCOUNTS], price adjustments [ADJUSTMENT_FORMULA], payment terms: net [DAYS]), (5) delivery ([DELIVERY_TERMS]: FOB [LOCATION], delivery schedule [SCHEDULE], risk of loss [RISK_ALLOCATION], shipping [SHIPPING_RESPONSIBILITY]), (6) quality control ([QC_STANDARDS], inspection rights [INSPECTION_PROCESS], defect remedies [REMEDIES], return procedures [RETURN_PROCEDURES]), (7) warranty (goods warranted to conform to [WARRANTY_SCOPE], free from defects [DEFECT_SCOPE], for [WARRANTY_PERIOD]), (8) insurance (Supplier insures goods [INSURANCE_COVERAGE] until delivery [DELIVERY_POINT]; Buyer insures upon receipt), (9) force majeure ([FORCE_MAJEURE_DEFINITION], notification [NOTIFICATION_TERMS], suspension of obligations [SUSPENSION_TERMS]), (10) confidentiality (mutual confidentiality regarding business terms and information), (11) compliance (goods comply with [LEGAL_REQUIREMENTS], documentation [DOCUMENTATION_REQUIREMENTS]), (12) intellectual property (Supplier retains IP in goods; Buyer uses only for own consumption/resale), (13) sustainability and ethics ([SUSTAINABILITY_REQUIREMENTS], labor standards [LABOR_STANDARDS], conflict minerals [CONFLICT_MINERALS]), (14) termination ([TERMINATION_RIGHTS], convenience termination with [NOTICE] notice, for cause [CAUSE_DEFINITION]), (15) liability and indemnity (Supplier indemnifies Buyer for defective goods; liability cap [CAP_TERMS]), and (16) dispute resolution ([MECHANISM]). Target length: 6-8 pages.

**Context:** Use for ongoing supply relationships where a supplier provides goods or materials to a buyer. Can be an annual requirements contract or a rolling order agreement.

**Difficulty:** Intermediate

**Follow-up:** PROMPT E5 (if you need a reseller agreement)

---

### PROMPT E5 — RESELLER AGREEMENT DRAFT
Draft a Reseller Agreement between [VENDOR_NAME] and [RESELLER_NAME] for [RESELLER_PRODUCTS: e.g., "software, hardware, cloud services, SaaS applications"]. The agreement should establish: (1) grant (Vendor grants Reseller the right to purchase Products from Vendor and resell to end customers in [TERRITORY] [EXCLUSIVITY_TERMS]), (2) products ([PRODUCT_LIST], pricing tiers [PRICING_TIERS], margin/pricing rights [MARGIN_DETAILS]), (3) term ([DURATION], with renewal options [RENEWAL_TERMS]), (4) ordering ([ORDER_PROCESS], minimum quantities [MINIMUMS], volume commitments [COMMITMENTS]), (5) pricing (Vendor's list price [PRICING], Reseller's cost [COST_STRUCTURE], Reseller's margin [MARGIN_PERCENTAGE], volume discounts [DISCOUNTS]), (6) payment ([PAYMENT_TERMS], net [DAYS], payment method [METHOD]), (7) support and services (Vendor provides [VENDOR_SUPPORT]: technical support [SUPPORT_LEVEL], documentation [DOCUMENTATION], training [TRAINING_TERMS]; Reseller provides [RESELLER_SUPPORT]: first-line support [SUPPORT_DETAILS], customer relationship [RELATIONSHIP_TERMS]), (8) marketing ([MARKETING_OBLIGATIONS]: Reseller promotes Products [PROMOTION_DETAILS], uses [BRAND_GUIDELINES], co-marketing [COMARKETING_TERMS], lead sharing [LEAD_TERMS]), (9) intellectual property and use (Reseller may use Vendor IP for [PERMITTED_USE]: marketing, customer communications; uses only [APPROVED_MATERIALS]; Vendor retains ownership; quality control [QC_TERMS]), (10) compliance ([COMPLIANCE_OBLIGATIONS]: laws, export controls, licensing terms, restrictions [RESTRICTIONS: e.g., "no sales to [PROHIBITED_PARTIES]"]), (11) customer support and SLAs (Reseller provides [RESELLER_SLA]: [SLA_DETAILS], escalation to Vendor [ESCALATION_TERMS]), (12) confidentiality (mutual; [DURATION]-year survival), (13) liability and indemnity (Reseller indemnifies Vendor for customer claims; each party indemnifies for IP infringement; liability caps [CAP_DETAILS]), (14) warranty ([WARRANTY_SCOPE]: Reseller warrants right to resell, authority, compliance), (15) termination (either party, [NOTICE] days notice; for cause [CAUSE_DEFINITION]; immediate for material breach), (16) transition post-termination (customer hand-off [PROCESS], inventory return [PROCESS], non-solicitation [TERMS]), and (17) dispute resolution ([MECHANISM]). Target length: 8-10 pages.

**Context:** Use for software, SaaS, and technology resellers who purchase from a vendor and resell to end-customers. Common in partner channel models.

**Difficulty:** Intermediate

**Follow-up:** PROMPT F1 (if you need to establish a joint venture)

---

## F. JOINT VENTURES & PARTNERSHIPS (5 prompts)

### PROMPT F1 — JOINT VENTURE AGREEMENT DRAFT
Draft a Joint Venture Agreement between [PARTY_A_NAME] and [PARTY_B_NAME] (and [PARTY_C_NAME] if applicable) to establish [JV_NAME] for [JV_PURPOSE: e.g., "developing and commercializing [PRODUCT/SERVICE]"]. The agreement should include: (1) formation ([JV_ENTITY]: [ENTITY_TYPE: e.g., "LLC, corporation"], organized in [JURISDICTION], managed by [MANAGEMENT_STRUCTURE]), (2) ownership ([PARTY_A] owns [PERCENTAGE_A]%, [PARTY_B] owns [PERCENTAGE_B]%, corresponding to capital contributions [CONTRIBUTIONS]), (3) contributions ([PARTY_A] contributes [CONTRIBUTION_A: e.g., "technology, IP, $[AMOUNT]"]; [PARTY_B] contributes [CONTRIBUTION_B]; schedule [CONTRIBUTION_SCHEDULE]), (4) governance (governing board [COMPOSITION], voting rights [VOTING_ALLOCATION], deadlock resolution [DEADLOCK_MECHANISM]), (5) management ([MANAGEMENT_DETAILS]: CEO [SELECTION_PROCESS], day-to-day operations [RESPONSIBILITY], budget [BUDGET_APPROVAL]), (6) capital calls (additional capital required [MECHANISM], pro-rata contributions [CONTRIBUTION_TERMS], failure to fund [CONSEQUENCES: e.g., "dilution"]), (7) business plan and budget (annual business plan approved [APPROVAL_PROCESS], annual budget [BUDGET_DETAILS]), (8) intellectual property ([IP_OWNERSHIP]: background IP owned by contributing party [BACKGROUND_IP_TERMS]; foreground IP (created by JV) owned by [JV_OWNERSHIP], licensed to parties [LICENSE_TERMS]), (9) profits and losses (allocated [ALLOCATION_FORMULA], distributed [DISTRIBUTION_FREQUENCY], retained earnings [RETENTION_POLICY]), (10) confidentiality ([CONFIDENTIALITY_SCOPE], [DURATION] survival), (11) non-compete ([COMPETITION_RESTRICTIONS] by parties [RESTRICTIONS_SCOPE], [DURATION]), (12) accounting and audit ([ACCOUNTING_STANDARDS], annual audit [AUDIT_REQUIREMENTS], financial reporting [REPORTING_FREQUENCY]), (13) transfer of interests (interests not transferable without [CONSENT_REQUIREMENT]: unanimous consent [TRANSFER_RESTRICTIONS], right of first refusal [ROFR_TERMS]), (14) exit scenarios ([EXIT_EVENTS]: sale of JV [SALE_TERMS], IPO [IPO_TERMS], one party's exit [EXIT_TERMS], buyout [BUYOUT_TERMS]), (15) dispute resolution ([DISPUTE_MECHANISM]: mediation [MEDIATION_TERMS], arbitration [ARBITRATION_TERMS]), and (16) termination ([TERMINATION_GROUNDS], wind-down procedures [WIND_DOWN_TERMS], asset distribution [DISTRIBUTION_FORMULA]). Target length: 10-15 pages. Include contribution schedule, business plan, and governance schedule as exhibits.

**Context:** Use when two or more parties form a new entity to pursue a specific venture. Critical for startups with co-founders, strategic partnerships between large companies, and emerging market ventures.

**Difficulty:** Advanced

**Follow-up:** PROMPT F2 (if you need to establish shareholders' rights in the JV)

---

### PROMPT F2 — SHAREHOLDERS' AGREEMENT FOR JV DRAFT
Draft a Shareholders' Agreement between the shareholders of [JV_ENTITY_NAME] ([SHAREHOLDER_1_NAME], [SHAREHOLDER_2_NAME], [SHAREHOLDER_3_NAME]) governing ownership and management of the [JV_ENTITY]. The agreement should establish: (1) share ownership ([SHAREHOLDER_1] owns [SHARES_1] shares ([PERCENTAGE_1]%); [SHAREHOLDER_2] owns [SHARES_2] shares ([PERCENTAGE_2]%); [SHAREHOLDER_3] owns [SHARES_3] shares ([PERCENTAGE_3]%)), (2) voting and governance (board composition [BOARD_COMPOSITION], director appointment [APPOINTMENT_PROCESS], voting rights [VOTING_STRUCTURE], class voting [CLASS_VOTING_TERMS]), (3) shareholder meetings (annual meetings [FREQUENCY], notice [NOTICE_TERMS], quorum [QUORUM], voting [VOTING_PROCEDURES]), (4) management ([MANAGEMENT_RIGHTS]: CEO selection [SELECTION_PROCESS], executive committee [COMMITTEE_DETAILS], reservation of matters [RESERVED_MATTERS: e.g., "major transactions, amendments, dissolution"]), (5) drag-along rights ([DRAG_RIGHTS]: if [DRAG_TRIGGERING_EVENT: e.g., "holders of [PERCENTAGE]% approve"], minority shareholders must sell shares on same terms [DRAG_TERMS]), (6) tag-along rights ([TAG_RIGHTS]: if controlling shareholder sells, minority shareholders may sell pro-rata shares on same terms [TAG_TERMS]), (7) anti-dilution ([ANTI_DILUTION_PROTECTION]: weighted average [METHODOLOGY], broad-based [SCOPE]), (8) preemptive rights ([PREEMPTIVE_RIGHTS]: shareholders have right of first refusal [ROFR_TERMS] on new share issuances [ISSUANCE_SCOPE] within [TIMEFRAME]), (9) redemption and buyback ([BUYBACK_RIGHTS]: [BUYBACK_TRIGGERS], pricing [PRICING_FORMULA], mechanics [MECHANICS]), (10) put and call options ([PUT_OPTION]: minority may force buyout [PUT_TRIGGERS], [PRICING]; [CALL_OPTION]: majority may force sale [CALL_TRIGGERS], [PRICING]), (11) transfer restrictions (shares not freely transferable; transfer requires [CONSENT_REQUIREMENT], subject to [ROFR_TERMS], [TAG_ALONG_TERMS]), (12) deadlock resolution ([DEADLOCK_MECHANISM]: if shareholders deadlocked [DEADLOCK_DEFINITION], [DISPUTE_RESOLUTION_PROCESS]), (13) registration rights ([REGISTRATION_RIGHTS]: demand rights [DEMAND_TERMS], piggyback rights [PIGGYBACK_TERMS]), (14) confidentiality (mutual; [DURATION] survival), (15) dispute resolution ([DISPUTE_MECHANISM]: arbitration [ARBITRATION_TERMS]), and (16) amendment ([AMENDMENT_PROCESS]: unanimous consent, [EXCEPTIONS]). Target length: 8-12 pages.

**Context:** Use for managing multiple shareholders in a closely-held company, especially joint ventures or partnerships with unequal ownership. Protects minority and majority interests.

**Difficulty:** Advanced

**Follow-up:** PROMPT F3 (if you prefer a partnership agreement structure)

---

### PROMPT F3 — PARTNERSHIP AGREEMENT DRAFT
Draft a Partnership Agreement between [PARTNER_1_NAME] and [PARTNER_2_NAME] (and [PARTNER_3_NAME] if applicable) to form [PARTNERSHIP_NAME], a [PARTNERSHIP_TYPE: e.g., "general partnership, limited partnership"]. The agreement should cover: (1) partnership formation (name [NAME], principal place of business [ADDRESS], jurisdiction [JURISDICTION], partners and their roles [PARTNER_ROLES]), (2) capital contributions ([PARTNER_1] contributes [CONTRIBUTION_1]; [PARTNER_2] contributes [CONTRIBUTION_2]; schedule [SCHEDULE], timing [TIMING]), (3) ownership and profit/loss ([PARTNER_1] owns [PERCENTAGE_1]% and receives [PERCENTAGE_1]% of profits/losses; [PARTNER_2] owns [PERCENTAGE_2]% and receives [PERCENTAGE_2]% of profits/losses), (4) management and voting (each general partner has equal management rights [MANAGEMENT_RIGHTS]; limited partners have no management rights; major decisions require [VOTING_REQUIREMENT]: unanimous, majority, or [SPECIFIED_THRESHOLD]), (5) compensation (salary to partners [SALARY_SCHEDULE], bonuses [BONUS_TERMS], distributions [DISTRIBUTION_FREQUENCY]), (6) capital calls (additional capital may be called [CALL_MECHANISM], pro-rata contributions [CONTRIBUTION_TERMS]), (7) draws (partners may draw funds [DRAW_TERMS], limited to [DRAW_LIMITS]), (8) personal assets (partners may loan money to partnership [LOAN_TERMS], personally liable [LIABILITY_SCOPE] for partnership debts [PERSONAL_LIABILITY_SCOPE]), (9) admission of new partners ([ADMISSION_PROCESS], unanimity requirement [CONSENT_TERMS]), (10) transfer of interests (interests not transferable without unanimous consent [TRANSFER_RESTRICTIONS], buyout terms [BUYOUT_TERMS], successor liability [LIABILITY_TERMS]), (11) dispute resolution ([DISPUTE_MECHANISM]: mediation [MEDIATION_TERMS], arbitration [ARBITRATION_TERMS]), (12) exit ([EXIT_MECHANISM]: retirement [RETIREMENT_TERMS], buyout [BUYOUT_MECHANISM], payments [PAYMENT_TERMS]), (13) dissolution ([DISSOLUTION_TRIGGERS], wind-down [WIND_DOWN_PROCEDURE], asset distribution [DISTRIBUTION_FORMULA]), (14) confidentiality (mutual; [DURATION] survival), and (15) non-compete ([COMPETITION_RESTRICTIONS], [DURATION]). Include a capital contribution schedule. Target length: 6-8 pages.

**Context:** Use for general and limited partnerships. Clarifies member roles, profit/loss allocation, management rights, and exit mechanisms. Important for protecting personal assets and managing partner relationships.

**Difficulty:** Intermediate

**Follow-up:** PROMPT F4 (if you need consortium agreement language)

---

### PROMPT F4 — CONSORTIUM AGREEMENT DRAFT
Draft a Consortium Agreement between [CONSORTIUM_MEMBER_1], [CONSORTIUM_MEMBER_2], [CONSORTIUM_MEMBER_3], and [CONSORTIUM_MEMBER_4] to jointly pursue [CONSORTIUM_OBJECTIVE: e.g., "bidding on a government contract, developing a technology standard, operating an airport"]. The agreement should establish: (1) purpose ([OBJECTIVE_DETAIL], deliverables [DELIVERABLES]), (2) governance ([STEERING_COMMITTEE_COMPOSITION], decision-making [DECISION_PROCESS], voting rights [VOTING_STRUCTURE]), (3) roles and responsibilities ([MEMBER_1] responsible for [RESPONSIBILITY_1]; [MEMBER_2] responsible for [RESPONSIBILITY_2]; etc.), (4) financial contributions ([MEMBER_1] contributes [AMOUNT_1]; [MEMBER_2] contributes [AMOUNT_2]; schedule [PAYMENT_SCHEDULE]; cost sharing [COST_ALLOCATION_FORMULA]), (5) profit/cost allocation ([PROFIT_SHARE]: [MEMBER_1] receives [PERCENTAGE_1]%, [MEMBER_2] receives [PERCENTAGE_2]%; or allocation based on [ALLOCATION_MECHANISM]), (6) lead member ([LEAD_MEMBER_NAME], authority [AUTHORITY_SCOPE], duties [DUTIES]), (7) employment and staffing (staffing plan [STAFFING_PLAN], dedicated personnel [DEDICATED_TERMS], management [MANAGEMENT_STRUCTURE]), (8) intellectual property ([IP_OWNERSHIP]: collectively owned IP [JOINT_IP_OWNERSHIP_TERMS], background IP [BACKGROUND_IP_OWNERSHIP], licensing to members [LICENSE_TERMS]), (9) liability and indemnity (each member liable for own acts [LIABILITY_SCOPE]; consortium liable to third parties [LIABILITY_ALLOCATION]; indemnification [INDEMNITY_STRUCTURE]), (10) termination ([TERMINATION_TERMS]: completion [COMPLETION_TERMS], exit of member [EXIT_TERMS], wind-down [WIND_DOWN_TERMS]), (11) confidentiality (members maintain confidentiality [CONFIDENTIALITY_SCOPE], [DURATION]), (12) non-compete ([COMPETITION_RESTRICTIONS] by members, [DURATION]), (13) dispute resolution ([DISPUTE_MECHANISM]: escalation [ESCALATION_PROCESS], mediation [MEDIATION_TERMS], arbitration [ARBITRATION_TERMS]), and (14) amendments ([AMENDMENT_PROCESS]). Target length: 8-10 pages. Include detailed governance schedule and financial allocation schedule.

**Context:** Use for multi-party collaborations on specific objectives (government contracts, industry standards, joint operations). Balances individual member interests with consortium goals.

**Difficulty:** Advanced

**Follow-up:** PROMPT F5 (if you need to establish co-development arrangements)

---

### PROMPT F5 — CO-DEVELOPMENT AGREEMENT DRAFT
Draft a Co-Development Agreement between [PARTY_A_NAME] and [PARTY_B_NAME] for jointly developing [PROJECT_NAME/TECHNOLOGY: e.g., "a new software product, medical device, biotechnology"]. The agreement should include: (1) objective ([DEVELOPMENT_OBJECTIVE], expected outcomes [OUTCOMES], timeline [TIMELINE]), (2) governance (steering committee [COMMITTEE_COMPOSITION], decision-making [DECISION_PROCESS], dispute resolution [DISPUTE_MECHANISM]), (3) roles and responsibilities ([PARTY_A] responsible for [PARTY_A_RESPONSIBILITIES: e.g., "R&D, prototyping, testing"]; [PARTY_B] responsible for [PARTY_B_RESPONSIBILITIES: e.g., "commercialization, market research, regulatory"]), (4) contributions ([PARTY_A] contributes [CONTRIBUTION_A: e.g., "personnel, $[AMOUNT], facilities"]; [PARTY_B] contributes [CONTRIBUTION_B: e.g., "personnel, $[AMOUNT], regulatory expertise"]), (5) funding ([PARTY_A] funds [FUNDING_A]; [PARTY_B] funds [FUNDING_B]; or shared funding [FUNDING_FORMULA]), (6) intellectual property ([IP_OWNERSHIP]: foreground IP (created during project) jointly owned [JOINT_IP_TERMS]; background IP owned by contributing party [BACKGROUND_IP_TERMS]; licenses to each other [LICENSE_TERMS]; access to source code [ACCESS_TERMS]; third-party IP [THIRD_PARTY_HANDLING]), (7) development schedule (phases [PHASES], milestones [MILESTONES], deliverables [DELIVERABLES], acceptance criteria [ACCEPTANCE_CRITERIA]), (8) quality standards ([QUALITY_STANDARDS], testing [TESTING_REQUIREMENTS], compliance [COMPLIANCE_REQUIREMENTS]), (9) confidentiality (mutual confidentiality; [DURATION] survival), (10) publication and disclosure ([PUBLICATION_RIGHTS]: publications require [APPROVAL_PROCESS], review period [REVIEW_PERIOD], restrictions on disclosures [RESTRICTIONS]), (11) commercialization ([COMMERCIALIZATION_RIGHTS]: [PARTY_A] has right to commercialize [COMMERCIAL_SCOPE]; [PARTY_B] has right to commercialize [COMMERCIAL_SCOPE]; exclusive or non-exclusive [EXCLUSIVITY]), (12) warranty ([WARRANTY_SCOPE]: each party warrants IP ownership, non-infringement [INDEMNITY_TERMS]), (13) liability and indemnity (each party indemnifies the other for IP claims; liability caps [CAP_TERMS]), (14) data and materials ([DATA_OWNERSHIP], [MATERIALS_OWNERSHIP], return/destruction [RETURN_TERMS]), (15) termination ([TERMINATION_TERMS]), and (16) post-termination ([POST_TERMINATION_OBLIGATIONS]: continuation of commercialization [CONTINUATION_TERMS], wind-down [WIND_DOWN_TERMS]). Target length: 10-12 pages.

**Context:** Use for R&D partnerships, joint product development, and technology collaborations where multiple parties contribute and share in commercialization. Critical for IP allocation and development management.

**Difficulty:** Advanced

**Follow-up:** PROMPT G1 (if you need to license IP)

---

## G. LICENSING (5 prompts)

### PROMPT G1 — IP LICENCE AGREEMENT DRAFT
Draft an Intellectual Property License Agreement between [LICENSOR_NAME] and [LICENSEE_NAME] for [LICENSE_SCOPE: e.g., "a non-exclusive license to use certain patent, trademark, and know-how"]. The agreement should establish: (1) licensed IP ([IP_DESCRIPTION]: patents [PATENTS_DETAIL], trademarks [TRADEMARK_DETAIL], know-how [KNOW_HOW_DETAIL], copyrights [COPYRIGHT_DETAIL]), (2) license grant (Licensor grants Licensee a [EXCLUSIVITY: "exclusive/non-exclusive"] license to [PERMITTED_USE: e.g., "make, use, sell products incorporating the licensed technology"]) in [TERRITORY: e.g., "North America"]), (3) sublicense rights ([SUBLICENSE_RESTRICTION]: Licensee may/may not sublicense to third parties [SUBLICENSE_TERMS]), (4) duration ([TERM_LENGTH], with renewal options [RENEWAL_TERMS], termination rights [TERMINATION_RIGHTS]), (5) royalties ([ROYALTY_RATE: e.g., "3% of net sales"] of [SALES_BASIS], minimum royalties [MINIMUM_ROYALTY], upfront payment [UPFRONT_PAYMENT], milestone payments [MILESTONES]), (6) payment terms (net [DAYS], quarterly reporting [REPORTING_FREQUENCY], audit rights [AUDIT_TERMS]), (7) improvements and modifications ([IMPROVEMENT_OWNERSHIP]: improvements made by Licensee belong to [IMPROVEMENT_OWNER], licensed back to other party [FEEDBACK_LICENSE_TERMS]), (8) warranty (Licensor warrants that it owns IP free and clear [WARRANTY_SCOPE], and that licensed IP does not infringe third-party rights [INDEMNITY_TERMS]), (9) no implied license (no license to Licensor's other IP [EXCLUSION_SCOPE]), (10) restrictions ([FIELD_OF_USE_RESTRICTION]: Licensee may use licensed IP only for [PERMITTED_FIELD]), ([TERRITORY_RESTRICTION]: Licensee may sell only in [TERRITORY]), ([COMPETITION_RESTRICTION]: Licensee may not use for competitive products [RESTRICTION_SCOPE]), (11) quality control (Licensor may inspect Licensee's quality [INSPECTION_PROCESS]; Licensor approves [APPROVAL_ITEMS]), (12) confidentiality (mutual confidentiality; [DURATION] survival), (13) indemnity (Licensee indemnifies Licensor for claims arising from Licensee's use), (14) liability and limitation (liability capped at [CAP_AMOUNT]), (15) infringement claims (procedure for handling third-party claims [CLAIM_PROCEDURE]), (16) termination ([TERMINATION_TRIGGERS], wind-down [WIND_DOWN_TERMS], post-termination use [POST_USE_TERMS]), and (17) governing law ([JURISDICTION]). Target length: 8-10 pages.

**Context:** Use for licensing patents, trademarks, copyrights, or proprietary technology. Can be exclusive or non-exclusive, and may include field-of-use or territorial restrictions.

**Difficulty:** Advanced

**Follow-up:** PROMPT G2 (if you need a brand license specifically)

---

### PROMPT G2 — BRAND LICENSING AGREEMENT DRAFT
Draft a Brand License Agreement (trademark license) between [LICENSOR_NAME] and [LICENSEE_NAME] for use of [BRAND_NAME] and [LICENSOR]'s brand assets. The agreement should cover: (1) license grant (Licensor grants Licensee a [EXCLUSIVITY: "exclusive/non-exclusive"] license to use [BRAND_ELEMENTS: e.g., "logo, wordmark, packaging design"]) on [LICENSED_PRODUCTS: e.g., "consumer goods, apparel"]), (2) territory ([GEOGRAPHIC_SCOPE], distribution channels [CHANNELS_SCOPE]), (3) duration ([TERM_LENGTH], renewal options [RENEWAL_TERMS], automatic renewal [AUTO_RENEWAL_TERMS]), (4) quality control (Licensor has right to inspect [INSPECTION_SCOPE], approve packaging [APPROVAL_ITEMS], marketing materials [MARKETING_APPROVAL]), (5) brand guidelines (Licensee must comply with Licensor's brand guidelines [GUIDELINES_REFERENCE], as updated [UPDATE_PROCESS]), (6) sublicense ([SUBLICENSE_RESTRICTION]: Licensee may/may not sublicense; Licensor approval required [APPROVAL_TERMS]), (7) royalties ([ROYALTY_RATE] of [SALES_BASIS], paid [PAYMENT_FREQUENCY]), (8) upfront payment ([UPFRONT_AMOUNT]), (9) minimum sales ([MINIMUM_SALES_TARGETS], targets [TARGET_SCHEDULE], failure consequences [CONSEQUENCE_TERMS]), (10) advertising and promotion (Licensee uses only approved advertising [ADVERTISING_APPROVAL_TERMS], minimum promotional spend [MINIMUM_SPEND]), (11) IP ownership (Licensor retains all rights in brand and trademark; Licensee has no ownership or rights [OWNERSHIP_CLARITY]), (12) licensed materials (Licensor provides [MATERIALS_PROVIDED]: logo files, brand guidelines, samples), (13) warranty ([WARRANTY_SCOPE]: Licensor warrants ownership and right to license), (14) non-infringement ([LICENSEE_WARRANTY]: Licensee's products do not infringe third-party rights [INDEMNITY_TERMS]), (15) confidentality and non-disclosure (Licensee does not disclose brand strategy or marketing plans [CONFIDENTIALITY_SCOPE]), (16) termination ([TERMINATION_RIGHTS], immediate termination for [CAUSE_DEFINITION]), (17) post-termination ([POST_TERMINATION_OBLIGATIONS]: cease use, destroy materials, sell inventory [SELL_TERMS]), and (18) dispute resolution ([MECHANISM]). Target length: 6-8 pages.

**Context:** Use for trademark/brand licensing where a third party uses your brand on their products or services. Essential for protecting brand quality and reputation.

**Difficulty:** Intermediate

**Follow-up:** PROMPT G3 (if you need a music or content license)

---

### PROMPT G3 — MUSIC/CONTENT LICENSING AGREEMENT DRAFT
Draft a Music or Content License Agreement between [CONTENT_OWNER_NAME] (the rights holder) and [LICENSEE_NAME] for use of [WORK_DESCRIPTION: e.g., "the song '[SONG_TITLE]' by [ARTIST], the film '[FILM_TITLE]', the photograph '[PHOTO_DESCRIPTION]'"]. The agreement should include: (1) license grant (Owner grants Licensee a [EXCLUSIVE/NON_EXCLUSIVE] license to use the Work [USE_SCOPE: e.g., "synchronize with video, distribute on streaming platforms, publicly perform"]) in [TERRITORY], (2) rights granted ([SPECIFIC_RIGHTS]: reproduction rights [REPRODUCTION_SCOPE], distribution rights [DISTRIBUTION_SCOPE], public performance rights [PUBLIC_PERFORMANCE_SCOPE], synchronization rights [SYNC_SCOPE], derivative works rights [DERIVATIVE_SCOPE], display rights [DISPLAY_SCOPE]), (3) restrictions ([RESTRICTIONS_LIST]: non-transferable [TRANSFERABILITY], no sublicense [SUBLICENSE_SCOPE], [USE_RESTRICTIONS]), (4) term ([DURATION], [EFFECTIVE_DATE] to [END_DATE]), (5) territory ([GEOGRAPHIC_SCOPE], [DISTRIBUTION_CHANNELS]), (6) consideration/royalties ([UPFRONT_PAYMENT], [ROYALTY_RATE] of [SALES_BASIS: e.g., "gross revenues from sales/streaming"]], minimum royalties [MINIMUM], reporting [REPORTING_FREQUENCY]), (7) payment terms (net [DAYS], quarterly/annually [PAYMENT_FREQUENCY]), (8) delivery of Work (Owner provides Work in [FORMAT], licensed materials [DELIVERY_DETAILS]), (9) attribution and credits (Licensee provides credits [CREDIT_LOCATION], in form [CREDIT_FORM]), (10) warranty ([WARRANTY_SCOPE]: Owner owns Work free and clear [OWNERSHIP_WARRANTY], right to license [LICENSE_WARRANTY], non-infringement [INDEMNITY_TERMS]), (11) representations ([REPRESENTATIONS_LIST]: work is original, no conflicts), (12) indemnity (Licensee indemnifies Owner for claims related to Licensee's use), (13) liability (liability capped at [CAP_AMOUNT]), (14) confidentiality (mutual), (15) audit rights (Owner may audit Licensee's sales/usage [AUDIT_FREQUENCY]), (16) termination ([TERMINATION_RIGHTS]), (17) post-termination ([POST_TERMINATION_OBLIGATIONS]: cease new use, wind-down existing [WIND_DOWN_TERMS]), and (18) applicable rights ([APPLICABLE_LAWS]: PRO licenses [PRO_TERMS], mechanical licenses [MECHANICAL_LICENSE_TERMS], right-holder permissions [RH_PERMISSIONS]). Target length: 6-8 pages. Note: Music licensing often involves multiple rights holders (composer, publisher, performer, label); coordinate all required permissions.

**Context:** Use for music, film, photography, literature, and other copyrighted content. May require coordination with multiple rights holders. PRO licenses and mechanical licenses may be required separately.

**Difficulty:** Advanced

**Follow-up:** PROMPT G4 (if you need a patent license specifically)

---

### PROMPT G4 — PATENT LICENCE AGREEMENT DRAFT
Draft a Patent License Agreement between [LICENSOR_NAME] and [LICENSEE_NAME] for use of [PATENT_DESCRIPTION: e.g., "U.S. Patent No. [PATENT_NO], titled '[PATENT_TITLE]', and related patents"]. The agreement should cover: (1) patent information (patents licensed [PATENT_LIST], including continuations [CONTINUATION_SCOPE], improvements [IMPROVEMENT_SCOPE]), (2) license grant (Licensor grants Licensee a [EXCLUSIVITY: "exclusive/non-exclusive"] license to [PERMITTED_USE: e.g., "make, use, offer for sale, sell, and import products incorporating the licensed patent"]) in [TERRITORY] [FIELD_OF_USE], (3) sublicense ([SUBLICENSE_PERMISSION]: Licensee may/may not sublicense [SUBLICENSE_TERMS]), (4) duration ([TERM_LENGTH], continuation through [PATENT_EXPIRY], renewal options [RENEWAL_TERMS]), (5) royalties ([ROYALTY_RATE] of [SALES_BASIS], payable [PAYMENT_FREQUENCY], minimum royalties [MINIMUM_ROYALTY], diligence milestones [DILIGENCE_MILESTONES]), (6) upfront and milestone payments (upfront license fee [UPFRONT_AMOUNT], milestone payments [MILESTONES]), (7) patent prosecution ([PATENT_PROSECUTION_RESPONSIBILITY]: Licensor prosecutes patents [PROSECUTION_TERMS], Licensee reimburses [REIMBURSEMENT_TERMS]; patent maintenance [MAINTENANCE_TERMS]), (8) enforcement (Licensor has first right to enforce patents [ENFORCEMENT_PRIORITY], at Licensor's expense [EXPENSE_ALLOCATION]; Licensee may join [ENFORCEMENT_PARTICIPATION_TERMS]), (9) no warranty (Licensor does not warrant patent validity [VALIDITY_DISCLAIMER], non-infringement of third-party rights [INFRINGEMENT_DISCLAIMER]), (10) improvements ([IMPROVEMENT_OWNERSHIP]: improvements made by Licensee belong to [IMPROVEMENT_OWNER], with license back to Licensor [LICENSE_BACK_TERMS]), (11) indemnity (Licensor indemnifies Licensee if patent is held invalid/unenforceable [INDEMNITY_SCOPE]; Licensee indemnifies Licensor for infringement claims related to Licensee's use [LICENSEE_INDEMNITY]), (12) no other license (license does not extend to other Licensor IP [SCOPE_LIMITATION]), (13) field of use restriction (Licensee may use patent only for [FIELD_OF_USE] [FIELD_RESTRICTION]), (14) diligence ([DILIGENCE_REQUIREMENTS]: Licensee must commercialize products [COMMERCIALIZATION_TIMELINE]), (15) termination ([TERMINATION_TRIGGERS], with [NOTICE] notice; for breach [BREACH_REMEDY]), (16) post-termination ([POST_TERMINATION_RIGHTS]: Licensee may sell inventory [INVENTORY_SELL_TERMS], but no new sales [NEW_SALES_RESTRICTION]), and (17) accounting ([ACCOUNTING_PROCEDURES], audit rights [AUDIT_TERMS]). Target length: 8-12 pages.

**Context:** Use for patent licensing arrangements. Can be exclusive or non-exclusive. Field-of-use restrictions common for multiple licensing of same patent. Diligence requirements ensure licensee commercializes.

**Difficulty:** Advanced

**Follow-up:** PROMPT G5 (if you need to review open source compliance)

---

### PROMPT G5 — OPEN SOURCE COMPLIANCE REVIEW
Conduct an Open Source Compliance Review for [COMPANY_NAME]'s [PRODUCT_NAME/CODEBASE] to identify open source dependencies and compliance risks. The review should: (1) identify all open source software used [IDENTIFICATION_METHOD: e.g., "dependency scanning tool, manual code review"], (2) catalog each dependency: library name [NAME], version [VERSION], license type [LICENSE: e.g., "MIT, GPL, Apache 2.0"], source [SOURCE: e.g., "GitHub, npm registry"], and use case [USE_CASE], (3) classify by license type (permissive licenses [PERMISSIVE: e.g., "MIT, Apache 2.0, BSD"], copyleft licenses [COPYLEFT: e.g., "GPL, LGPL, AGPL"], mixed licenses [MIXED]), (4) assess license compatibility (which licenses are compatible with [OUR_LICENSE: e.g., "our proprietary license"]), identify conflicts [CONFLICTS], and derivative work implications [DERIVATIVE_IMPLICATIONS]), (5) identify copyleft implications (if using GPL, LGPL, or AGPL, triggering implications for source code disclosure [COPYLEFT_IMPLICATIONS]), (6) compliance requirements ([COMPLIANCE_REQUIREMENTS]: license notices [NOTICE_REQUIREMENTS], attribution [ATTRIBUTION_REQUIREMENTS], source code availability [SOURCE_CODE_REQUIREMENTS]), (7) commercial risks ([COMMERCIAL_RISKS]: revenue model compatibility [REVENUE_IMPACT], monetization restrictions [MONETIZATION_RESTRICTIONS]), (8) governance ([GOVERNANCE_RECOMMENDATIONS]: version control [VERSION_CONTROL], dependency management [DEPENDENCY_MANAGEMENT]), and (9) remediation recommendations (for each license: (a) current status, (b) risks, (c) recommended action [ACTIONS: e.g., "replace with permissive alternative, update to latest version, obtain written permission, remove dependency"]). Provide a summary risk assessment and prioritized remediation list. Target output: detailed report with dependency matrix, license compatibility chart, and action items.

**Context:** Use to ensure compliance with open source licenses and avoid copyleft triggering (especially GPL). Protects against license violation exposure and ensures contractual compliance for commercial sales.

**Difficulty:** Advanced

**Follow-up:** PROMPT H1 (if you need to review construction contracts)

---

## H. CONSTRUCTION & DEVELOPMENT (5 prompts)

### PROMPT H1 — CONSTRUCTION CONTRACT REVIEW
Review the attached construction contract between [CONTRACTOR_NAME] and [OWNER_NAME] for construction of [PROJECT_DESCRIPTION]. Provide a detailed analysis covering: (1) scope of work (description of work [SCOPE_DESCRIPTION], plans and specifications [PLANS_REFERENCE], change orders [CHANGE_ORDER_PROCESS], exclusions [EXCLUSIONS]), (2) price and payment (total contract price [PRICE], payment schedule [SCHEDULE], retainage [RETAINAGE_PERCENTAGE], markup [MARKUP_TERMS], contingency [CONTINGENCY_AMOUNT]), (3) timeline (start date [START_DATE], completion date [COMPLETION_DATE], schedule delays [DELAY_CONSEQUENCES], weather delays [WEATHER_TERMS]), (4) permits and insurance (who obtains permits [PERMIT_RESPONSIBILITY], insurance requirements [INSURANCE_REQUIREMENTS], lien waivers [LIEN_WAIVER_TERMS]), (5) labor and wage laws (prevailing wage [PREVAILING_WAGE_TERMS], union requirements [UNION_TERMS], safety [SAFETY_STANDARDS]), (6) quality and inspection ([QA_STANDARDS], inspections [INSPECTION_FREQUENCY], punch list [PUNCHLIST_TERMS], completion standards [COMPLETION_STANDARDS]), (7) warranty and defects ([WARRANTY_PERIOD], latent defect obligations [DEFECT_OBLIGATIONS], resolution process [DEFECT_RESOLUTION]), (8) liability and indemnity (liability caps [LIABILITY_CAP], indemnification [INDEMNITY_TERMS], dispute mechanics [MECHANICS]), (9) delay and acceleration ([DELAY_DAMAGES]: liquidated damages [LIQUIDATED_DAMAGES_AMOUNT], excusable delays [EXCUSABLE_DELAY_DEFINITION], acceleration [ACCELERATION_TERMS]), (10) changes (change order process [CHANGE_ORDER_MECHANICS], approval authority [APPROVAL_TERMS], cost impact [COST_IMPACT_TERMS]), (11) termination ([TERMINATION_RIGHTS], termination for cause [TERMINATION_FOR_CAUSE_TERMS], termination for convenience [TERMINATION_FOR_CONVENIENCE_TERMS]), (12) liens and claims ([LIEN_WAIVER_SCHEDULE], notice requirements [NOTICE_REQUIREMENTS]), (13) insurance and bonding ([BOND_REQUIREMENTS], insurance coverage [COVERAGE_REQUIREMENTS], certificate of insurance [CERTIFICATE_REQUIREMENTS]), (14) dispute resolution ([DISPUTE_MECHANISM]: mediation [MEDIATION_TERMS], arbitration [ARBITRATION_TERMS]), (15) governing law and jurisdiction ([GOVERNING_LAW], venue [VENUE]), and (16) other (site conditions [SITE_CONDITIONS_TERMS], existing conditions [EXISTING_CONDITIONS_TERMS], utilities [UTILITIES_TERMS]). Format findings as: Topic | Current Language | Concerns | Recommendations. Identify 5-10 key risk areas and suggest mitigation. Provide executive summary.

**Context:** Use before signing a construction contract or during contract negotiation. Construction contracts have substantial financial and legal implications.

**Difficulty:** Advanced

**Follow-up:** PROMPT H2 (if you need to review subcontractor agreements)

---

### PROMPT H2 — SUBCONTRACTOR AGREEMENT DRAFT
Draft a Subcontractor Agreement between [CONTRACTOR_NAME] (General Contractor) and [SUBCONTRACTOR_NAME] for [TRADE/SCOPE: e.g., "electrical work, HVAC installation, concrete"]. The agreement should include: (1) scope of work (detailed description of work [WORK_DESCRIPTION], plans and specifications [PLANS_REFERENCE: e.g., "Project Plans dated [DATE]"], exclusions [EXCLUSIONS]), (2) project information (project name [PROJECT_NAME], location [LOCATION], owner [OWNER_NAME], general contractor [GC_NAME]), (3) contract amount ([LUMP_SUM_AMOUNT] or [UNIT_PRICING: e.g., "labor at $[RATE]/hour"]], includes labor, materials, equipment [INCLUSIONS]), (4) payment terms (net [DAYS], monthly invoices [INVOICING_FREQUENCY], retainage [RETAINAGE_PERCENTAGE], final payment upon [FINAL_PAYMENT_TRIGGER]), (5) schedule (work begins [START_DATE], substantial completion [COMPLETION_DATE], working hours [WORKING_HOURS], continuity of work [CONTINUITY_TERMS]), (6) permits and licenses (Subcontractor holds all required licenses [LICENSE_REQUIREMENTS], permits [PERMIT_REQUIREMENTS]), (7) insurance and bonding (Subcontractor maintains insurance [INSURANCE_TYPES]: general liability ($[COVERAGE_AMOUNT]), worker's comp [WC_REQUIREMENTS], listed as additional insured [AI_REQUIREMENTS]; certificate provided [CERTIFICATE_REQUIREMENTS]; performance bond [BOND_REQUIREMENTS]), (8) labor and compliance (Subcontractor provides labor [LABOR_PROVISION], complies with labor laws [LABOR_COMPLIANCE], prevailing wage if applicable [PREVAILING_WAGE_TERMS], union requirements if applicable [UNION_TERMS]), (9) quality and inspection (work meets [QUALITY_STANDARD], inspections [INSPECTION_TERMS], punch list [PUNCHLIST_PROCESS]), (10) safety ([SAFETY_REQUIREMENTS]: OSHA compliance [OSHA_TERMS], site safety plan [SAFETY_PLAN_TERMS], incident reporting [INCIDENT_REPORTING]), (11) changes (change orders required [CHANGE_ORDER_PROCEDURE], GC approval [APPROVAL_TERMS], cost impact [COST_IMPACT_TERMS]), (12) delays and acceleration (responsibility for delays [DELAY_RESPONSIBILITY], liquidated damages [LD_TERMS], acceleration [ACCELERATION_TERMS]), (13) warranty ([WARRANTY_PERIOD]: Subcontractor warrants workmanship [WARRANTY_SCOPE], materials [MATERIAL_WARRANTY]), (14) liens and claims (Subcontractor pays all suppliers/workers [PAYMENT_RESPONSIBILITY], waives liens [LIEN_WAIVER_TIMING], final lien waiver [FINAL_LIEN_WAIVER_CONDITION]), (15) termination (GC may terminate for cause [TERMINATION_FOR_CAUSE_TERMS], convenience [TERMINATION_FOR_CONVENIENCE_TERMS]), (16) indemnity and liability (Subcontractor indemnifies GC [INDEMNITY_SCOPE], liability limits [LIABILITY_LIMITS]), (17) insurance and indemnity crossover ([INSURANCE_INTERACTION]), and (18) dispute resolution ([DISPUTE_MECHANISM]). Target length: 4-6 pages. Include a detailed scope of work schedule.

**Context:** Use for engaging subcontractors on construction projects. Critical for clarifying scope, payment, schedule, and liability.

**Difficulty:** Intermediate

**Follow-up:** PROMPT H3 (if you need to contract design services)

---

### PROMPT H3 — DESIGN SERVICES AGREEMENT DRAFT
Draft a Design Services Agreement between [DESIGN_FIRM_NAME] and [CLIENT_NAME] for design services relating to [PROJECT_DESCRIPTION: e.g., "architectural design for commercial building, interior design, graphic design"]. The agreement should establish: (1) services ([SERVICES_SCOPE]: design phases [PHASES: e.g., "schematic design, design development, construction documents"], deliverables [DELIVERABLES], deliverable format [DELIVERABLE_FORMAT: e.g., "CAD files, drawings, specifications"]), (2) scope (design scope [SCOPE_DEFINITION], excluded services [EXCLUSIONS]), (3) project team ([DESIGN_FIRM] assigns [TEAM_COMPOSITION], principal designer [PRINCIPAL], consultants [CONSULTANTS: e.g., "structural engineer, MEP engineer"]), (4) client responsibilities (Client provides [CLIENT_RESPONSIBILITIES]: existing conditions information [INFORMATION], decisions [DECISIONS], approvals [APPROVAL_PROCESS]), (5) contract amount ([PROJECT_FEE: e.g., "$[AMOUNT]", "[PERCENTAGE]% of construction cost"] or [TIME_AND_MATERIALS: "[HOURLY_RATE] per hour, estimated [BUDGET]"]), (6) payment schedule ([PAYMENT_SCHEDULE]: upon signing [AMOUNT], at design phase completion [AMOUNTS], final payment upon [FINAL_PAYMENT_TRIGGER]), (7) additional services (services not in scope require additional fee [CHANGE_PROCESS], change orders [CHANGE_ORDER_PROCESS]), (8) reimbursable expenses ([EXPENSE_CATEGORIES], with [APPROVAL_THRESHOLD] approval, billed at [MARKUP_RATE]), (9) schedule (design timeline [TIMELINE], phases [PHASES] with completion dates [DATES]), (10) client review and approval (Client reviews deliverables [REVIEW_FREQUENCY], approves design [APPROVAL_AUTHORITY], feedback timing [FEEDBACK_TIMELINE]), (11) changes (Client-requested changes require change order [CHANGE_ORDER_TERMS], fee adjustment [FEE_ADJUSTMENT]), (12) intellectual property (Client owns the design [DESIGN_OWNERSHIP], design firm retains rights to use design in portfolio [PORTFOLIO_USE], publications [PUBLICATION_TERMS]), (13) reuse of design (Design for [SPECIFIC_PROJECT] only; reuse for different project requires additional fee [REUSE_TERMS]), (14) insurance (Design firm maintains professional liability insurance [INSURANCE_COVERAGE], certificate provided [CERTIFICATE_REQUIREMENT]), (15) warranty (Design firm warrants professional standard [WARRANTY_SCOPE], compliance with [COMPLIANCE_SCOPE: e.g., "building codes, safety standards"]], latent defect obligation [[LATENT_DEFECT_TIMELINE]]), (16) confidentiality (mutual [CONFIDENTIALITY_SCOPE]), (17) termination ([TERMINATION_RIGHTS], fees due through termination [TERMINATION_PAYMENT]), and (18) dispute resolution ([MECHANISM]). Target length: 5-7 pages.

**Context:** Use for architectural, engineering, interior design, graphic design, and creative services. Clarifies deliverables, payment, ownership, and scope.

**Difficulty:** Intermediate

**Follow-up:** PROMPT H4 (if you need project management agreement)

---

### PROMPT H4 — PROJECT MANAGEMENT AGREEMENT DRAFT
Draft a Project Management Agreement between [PROJECT_MANAGER_FIRM_NAME] and [CLIENT_NAME] for project management services for [PROJECT_DESCRIPTION: e.g., "commercial construction project, renovation, technology implementation"]. The agreement should cover: (1) services ([PM_SERVICES_SCOPE]: project administration [ADMINISTRATION_SCOPE], contractor coordination [COORDINATION_SCOPE], schedule management [SCHEDULE_MANAGEMENT], budget management [BUDGET_MANAGEMENT], quality control [QC_SCOPE], site management [SITE_MANAGEMENT_SCOPE]), (2) project information (project name [NAME], location [LOCATION], estimated cost [BUDGET], timeline [TIMELINE], phases [PHASES]), (3) role of project manager (coordinates [COORDINATION_SCOPE], supervises [SUPERVISION_SCOPE], does not employ contractors [EMPLOYMENT_CLARIFICATION]), (4) contract amount ([MANAGEMENT_FEE]: fixed fee [FEE_AMOUNT], percentage of construction cost [PERCENTAGE], time and materials [HOURLY_RATE_WITH_BUDGET], or cost-plus-fee [FEE_STRUCTURE]), (5) payment schedule ([PAYMENT_SCHEDULE]), (6) reimbursable expenses ([EXPENSE_CATEGORIES], approval [APPROVAL_THRESHOLD], reimbursement [REIMBURSEMENT_TERMS]), (7) staffing (PM firm assigns [STAFFING_DETAIL], project manager [PM_DETAIL]), (8) schedule (project timeline [TIMELINE], PM involvement [PM_TIMELINE]), (9) meetings and reporting ([MEETING_FREQUENCY], attendance [ATTENDANCE_REQUIREMENTS], reporting [REPORTING_FREQUENCY]), (10) contractor administration (manages RFQ process [RFQ_PROCESS], reviews contracts [CONTRACT_REVIEW], processes change orders [CHANGE_ORDER_PROCESS], approves invoices [INVOICE_APPROVAL]), (11) budget management (tracks costs [COST_TRACKING], flags overruns [OVERRUN_MANAGEMENT]), (12) quality control (inspects work [INSPECTION_FREQUENCY], punch list [PUNCHLIST_MANAGEMENT]), (13) change orders (review and approval [CHANGE_ORDER_PROCESS], authorization [AUTHORIZATION_AUTHORITY]), (14) communication (liaisons with contractors [COMMUNICATION_CHANNELS], owner updates [UPDATE_FREQUENCY]), (15) closeout (completion checklist [CHECKLIST], final inspections [INSPECTION_PROCESS], final accounting [ACCOUNTING_CLOSURE]), (16) limits of authority ([AUTHORITY_LIMITS]: PM cannot [RESTRICTIONS], requires owner approval [APPROVAL_ITEMS]), (17) liability and insurance (PM firm maintains errors & omissions insurance [INSURANCE_COVERAGE], indemnifies client [INDEMNITY_SCOPE], liability limits [LIABILITY_CAP]), (18) termination ([TERMINATION_TERMS]), and (19) dispute resolution ([MECHANISM]). Target length: 6-8 pages.

**Context:** Use for hiring a professional project manager for complex projects. Clarifies PM responsibilities, authority limits, and payment structure.

**Difficulty:** Intermediate

**Follow-up:** PROMPT H5 (if you need to analyze defects liability)

---

### PROMPT H5 — DEFECTS LIABILITY ANALYSIS
Analyze the Defects Liability Clause in the attached construction contract and provide a detailed assessment. The analysis should address: (1) defect definition ([DEFECT_DEFINITION]: what constitutes a defect, latent vs. apparent [DISTINCTION], workmanship standard [STANDARD], materials standard [MATERIAL_STANDARD]), (2) discovery and notice ([NOTICE_REQUIREMENT]: who discovers defects [DISCOVERY_PROCESS], notice timing [NOTICE_TIMELINE], notice format [NOTICE_FORMAT]), (3) contractor obligation ([CONTRACTOR_OBLIGATION]: must repair [REPAIR_OBLIGATION], must replace [REPLACEMENT_OBLIGATION], timing [REPAIR_TIMELINE]), (4) warranty period ([WARRANTY_PERIOD]: duration [DURATION_TERM], commencement [COMMENCEMENT_POINT: e.g., "substantial completion, final payment"]), (5) latent defects ([LATENT_DEFECT_PERIOD]: separate period after warranty [LATENT_PERIOD: e.g., "2 years"]], discovery within period triggers obligation [DISCOVERY_TRIGGER]), (6) defects excluded ([EXCLUSIONS]: normal wear and tear [WEAR_AND_TEAR_EXCLUSION], modifications by owner [MODIFICATION_EXCLUSION], maintenance failure [MAINTENANCE_EXCLUSION], third-party work [THIRD_PARTY_EXCLUSION]), (7) remedy process (who initiates [INITIATION_PROCESS], who performs repair [REPAIR_RESPONSIBILITY], owner right to self-help [SELF_HELP_TERMS], cost responsibility [COST_ALLOCATION]), (8) cost caps ([COST_CAP_STRUCTURE]: capped at [CAP_AMOUNT], percentage of contract [CAP_PERCENTAGE], per-occurrence caps [PER_ITEM_CAPS]), (9) contractor cooperation ([COOPERATION_OBLIGATIONS]: timely response [RESPONSE_TIMELINE], completion [COMPLETION_TIMELINE], access [ACCESS_TERMS]), (10) independent inspection ([INSPECTION_PROCESS]: who inspects [INSPECTION_AUTHORITY], timing [INSPECTION_TIMELINE], dispute resolution [DISPUTE_MECHANISM]), (11) retention and release (retainage amount [RETAINAGE_AMOUNT], release timing [RELEASE_TIMING], final release post-warranty [FINAL_RELEASE_TIMING]), (12) special risk areas ([SPECIAL_RISKS]: roof [ROOF_WARRANTY], windows [WINDOW_WARRANTY], HVAC [HVAC_WARRANTY], plumbing [PLUMBING_WARRANTY]), (13) third-party warranties ([THIRD_PARTY_WARRANTIES]: manufacturer warranties [MANUFACTURER_TERMS], integration with contractor warranty [INTEGRATION]), (14) notice and dispute process ([NOTICE_REQUIREMENTS], dispute resolution [DISPUTE_RESOLUTION], mediation [MEDIATION_REQUIREMENT]), and (15) risk assessment ([RISK_ASSESSMENT]: whether terms are balanced, any unusual risk allocation, enforceability issues). Provide: (a) clause-by-clause analysis, (b) gap analysis (missing protections), (c) risk ranking (Low/Medium/High), and (d) recommended modifications for [PARTY: owner/contractor]. Format as table and narrative summary.

**Context:** Use to evaluate defects liability clauses before contract execution. Critical for managing post-completion defects and warranty obligations.

**Difficulty:** Advanced

**Follow-up:** PROMPT I1 (if you need to analyze procurement agreements)

---

## I. PROCUREMENT & PURCHASING (4 prompts)

### PROMPT I1 — MASTER SERVICES AGREEMENT REVIEW
Review the attached Master Services Agreement (MSA) between [VENDOR_NAME] and [CLIENT_NAME] and provide a detailed risk assessment. The review should address: (1) scope of services ([SERVICES_DESCRIPTION], statement of work process [SOW_PROCESS], exclusions [EXCLUSIONS]), (2) term and renewal ([TERM_LENGTH], renewal options [RENEWAL_OPTIONS], termination triggers [TERMINATION_TRIGGERS]), (3) governing documents (hierarchy of documents [DOCUMENT_HIERARCHY]: MSA, SOW, schedules [PRIORITY_RULES]), (4) pricing ([PRICING_MECHANISM]: fixed pricing [FIXED_TERMS], time-and-materials [T&M_TERMS], change management [CHANGE_PROCESS]), (5) payment terms (net [DAYS], invoicing [INVOICING_FREQUENCY], payment method [PAYMENT_METHOD]), (6) service levels ([SLA_METRICS]: uptime [UPTIME_TARGETS], response time [RESPONSE_TIMES], remedy structure [REMEDY_STRUCTURE]), (7) termination (for cause [CAUSE_DEFINITIONS], for convenience [CONVENIENCE_TERMS], notice [NOTICE_PERIOD], wind-down [WIND_DOWN_OBLIGATIONS]), (8) liability and limitation ([LIABILITY_CAP], excluded damages [EXCLUDED_DAMAGES: e.g., "consequential, indirect"], carve-outs [CARVE_OUTS]), (9) indemnification ([INDEMNITY_STRUCTURE]: vendor indemnifies for [VENDOR_INDEMNITY], client indemnifies for [CLIENT_INDEMNITY], process [INDEMNITY_PROCESS]), (10) intellectual property ([IP_OWNERSHIP]: vendor IP [VENDOR_IP_TERMS], client IP [CLIENT_IP_TERMS], foreground IP [FOREGROUND_IP_TERMS], license grants [LICENSE_GRANTS]), (11) data security and compliance ([SECURITY_STANDARDS], certifications [CERTIFICATIONS: e.g., "SOC 2, ISO 27001"], data location [DATA_LOCATION_TERMS], breach notification [BREACH_NOTIFICATION_TIMELINE]), (12) confidentiality (scope [CONFIDENTIALITY_SCOPE], duration [DURATION_OF_OBLIGATION], permitted use [PERMITTED_USE]), (13) insurance (required coverage [COVERAGE_AMOUNTS], certificate requirements [CERTIFICATE_TERMS]), (14) change management (process [CHANGE_PROCESS], approval [APPROVAL_AUTHORITY], cost impact [COST_IMPACT_HANDLING]), (15) dispute resolution ([DISPUTE_MECHANISM]: escalation [ESCALATION_PROCESS], mediation [MEDIATION_TERMS], arbitration [ARBITRATION_TERMS]), and (16) other issues (assignment [ASSIGNMENT_TERMS], force majeure [FORCE_MAJEURE_TERMS], governing law [GOVERNING_LAW]). Provide: (a) strengths and weaknesses, (b) risk ranking by area (Low/Medium/High), (c) key negotiation points, (d) gaps (missing protections), and (e) 5-10 specific recommended redlines with suggested language. Format as summary with prioritized recommendations table.

**Context:** Use before signing an MSA or at renewal. MSAs establish terms for multiple future SOWs and engagements.

**Difficulty:** Advanced

**Follow-up:** PROMPT I2 (if you need to establish PO terms)

---

### PROMPT I2 — PURCHASE ORDER TERMS DRAFT
Draft Terms and Conditions for Purchase Orders (POs) issued by [BUYER_NAME] to [VENDOR/SUPPLIER_NAME(S)]. The T&Cs should establish: (1) purchase order acceptance (PO is offer [PO_TERMS]; acceptance via acknowledgment [ACCEPTANCE_METHOD], shipment [SHIPMENT_ACKNOWLEDGMENT], or [ACCEPTANCE_MECHANISM]), (2) products and services ([PRODUCTS_DEFINED], specifications [SPECIFICATION_REFERENCE], approved suppliers [SUPPLIER_APPROVAL]), (3) pricing and payment (unit price [PRICING_TERMS], extended price [CALCULATION], volume discounts [DISCOUNT_TIERS], net [DAYS] payment terms), (4) order modifications (changes require written amendment [AMENDMENT_PROCESS], cost adjustments [COST_ADJUSTMENT_PROCEDURE]), (5) delivery ([DELIVERY_TERMS]: delivery location [DELIVERY_LOCATION], FOB point [FOB_POINT], delivery date [DELIVERY_DATE_BINDING], rush orders [RUSH_TERMS]), (6) inspection and acceptance (Buyer may inspect upon receipt [INSPECTION_RIGHTS], acceptance period [ACCEPTANCE_PERIOD], defect notification [DEFECT_NOTIFICATION_TIMELINE]), (7) risk of loss (transfers upon [TRANSFER_POINT: e.g., "delivery"]], before delivery Vendor bears risk [RISK_ALLOCATION]), (8) quality ([QUALITY_REQUIREMENTS], conformance to specifications [CONFORMANCE_REQUIREMENT], workmanship [WORKMANSHIP_STANDARDS]), (9) warranty (products/services conform to [WARRANTY_SCOPE], free from defects [DEFECT_WARRANTY], for [WARRANTY_PERIOD]), (10) returns and refunds (defective products may be returned [RETURN_TERMS], refunds or replacement [REFUND_TERMS]), (11) intellectual property (Buyer retains IP in any specifications [IP_OWNERSHIP], Vendor warrants no infringement [INFRINGEMENT_WARRANTY]), (12) insurance and liability (Vendor maintains insurance [INSURANCE_COVERAGE], liability capped at [LIABILITY_CAP] per PO), (13) indemnification (Vendor indemnifies Buyer for product defects [INDEMNITY_SCOPE]), (14) compliance (Vendor warrants compliance with [COMPLIANCE_SCOPE]: laws, regulations, environmental, conflict minerals [COMPLIANCE_REPRESENTATIONS]), (15) termination ([TERMINATION_RIGHTS]: for non-delivery [NON_DELIVERY_TERMS], for defects [DEFECT_TERMINATION]), (16) dispute resolution ([DISPUTE_MECHANISM]), (17) confidentiality, and (18) general terms (governing law [JURISDICTION], assignment [ASSIGNMENT_RESTRICTIONS], entire agreement [INTEGRATION]). PO T&Cs should be brief (1-2 pages), comprehensive, and unambiguous. Include as printed on back of PO or as document incorporated by reference. Provide sample "purchase order terms and conditions" form that can be printed/referenced.

**Context:** Use to establish standard terms for all purchase orders issued by your company. PO T&Cs protect your company and establish consistent commercial practices.

**Difficulty:** Intermediate

**Follow-up:** PROMPT I3 (if you need a framework agreement)

---

### PROMPT I3 — FRAMEWORK AGREEMENT DRAFT
Draft a Framework Agreement between [BUYER_NAME] and [SUPPLIER_NAME] establishing the terms under which Buyer will issue purchase orders to Supplier for [PRODUCTS/SERVICES_DESCRIPTION: e.g., "IT equipment and software, logistics services, office supplies"]. The framework should include: (1) purpose (establishes terms for [PRODUCTS_SCOPE], underlying individual orders [ORDER_MECHANISM]), (2) products/services ([PRODUCTS_LIST], updates [UPDATE_TERMS], discontinued items [DISCONTINUATION_TERMS]), (3) term ([DURATION], automatic renewal unless [NOTICE] notice given), (4) pricing ([PRICING_STRUCTURE]: fixed pricing [FIXED_PRICING], volume discounts [VOLUME_DISCOUNT_TIERS], price escalation [ESCALATION_FORMULA]), (5) minimum purchase ([MINIMUM_ANNUAL_PURCHASE], enforcement [ENFORCEMENT_TERMS]), (6) maximum purchase ([MAXIMUM_PURCHASE] if applicable [MAX_PURCHASE_TERMS]), (7) ordering ([ORDER_PROCESS]: POs issued against framework [ORDER_MECHANISM], delivery [DELIVERY_TERMS], lead time [LEAD_TIME_TERMS]), (8) payment ([PAYMENT_TERMS]: net [DAYS], payment method [PAYMENT_METHOD], invoicing [INVOICING_TERMS]), (9) quality and warranties ([QUALITY_STANDARDS], warranty [WARRANTY_PERIOD]), (10) delivery ([DELIVERY_LOCATION], delivery schedule [DELIVERY_SCHEDULE], risk of loss [RISK_ALLOCATION]), (11) intellectual property (framework doesn't grant IP rights [IP_CLARIFICATION]; PO terms govern [PO_IP_TERMS]), (12) confidentiality (mutual [CONFIDENTIALITY_SCOPE], duration [DURATION]), (13) insurance (Supplier maintains insurance [INSURANCE_REQUIREMENTS]), (14) compliance (Supplier complies with [COMPLIANCE_SCOPE]: laws, safety, environmental), (15) termination (either party [NOTICE] notice; termination for breach [BREACH_DEFINITION]), (16) individual orders (each PO incorporates framework [PO_INCORPORATION]), (17) dispute resolution ([DISPUTE_MECHANISM]), and (18) governing law ([JURISDICTION]). Framework agreements provide volume/long-term commitment discounts while maintaining flexibility on individual order quantities and timing. Target length: 5-7 pages.

**Context:** Use for ongoing supplier relationships where you anticipate multiple orders over a period. Negotiates volume pricing upfront.

**Difficulty:** Intermediate

**Follow-up:** PROMPT I4 (if you need to evaluate RFP responses)

---

### PROMPT I4 — REQUEST FOR PROPOSAL (RFP) EVALUATION MATRIX
Create an RFP Evaluation Matrix to assess and score proposals from [RESPONDENT_TYPE: e.g., "software vendors, consulting firms, service providers"]] responding to [RFP_DESCRIPTION]. The matrix should include: (1) evaluation criteria categories: [CATEGORY_1: e.g., "Technical Capability"], [CATEGORY_2: e.g., "Price"], [CATEGORY_3: e.g., "Vendor Stability"], [CATEGORY_4: e.g., "Implementation Timeline"], [CATEGORY_5: e.g., "Support and Service Levels"]], (2) specific evaluation criteria within each category: [CATEGORY_1_SUBCRITERIA: e.g., "Product features, scalability, integration capability, customization flexibility"; CATEGORY_2_SUBCRITERIA: e.g., "Upfront cost, ongoing fees, ROI, cost transparency"; CATEGORY_3_SUBCRITERIA: e.g., "Financial stability, customer retention, industry experience"; CATEGORY_4_SUBCRITERIA: e.g., "Implementation timeline, resource allocation, risk management"; CATEGORY_5_SUBCRITERIA: e.g., "Support hours, response time, training, documentation"]], (3) weighting (assign weight to each criterion: [CATEGORY_1_WEIGHT: e.g., "40%"], [CATEGORY_2_WEIGHT], [CATEGORY_3_WEIGHT], [CATEGORY_4_WEIGHT], [CATEGORY_5_WEIGHT], totaling 100%), (4) scoring scale ([SCALE: e.g., "1-5 points, where 1=Does Not Meet, 3=Meets, 5=Exceeds"]), (5) evaluation sheet ([PROPOSAL_ID], [VENDOR_NAME], score by criterion [SCORES], weighted score [WEIGHTED_SCORES], total score [TOTAL_SCORE]), (6) tie-breaker criteria ([TIE_BREAKER_CRITERIA] if scores are equal), and (7) evaluation notes (space for evaluator comments [COMMENTS_SPACE]). Provide a sample matrix as a spreadsheet template with: (a) list of evaluation criteria and weights, (b) sample scoring for 2-3 hypothetical proposals showing calculation, (c) recommendation summary (ranking, final scores, recommended vendor [RECOMMENDED_VENDOR]), (d) risk factors and caveats [RISK_FACTORS], and (e) guidance on evaluation process [PROCESS_GUIDANCE]. The matrix should be objective, transparent, and defensible.

**Context:** Use to systematically evaluate and score vendor proposals, especially for complex procurements with multiple evaluation criteria. Ensures objective decision-making and can be used to justify vendor selection.

**Difficulty:** Intermediate

**Follow-up:** PROMPT J1 (if you need to draft a settlement agreement)

---

## J. SETTLEMENT & RELEASE (4 prompts)

### PROMPT J1 — SETTLEMENT AGREEMENT DRAFT
Draft a Settlement Agreement between [PARTY_A_NAME] and [PARTY_B_NAME] to resolve the dispute regarding [DISPUTE_SUBJECT: e.g., "breach of contract, IP infringement, employment termination, product liability"]. The agreement should include: (1) recitals (background on dispute [DISPUTE_BACKGROUND], no admission of liability [NO_LIABILITY_ADMISSION], parties' intent to resolve [RESOLUTION_INTENT]), (2) consideration (what each party receives [CONSIDERATION_DETAIL]: [PARTY_A] receives [PARTY_A_CONSIDERATION: e.g., "$[AMOUNT] payment"]; [PARTY_B] receives [PARTY_B_CONSIDERATION: e.g., "release of claims", "dismissal of lawsuit"]], mutual consideration found sufficient [CONSIDERATION_SUFFICIENCY]), (3) payment terms (if applicable: amount [PAYMENT_AMOUNT], due date [PAYMENT_DATE], payment method [PAYMENT_METHOD], late payment [LATE_PAYMENT_CONSEQUENCES]), (4) dismissal or release (parties release each other from all claims [RELEASE_SCOPE] arising out of [RELEASE_BASIS], through [EFFECTIVE_DATE], known and unknown [KNOWN_UNKNOWN_SCOPE], with exceptions [EXCEPTIONS: e.g., "indemnification obligations, confidentiality"]], [PARTY_A] dismisses any lawsuit with prejudice [DISMISSAL_TERMS]), (5) mutual release (mutual release language [MUTUAL_LANGUAGE]; [PARTY_A] releases [PARTY_B], officers, directors, employees, agents [RELEASED_PARTIES_A]; [PARTY_B] releases [PARTY_A], officers, directors, employees, agents [RELEASED_PARTIES_B]), (6) confidentiality (terms of settlement are confidential [CONFIDENTIALITY_SCOPE]; parties may not disclose amount [AMOUNT_CONFIDENTIALITY], terms [TERMS_CONFIDENTIALITY]; exceptions: attorneys, accountants, as required by law [EXCEPTIONS]), (7) no admission of liability ([NO_ADMISSION_CLAUSE]: settlement does not constitute admission [ADMISSION_SCOPE], may not be used as evidence [EVIDENCE_RESTRICTION]), (8) cooperation (parties cooperate in resolving any remaining administrative/tax issues [COOPERATION_OBLIGATIONS]), (9) non-disparagement ([NON_DISPARAGEMENT_SCOPE]: [PARTY_A] will not disparage [PARTY_B], and vice versa, for [DURATION]; exceptions [EXCEPTIONS: e.g., "truthful testimony"]], (10) indemnity (indemnities survive settlement [INDEMNITY_SURVIVAL_SCOPE]), (11) continuing obligations (other agreements survive [SURVIVAL_SCOPE]: confidentiality, IP assignment, non-compete, etc.), (12) integration clause (this is the entire agreement [INTEGRATION_SCOPE]), (13) governing law ([JURISDICTION]), (14) dispute resolution ([DISPUTE_MECHANISM] for disputes about settlement itself), and (15) execution ([SIGNATURE_BLOCKS], effective upon [EFFECTIVE_DATE]), including any schedule of payments [PAYMENT_SCHEDULE]. Consider whether settlement is conditioned on third-party consent [CONDITION_PRECEDENT], regulatory approval [REGULATORY_APPROVAL], or other parties' agreement [OTHER_CONDITIONS]. Target length: 3-5 pages. Ensure confidentiality is carefully tailored to what can/cannot be disclosed.

**Context:** Use to document settlement of any dispute (contractual, IP, employment, tort) and release mutual claims.

**Difficulty:** Intermediate

**Follow-up:** PROMPT J2 (if you need a simple mutual release)

---

### PROMPT J2 — MUTUAL RELEASE DRAFT
Draft a Mutual Release between [PARTY_A_NAME] and [PARTY_B_NAME] whereby each party releases the other from all claims [CLAIM_SCOPE: e.g., "arising out of the parties' business relationship, contract, or dealings"]. The release should include: (1) recitals (parties have had a business relationship [RELATIONSHIP_DESCRIPTION], parties desire to resolve all matters [RESOLUTION_INTENT], mutual release is fair consideration [CONSIDERATION_FINDING]), (2) release ([PARTY_A] hereby releases and forever discharges [PARTY_B], and [PARTY_B]'s officers, directors, employees, agents, representatives, successors, and assigns, from any and all claims, demands, causes of action, damages, losses, and liabilities [CLAIM_SCOPE], whether known or unknown, arising out of or related to [RELEASE_BASIS: e.g., "the parties' business dealings from [START_DATE] to [END_DATE]"]], except [EXCEPTIONS: e.g., "any indemnification obligations under the [CONTRACT_NAME]", "confidentiality obligations"]], (3) mutual release ([PARTY_B] makes the same release of [PARTY_A] [MUTUAL_RELEASE_LANGUAGE]), (4) no admission (release does not constitute admission of any liability, wrongdoing, or fault [NO_ADMISSION_SCOPE]), (5) knowing and voluntary (each party acknowledges that it makes this release with full knowledge and understanding [KNOWINGNESS_ACKNOWLEDGMENT], having had opportunity to consult with counsel [COUNSEL_CONSULTATION]), (6) confidentiality (terms of release are confidential and may not be disclosed [CONFIDENTIALITY_SCOPE]; exceptions [EXCEPTIONS: e.g., "attorneys, accountants", "required by law"]], (7) integration (this constitutes the entire agreement regarding release [INTEGRATION_SCOPE]; prior negotiations are superseded [SUPERSESSION]), (8) governing law ([JURISDICTION]), and (9) signature blocks ([SIGNATURE_REQUIREMENTS]: party and representative [SIGNATORY], date [DATE]). Consider whether release is immediate and absolute [IMMEDIATE_RELEASE] or conditioned on [CONDITIONS_PRECEDENT: e.g., "no material breach by other party"]. Target length: 1-2 pages. Simple mutual release is useful for amicable partings, end of business relationships, or settling small disputes without money changing hands.

**Context:** Use for mutual releases between parties ending a business relationship or settling minor disputes. Simpler than a settlement agreement if no payment is involved.

**Difficulty:** Beginner

**Follow-up:** PROMPT J3 (if you need a deed of release for creditor/debtor situations)

---

### PROMPT J3 — DEED OF RELEASE DRAFT
Draft a Deed of Release between [CREDITOR_NAME] (as Releasor) and [DEBTOR_NAME] (as Releasee) releasing the Debtor from [DEBT_DESCRIPTION: e.g., "a promissory note dated [DATE] in the amount of $[AMOUNT]", "outstanding accounts payable", "equipment lease obligations"]. The deed should include: (1) recitals (Creditor holds claim against Debtor [CLAIM_DESCRIPTION], parties agree to release the claim [RELEASE_AGREEMENT], mutual benefit [MUTUAL_BENEFIT_FINDING]), (2) operative clause (Creditor, in consideration of [CONSIDERATION_EXCHANGE: e.g., "Debtor's agreement to pay $[AMOUNT]", "mutual release"]], hereby releases and discharges Debtor, and Debtor's officers, directors, employees, agents, successors, and assigns, from any and all claims, debts, obligations, and liabilities [DEBT_SCOPE] arising out of [DEBT_BASIS: e.g., "the [INSTRUMENT_NAME] dated [DATE]", "Debtor's failure to pay [OBLIGATION]"]], (3) prior obligations (Creditor confirms that Debtor owes [DEBT_AMOUNT] and acknowledges receipt/satisfaction of [CONSIDERATION: e.g., "$[PAYMENT_AMOUNT] in full satisfaction" or "partial payment"], or [NO_CONSIDERATION: "Creditor waives the debt as a matter of grace"] [PAYMENT_ACKNOWLEDGMENT]), (4) no admission (release does not constitute admission of any liability [NO_LIABILITY_ADMISSION]), (5) discharge (Debtor is released from all further liability [DISCHARGE_SCOPE]), (6) return of instruments (Creditor returns any security, collateral, or documents [DOCUMENT_RETURN]), (7) cooperation (Creditor agrees to execute any documents necessary to evidence the release [COOPERATION_TERMS]), (8) waiver of claims (Creditor waives any claims for interest, penalties, costs [CLAIM_WAIVER_SCOPE]), (9) binding on successors (release binds successors and assigns [BINDING_SCOPE]), (10) integration (this constitutes the entire agreement [INTEGRATION]), (11) governing law ([JURISDICTION]), and (12) acknowledgment ([ACKNOWLEDGMENT]: Creditor and Debtor acknowledge they understand this deed, have had opportunity to consult counsel [COUNSEL_CONSULTATION], and sign voluntarily [VOLUNTARY_EXECUTION]). Include signature blocks for Creditor and Debtor (and Debtor's spouse if marital property may be involved). Consider whether this is a full or partial release [RELEASE_TYPE] and whether Creditor retains claims against guarantors/other obligors [GUARANTOR_CLAIMS]. A deed of release is often used in non-bankruptcy workouts to forgive or settle debt. Target length: 2-3 pages.

**Context:** Use to release or forgive outstanding debts, settlement of debt obligations, or non-bankruptcy workouts.

**Difficulty:** Intermediate

**Follow-up:** PROMPT J4 (if you need a compromise agreement)

---

### PROMPT J4 — COMPROMISE AGREEMENT DRAFT
Draft a Compromise Agreement between [PARTY_A_NAME] and [PARTY_B_NAME] whereby the parties agree to compromise [DISPUTED_MATTER: e.g., "payment obligation, performance dispute, contract interpretation, property damage claim"]. The agreement should establish: (1) background (dispute regarding [DISPUTE_SUBJECT], parties have discussed and agreed to compromise [COMPROMISE_INTENT]), (2) original claim ([ORIGINAL_CLAIM_DETAIL]: [PARTY_A] claimed [CLAIM_AMOUNT] from [PARTY_B], or [PARTY_B] disputed [DISPUTED_OBLIGATION]), (3) compromise ([PARTY_A] agrees to accept [COMPROMISE_AMOUNT/REMEDY: e.g., "$[AMOUNT] in full and final settlement", "specific performance on [TERMS]", "repair/replacement of [ITEM]"]; [PARTY_B] agrees to pay/perform [COMPROMISE_PAYMENT/PERFORMANCE: e.g., "$[AMOUNT] by [DATE]", "complete [WORK] by [DATE]"]], (4) payment/performance ([PAYMENT_SCHEDULE] if applicable, [PAYMENT_METHOD], [PERFORMANCE_SCHEDULE] if applicable, [PERFORMANCE_TERMS]), (5) release (upon [TRIGGER: e.g., "payment" or "performance completion"]], [PARTY_A] releases [PARTY_B] from all related claims [RELEASE_SCOPE], and vice versa [MUTUAL_RELEASE]), (6) no admission (compromise does not imply either party admits liability or wrongdoing [NO_ADMISSION_LANGUAGE]), (7) confidentiality ([CONFIDENTIALITY_SCOPE]: terms are confidential, may not be disclosed [DISCLOSURE_RESTRICTION]; exceptions [EXCEPTIONS]), (8) cooperation (parties cooperate in executing any needed documents [COOPERATION_OBLIGATION]), (9) integration (this is the entire compromise agreement [INTEGRATION_CLAUSE]), (10) dispute resolution ([DISPUTE_MECHANISM] for disputes about the compromise itself), (11) governing law ([JURISDICTION]), and (12) execution ([SIGNATURE_BLOCKS], effective upon execution or [EFFECTIVE_DATE]). A compromise agreement is useful when both parties make concessions (neither gets full relief). Can include partial payment, payment over time, performance remedies, or a combination. Target length: 2-3 pages.

**Context:** Use when disputing parties reach a middle-ground settlement involving give-and-take. Common in payment disputes, performance disagreements, and contractual interpretations.

**Difficulty:** Intermediate

**Follow-up:** For additional contract types or analysis, return to relevant previous prompts or explore specific transaction contexts not yet covered.

---

## USAGE NOTES

- **Copy-Paste Ready:** Each prompt is formatted for direct insertion into Claude or similar AI tools. Replace [BRACKETED PLACEHOLDERS] with specific information.
- **Customization:** Modify prompts to fit your specific transaction, jurisdiction, and risk profile. Prompts are templates and should be adapted to your situation.
- **Follow-Up Workflow:** Use suggested follow-up prompts to iteratively refine contracts through multiple drafts, reviews, and negotiation rounds.
- **Legal Review:** All AI-generated contracts should be reviewed by qualified legal counsel in your jurisdiction before execution. AI is a tool to accelerate drafting, not a substitute for legal advice.
- **Jurisdiction Variation:** Contract terms vary significantly by jurisdiction, especially for employment, real estate, construction, and franchise agreements. Ensure compliance with local law.

---

**End of V2.02 Contracts — Specific Types**

**Total Prompts: 50**

