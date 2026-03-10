# AI Prompts for Financial Regulation

## Overview
This library contains 45+ prompts designed to assist legal and compliance professionals in Singapore, the broader APAC region, and international financial regulation. Prompts cover MAS framework, FCA/SEC cross-references, AML/CFT, licensing, capital markets, payment services, fund management, insurance, fintech, and regulatory filings.

---

## MAS Regulatory Framework & Core Requirements

**PROMPT 1 — MAS Regulatory Perimeter Analysis**

I need to determine whether our business activity falls within the MAS regulatory perimeter. Please analyze the following business description and activities: [INSERT DETAILED DESCRIPTION OF BUSINESS MODEL, SERVICES, PRODUCTS, CUSTOMER BASE, AND JURISDICTIONAL PRESENCE].

Using MAS Guidelines on Differentiated Treatment of Financial Institutions and the Financial Services Act (FSA), identify: (1) which regulated activities apply to this business; (2) the specific FSA sections and/or MAS notices that trigger regulatory oversight; (3) whether exemptions from specific requirements exist (e.g., the merchant acquiring exemption, the financial advisory exemption, the insurance intermediary exemption); (4) any timing or transition provisions that apply.

Please cross-reference against MAS Technology Risk Management Guidelines and Payment Systems Act where relevant. Provide a clear summary table identifying each regulated activity, the applicable MAS notice/guideline, and the compliance burden intensity (low/medium/high).

Context: Use when establishing a financial services business or onboarding a new product in Singapore
Difficulty: Intermediate
Best AI tool: Claude / ChatGPT
Follow-up: PROMPT 5 (MAS Notice to Financial Institutions)

---

**PROMPT 2 — MAS Notice Compliance Checklist Builder**

I have received the following MAS Notice: [INSERT FULL TEXT OR TITLE OF MAS NOTICE, e.g., MAS Notice 610 (Internal Audit), MAS Notice 637 (AML/CFT)].

Please create a detailed, risk-weighted compliance checklist for our institution that: (1) breaks down the Notice into its key requirements and sub-requirements, organized by topic; (2) assesses implementation complexity (1-5 scale) for each requirement; (3) identifies interdependencies with other MAS requirements and industry guidelines; (4) highlights any ambiguous or contested interpretations that may require MAS clarification; (5) maps specific requirements to our organization's departments and roles (e.g., Compliance, IT, HR, Audit); (6) suggests timeline for implementation based on realistic assessment of our resources.

Format as an Excel-ready table with columns for: Requirement ID, Requirement Text, Complexity, Owner, Timeline, Current Status, Evidence of Compliance.

Context: When implementing a new MAS regulatory requirement across your organization
Difficulty: Advanced
Best AI tool: ChatGPT / Claude (better at structured output)
Follow-up: PROMPT 3 (Documentation & Evidence Strategy)

---

**PROMPT 3 — MAS Documentation & Evidence Strategy**

We are preparing for MAS examination/inspection in the area of [INSERT AREA, e.g., technology governance, risk management, AML/CFT]. I need to build a comprehensive documentation and evidence strategy to demonstrate compliance.

Please provide: (1) a checklist of typical documentary evidence MAS examiners expect to see for this area (with references to specific MAS Guidelines and Notices); (2) a template for an evidence matrix mapping each regulatory requirement to the specific documents/records we should maintain; (3) guidance on record retention periods, formats (physical vs. electronic), and accessibility; (4) common deficiencies MAS has noted in its last 2-3 years of inspection reports for this area, with practical mitigation strategies; (5) a calendar/timeline for gathering and organizing evidence pre-inspection; (6) a quality assurance framework to ensure documentation is complete, current, and defensible.

Include sector-specific examples where available (e.g., banking, insurance, capital markets).

Context: 6-12 months before anticipated MAS examination or ongoing compliance maintenance
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 4 (MAS Interaction Protocol)

---

**PROMPT 4 — MAS Interaction Protocol & Escalation**

Our institution has received [INSERT COMMUNICATION TYPE: inspection notice, request for information, warning letter, or enforcement action]. The communication concerns [INSERT SUBJECT MATTER].

Please advise on: (1) our statutory obligations for timely response, including any filing deadlines under the FSA and MAS directions; (2) the appropriate approval and escalation pathway within our institution (Board, Senior Management, Compliance, Legal); (3) engagement strategy with MAS—when to proactively engage, when to seek clarification, risk factors that should trigger escalation; (4) format and tone requirements for responses to avoid misinterpretation; (5) privilege considerations—how to structure our response to preserve legal advice privilege; (6) stakeholder management (disclosure to auditors, bankers, insurers, ratings agencies); (7) public disclosure obligations (SGX announcements, financial reporting disclosures); (8) dispute resolution options if we disagree with MAS position.

Context: Upon receipt of regulatory communication from MAS
Difficulty: Advanced
Best AI tool: Claude / Copilot
Follow-up: PROMPT 6 (Risk Rating & Supervisory Engagement)

---

**PROMPT 5 — MAS Notice to Financial Institutions Implementation**

MAS has issued [INSERT NOTICE REFERENCE AND TITLE, e.g., "Notice on Technology Governance for Financial Institutions"]. We are a [INSERT INSTITUTION TYPE: bank, insurance, fund manager, fintech, payment service provider].

Using this Notice and related guidance documents: (1) identify the 5-7 core strategic and operational changes this Notice requires; (2) assess our current state of maturity against the Notice requirements using a 1-5 scale (1=non-compliant, 5=best practice); (3) create a phased roadmap (24-36 months) showing: Quick Wins (achievable in 0-6 months), Medium-term Changes (6-18 months), Long-term Structural Changes (18-36 months); (4) estimate budget and resourcing requirements for each phase; (5) identify overlaps with other regulatory requirements to create efficiencies; (6) document key risks and mitigation strategies for each phase; (7) define success metrics and key performance indicators to track progress.

Context: When MAS issues new or updated regulatory guidance
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 7 (Technology Implementation & Testing)

---

**PROMPT 6 — MAS Risk Rating & Supervisory Engagement Strategy**

I need to understand how MAS rates our institution's risk profile and supervisory approach. Please provide: (1) an overview of MAS's Supervisory Framework for [INSERT INSTITUTION TYPE], including how risk ratings are assigned; (2) the key risk categories and indicators MAS typically focuses on; (3) common reasons for rating upgrades/downgrades based on recent MAS inspection and enforcement trends; (4) strategies to proactively engage with MAS to improve our institution's risk profile; (5) how changes in our business model, strategy, or governance should be communicated to MAS; (6) best practices for managing our relationship with MAS's assigned supervisor/examiner team; (7) impact of risk rating changes on regulatory requirements, supervisory intensity, and capital/liquidity requirements.

Include reference to MAS's latest annual Financial Stability Review and supervisory priorities.

Context: Ongoing relationship management with MAS; when planning strategic changes
Difficulty: Intermediate
Best AI tool: Claude / ChatGPT
Follow-up: PROMPT 1 (Regulatory Perimeter Analysis)

---

## FCA/SEC Cross-Reference & International Coordination

**PROMPT 7 — UK/US Regulatory Requirements Mapping (Singapore Hub)**

Our Singapore-based [INSERT ENTITY TYPE: wealth management, fund manager, investment bank, fintech] serves clients/conducts business in the UK and/or US. I need to understand regulatory overlaps and conflicts.

Please provide: (1) a matrix comparing key regulatory frameworks—MAS vs. FCA (UK) and MAS vs. SEC (US)—for [INSERT SPECIFIC AREA: market abuse, MiFID II / Reg SHO / short selling, suitability/best execution, AML/CFT, data protection, conduct risk]; (2) identification of conflicting requirements and practical workarounds; (3) regulatory hierarchy—which jurisdiction's rules take precedence in specific scenarios; (4) cost-benefit analysis of dual-compliance vs. choosing a primary jurisdiction; (5) common pitfalls multinational firms face in managing multiple jurisdictions; (6) regulatory change tracking—how to monitor FCA/SEC initiatives that may affect our Singapore operations; (7) notification/licensing requirements for Singapore firms operating into these markets.

Context: When expanding operations or managing cross-border services
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 8 (Market Conduct Regulation)

---

**PROMPT 8 — Market Conduct & Conduct Risk (MAS/FCA Alignment)**

We are operationalizing a market conduct and conduct risk program for our Singapore entity serving international clients. Please create a comprehensive framework that aligns MAS expectations (MAS Guidelines on Conduct of Financial Advisers, MAS Principles of Market Conduct) with FCA expectations (COBS rules, market abuse regime).

Structure should include: (1) definition of "market conduct" and "conduct risk" in both regulatory regimes; (2) 12-15 specific conduct areas (e.g., front-running, unsuitable advice, misrepresentation, conflicts of interest, communications fairness, complaint handling); (3) for each conduct area: MAS requirement vs. FCA requirement, how they differ, operational controls to satisfy both; (4) governance framework—Board and management oversight, training, monitoring, escalation; (5) case studies of recent MAS and FCA enforcement actions relevant to similar institutions; (6) annual audit/testing plan to validate conduct controls; (7) whistleblowing and incident management protocols.

Context: Building or enhancing market conduct programs for regulated entities
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 14 (AML/CFT Control Framework)

---

## AML/CFT Compliance & Financial Crime Prevention

**PROMPT 9 — MAS AML/CFT Risk Assessment Framework**

We need to conduct a comprehensive AML/CFT risk assessment in accordance with MAS Notice 626 (Notice on AML/CFT). Please help me build an assessment framework that: (1) covers all required risk assessment areas per MAS Notice 626—institutional risk, customer risk, product/service risk, delivery channel risk, geographic risk; (2) includes a detailed questionnaire (50+ questions) for each risk area; (3) provides a risk rating scale (Low/Medium/High) with clear criteria for each rating; (4) produces a risk profile heat map identifying our institution's highest-risk areas; (5) maps findings to specific AML/CFT control requirements—the higher the risk, the more robust the controls; (6) documents assumptions and data sources; (7) includes a plan for periodic reassessment (annually, or when material business changes occur).

Format as a workable Excel template with scoring, weighting, and output visualizations.

Context: Annual AML/CFT compliance exercise; when launching new products/geographic markets
Difficulty: Advanced
Best AI tool: ChatGPT / Claude (for structured frameworks)
Follow-up: PROMPT 10 (KYC/CDD Procedures)

---

**PROMPT 10 — KYC/CDD/EDD Procedures Design**

I need to design a comprehensive Know Your Customer (KYC), Customer Due Diligence (CDD), and Enhanced Due Diligence (EDD) procedure manual for our [INSERT INSTITUTION TYPE: bank, money changer, remittance, fund manager] in Singapore.

The manual should include: (1) clear triggers for each level of due diligence (KYC baseline, CDD, EDD) based on MAS risk assessment and regulatory categories; (2) information requirements for each level—documents, beneficial ownership investigation, source of funds, politically exposed person (PEP) screening, etc.; (3) timing requirements—when due diligence must be completed relative to account opening or transaction; (4) procedures for verifying identity using government-issued documents, electronic verification methods, and third-party verification providers; (5) specific requirements for high-risk customers (PEPs, high-net-worth, shell companies, trusts); (6) refresh/update procedures for ongoing due diligence; (7) documentation and record-keeping requirements; (8) escalation procedures when information is unclear or suspicious; (9) template forms and checklists; (10) case studies showing application to different customer types.

Include references to MAS Guidelines on Know Your Customer (Guideline 4.1) and sanctions regulations.

Context: Establishing or updating customer onboarding procedures
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 11 (AML/CFT Monitoring & Detection)

---

**PROMPT 11 — Transaction Monitoring & Suspicious Activity Detection**

We operate a transaction monitoring system to identify suspicious activities under MAS Notice 626. Please help me build a comprehensive transaction monitoring and suspicious activity detection program that includes: (1) clear regulatory definition of "suspicious" under MAS Notice 626 and FATF Recommendations; (2) 20+ specific indicators/red flags (e.g., round-dollar transactions, frequency anomalies, geographic inconsistencies, layering patterns, structuring/smurfing); (3) risk-weighted rules engine—different thresholds for different customer risk ratings; (4) system design requirements (data sources, processing frequency, alert generation); (5) procedures for investigating alerts—investigation template, documentation, time limits; (6) decision framework—when to escalate to compliance, report to CCCS/FIU, or close as false positive; (7) quarterly performance metrics (alert volume, accuracy rate, reporting rate); (8) staff training requirements; (9) regulatory reporting (Suspicious Transaction Reports, Suspicious Movement Reports, Currency Transaction Reports to CCCS).

Include specific Singapore regulatory reporting deadlines and formats.

Context: Implementing or optimizing AML transaction monitoring
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 12 (CCCS Reporting & Cooperation)

---

**PROMPT 12 — CCCS Reporting & Regulatory Cooperation**

We have identified suspicious activities that may require reporting to the Corrupt Practices Investigation Bureau (CPIB) or CCCS (Commerce Commission). Please guide me through: (1) the legal obligation to report under Singapore's Corruption, Drug Trafficking and Other Serious Crimes (Cash Transaction Reports) Act and Anti-Money Laundering/Countering Terrorism Financing (AML/CFT) regime; (2) when and how to file Suspicious Transaction Reports (STRs) and Suspicious Movement Reports (SMRs) with the CCCS; (3) procedures to avoid tipping off (alerting the customer that suspicious activity has been reported); (4) protective safeguards for staff involved in reporting; (5) internal documentation requirements—privilege considerations, investigation files, decision records; (6) coordination with external parties (auditors, MAS, law enforcement); (7) follow-up reporting when initial suspicious activity leads to ongoing investigations; (8) regulatory feedback mechanisms—how CCCS communicates back to reporting institutions; (9) case studies of successful prosecutions involving private sector reports.

Context: When suspicious activity has been identified during monitoring
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 13 (Sanctions Screening & OFAC)

---

**PROMPT 13 — Sanctions Screening & OFAC/UN Compliance**

We need to implement comprehensive sanctions screening procedures for MAS and international sanctions (OFAC, UN, EU). Please create a detailed framework covering: (1) Singapore-specific sanctions regimes (MAS directions on sanctions, Schedule to the Constitution, Monetary Authority of Singapore (Sanctions and Freezing of Assets) Regulations); (2) comparison with OFAC (US), UN Security Council, EU sanctions lists; (3) technical screening requirements—how to match customer names/identifiers against sanctions lists; (4) false positive management—procedures when a customer matches a sanctions list; (5) transaction blocking procedures—when and how to prevent transactions; (6) reporting obligations to MAS when sanctions matches occur; (7) internal documentation and approval workflows; (8) staff training on sanctions compliance; (9) periodic audits and testing; (10) integration with KYC and transaction monitoring systems; (11) third-party sanctions screening vendors—evaluation and governance; (12) case studies of enforcement actions for sanctions violations.

Include current MAS-designated terrorist financing lists and targeted financial sanctions designations.

Context: Establishing or enhancing sanctions compliance controls
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 14 (Compliance Programme Framework)

---

**PROMPT 14 — AML/CFT Compliance Programme Design**

MAS Notice 626 requires financial institutions to establish and maintain an AML/CFT compliance programme. Please help me design a comprehensive, board-approved programme that includes: (1) clearly documented AML/CFT policies and procedures covering all of MAS Notice 626 (Sections 11-18); (2) governance structure—Board policy, Senior Management Committee oversight, Compliance function independence and reporting; (3) roles and responsibilities for: Compliance Officer, Branch/Business Unit Heads, Customer-Facing Staff, Finance Team; (4) training and awareness program—initial training, refresher training, role-specific modules, testing and certification; (5) external audit and testing—scope, frequency, audit committee review; (6) MAS reporting—Annual Compliance Certification, incident reporting; (7) review and update mechanisms—when to update policies (business changes, regulatory changes, lessons learned); (8) document retention for 5 years post-transaction; (9) communication cascading—how to disseminate policies throughout the organization; (10) Board and Senior Management sign-off process.

Provide template policies, committee charters, training plans, and audit checklists.

Context: When establishing or overhauling AML/CFT compliance program
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 15 (Regulatory Reporting & MAS Certification)

---

## Licensing, Registration & Authorization

**PROMPT 15 — Financial Services Licensing Pathway**

We intend to offer [INSERT SPECIFIC FINANCIAL SERVICE, e.g., securities trading, fund management, insurance intermediation, money lending, money changing, remittance services] in Singapore. Please provide a comprehensive licensing pathway that includes: (1) identification of which license(s) under the Financial Services Act, Securities and Futures Act, or Insurance Act are required; (2) detailed requirements for each license type—capital, staff qualifications, office location, systems, compliance infrastructure; (3) eligibility criteria for directors, shareholders, and key senior management (fit and proper test requirements); (4) application process steps and timeline; (5) pre-application engagement with MAS (optional but recommended); (6) documentation checklist; (7) fees and costs; (8) post-licensing obligations and conditions; (9) ongoing compliance requirements specific to this license type; (10) periodic reviews/renewals; (11) common application deficiencies and how to avoid them; (12) appeal process if application is rejected.

Include specific references to relevant MAS Notices (e.g., Notice 616 on Fit and Proper Criteria).

Context: When planning to enter a regulated financial services business
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 16 (Fit & Proper Assessment)

---

**PROMPT 16 — Fit & Proper Assessment & Appointment**

We plan to appoint [INSERT NAME AND PROPOSED ROLE: Director, Chief Executive Officer, Chief Risk Officer, etc.] to our financial services institution. Please guide us through the "fit and proper" assessment and appointment process required by MAS, including: (1) the regulatory definition of "fit and proper" under MAS Notice 616 and relevant acts; (2) specific criteria for assessing competence, integrity, and financial soundness; (3) a questionnaire/assessment tool to evaluate the proposed appointee against MAS criteria; (4) background checks and due diligence procedures—criminal record checks, financial history, regulatory history, business conduct record; (5) documentation requirements for the appointment file; (6) prior notification requirements to MAS (notification, approval, or no-action threshold); (7) specific requirements for certain roles (e.g., Chief Executive Officer, Compliance Officer); (8) induction and onboarding requirements; (9) ongoing fitness monitoring during their tenure; (10) disqualification events that would require immediate notification to MAS.

Context: When appointing key personnel to regulated entity
Difficulty: Intermediate
Best AI tool: ChatGPT / Claude
Follow-up: PROMPT 17 (CMS/RFA Registration)

---

**PROMPT 17 — CMS/RFA Representative Registration**

We have hired representatives to conduct [INSERT ACTIVITIES: financial advisory, securities dealing, fund management, insurance intermediation] in Singapore. Please help us navigate the registration requirements under the relevant MAS regulatory framework. For each representative, provide: (1) determination of whether registration is required (some activities/representatives are exempt); (2) identification of the correct registration category (CMS, RFA, or exempt); (3) requirements if registration is required: qualification exams (relevant modules from the Institute of Banking and Finance), fit and proper criteria, training before appointment; (4) application process and documentation; (5) ongoing professional development requirements; (6) code of ethics and conduct obligations; (7) periodic review/renewal; (8) disciplinary procedures if conduct violations occur; (9) notification to MAS of termination or serious violations.

Use specific references to MAS Guidelines and IBF examination frameworks.

Context: When hiring representatives for regulated activities
Difficulty: Intermediate
Best AI tool: ChatGPT / Claude
Follow-up: PROMPT 18 (PI/Promoter Registration)

---

**PROMPT 18 — PI/Promoter Registration for Investment Schemes**

We are organizing an investment scheme (e.g., mutual fund, investment fund, capital guaranteed structured product) in Singapore. Please advise on the registration and approval requirements under the Securities and Futures Act, including: (1) determination of whether the scheme must be registered (collective investment scheme classification); (2) requirements for the promoter/fund manager (financial soundness, key personnel fit and proper); (3) requirements for the custodian/trustee; (4) requirement for a compliant Information Memorandum or Prospectus; (5) ongoing annual returns and financial reporting to MAS; (6) restrictions on marketing and distribution; (7) valuation and pricing requirements; (8) investor protection mechanisms (segregation of assets, audit requirements); (9) periodic management reviews by MAS; (10) amendment/variation procedures; (11) winding-up requirements.

Include specific references to MAS Notice 334 (Collective Investment Schemes) and SFA sections 286-338.

Context: When organizing a new investment scheme in Singapore
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 35 (Fund Management Governance)

---

## Capital Markets Regulation

**PROMPT 19 — Securities Dealing & Market Abuse Prevention**

Our firm engages in securities dealing (trading on behalf of clients and/or proprietary trading) on the Singapore Exchange (SGX). Please create a comprehensive framework covering: (1) core MAS regulatory requirements for securities dealing (MAS Principles of Market Conduct, MAS Guidelines on Conduct of Financial Advisers); (2) market abuse prevention—identifying and preventing front-running, insider trading, market manipulation; (3) internal controls for order management: pre-trade transparency, order review/approval, trade execution best execution procedures, post-trade reporting; (4) conflicts of interest management—Chinese walls, information barriers, blackout periods; (5) communication governance—monitoring of communications to identify potential market abuse; (6) staff training and certification; (7) incident reporting procedures; (8) coordination with SGX and MAS; (9) regulatory reporting requirements; (10) case studies of recent MAS/SGX enforcement against similar firms.

Context: For securities trading operations
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 20 (Corporate Actions & Disclosure)

---

**PROMPT 20 — Corporate Actions, M&A Disclosure & Insider Information**

Our firm advises clients on corporate actions (M&A transactions, capital reorganizations, major contracts, etc.). I need guidance on managing insider information and regulatory disclosure obligations, including: (1) what constitutes "material non-public information" under SFA and MAS regulations; (2) identification of when disclosure to SGX and the market is required (immediate announcements); (3) pre-announcement procedures—timing of disclosure to advisors, investors, and counterparties; (4) trading halts—when to request, how to coordinate with SGX; (5) investor relations communications—what can and cannot be disclosed pre-announcement; (6) blackout periods for insiders—restricting share dealings by company directors and employees; (7) documentation and file management during transaction (privilege considerations); (8) post-announcement obligations; (9) communications with media, analysts, and investors; (10) common disclosure violations and penalties.

Context: For transaction advisory and corporate actions
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 21 (IPO & Capital Raising)

---

**PROMPT 21 — IPO Process & Capital Raising Compliance**

We are advising a company through an Initial Public Offering (IPO) on SGX. Please create a detailed IPO compliance roadmap covering: (1) pre-IPO stages—regulatory determinations (disclosure standards, SGX Listing Rules, SFA compliance); (2) prospectus preparation and MAS approval process; (3) pre-marketing phase—investor relations, due diligence roadshow, quiet period rules (no selective disclosure); (4) offer phase—pricing, trading halt coordination, settlement; (5) post-IPO obligations—quarterly announcements, annual reports, continuing disclosure obligations; (6) corporate governance requirements under SGX Listing Rules Code of Corporate Governance; (7) management of inside information pre-IPO; (8) common deficiencies in IPO documentation noted by MAS/SGX; (9) timeline and key milestone dates; (10) costs and fee structure.

Include specific references to SGX Listing Rules and MAS requirements.

Context: During IPO preparation and execution
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 22 (Rights Issues & Dividends)

---

**PROMPT 22 — Rights Issues, Dividends & Shareholder Communications**

We are assisting a listed company with [INSERT CORPORATE ACTION: rights issue, dividend/bonus share distribution, capital reduction, name change]. Please provide guidance on regulatory requirements and best practices, including: (1) SGX Listing Rules requirements specific to this corporate action; (2) announcement timing and content; (3) circular to shareholders—content requirements, voting procedures; (4) shareholder meeting procedures if required; (5) timing of implementation (ex-date, record date, payment date); (6) impact on share price and trading; (7) tax considerations and disclosure to shareholders; (8) investor communications; (9) regulatory approvals or notifications required; (10) systems and back-office procedures to handle the corporate action; (11) common procedural errors and how to avoid them.

Context: When a listed company is undertaking corporate actions
Difficulty: Intermediate
Best AI tool: ChatGPT / Claude
Follow-up: PROMPT 23 (Analyst Coverage & Communications)

---

**PROMPT 23 — Equity Research, Analyst Coverage & Conflicts of Interest**

Our firm publishes equity research on SGX-listed companies. Please help us establish a research governance framework compliant with MAS and SGX requirements, covering: (1) definition of "research report" and when it triggers regulatory requirements; (2) financial interest disclosure requirements (analyst compensation, firm holdings, underwriting relationships); (3) conflicts of interest between research and investment banking/trading divisions; (4) recommendations and rating systems—definition, revision procedures, basis; (5) factual accuracy and basis for opinions; (6) pre-publication review and approval procedures; (7) restrictions on communications with management and other parties (quiet period rules); (8) distribution controls—timing, recipient identification; (9) use of proprietary models and quantitative methods; (10) disclaimers and legends; (11) record-keeping requirements; (12) staff training on research standards.

Reference MAS Principles of Market Conduct and SGX rules on research.

Context: For equity research production and distribution
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 24 (Short Selling Regulations)

---

**PROMPT 24 — Short Selling & Market Manipulation Prevention**

Our fund or proprietary trading operation engages in short selling activities. Please create a comprehensive short selling compliance framework that includes: (1) overview of Singapore's short selling regime (Regulation 144A/Reg SHO equivalent in Singapore context); (2) operational requirements: locating shares before short sale, delivery timing, fails management; (3) disclosure and reporting requirements for significant short positions; (4) market manipulation considerations—price stabilization, squeeze risks; (5) internal controls and pre-trade checks; (6) coordination with clearing houses and brokers; (7) regulatory reporting to MAS and SGX; (8) crisis management if market manipulation is alleged; (9) recent enforcement actions and lessons learned; (10) best practices from leading global market operators.

Context: For short selling and market abuse prevention
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 25 (Bond Market Regulation)

---

## Payment Services & Digital Assets

**PROMPT 25 — Payment Services Act Licensing & Compliance**

We provide [INSERT PAYMENT SERVICE: e-wallet, money remittance, merchant acquiring, bill payment platform, virtual asset service provider]. Under Singapore's Payment Systems Act (replaced Parts of the FSA), we need to understand licensing requirements and compliance obligations. Please provide: (1) identification of the specific payment service category; (2) determination of whether a Major Payment Institution (MPI) or Exempt Payment Institution (EPI) license is required, or if we're exempt; (3) requirements for each category: capital (percentage of transaction value), systems and security, business continuity, AML/CFT, customer protection, consumer grievance handling; (4) key personnel appointment requirements; (5) application process and MAS engagement; (6) ongoing compliance obligations—MAS reporting (quarterly returns, annual reports), audit, customer fund protection; (7) limits on activities for different license categories; (8) partnership arrangements with other institutions (how to minimize regulatory burden); (9) API and third-party integration governance; (10) cross-border payment rules and foreign exchange considerations.

Context: When launching or licensing a payment service
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 26 (Cyber Security & Operational Resilience)

---

**PROMPT 26 — Virtual Asset Service Provider (VASP) Regulation & Compliance**

We provide virtual asset services (cryptocurrency exchange, custody, lending, staking) in Singapore. Please guide us through the regulatory requirements for Virtual Asset Service Providers under MAS Notice 757 and the Payment Systems (General) Regulations, including: (1) definition of virtual assets and which services trigger VASP licensing; (2) license requirements—capital, systems, governance, AML/CFT; (3) customer due diligence for virtual asset transactions (enhanced requirements due to AML/CFT risk); (4) transaction monitoring for virtual asset movements (detection of structuring, mixing services, unusual patterns); (5) record-keeping and reporting requirements; (6) cross-border virtual asset transaction reporting; (7) custody and segregation of virtual assets (consumer protection); (8) operational risk—cybersecurity, incident response, business continuity; (9) technology risk management specific to blockchain and smart contracts; (10) regulatory cooperation with other APAC and global regulators; (11) compliance with Travel Rule requirements (data sharing for virtual asset transfers); (12) Stablecoin-specific considerations if applicable.

Context: For cryptocurrency/digital asset service providers
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 27 (Fintech Sandboxes & Innovation)

---

**PROMPT 27 — Fintech Regulatory Sandbox & Regulatory Innovation Facilitator**

We are developing a fintech product/service that may not fit existing regulatory categories. We want to explore MAS's Regulatory Sandbox or Regulatory Innovation Facilitator (RIF) programme. Please advise on: (1) eligibility criteria for Sandbox entry (novel technology, consumer benefit, manageable risk); (2) application process and supporting documentation required; (3) sandbox benefits—how does it defer or reduce regulatory obligations; (4) sandbox terms and conditions—duration (typically 6 months, extendable), testing constraints, customer limitations; (5) transition pathway from sandbox to mainstream regulation—timeline and milestones; (6) reporting and monitoring requirements during sandbox period; (7) exit procedures if sandbox testing is unsuccessful; (8) publicizing participation in sandbox (regulatory benefits vs. market perception); (9) case studies of successful sandbox graduates and their regulatory paths; (10) considerations for cross-border sandbox testing (UK FCA Sandbox, etc.).

Context: When developing innovative products that don't fit existing regulatory frameworks
Difficulty: Intermediate
Best AI tool: Claude / ChatGPT
Follow-up: PROMPT 28 (API Governance & Third-Party Risk)

---

**PROMPT 28 — API Governance, Open Banking & Third-Party Risk Management**

We are opening our systems via APIs to third-party developers and partners (open banking model). We need a comprehensive API governance and third-party risk management framework compliant with MAS expectations, including: (1) API security standards and requirements (authentication, encryption, rate limiting, data minimization); (2) third-party vendor assessment framework—onboarding criteria, contracts, audit rights, risk rating; (3) data sharing governance—what data can be shared via API, consent procedures, data localization; (4) operational resilience—API availability, performance, incident management; (5) consumer protection—disclosures, dispute resolution, liability allocation; (6) AML/CFT considerations—ensuring third parties maintain AML controls; (7) cyber security and penetration testing requirements; (8) incident response and breach notification procedures; (9) offboarding procedures when vendor relationships terminate; (10) regulatory reporting and MAS oversight; (11) insurance and indemnification; (12) evolving international standards (ISO/IEC 27001, OWASP API Security).

Context: For open banking and API enablement initiatives
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 29 (Cyber Resilience & Incident Response)

---

## Insurance Regulation

**PROMPT 29 — Insurance Agent/Broker Licensing & Conduct**

We operate an [INSERT: insurance agency, brokerage, bancassurance distribution]. Please guide us through MAS insurance intermediary requirements, including: (1) determination of whether agent or broker license is required; (2) application process and documentation; (3) qualification requirements for insurance agents (exam modules, fit and proper criteria); (4) capital requirements (if applicable for certain brokers); (5) conduct obligations—suitability, disclosure, conflicts of interest, best advice; (6) commissions and fee transparency; (7) client money handling (if applicable); (8) complaints handling procedures; (9) professional indemnity insurance requirements; (10) continuing professional development; (11) regulatory reporting and file maintenance; (12) disciplinary procedures and suspension/cancellation grounds.

Include references to Insurance Intermediaries Act and relevant MAS Guidelines.

Context: When establishing insurance intermediary operations
Difficulty: Intermediate
Best AI tool: ChatGPT / Claude
Follow-up: PROMPT 30 (Insurance Product Governance)

---

**PROMPT 30 — Insurance Product Governance & Suitability**

We develop and distribute insurance products (life, general, travel, etc.). I need to establish a product governance framework aligned with MAS expectations and international standards (EIOPA, ASIC), including: (1) product development process—target market definition, risk assessment, product characteristics, pricing; (2) suitability assessment—when recommending products to customers, matching customer needs to product features; (3) product review and monitoring—ongoing suitability check, market feedback, poor performance exit triggers; (4) communications—FAQs, website disclosures, sales materials, annual policy statements; (5) staff training—product knowledge, suitability assessment, ethical selling; (6) conflicts of interest management—commission structures, tied distribution, alternative compensation; (7) monitoring and testing—supervisory checks, mystery shopping, complaint analysis; (8) remediation procedures when unsuitable sales are identified; (9) record-keeping and file documentation; (10) regulatory reporting to MAS.

Context: For insurance product management and distribution
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 31 (Business Continuity & Insurance)

---

**PROMPT 31 — Insurance Claims Management & Dispute Resolution**

We manage insurance claims and disputes (life claims, general claims, policyholder disputes). Please provide guidance on best practices and regulatory requirements, including: (1) claims handling procedures—initial notification, investigation, documentation, assessment; (2) statutory timeline requirements for claims decisions; (3) partial benefit determination and advance payments; (4) claims investigation framework (preventing fraud, managing third-party claims); (5) disputes and appeals procedures—internal escalation, independent ombudsman referral; (6) Financial Industry Disputes Resolution Centre (FIDREC) requirements and procedures; (7) communications with claimants—clarity, transparency, accessibility; (8) complaints handling—feedback mechanisms, root cause analysis, process improvement; (9) record retention (minimum 5 years post-claim); (10) cyber incidents and data breach notification to customers and MAS; (11) case studies of recent FIDREC cases and insurance ombudsman decisions.

Context: For claims operations and customer dispute management
Difficulty: Intermediate
Best AI tool: ChatGPT / Claude
Follow-up: PROMPT 32 (Policyholder Communications)

---

## Regulatory Filings & Notifications

**PROMPT 32 — MAS Annual Reporting & Regulatory Returns**

We are preparing our institution's annual regulatory returns and financial reporting to MAS. Please create a comprehensive filing checklist and timeline, including: (1) identification of all required annual filings (audit reports, financial statements, compliance certifications, prudential returns, AML/CFT certification); (2) specific requirements for each filing—format, content, sign-off requirements, submission timeline; (3) comparative analysis to statutory accounting (book vs. regulatory); (4) financial ratio calculations and thresholds (capital adequacy, liquidity, concentration limits); (5) balance of payments and foreign exchange disclosures (if applicable); (6) audit certifications and independence requirements; (7) data integrity and controls—validation procedures, system reconciliations; (8) pre-filing review checklist by internal teams; (9) sign-off procedures (CEO, CFO, Audit Committee, Board); (10) submission procedures (electronic filing systems, acknowledgment); (11) error correction/amendment procedures; (12) timeline for MAS review and feedback.

Context: During annual reporting and regulatory compliance cycles
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 33 (Capital Adequacy & Stress Testing)

---

**PROMPT 33 — Capital Adequacy & Stress Testing**

We are managing capital adequacy and conducting stress testing as required by MAS. Please provide detailed guidance on: (1) MAS capital requirements framework (if applicable to your institution type—banks, insurers, securities firms); (2) calculation of capital ratios and risk-weighted assets; (3) treatment of different asset types under risk weights; (4) operational and market risk capital calculations; (5) stress testing framework—macro-economic scenarios, reverse scenarios, concentration risks; (6) stress test model development and validation; (7) scenario definition—interest rates, credit spreads, FX rates, equity prices, property prices; (8) impact assessment—capital adequacy under stress, liquidity stress, earnings pressure; (9) escalation procedures—when stress results indicate capital concerns; (10) board reporting and strategic responses to stress test findings; (11) regulatory communication—when to notify MAS of capital adequacy concerns; (12) internal capital adequacy assessment processes (ICAAP).

Context: For capital planning and prudential compliance
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 34 (Liquidity Management)

---

**PROMPT 34 — Liquidity Risk Management & Regulatory Reporting**

We are implementing a liquidity risk management framework aligned with MAS requirements. Please provide comprehensive guidance on: (1) liquidity risk definitions and regulatory framework (MAS Guidelines on Liquidity Risk Management); (2) cash flow maturity analysis and liquidity gap reporting; (3) liquidity coverage ratio (LCR) and net stable funding ratio (NSFR) calculations (if applicable); (4) funding sources assessment—stability, concentration, diversification; (5) liquidity stress testing—crisis scenarios, behavioral assumptions, recovery actions; (6) intraday liquidity management and settlement risk; (7) contingency funding planning—trigger events, escalation, communication; (8) collateral management and availability; (9) market access monitoring—market confidence indicators, funding cost trends; (10) regulatory reporting (quarterly/annual liquidity returns); (11) Board reporting on liquidity; (12) coordination with treasury and business unit managers on liquidity constraints.

Context: For liquidity and treasury risk management
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 35 (Fund Management Governance)

---

**PROMPT 35 — Fund Management Governance, Valuations & Investor Reporting**

We manage investment funds and need to establish strong governance and investor reporting frameworks. Please provide guidance covering: (1) fund governance—Board oversight, management meetings, policies and procedures; (2) valuation policies—asset pricing, illiquid asset valuation, fair value hierarchy; (3) valuation governance—independent price verification, dispute resolution, valuation committee; (4) investor reporting—prospectus updates, periodic fact sheets, annual reports, performance disclosures; (5) performance calculation methodologies (time-weighted, money-weighted, sector benchmarking); (6) comparative disclosure (vs. benchmarks, vs. peer funds); (7) fee structures and fee disclosure; (8) redemption/distribution procedures—fair treatment of investors, timing, documentation; (9) related-party transactions—approval, disclosure, arm's length testing; (10) regulatory audit requirements; (11) fund winding-up or restructuring procedures; (12) MAS reporting and fund statistics.

Context: For asset management and fund administration
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 36 (Outsourcing & Service Provider Management)

---

**PROMPT 36 — Outsourcing Governance & Third-Party Service Provider Management**

We outsource key functions [INSERT: IT, payroll, operations, compliance, AML monitoring] to third-party service providers. I need a comprehensive outsourcing governance framework compliant with MAS expectations, including: (1) determination of "critical functions" where outsourcing governance is mandatory (MAS Guidelines on Outsourcing of Financial Services); (2) assessment of service provider suitability—financial soundness, operational capability, security controls, geographic location; (3) contractual requirements—service level agreements, security provisions, audit/inspection rights, termination clauses; (4) ongoing monitoring and performance metrics; (5) cyber security and data protection requirements (including data localization); (6) contingency planning and business continuity arrangements; (7) MAS notification procedures for certain outsourcing arrangements; (8) customer notification requirements; (9) exit procedures—transition planning, data retrieval, service continuity; (10) audit and compliance monitoring; (11) concentration risk management when multiple critical functions are outsourced to the same provider; (12) intra-group outsourcing considerations.

Context: When establishing or reviewing outsourced service arrangements
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 37 (Technology & Cyber Risk Management)

---

**PROMPT 37 — Technology Risk Management & MAS Technology Risk Governance**

We need to strengthen our Technology Risk Management framework aligned with MAS Guidelines on Technology Risk Management. Please provide guidance on: (1) technology risk definition and MAS framework overview; (2) technology risk assessment—system dependencies, obsolescence, technical debt; (3) information security framework—CISO/Head of Technology role and responsibilities, Board oversight; (4) system development lifecycle (SDLC)—security by design, testing, deployment controls; (5) incident response and breach notification (MAS Notice on Cyber Hygiene and MAS Technology Risk Guidelines); (6) business continuity and disaster recovery—RTO/RPO targets, testing frequency, failover procedures; (7) third-party technology vendor assessment and monitoring; (8) cloud computing governance—security, data sovereignty, exit strategies; (9) emerging technology risk (AI/ML, blockchain, API gateway); (10) threat landscape monitoring and proactive defense; (11) penetration testing and vulnerability assessments; (12) cyber insurance and risk transfer.

Context: For IT governance and technology risk compliance
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 38 (Data Protection & Privacy)

---

**PROMPT 38 — Personal Data Protection Act (PDPA) Compliance & Privacy**

We process customer personal data and need to ensure PDPA compliance. Please create a comprehensive PDPA compliance framework that includes: (1) PDPA scope and core requirements—consent, collection notice, legitimate purpose, accuracy, protection, retention, right to access/correct; (2) consent procedures and documentation—explicit consent timing and evidence; (3) privacy notices—content requirements, accessibility, multilingual considerations; (4) data minimization—collecting only necessary data; (5) third-party data sharing—recipient assessment, contractual requirements, customer notification; (6) cross-border data transfers—restrictions and safeguards; (7) data retention and deletion procedures; (8) customer rights management—access requests, correction requests, withdrawal of consent; (9) data security measures—encryption, access controls, audit logging; (10) data breach incident management and PDPC notification; (11) Data Protection Impact Assessments (DPIA) for high-risk processing; (12) vendor/processor contracts and audit rights; (13) staff training and accountability.

Context: For all entities handling customer personal data
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 39 (Complaints Handling & Escalation)

---

**PROMPT 39 — Customer Complaints Handling & Regulatory Escalation**

We process customer complaints and need robust procedures aligned with MAS expectations. Please develop a comprehensive complaints management framework covering: (1) complaints definition and capture—multiple channels (email, phone, in-person, ombudsman referrals); (2) assessment and categorization—complaint type, complexity, urgency; (3) investigation procedures—fact gathering, liability assessment, remediation options; (4) resolution timelines—MAS expectations (28 days for most complaints, expedited for urgent); (5) escalation triggers—amounts, complexity, patterns, potential enforcement risk; (6) communication with complainants—acknowledgment, interim updates, resolution notification; (7) remediation mechanisms—refunds, account credits, apology letters, systemic improvements; (8) trends analysis—root cause analysis, process improvements, staff retraining; (9) regulatory reporting to MAS (annual complaints statistics, escalated complaints); (10) Financial Industry Disputes Resolution Centre (FIDREC) referral procedures; (11) documentation and record retention (minimum 5 years); (12) board reporting on complaints metrics.

Context: For customer service and compliance operations
Difficulty: Intermediate
Best AI tool: ChatGPT / Claude
Follow-up: PROMPT 40 (Governance & Risk Management)

---

**PROMPT 40 — Board & Senior Management Governance**

We need to strengthen Board and Senior Management oversight of regulatory compliance. Please create a governance framework that includes: (1) clear Board committee structure (Audit Committee, Risk Committee, Compliance Committee); (2) Board policies on oversight of key risk areas (credit, market, operational, technology, compliance, AML/CFT); (3) senior management roles and responsibilities—Chief Risk Officer, Chief Compliance Officer, Chief Information Officer; (4) regular Board reporting cadence and metrics (quarterly risk reports, annual compliance certification, AML/CFT certification); (5) escalation procedures for regulatory matters—when to involve Board, triggers for outside counsel engagement; (6) Board self-assessment and effectiveness review; (7) induction program for new Board members on regulatory obligations; (8) director and officer liability insurance; (9) conflict of interest policies for Board members; (10) Board interaction with external auditor and MAS; (11) annual Board approval of regulatory strategy and compliance budgets; (12) documentation of Board decisions and minutes.

Context: Ongoing governance and regulatory oversight
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 41 (Business Continuity & Resilience)

---

**PROMPT 41 — Business Continuity Planning & Operational Resilience**

We need to develop a comprehensive Business Continuity Plan (BCP) and Operational Resilience framework aligned with MAS expectations. Please provide guidance on: (1) business continuity framework overview—strategy, roles, testing; (2) criticality assessment—critical business functions, interdependencies, recovery time objectives (RTO), recovery point objectives (RPO); (3) risk identification—natural disasters, pandemics, cyber attacks, third-party failures, key person dependencies; (4) contingency strategies—backup systems, alternative locations, supplier redundancy, manual procedures; (5) communication plan during disruptions—staff, customers, regulators, media; (6) testing and exercising—tabletop exercises, simulation tests, full-scale tests, frequency; (7) documentation—BCP manual, procedure runbooks, contact lists; (8) third-party dependencies and BCP coordination; (9) recovery team structure and training; (10) post-incident review and continuous improvement; (11) Board and MAS notification procedures; (12) insurance for business interruption.

Context: For business continuity and operational risk management
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 42 (Stress Testing & Scenario Analysis)

---

**PROMPT 42 — Scenario Analysis & Stress Testing Framework (Advanced)**

We are building an advanced stress testing and scenario analysis framework for strategic planning and risk management. Please provide comprehensive guidance on: (1) macroeconomic scenario development—interest rate movements, credit cycles, property cycles, FX dynamics; (2) idiosyncratic scenarios—competitor actions, regulatory changes, technology disruptions; (3) reverse stress testing—what scenarios would threaten viability; (4) impact modeling—how scenarios affect revenues, costs, capital, liquidity; (5) interconnectedness analysis—how shocks propagate through systems; (6) concentration risks—large customer/sector/counterparty exposures; (7) feedback effects—how outcomes in one area trigger changes in others (e.g., rising losses trigger capital concerns which trigger funding stress); (8) model governance—model development, validation, governance, limitations; (9) assumption transparency—documenting scenario assumptions and sensitivities; (10) communication to Board and stakeholders; (11) decision-making based on stress results—capital planning, hedging strategies, business adjustments; (12) emerging risks not yet captured in historical data (e.g., climate risk, geopolitical risk).

Context: For strategic planning, capital management, and risk oversight
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 43 (Regulatory Change Tracking)

---

**PROMPT 43 — Regulatory Change Tracking & Compliance Pipeline**

We need a systematic process to monitor, analyze, and implement changes in Singapore and APAC financial regulation. Please create a "Regulatory Change Pipeline" that includes: (1) monitoring mechanisms—MAS website, SGX bulletins, industry association alerts, regulatory horizon scanning; (2) change identification and filtering—which changes apply to us; (3) impact assessment—scope of change, implementation requirements, timeline, resource needs; (4) prioritization framework—regulatory urgency, business impact, implementation complexity; (5) project planning—workstreams, milestones, resource allocation, budget; (6) cross-functional communication—disseminating changes to affected departments; (7) testing and validation—confirming systems/procedures align with new requirements; (8) documentation updates—policy revisions, procedure updates, training materials; (9) staff training and certification; (10) implementation sign-off and evidence of compliance; (11) periodic audits confirming ongoing compliance; (12) horizon scanning for anticipated regulatory changes (consultation papers, parliamentary bills, international developments).

Context: Ongoing regulatory governance and compliance management
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 44 (Regulatory Relationship Management)

---

**PROMPT 44 — Proactive Regulatory Relationship Management**

We want to establish a proactive, positive relationship with MAS and other regulators. Please advise on best practices and strategies including: (1) pre-engagement protocol—when to voluntarily engage with MAS on new products, business models, or risks; (2) structured dialogue—regular meetings with MAS supervisor/examiner team, agenda setting, follow-up documentation; (3) transparency and early warning—notifying MAS of significant business changes, risk escalations, compliance concerns before they become enforcement issues; (4) responding to MAS inquiries—procedures for timely, complete, accurate responses; (5) managing MAS examinations—inspector reception, data requests, accommodation, documentation management; (6) working with MAS on remediation—agreeing timelines, progress reporting, completion certification; (7) industry participation—contributing to MAS public consultations, participating in industry working groups, providing market insights; (8) reputation and public perception—aligning public statements with MAS expectations, avoiding public disputes; (9) communication protocol for MAS interaction (designating points of contact, escalation procedures); (10) documentation of MAS interactions and regulatory feedback; (11) annual review of MAS feedback and areas for improvement; (12) learning from regulatory enforcement against competitors.

Context: Ongoing relationship management and regulatory engagement
Difficulty: Intermediate
Best AI tool: Claude / ChatGPT
Follow-up: PROMPT 1 (Regulatory Perimeter Analysis) — cycle back to assess changing perimeter

---

## Summary

This Financial Regulation library comprises 44 detailed prompts covering Singapore MAS requirements, FCA/SEC cross-reference, AML/CFT compliance, licensing, capital markets, payment services, fund management, insurance, and comprehensive regulatory filings and governance frameworks. Each prompt is designed for deep implementation and provides practical, actionable guidance for legal and compliance professionals in the APAC region.
