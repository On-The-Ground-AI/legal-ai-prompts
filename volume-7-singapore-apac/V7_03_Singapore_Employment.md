# AI Prompts for Singapore Employment Law

## Overview
Singapore employment law is governed primarily by the Employment Act (Cap. 91), the Ministry of Manpower (MOM) regulations, and industry-specific frameworks. This prompt library focuses on practical scenarios involving employment contracts, statutory obligations, workplace disputes, and regulatory compliance specific to Singapore's labor market.

---

## SECTION 1: EMPLOYMENT ACT COMPLIANCE

**PROMPT 1 — Employment Contract Review for Singapore Statutory Compliance**

I have an employment contract for a [POSITION TITLE] role in [COMPANY NAME] operating in Singapore. The contract includes: [DESCRIBE KEY TERMS: salary structure, working hours, leave provisions, probation period, termination clause]. Please analyze this contract against the Singapore Employment Act (Cap. 91) and identify:

1. Any provisions that conflict with or fall below statutory minimums (e.g., Section 37 minimum wage, Section 43 maximum working hours of 44 hours/week, Section 53 annual leave entitlements)
2. Whether mandatory clauses under the Employment Act are present (e.g., section 10 essential terms, section 66 gratuity if applicable)
3. Specific risks if this is a [EMPLOYEE TYPE: domestic worker / foreign worker / part-time employee], noting different statutory protections for each category
4. Whether termination-related clauses comply with Section 14 (unfair dismissal) and Section 15 (notice requirements and in-lieu-of-notice payments)
5. Recommendations for amendments to strengthen protection or ensure full compliance

Context: Use when negotiating employment terms, onboarding new staff, or reviewing existing contracts pre-dispute.
Difficulty: Intermediate
Best AI tool: Claude
Follow-up: PROMPT 2 (Wrongful Dismissal Analysis)

---

**PROMPT 2 — Wrongful Dismissal Claim Analysis Under Singapore Employment Act**

My client [CLIENT NAME] was dismissed from their position as [JOB TITLE] on [DISMISSAL DATE] by [EMPLOYER NAME]. The stated reason was [DISMISSAL REASON]. Before dismissal, [DESCRIBE RELEVANT FACTS: disciplinary warnings, performance issues, layoff context, procedural steps taken].

Analyze whether this dismissal constitutes wrongful termination under Singapore law by examining:

1. Compliance with Section 14 of the Employment Act (definition of unfair dismissal—no legitimate reason, inadequate notice, or procedures violated)
2. Whether the employer provided proper notice period (Section 5 states default is 1 month unless contract specifies shorter) or paid in-lieu-of-notice compensation
3. If this is a retrenchment, whether Section 71A obligations were met (notice to MOM, redundancy gratuity calculations per Section 71)
4. Whether dismissal procedures followed natural justice (opportunity to be heard, investigation if misconduct-based)
5. Available remedies: reinstatement, compensation up to 2 months' salary under Section 14(6), and aggravated damages for procedural unfairness
6. Limitation period (2 years from dismissal date per Section 138) and any evidence preservation urgency

Context: Use when advising employees on potential claims or employers assessing exposure.
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 17 (Workplace Dispute Resolution Strategy)

---

**PROMPT 3 — Section 71 Retrenchment Gratuity Calculation & MOM Notification**

[EMPLOYER NAME] is retrenching [NUMBER] employees due to [REASON: restructuring/downsizing/business closure]. The affected employees include: [LIST: names, position, salary, length of service in years]. Calculate the retrenchment gratuity payable to each employee under Section 71 of the Employment Act, which mandates:

- Employees with 2+ years of continuous service: 1 month's salary (for first 3 years service) + 1/2 month's salary (for each additional year after 3 years), capped at the last 12 months' average salary
- Maximum gratuity: 4 months' salary regardless of length of service

For each affected employee:
1. Confirm continuous service eligibility (breaks, leave without pay, non-renewal of contract terms)
2. Calculate gratuity based on salary definition (basic + fixed allowances, excluding overtime, discretionary bonuses, etc.)
3. Cross-check against any contractual enhanced gratuity entitlements (which supersede statutory minimums)
4. Note any non-monetary deductions (pending disciplinary findings, loan repayments—permissible under Section 71(7))
5. Draft the MOM Section 71A notification form (required before actual retrenchment)
6. Identify employee data needed to avoid disputes (length of service records, salary slips for 12-month average)

Context: Use during layoffs, business closures, or when calculating severance obligations.
Difficulty: Intermediate
Best AI tool: Claude
Follow-up: PROMPT 4 (CPF Contribution Settlement)

---

**PROMPT 4 — CPF Contribution Settlements & Employee Overpayment Disputes**

[EMPLOYER NAME] has identified a discrepancy in CPF contributions for employee [EMPLOYEE NAME] spanning [DATE RANGE]. The issue involves: [DESCRIBE: incorrect salary reported to CPFB, missed contributions, overpayment by employer due to calculation error]. The amount in question is SGD [AMOUNT].

Analyze the employer's obligations and remedies under the Central Provident Fund Act (Cap. 36) and MOM guidelines:

1. Confirm whether this is an undercontribution (employer liability to pay arrears + late interest to CPFB) or overcontribution (whether employee must refund or employer absorbs as discretionary bonus)
2. Calculate interest accrued: CPFB charges statutory interest at 1% per annum on late contributions, compounded quarterly
3. Determine if the error triggers MOM enforcement action or CPFB's debt collection process
4. Assess whether the employee's CPF withdrawal eligibility is affected (retirement account shortfall, housing withdrawal restrictions)
5. Draft settlement/correction options: (a) employer pays CPFB arrears + interest, (b) payment plan if cash flow constrained, (c) offset from future salary (only with employee written consent per Section 23 restrictions)
6. Document the correction in the employer's payroll and notify CPFB within statutory timeframes to avoid compound penalties

Context: Use when addressing payroll compliance issues, pre-termination CPF settlement, or responding to MOM audits.
Difficulty: Intermediate
Best AI tool: Claude
Follow-up: PROMPT 5 (MOM Inspection Preparation)

---

**PROMPT 5 — MOM Inspection & Audit Preparation Checklist**

[EMPLOYER/HR MANAGER NAME] has received a notice from the Ministry of Manpower (MOM) scheduling an inspection on [DATE] regarding [INSPECTION SCOPE: general compliance / specific complaint / fatal accident investigation]. The notice references [REFERENCE CODE/COMPLAINT DETAILS].

Prepare a comprehensive audit checklist and action plan covering:

1. **Document Compilation**: Organize employment contracts (all current + last 3 years' terminated employees), salary records, CPF contribution statements, leave records (annual, medical, emergency), overtime logs, contract renewal/termination correspondence
2. **Statutory Compliance Review**: Cross-check all employment contracts for Section 10 terms, verify leave entitlements (Section 43: minimum 7 days annual leave for first 5 years, 8 days thereafter), confirm working hours do not exceed 44/week per Section 43(3), verify gratuity arrangements
3. **MOM Regulations Check**: Verify Foreign Worker Levy paid (if applicable), work permits/passes current, Work Injury Compensation Insurance (WICI) valid, no violations of Ministry's Workplace Safety and Health Act requirements
4. **Complaint-Specific Preparation** (if applicable): Document disciplinary procedures if misconduct-related complaint; gather medical reports and incident investigation files if injury-related; compile communication records if discrimination/harassment alleged
5. **Personnel Interview Preparation**: Brief all managers on permitted scope of questioning, ensure HR representative present during interviews, prepare factual responses to anticipated questions
6. **Remedial Actions Before Inspection**: Rectify any readily identifiable breaches (unpaid gratuity, missing contract terms, overdue leave compliance) to demonstrate good-faith compliance

Context: Use when receiving MOM notices, preparing for routine audits, or managing complaint investigations.
Difficulty: Intermediate
Best AI tool: Claude
Follow-up: PROMPT 6 (Workplace Safety & Health Compliance)

---

## SECTION 2: MOM REGULATIONS & WORKPLACE SAFETY

**PROMPT 6 — Workplace Safety & Health Act (WSH Act) Compliance & Incident Investigation**

An incident occurred at [WORKPLACE LOCATION] on [DATE] involving [DESCRIPTION: slip and fall, equipment malfunction, chemical exposure, etc.]. The injured employee is [EMPLOYEE NAME], suffering [INJURY TYPE]. The employer [EMPLOYER NAME] is now facing a potential WSH Act investigation or claim.

Conduct a comprehensive WSH Act compliance review:

1. **Immediate Post-Incident Obligations**: Verify that (a) first aid was administered, (b) serious injury was reported to MOM within 24 hours if loss of consciousness, severe fracture, or hospitalization occurred per Section 119, (c) incident scene was preserved for investigation
2. **Workplace Health & Safety Assessment**: Review whether the employer conducted a Risk Assessment for the hazard involved (mandatory under Section 11—failure is strict liability offense); identify whether control measures were inadequate (hierarchy of controls: elimination, substitution, engineering, administration, PPE)
3. **Compliance Documentation**: Obtain the employer's WSH Policy (mandatory under Section 36), accident reporting and investigation procedures, relevant permits (e.g., confined space work, hot work), maintenance records for equipment involved, and safety training records for affected workers
4. **Investigation Depth**: Determine whether the employer conducted a timely root-cause investigation identifying not only immediate cause but systemic failures (training gaps, maintenance lapses, procedure violations)
5. **Regulatory Exposure**: Assess potential offenses: Section 12 (failure to ensure health & safety), Section 11 (inadequate risk assessment), Section 18 (inadequate provision of safe systems of work); penalties range from SGD 5,000 (fine) to SGD 800,000 (imprisonment up to 2 years for grievous bodily harm)
6. **Remedial Steps**: Document all corrective actions implemented post-incident and communicate to relevant authorities if requested

Context: Use following workplace incidents, preparing responses to MOM notices, or advising employers on WSH compliance.
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 7 (Work Injury Compensation Claims)

---

**PROMPT 7 — Work Injury Compensation Insurance (WICI) Claims & Employee Entitlements**

[EMPLOYEE NAME] suffered a [INJURY/ILLNESS TYPE] on [DATE] while employed by [EMPLOYER NAME]. The employer carries Work Injury Compensation Insurance (WICI) with [INSURER NAME]. The employee is claiming [DESCRIBE CLAIM: medical expenses, wage compensation during absence, permanent injury benefit, dependents' benefits if fatal].

Analyze the claim under Singapore's work injury compensation framework:

1. **Coverage Eligibility**: Confirm the employee qualifies (full-time employment, registered with insurer on injury date); verify no exclusions apply (e.g., occupational disease, pre-existing condition unrelated to work)
2. **Accident vs. Occupational Disease**: Distinguish whether this is a covered "accident" (sudden, identifiable event) per Section 3 definition, or occupational disease (Work Injury Compensation and Occupational Diseases Act definitions)
3. **Medical Expenses**: Claim limited to SGD 3,000 (or higher if hospitalized) for approved medical providers; verify all invoices are from MOM-accredited facilities or GPs
4. **Wage Compensation**: First 3 days borne by employer; from day 4-365, insurer pays 70% of normal wages (capped at SGD 2,800/month, indexed annually) for total incapacity; calculation based on last month's earnings (including basic salary + fixed allowances)
5. **Permanent Disability/Death Benefits**: Assess disability rating if injury results in permanent impairment (Schedule of Injuries sets percentage awards, e.g., loss of limb = 100%); calculate lump-sum benefit (percentage × SGD 254,500 standard amount); death benefits to dependents include funeral expenses (SGD 1,200) + monthly allowance scaled to dependents' ages
6. **Claim Process & Deadlines**: Ensure notice to insurer within 30 days of accident; verify Form 8 (claim form) submitted with supporting medical reports, wage evidence, employer statement

Context: Use when employees injured at work, assessing compensation claims, or managing insurer correspondence.
Difficulty: Intermediate
Best AI tool: Claude
Follow-up: PROMPT 8 (Foreign Worker Management & Regulations)

---

**PROMPT 8 — Foreign Worker Recruitment, Levy Payment & Compliance Management**

[EMPLOYER NAME] intends to hire [NUMBER] foreign workers for [JOB CATEGORY: manufacturing/construction/marine/domestic work] positions. The worker categories are [SPECIFY: Work Permit Level 5, Employment Pass, S Pass, Dependant's Pass]. Current workforce composition: [DESCRIBE] locals, [DESCRIBE] foreign workers.

Prepare a comprehensive foreign worker management and compliance framework:

1. **Levy Calculation & Payment**: Determine applicable Foreign Worker Levy (FWL) by category: Level 5 Work Permit (unskilled): SGD 0 (March 2024 rate); S Pass (semi-skilled): SGD 580/month; Employment Pass Level 1-2: typically SGD 0-580 depending on salary tier; confirm employer's monthly payroll runs concurrent with MOM's billing cycle; verify no arrears from previous employees
2. **Entitlement to Work Scheme**: Confirm worker's eligibility (age, skill level, health clearance); verify employer is in approved sectors; check Complementarity Assessment (CA) if applicable for sector (non-domestic, in-principle approval for certain roles since 2020)
3. **Employment Pass Restrictions**: If hiring EP holders, confirm salary meets MOM minimums (current: SGD 5,000+/month for Level 1/2 depending on sector), no local recruitment required if role listed as specialist/executive, and employer's financial standing is sound (ACRA filings reviewed)
4. **Housing & Safety**: Comply with foreign worker housing regulations (where applicable); ensure accommodation standards, security, and safety requirements per MOM guidelines; register hostel if employer-provided
5. **Contract & Repatriation**: Draft employment contract in worker's native language covering salary, leave, termination, repatriation provisions; mandatory return-to-work requirement at contract end unless renewed
6. **Breach & Penalties**: Understand consequences of non-compliance: overstaying workers, undeclared workers incur fines up to SGD 10,000 (employer) + SGD 20,000 (worker), plus potential contract cancellation and debarment from hiring

Context: Use when planning foreign worker recruitment, managing compliance renewals, or assessing levy obligations.
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 9 (Non-Compete & IP Assignment Enforcement)

---

## SECTION 3: CONTRACTUAL ENFORCEMENT & IP PROTECTION

**PROMPT 9 — Non-Compete & Restraint of Trade Clause Enforceability in Singapore**

[EMPLOYER NAME] has a departing employee [EMPLOYEE NAME] who is subject to a non-compete clause in their employment contract, dated [DATE]. The clause states: "[QUOTE EXACT CLAUSE]". The employee is planning to join competitor [COMPETITOR NAME] in [LOCATION/ROLE DESCRIPTION] starting [DATE]. The original employment was in the [INDUSTRY] sector in Singapore, covering [DESCRIBE: customer relationships, technical knowledge, business development area].

Analyze the enforceability of this non-compete restriction under Singapore common law and equitable principles:

1. **Reasonableness Test (Nordenfelt Principle)**: Assess the clause against three-part test: (a) Is the scope reasonable to protect legitimate business interests (trade secrets, confidential information, customer relationships, training investment)? (b) Is the geographic scope limited to areas where employer had actual business presence (Singapore-only? APAC-wide?)? (c) Is the duration reasonable (typically 6 months for routine roles, 1-2 years for senior/technical roles)?
2. **Blue-Pencil Doctrine**: If clause is overbroad, determine whether Singapore courts would apply "blue pencil" severance to strike unreasonable portions, or whether entire clause is void as unenforceable
3. **Legitimate Business Interests**: Assess strength of employer's protectable interest: (a) confidential information/trade secrets (specificity and actual confidentiality matter), (b) customer relationships (duration of relationship, switching costs, identified customer list), (c) training investment (extent and recency)
4. **Employee Hardship & Public Interest**: Consider whether enforcement would impose undue hardship on employee restricting livelihood, or public interest in employee mobility (courts disfavor restraints limiting general skill employment)
5. **Remedies Available**: If enforceable, injunctive relief (interim & final) to prevent competition; damages claims for actual losses (if breached) calculated as lost profits during restriction period or customer/revenue diversion; employer must demonstrate actual loss, not speculative damage
6. **Practical Enforcement Strategy**: Timeline for obtaining interim injunction (Court application within days), evidence needed (contract, proof of employee's new role, proof of competition), likelihood of success assessment

Context: Use when employee departure triggers non-compete concern, or when defending against employer injunction.
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 10 (IP Ownership & Work-Related Assignment Disputes)

---

**PROMPT 10 — Intellectual Property Ownership Disputes in Employment Context**

[EMPLOYEE NAME], formerly employed by [COMPANY NAME] as [JOB TITLE] (employment period: [DATES]), has created/developed [DESCRIBE IP: software code/patent-eligible invention/design/business process/written work]. The employee [HAS/HAS NOT] assigned IP rights per their employment contract, which states: "[QUOTE RELEVANT CLAUSE]".

[DISPUTE SCENARIO: Company claims ownership; employee claims independent creation; third party now seeks to license/acquire IP.]

Analyze IP ownership rights and enforceability under Singapore law:

1. **Copyright Ownership**: Under Copyright Act (Cap. 63), originality vests in creator (employee) by default, UNLESS the contract explicitly assigns copyright to employer OR creation falls within employment scope (specifically assigned duties). Assess whether: (a) employee's job description explicitly included creating this work type, (b) contract includes "work-made-for-hire" language specific enough to transfer ownership, (c) creation was made during working hours using employer resources (strong inference of assignment, but not conclusive without express clause)
2. **Patent Ownership**: Patents do not automatically vest in employer under Singapore law (unlike some jurisdictions). The Patent Act (Cap. 221) provides that if an employee invents something related to employer's business OR developed using employer resources/confidential information, employer has right to equitable compensation (even if employee retains ownership), UNLESS contract assigns patents to employer
3. **Trade Secrets & Confidential Information**: Regardless of formal ownership, if the IP embodies trade secrets (confidential technical/business information with independent economic value), employer may enforce confidentiality restrictions post-employment, preventing employee from using/disclosing secrets even if ownership is unclear
4. **Contract Interpretation Issues**: Review clarity of assignment clause (does it cover inventions during employment only, or post-employment?); distinguish between "background IP" (pre-existing employee work) and "foreground IP" (created during employment—typically assigned); confirm whether employee signed acknowledgment/assignment form at creation time
5. **Equity & Fiduciary Duties**: Even absent express assignment, if employee held senior position (director, manager overseeing innovation), courts may imply obligation to assign IP to employer due to fiduciary duty, particularly if IP created using confidential information or employer resources
6. **Remedies & Licensing Strategy**: If ownership disputed, interim declarations sought; if infringement alleged, injunctive relief to prevent licensing to third parties; damages calculated as lost licensing/sale revenue; settlement typically involves IP assignment/co-ownership + retrospective compensation

Context: Use when IP ownership disputed post-employment, defending against employer IP claims, or investigating third-party IP transactions.
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 11 (Trade Secrets & Confidential Information Breaches)

---

**PROMPT 11 — Trade Secrets & Confidential Information Breach — Injunction & Damages**

[EMPLOYEE NAME] or [THIRD-PARTY NAME] has disclosed/misappropriated confidential information belonging to [COMPANY NAME] by [DESCRIBE: sharing customer list with competitor, selling source code, using proprietary method at new company, leaking trade secrets to media]. The information includes [SPECIFY: customer database, manufacturing process, pricing information, business strategy documents]. The breach occurred on [DATE] and was discovered on [DATE].

Analyze the claim and remedies under Singapore common law (trade secrets/breach of confidence) and statutory framework:

1. **Three-Part Test for Confidential Information** (Coco v A.N. Clark): (a) Does the information have necessary quality of confidence (not public domain, genuinely secret, specific/identifiable)? (b) Was it communicated in circumstance importing obligation of confidence (employment relationship creates presumption; third party may have implied notice of confidentiality)? (c) Would disclosure cause unauthorized use causing damage (financial loss, competitive harm, client/customer relationship loss)?
2. **Trade Secrets Specificity**: Distinguish between general industry knowledge (non-protectable) and specific trade secrets (protectable): customer list with contact info/transaction history, proprietary formulas/methods, pricing strategies tied to specific customers, strategic business plans, source code. The more specific and compiled the information, the stronger the claim
3. **Employee's Knowledge**: Confirm employee signed confidentiality agreement (facilitates injunction) and received notice that certain information was trade secrets (confidential labeling, restricted access, compartmentalization). Absence of written notice weakens claim but does not eliminate it if circumstances show obvious confidentiality
4. **Breach Mechanics**: Identify how breach occurred (email to third party, bringing documents away, verbal disclosure, incorporation of secrets into new company's processes) and extent of disclosure (full or partial, to competitors or public, one disclosure or ongoing)
5. **Equitable Remedies**: (a) Interim injunction: court grants if serious issue to be tried + balance of convenience favors plaintiff + applicant shows uncompensable harm if disclosure continues; (b) Final injunction: if breach established, restrains further disclosure/use; (c) Delivery up: compels return of confidential documents
6. **Damages Assessment**: Calculated as lost profits from diverted customers, lost licensing fees from sale of confidential information, cost of remediation/replacement, or disgorged profits earned by wrongdoer using secrets. Damages typically difficult to quantify; account of profits (wrongdoer's gains) sometimes available as alternative remedy

Context: Use when discovering confidential information breaches, pursuing employee injunctions, or defending breach allegations.
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 12 (TAFEP Fair Employment Compliance & Discrimination Claims)

---

## SECTION 4: FAIR EMPLOYMENT & DISPUTE RESOLUTION

**PROMPT 12 — TAFEP Fair Employment Compliance & Discrimination Risk Assessment**

[EMPLOYER NAME] (sector: [INDUSTRY], size: [NUMBER] employees) seeks to conduct a fair employment audit against Tripartite Alliance for Fair and Progressive Employment Practices (TAFEP) guidelines. [OPTIONAL: Following a recent complaint from [CLAIMANT NAME] alleging [TYPE: age discrimination/gender discrimination/disability discrimination/nationality discrimination] in context of [HIRING/PROMOTION/TERMINATION/COMPENSATION].]

Conduct a comprehensive TAFEP compliance assessment:

1. **Recruitment & Selection**: Review job advertisements for non-discriminatory language (avoid age specifications, gender preferences, nationality restrictions unless justified by genuine occupational qualification); confirm selection criteria assess competency (qualifications, experience, skills) not protected characteristics; verify interview panels diverse and trained on unconscious bias; assess whether recruitment consultants briefed on non-discrimination requirements
2. **Pay Equity Analysis**: Compare salary/benefits across demographic groups (gender, age, nationality) for same/similar roles; investigate unexplained pay gaps (legitimate factors: experience level, performance, market rates, contract terms); TAFEP guidelines suggest regular audits to identify and remedy systematic discrimination
3. **Promotion & Development**: Confirm advancement decisions based on performance, merit, competency demonstrated; assess whether certain groups disproportionately excluded from leadership pipeline; verify talent development opportunities (training, mentoring, secondment) equally available regardless of demographic status
4. **Termination Practices**: Review if termination, retrenchment, or redundancy selection disproportionately affects protected groups (e.g., only older workers selected for retrenchment, female workers targeted for exit); confirm objective selection criteria and documentation of decisions
5. **Complaint & Grievance Handling**: Verify employer has clear, accessible formal channels for reporting discrimination; assess whether complaints investigated promptly and impartially; confirm no retaliation against complainants (retaliation itself violates TAFEP principles)
6. **Policy & Culture**: Review employee handbook for non-discrimination policy, diversity statement, accessibility accommodations (for employees with disabilities); assess workplace culture through employee surveys for evidence of inclusion/exclusion
7. **Remedial Actions**: If gaps identified, develop action plan (policy amendments, training programs, pay equity corrections, promotion review, grievance process enhancement); timeline for implementation and accountability metrics

Context: Use for routine compliance audits, responding to discrimination complaints, or pre-litigation risk assessment.
Difficulty: Intermediate
Best AI tool: Claude
Follow-up: PROMPT 13 (Formal Dispute Resolution — Mediation & Adjudication)

---

**PROMPT 13 — Employment Dispute Resolution Strategy — Mediation vs. Adjudication**

[PARTY NAME: Employee/Employer] has a [DISPUTE TYPE: wrongful dismissal / unfair retrenchment / salary/gratuity non-payment / discrimination / breach of contract] dispute with [OTHER PARTY]. The facts are: [DESCRIBE DISPUTE IN DETAIL: background, key events, amounts at stake, current impasse]. Previous informal resolution attempts: [DESCRIBE OR STATE "None yet"].

Develop a comprehensive dispute resolution strategy evaluating all available forums and tactics:

1. **Mediation Pathway**: (a) Informal negotiation through mutual advisors (lower cost, preserve relationship, quicker timeline); (b) Formal mediation through mediator (Singapore Mediation Centre provides mediation services; confidential, facilitates settlement); (c) Tripartite mediation through MOM's Tripartite Dispute Resolution Program (free, MOM mediator, focused on industrial relations disputes); assess likelihood of settlement (employer cash flow constraints, employee credibility of claim, pride factors)
2. **Adjudication Pathway**: (a) MOM's Employment Inspectorate (if involving statutory rights: minimum wage, leave entitlements, gratuity, notice period—investigates and makes determination binding on employer; costs are borne by MOM); (b) Arbitration before Arbitrator appointed under Employment Act Section 115 (limited to issues arising under the Act; awards can be enforced; confidential process); (c) Civil Court claim (District Court for claims up to SGD 250,000, High Court above—full contract/tort remedies available; public proceedings; longer timelines, higher costs)
3. **Strategic Analysis**:
   - **Mediation Pros**: Faster (4-8 weeks), lower cost, relationship preservation, business-friendly, parties retain control, higher satisfaction rates
   - **Mediation Cons**: No binding power if unsuccessful; weak negotiating position if party has weak case; may signal weakness to other party
   - **Arbitration Pros**: Specialist employment arbitrator, confidential, faster than court, expert decision-maker
   - **Arbitration Cons**: Limited appeal rights, arbitrator fees shared by parties, limited discovery, statutory remedies only
   - **Court Pros**: Full remedies available, precedent value, enforcement through court machinery
   - **Court Cons**: High cost (lawyer fees, court fees, expert witnesses), slow (2-3 years), public proceedings, technical procedural rules
4. **Strengths & Weaknesses Assessment**: (a) For applicant's case: strength of evidence, sympathetic facts, damages quantification clarity, witness availability; (b) For respondent's case: legal defenses, procedural breaches by applicant, counterclaims; (c) Risk evaluation for both parties: best-case vs. worst-case outcomes
5. **Timing Considerations**: Note any limitation periods (wrongful dismissal/breach of contract claims: 6 years under Limitation Act Cap. 163; MOM claims: 2 years from breach date per Employment Act Section 138); assess urgency (employee interim income needs, employer reputational risk)
6. **Recommended Pathway**: Provide phased approach: (a) Stage 1: Attempt mediation (4 weeks, low-cost, settlement-focused); (b) Stage 2: If mediation fails, escalate to [Arbitration/Court] with clear timeline, document preservation instructions, witness preparation
7. **Settlement Negotiation Framework**: Establish settlement authority parameters (employer: maximum financial offer + non-admission clause; employee: minimum amount + reference letter/severance package terms); identify non-monetary interests (timing, confidentiality, rehiring agreement)

Context: Use when employment dispute arises, evaluating best forum, or preparing clients for dispute resolution process.
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 14 (Sexual Harassment & Workplace Misconduct Investigation)

---

**PROMPT 14 — Sexual Harassment & Workplace Misconduct Investigation Protocol**

[COMPLAINANT NAME] has alleged [DESCRIBE SEXUAL HARASSMENT OR MISCONDUCT: unwanted physical contact, verbal harassment, quid pro quo situation, hostile work environment, retaliation] by [RESPONDENT NAME/POSITION] on [DATES/ONGOING PERIOD]. The alleged conduct occurred at [LOCATION]. Witness(es): [NAMES if known]. [EMPLOYER NAME] must now conduct a formal investigation.

Prepare a comprehensive investigation protocol compliant with Singapore law and best practices:

1. **Interim Protective Measures**: (a) Immediately advise both parties that investigation is underway and retaliation is prohibited; (b) implement temporary work arrangement to separate complainant and respondent (different shifts, temporary reassignment) to prevent further contact; (c) document interim measures taken; (d) note that retaliation (adverse action against complainant for making complaint) is independently actionable and voids any disciplinary findings against complainant
2. **Investigation Scope & Terms of Reference**: Define scope (What specific conduct is alleged? Over what period? What outcome sought?); confirm independence of investigator (external investigator preferred if serious allegation or respondent is senior); establish timeline (investigation should complete within 30 days unless complex); clarify confidentiality obligations and information-sharing boundaries
3. **Evidentiary Collection**: (a) Request written account from complainant with specific dates, times, witnesses, impact (document within 3 days); (b) obtain respondent's written response (opportunity to be heard per natural justice); (c) interview witnesses separately, document statements verbatim, avoid influencing narratives; (d) preserve physical evidence (emails, text messages, photographs, workplace layout); (e) obtain workplace CCTV footage if relevant and available
4. **Credibility Assessment**: Evaluate consistency of accounts (internal contradictions, corroboration), witness reliability (proximity to events, independent knowledge), temporal proximity (immediately reported vs. delayed report—delay does not negate claim), patterns if multiple allegations against respondent, and complainant's motive (legitimate grievance vs. personal vendetta—rare in harassment cases)
5. **Legal Standards for Sexual Harassment**: Under common law and TAFEP guidelines, assess whether conduct constitutes sexual harassment (unwanted sexual conduct, conduct with sexual element that is reasonably perceived as hostile/offensive/intimidating). Conduct does not require sexual motivation; intent irrelevant; objective reasonableness standard applied (would reasonable person in complainant's position find conduct offensive/unwelcome?)
6. **Disciplinary Outcomes**: If investigation confirms allegations, determine appropriate discipline (warnings, suspension, termination) proportionate to conduct severity; consider respondent's prior disciplinary history, acknowledgment/remorse, organizational impact; ensure consistency with disciplinary policy applied to similar offenses
7. **Documentation & Communication**: Document all investigation steps (interviews, evidence reviewed, findings, reasoning); prepare written findings within timelines; communicate outcome to complainant and respondent separately; advise complainant of external remedies (police report for criminal conduct, civil suit, MOM complaint, CCDC complaint if applicable) if serious; advise respondent of appeal process if termination
8. **Follow-Up & Monitoring**: Confirm no retaliation occurs post-investigation; provide support (counseling services referral) if appropriate; conduct follow-up interview with complainant to confirm hostile environment has ended; document ongoing monitoring

Context: Use when sexual harassment or serious misconduct complaint received, ensuring compliant investigation protecting employer and providing fairness to both parties.
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 15 (Union Negotiation & Collective Agreement Enforcement)

---

**PROMPT 15 — Union Representation & Collective Bargaining Agreement Interpretation**

[EMPLOYER NAME] employs [NUMBER] union members represented by [UNION NAME] (affiliated with [PARENT FEDERATION if applicable]). A [DESCRIBE: wages dispute / benefits dispute / work condition dispute / disciplinary matter involving union member / proposed change to work rules] has arisen. The current Collective Bargaining Agreement (CBA) is dated [DATE] and expires [DATE]. [OPTIONAL: Union has issued notice of intention to negotiate new CBA / formal dispute notice regarding alleged CBA breach.]

Analyze the employer's obligations and strategic approach under Singapore's union framework:

1. **Statutory Framework**: Confirm employer's registration with Ministry of Manpower (unions must be registered per Industrial Arbitration Act); verify union's negotiating authority (CBA must be signed by authorized union representatives); understand right to strike/arbitration: industrial disputes resolved through tripartite mediation or arbitration before strike permitted (Industrial Arbitration Act Sections 35-48); strikes/lockouts without resolution mechanism are illegal
2. **CBA Interpretation**: Review relevant CBA clause(s): (a) Wage scales and increments; (b) Benefits (medical, dental, insurance); (c) Hours of work and overtime premiums; (d) Leave entitlements; (e) Disciplinary procedures; (f) Grievance handling; (g) Union recognition and dues collection; (h) Management prerogatives clause (identify if employer retained discretion disputed by union)
3. **Specific Disputes**: (a) **Wage Disputes**: Confirm wage changes comply with CBA (e.g., no unilateral cuts, merit increases within negotiated parameters); distinguish between contractual entitlements and discretionary benefits; (b) **Dismissal of Union Member**: Confirm disciplinary procedure followed CBA (often requires union representation at discipline meetings, opportunity to respond); ensure no discrimination against member for union activity (strictly prohibited); (c) **Work Rule Changes**: If CBA restricts management's ability to unilaterally change work rules, proposed change may be "subject matter" of collective bargaining, requiring negotiation before implementation
4. **Negotiation Process & Deadlock Resolution**: If CBA expires and new negotiation underway: (a) Schedule bargaining sessions at reasonable intervals; (b) engage in good faith negotiations (not merely going through motions); (c) make genuine attempts to resolve differences; (d) if negotiation reaches impasse (both parties remain firm despite extended discussions), refer to conciliation through MOM's Conciliation & Mediation Board; (e) if conciliation fails, either party may apply for arbitration through Singapore's Industrial Arbitration Court—arbitration award is binding
5. **Strike/Industrial Action Risk**: Assess likelihood (union member satisfaction with negotiations, history of industrial action, union leadership strength, membership vote on strike authorization); if strike threatened, evaluate employer impact (critical production? service disruption risk?) and strategic response (whether to make final offer, contingency staffing plans, communicate with customers/regulators)
6. **Strategic Options**: (a) **Concession Strategy**: Identify areas where employer can offer gains to union (wage increase within budget, improved benefits) in exchange for union acceptance of management's priorities (flexibility on work rules, no increase in staffing demands); (b) **Dispute Avoidance**: Review any disputed CBA interpretation with union in early discussion rather than implementing unilaterally; (c) **Non-Union Workforce**: Confirm no erosion of union's negotiating position by shifting work to non-union contract staff (careful—if practice undermines collective agreement, may be unfair labor practice); (d) **Legal Preparation**: If union challenges employer action (e.g., dismissal of member, unilateral rule change), prepare defense (contractual authority, compliance with CBA procedures, non-discriminatory rationale)
7. **Dispute Resolution**: Prepare for Conciliation & Mediation Board conciliation (informal process focusing on settlement); if mandatory arbitration required, prepare detailed submissions on CBA interpretation, evidence of past practice, employer's business justification for position

Context: Use during union negotiations, CBA expiry/renewal, alleged CBA breaches, or when industrial relations dispute arises.
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 16 (Retrenchment & Collective Dismissal Procedures)

---

**PROMPT 16 — Mass Retrenchment Planning & Collective Redundancy Procedures**

[EMPLOYER NAME] (sector: [INDUSTRY], workforce size: [TOTAL], union status: [Unionized/Non-unionized]) is planning a significant workforce reduction of [NUMBER] employees ([PERCENTAGE]%) due to [REASON: business restructuring/market downturn/technological change/merger/facility closure]. Affected departments: [LIST]. Timeline: implementation by [DATE]. Current status: [Decision stage/Pre-notification planning/Post-notification in progress].

Develop a comprehensive retrenchment strategy compliant with statutory and contractual requirements:

1. **Notification & Consultation Obligations**: (a) **Union Consultation** (if unionized): Notify union of intention to retrench and consult on selection criteria, timeline, severance packages **before** informing affected employees—tripartite consultation recommended under MOM guidelines; (b) **MOM Notification**: Complete MOM Form 8 (Notification of Retrenchment) stating number of employees, positions, criteria for selection, and attach MOM-approved redundancy package details; (c) **Employee Notification**: Provide written notice to each affected employee (recommended minimum 30 days advance notice, though statutory requirement is regular notice period: typically 1 month); notification should state reason, effective date, severance entitlement, and applicable support services
2. **Selection Criteria & Non-Discrimination**: Establish objective, documented selection criteria (last-in-first-out [LIFO] by seniority, performance-based, role-specific redundancy, plant closure); ensure criteria do not discriminate against protected groups (age, gender, race, nationality, union membership, disability); document selection rationale for each individual to defend against discrimination claims; TAFEP scrutiny will focus on whether retrenchment disproportionately affected particular groups
3. **Redundancy Package Calculation**: (a) **Statutory Entitlements**: Section 71 gratuity (1 month for first 3 years + 1/2 month per year after, capped at 4 months' salary); accrued annual leave payout; notice period (unless paid in-lieu); (b) **Enhanced Package** (if offered): Above-statutory gratuity (common practice: 1.5-2 months per year of service), outplacement support, training/upskilling funds, early termination option (enhanced benefits for voluntary take-up), ex-gratia bonus; document enhanced package clearly (oral promises create ambiguity and disputes)
4. **Financial Planning & Cash Flow**: Model total retrenchment cost (statutory entitlements × affected employees + voluntary offers + outplacement + potential litigation provisions); confirm cash position sufficient; consider phasing if immediate lump-sum unaffordable; negotiate with union (if applicable) on payment schedule if needed; maintain contingency for severance disputes/litigation
5. **Retention & Transition**: Identify critical roles/people required for transition period (wind-down of operations, knowledge transfer to remaining staff, customer account handover); consider retention bonuses (clawback terms if employee leaves before transition completion); plan succession/promotion for remaining staff to address capability gaps
6. **Outsourcing & Subcontracting Risk**: If retrenchment is driven by outsourcing (e.g., manufacturing to vendor), ensure no implicit assumption that employees can be re-hired by vendor at reduced terms—this does not constitute true separation and may trigger wrongful dismissal claims; confirm vendor relationship does not create direct employment relationship with original employer's employees (otherwise employer remains liable for their entitlements)
7. **Litigation & Dispute Preparedness**: Anticipate wrongful dismissal claims (some employees may argue selection was unfair/discriminatory despite criteria); prepare evidence of business necessity and proper selection process; reserve legal contingency in budget; consider offering structured settlement option to reduce litigation risk (employee receives modest additional payment in exchange for waiver of wrongful dismissal claim—document clearly to avoid enforceability disputes)
8. **Outplacement & Support Services**: Arrange job placement services, resume support, interview coaching; provide notice of employer-sponsored counseling; direct to statutory retraining (SkillsFuture credit), CPF Housing/health-related withdrawals available to retrenchees with 10+ years service; communicate these supports to reduce employee distress and associated grievances
9. **Reputational & Stakeholder Management**: Prepare communication for remaining employees (messaging focused on business continuity, retained roles, career development for survivors), customers (assurance of ongoing service capability), and media (transparent business rationale without sensitive commercial details); acknowledge impact on affected employees while explaining business necessity

Context: Use during business restructuring, facility closures, or significant workforce reductions to ensure compliance and minimize disputes.
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 17 (Workplace Dispute Resolution & Negotiation Strategy)

---

**PROMPT 17 — Complex Employment Dispute Resolution & Negotiation Framework**

[PARTY NAME] is involved in a multi-faceted employment dispute with [OTHER PARTY] involving [DESCRIBE: multiple alleged breaches—e.g., wrongful dismissal + unpaid salary + benefits fraud + non-compete breach]. The dispute involves [NUMBER] employees / affects [DEPARTMENT/DIVISION]. Alleged damages: [AMOUNT/MULTIPLE ISSUES]. Previous resolution attempts: [DESCRIBE OR NONE].

Develop a sophisticated dispute resolution and negotiation strategy addressing the entire dispute ecosystem:

1. **Dispute Mapping & Issue Prioritization**: Map all individual disputes (organize by strength: strong claims, moderate, weak); distinguish liabilities (employer's clear exposure, ambiguous, defensible); calculate damages range for each claim; prioritize issues for negotiation focus (high-value, high-risk items first); identify non-monetary interests (references, non-disparagement, rehiring, public statement) that may unlock settlement
2. **Stakeholder Impact Analysis**: Assess who benefits from settlement vs. continued dispute (management vs. union, complainant vs. employer, third parties); identify emotional/pride factors preventing settlement (ego of decision-makers, perceived injustice, need to "save face"); consider impact on remaining employees (morale, retention risk if dispute public, confidence in employment security)
3. **Mediation Strategy**: (a) Identify mediator (MOM tripartite program if industrial relations focus; Singapore Mediation Centre for general disputes; private mediator if complex/high-value); (b) prepare mediation statement (concise narrative of dispute, legal position, settlement objectives, authority to settle); (c) strategize opening offer (often first offer anchors negotiation—consider whether to make first offer or respond to other party); (d) establish settlement parameters (walk-away point for both parties, areas of flexibility, non-negotiables)
4. **Legal Strength Assessment**: Analyze for each claim: (a) Probability of success if litigated (strong = 75%+, moderate = 50-75%, weak = <50%); (b) Likely remedies if successful (damages quantum, injunctive relief, specific performance feasibility); (c) Litigation costs & timeline; (d) Calculate expected value: (Probability of Success × Likely Damages) − Litigation Costs = Settlement Range; this provides objective framework for evaluating settlement offers
5. **Alternative Dispute Resolution Mechanisms**: Beyond mediation: (a) Expert determination (if technical issue like bonus calculation, salary dispute on contractual interpretation); (b) baseball arbitration (each party submits final number, arbitrator chooses one as-submitted, encourages realistic final offers); (c) structured negotiation with phased decision points (resolve liability first, then damages; resolve quick-win issues to build momentum)
6. **Negotiation Tactics & Behavioral Dynamics**: (a) **Information Management**: Control what information revealed (discovery in litigation is involuntary; in mediation, can control narrative); (b) **BATNA Assessment** (Best Alternative to Negotiated Agreement): Understand other party's BATNA (if litigation is attractive for them because employer's exposure high, settlement demands will be higher); (c) **Anchoring**: First number in negotiations influences final range; research optimal first offer; (d) **Reciprocity**: Make concession to elicit reciprocal concession; avoid appearing weak (concede strategically, not reflexively); (e) **Principled Negotiation**: Frame settlement around objective criteria (industry standards, legal precedent) rather than positional bargaining
7. **Settlement Structure & Documentation**: (a) **Payment Terms**: Lump-sum vs. installment (installment reduces immediate cash impact but creates enforcement risk); (b) **Conditions**: Severance conditioned on sign-on of release; timing of payment relative to signing; (c) **Release Scope**: Broad release (waives all claims including unknown claims) vs. narrow (only specified claims); employee likely demands limitations (future whistleblower claims, statutory breach claims, retaliation claims often excluded from releases); (d) **Confidentiality & Non-Disparagement**: Mutual or one-way?; carve-outs for legal proceedings, regulatory compliance, internal business need-to-know; (e) **References**: What future employer reference will employer provide?; written reference or verbal only?; (f) **Rehiring**: Is re-engagement possible/excluded? (g) **Tax Treatment**: Confirm settlement structure (redundancy payment vs. bonus) for tax efficiency; severance may be partially tax-exempt in Singapore if structured as redundancy gratuity
8. **Dispute Escalation & Litigation Preparation**: If mediation fails: (a) Decide forum (MOM arbitration for statutory claims, District/High Court for contract/tort claims); (b) engage litigation counsel for pleading drafting; (c) implement litigation hold on documents (preserve all relevant emails, files, communications); (d) prepare witnesses (interviews with key witnesses to assess testimony quality); (e) quantify damages carefully (lost wages calculation, benefits, reputational harm quantification—punitive damages rare in Singapore employment law)
9. **Risk Allocation in Multi-Party Context**: If dispute involves multiple employees with differing claims: (a) Offer differentiated settlement packages (some claims worth more than others; settlement amounts reflect claim strength); (b) avoid appearing to reward spurious claims with same settlement amount as valid claims (morale issue); (c) consider structured deals (example: high-value wrongful dismissal claim settled at 70% of demand; low-value unpaid leave claim settled at 90% of demand, reflecting relative strength)

Context: Use for complex multi-issue employment disputes, major retrenchment litigation, or settlement negotiations involving multiple claimants.
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 1 (Employment Contract Review) for post-settlement contract revisions

---

**PROMPT 18 — Director & Officer Duties in Employment Relationships**

[DIRECTOR/OFFICER NAME], a director of [COMPANY NAME] (Singapore-incorporated company), is involved in a dispute involving [DESCRIBE: alleged wrongful dismissal of employee, alleged breach of employee's contractual rights, alleged discriminatory employment practice, alleged non-payment of statutorily-mandated benefits]. The affected employee claims [DESCRIBE ALLEGED HARM]. The company may be liable; additionally, the director personally may face allegations of breach of duty.

Analyze the director's and company's legal exposure under Singapore law:

1. **Statutory Duties of Directors Under Companies Act**: Directors owe duties to the company (not directly to employees), but these duties constrain how directors manage employment matters: (a) **Duty of Care** (Section 403A): Director must exercise care and diligence reasonably expected of person in that position (objective standard); mismanaging employment law (e.g., ignoring MOM regulations, failing to implement statutory safeguards) may constitute breach if director's negligence caused loss; (b) **Duty of Honesty** (Section 403B): Directors must act honestly in exercise of powers; if director deliberately mismanages employment matters or conceals non-compliance, breach likely
2. **Fiduciary Duties & Employee Relationships**: While fiduciary duty runs to the company (not to employees), if director's conduct causes employee harm (e.g., fraudulent misrepresentation in employment contract, theft of employee's trade secrets), director may face personal liability in tort/equity: (a) **Inducement Fraud**: Director misstated employment terms to induce employee's acceptance; (b) **Breach of Confidence**: Director misused employee's confidential information; (c) **Negligent Misstatement**: Director provided false information about job role/compensation relied upon by employee
3. **Personal Liability for Employment Law Breaches**: In certain circumstances, director may be personally liable: (a) **Statutory Offense Liability**: Under WSH Act Section 42, officers (including directors) may be personally liable for corporate breaches if conduct was within officer's knowledge/responsibility; (b) **Non-Payment of Wages**: If director directed that employee not be paid statutory entitlements, director may face personal liability under Employment Act Section 133; (c) **Wrongful Dismissal**: Director may be personally liable if dismissal decision was director's personal instruction (though more commonly employer company is liable)
4. **Due Diligence & Risk Management**: To reduce director exposure: (a) Ensure employment law compliance systems are in place (HR policies, legal review of contracts, compliance calendar); (b) document employment decisions (performance reviews, disciplinary procedures, decision rationale); (c) seek external legal advice for material employment decisions; (d) maintain adequate employment liability insurance; (e) ensure company adequately funds employment-related liabilities (gratuity reserves, tax provisions)
5. **D&O Insurance Implications**: Directors' & Officers' Liability insurance typically covers (a) defense costs for personal liability claims; (b) damages awards against directors individually; but excludes (a) criminal conduct/fraud; (b) deliberate law violations; (c) claims arising from director's dishonesty. Confirm coverage scope if employment-related claim arises
6. **Enforcement & Remedies**: Employees suing for wrongful dismissal/breach typically sue the company, not individual director. However, if director conduct was egregious (fraud, intentional tort), employee may pursue personal liability: (a) In court action against both company and director; (b) demand director's personal indemnity from director's personal assets; (c) seek to pierce corporate veil (rare—requires evidence director deliberately used company as instrument of fraud/illegality)

Context: Use when director faces personal employment liability exposure, assessing risk management obligations for boards, or defending against claims of personal director liability.
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 2 (Wrongful Dismissal Claim Analysis) for substantive employment claims

---

**PROMPT 19 — Probation Period Management & Performance Management During Probation**

[EMPLOYEE NAME] was hired by [EMPLOYER NAME] on [DATE] for position [TITLE] with an agreed probation period of [DURATION: e.g., 3 months] per employment contract. During probation, [DESCRIBE: performance issues, conduct concerns, health issues, training insufficiency]. The employer is now considering [DECIDE: termination at end of probation / early termination during probation / extension of probation].

Analyze the legal framework and risk management strategy for probation matters:

1. **Statutory Treatment of Probation Under Employment Act**: Singapore law does not distinguish probation legally from regular employment (unlike some jurisdictions). Once contract is executed, employee is entitled to most statutory protections: (a) **Minimum Wage**: Applies during probation (Section 37: no minimum, but any agreed wage must be paid in full); (b) **Leave Entitlements**: Section 43 annual leave applies only after 3 months continuous service (during probation, leave is not accrued unless contract grants it); (c) **Notice/Termination**: Section 5 applies (notice period per contract or statutory default of 1 month applies during probation unless contract specifies different period); (d) **Gratuity**: Section 71 applies (gratuity only after 2+ years service, so not applicable during initial probation); (e) **Unfair Dismissal**: Section 14 applies during probation—employer cannot dismiss without fair reason and procedure unless contract legitimizes probationary termination without reason
2. **Contractual Probation Clauses**: Many employment contracts include probation provisions stating employee can be terminated during/at end of probation "without cause" or "at employer's discretion." **Critical legal issue**: Such clauses may be unenforceable as contrary to statutory protections if they purport to eliminate all fairness protections. Conservative approach: Probation clause should state it is subject to statutory rights (e.g., "employee may be terminated during probation provided statutory notice/fairness procedures are observed")
3. **Performance Management During Probation**: Best practice minimizes dispute risk: (a) **Clear Expectations**: Communicate job requirements, expected performance standards, training timeline at start; (b) **Regular Feedback**: Conduct monthly check-ins (not just informal chat, but documented conversations); (c) **Interim Reviews**: At 1 month and 2 months (if 3-month probation) formally assess against criteria; (d) **Documentation**: Record conversations, performance concerns, expectations, and employee responses; (e) **Support**: If performance gaps identified, clarify whether role fit issue (employee unsuitable) or competency gap (additional training may remedy)
4. **Probation Extension vs. Termination Decision**: If performance is borderline: (a) **Extension Rationale**: Consider extension (additional 1-3 months) if: competency gap addressable with training, role fit uncertain, employee shows improvement trajectory; document reasons for extension in writing; (b) **Termination Rationale**: Proceed to termination if: core competencies absent, conduct concerns despite warnings, role misfit evident, training efforts have failed; ensure termination decision has documentary support
5. **Termination During Probation—Procedural Compliance**: Even if contract permits probationary termination, observe basic fairness to minimize wrongful dismissal risk: (a) Provide notice period or pay in-lieu (unless contract explicitly waives); (b) give employee opportunity to respond to concerns (brief meeting); (c) document reasons for termination and employee's response; (d) ensure decision is not discriminatory (not selecting for termination based on age, gender, race, etc.); (e) provide reference (or confirm what reference will state) to avoid defamation claims
6. **Wrongful Dismissal Risk During Probation**: Employee can challenge probationary termination by arguing: (a) Contractual probation clause is void (restricts statutory rights unreasonably); (b) termination was unfair (no legitimate reason per Section 14, despite probation clause); (c) termination was discriminatory (breach of TAFEP); (d) termination was in breach of contract (notice/procedure not observed); (e) termination was retaliation (if employee made complaint/disclosed breach before termination). Employer's defense: documented performance issues, fair process, legitimate business reason, consistency with other probationary terminations
7. **Settlement & References**: If wrongful dismissal claim raised by terminated probationer: employer may offer settlement (modest amount + agreed reference statement) to avoid litigation; negotiating settlement during probation disputes often efficient given smaller sums involved relative to litigation costs

Context: Use when managing employees during probation, addressing performance concerns, or deciding between extension vs. termination.
Difficulty: Intermediate
Best AI tool: Claude
Follow-up: PROMPT 2 (Wrongful Dismissal Claim Analysis) if termination disputed

---

**PROMPT 20 — Remuneration Structure & Bonus Disputes in Singapore Employment**

[EMPLOYEE NAME] (position: [TITLE], tenure: [YEARS] years) is in dispute with [EMPLOYER NAME] regarding [DESCRIBE: non-payment of expected bonus / reduction in bonus / change to bonus calculation formula / termination before bonus payout]. The employment contract states: "[QUOTE RELEVANT BONUS CLAUSE]". Bonus practice/history: [DESCRIBE: bonus paid consistently for [YEARS], amount [TYPICAL RANGE], timing [USUAL PAYOUT DATE]].

Analyze bonus entitlements and dispute resolution:

1. **Contractual vs. Discretionary Bonus Analysis**: (a) **Contractual Bonus**: If employment contract expressly promises bonus (fixed amount, percentage of salary, or formula), bonus is enforceable contractual entitlement; employer cannot refuse payment once triggering condition met (e.g., "annual bonus of 2 months' salary," "performance-based bonus if revenue exceeds SGD X"); (b) **Discretionary Bonus**: If contract states bonus is "at employer's discretion" or "subject to company performance," bonus is non-contractual gift; employer has discretion to withhold, reduce, or eliminate without legal consequence (provided not done for discriminatory reason); (c) **Past Practice**: If employer has paid discretionary bonus for consecutive years, ambiguity may arise—did practice transform discretionary bonus into contractual entitlement? (depends on circumstances: consistent amount and timing suggest intention to create entitlement; variable discretion suggests intent to retain discretion)
2. **"Termination Before Payout" Scenarios**: (a) **Contractual Bonus**: If employee dismissed before bonus payout date but earned/accrued bonus (e.g., annual bonus earned during year, but not paid until Q1 following year), dismissed employee generally entitled to earned bonus unless contract explicitly waives bonus on termination; (b) **Discretionary Bonus**: If dismissed employee has not yet earned discretion entitlement (e.g., discretionary bonus is "subject to continued employment through bonus payment date"), employer often can withhold without liability (though equity may suggest moderation if dismissal is unfair); (c) **Wrongful Dismissal Context**: If dismissal itself is wrongful, damages may include loss of bonus (both contractual and reasonable expectation of discretionary bonus) if employee would have received bonus absent wrongful dismissal
3. **Bonus Calculation Disputes**: Common disputes: (a) **Performance Metrics**: If bonus dependent on performance targets (revenue, profit, KPIs), dispute centers on whether targets were met. Employer's representations regarding targets (if misrepresented, withheld information) may support employee's claim; (b) **Salary Definition**: Bonus often calculated as percentage of "salary" or "basic salary"—ambiguity arises whether includes allowances, commissions, overtime. Confirm contract language; if ambiguous, construe in favor of employee (contra proferentem); (c) **Prorating**: If employee terminates mid-year, entitled to pro-rata bonus (common practice: bonus × (months worked/12) if termination is unfair; if termination justified, pro-rata may not apply unless contract mandates)
4. **Non-Payment & Recovery**: (a) **Contract Breach Claim**: If bonus is contractual, sue in court for non-payment (amount is quantifiable); entitlement clear; interest may be claimed from date of breach; (b) **Estoppel/Promissory Estoppel**: If employer promised bonus and employee relied (declined other job), may enforce promise through equitable estoppel even if not formally contracted; (c) **Restitution**: If employee provided services "encouraged by" expectation of bonus, recovery may be available on restitution basis (quantum meruit); rare but available if employer's conduct inequitable
5. **Defensive Arguments & Contra-Indications**: Employer may argue: (a) Bonus was never earned (performance targets unmet—burden on employer to prove if targets were clear and agreed); (b) Bonus was discretionary and legitimately withheld—but discretion is not unfettered (cannot be exercised capriciously, discriminatorily, or in breach of good faith); (c) Employee forfeited bonus by termination/dismissal—defensible only if contract explicitly permits forfeiture; (d) Company financial hardship—generally not a defense (employer's financial position is not employee's risk unless expressly agreed); (e) Bonus was conditional on "continued employment through payout"—legitimate only if clearly stated in contract
6. **Procedural Mechanisms**: If bonus dispute arises in context of wrongful dismissal claim: (a) **Court Claim**: Claim for unpaid bonus as part of broader wrongful dismissal damages; (b) **Negotiation**: Settle bonus dispute alongside severance (employee may accept partial bonus in exchange for larger severance package to reduce total exposure); (c) **MOM Complaint**: If amount is modest (e.g., < SGD 5,000), MOM Inspectorate may investigate unpaid bonus as wage dispute and issue compliance order to employer

Context: Use when bonus payment disputes arise, calculating damages in wrongful dismissal cases, or negotiating settlement of deferred compensation issues.
Difficulty: Intermediate
Best AI tool: Claude
Follow-up: PROMPT 1 (Employment Contract Review) if contract requires amendment for bonus clarity

---

**PROMPT 21 — Termination Letter Drafting & Notice Period Calculations**

[EMPLOYER NAME] has decided to terminate employment of [EMPLOYEE NAME] (position: [TITLE], hire date: [DATE], termination reason: [REASON]). The employment contract specifies: [QUOTE NOTICE PROVISION]. The effective termination date intended: [DATE]. Confirm tax/final paycheck requirements.

Draft a legally compliant termination letter and calculate final payments:

1. **Notice Period Calculation**: (a) If contract specifies notice period (e.g., "1 month notice"), calculate from notice date to intended termination date; if notice period is "1 month" and notice given on March 10, effective termination is April 10; (b) If contract silent, default notice period under Employment Act Section 5 is 1 month; (c) Special situations: for senior employees/executives, notice may be longer (3-6 months); for certain gross misconduct (theft, violence), notice may be waived per Section 14(3) which permits summary dismissal without notice
2. **Pay-In-Lieu-of-Notice**: If employer desires immediate separation (not waiting notice period), pay employee in-lieu amount = notice period salary (basic + fixed allowances, up to notice period amount); example: 1 month notice period × monthly salary = pay-in-lieu amount; this satisfies notice obligation and permits immediate departure
3. **Final Paycheck Components**: Calculate total amount due by termination date: (a) **Accrued Salary**: Salary up to termination date (e.g., if terminated mid-month, pro-rata salary for days worked); (b) **Accrued Leave Payout**: Unused annual leave days × daily rate (unused annual leave is paid out on termination per Section 43(5)); calculate by taking annual leave entitlement for the year, subtract leave taken, multiply unused days by daily salary rate (daily rate = monthly salary / 26 assuming 6-day week); (c) **Gratuity** (if applicable): Only if continuous service 2+ years per Section 71 (see PROMPT 3 for calculation); (d) **Bonus** (if contracted): If termination occurs before bonus payout, assess whether employee entitled (see PROMPT 20); (e) **Deductions**: Only permitted deductions are taxes (if amount exceeds SGD 8,000), CPF contributions (employer + employee), and court orders (maintenance, bankruptcy); unauthorized deductions (uniform cost, shortage) are prohibited per Section 23
4. **Termination Letter Format & Content**: Structure:
   - Date of letter
   - Employee name, designation, employment start date
   - Statement: "Your employment with [COMPANY] is hereby terminated effective [DATE]"
   - Reason (if applicable): Optional, but recommended to be transparent; if reason is performance/conduct, brevity and factuality reduce dispute risk
   - Notice period: "This letter constitutes [X months] notice as per your employment contract" OR "Payment-in-lieu of notice of [SGD AMOUNT] is enclosed"
   - Final payment details: "Your final payment, comprising accrued salary (SGD X), leave payout (SGD Y), and gratuity (SGD Z), totaling SGD TOTAL, will be paid on [DATE]"
   - Benefits conclusion: "Your CPF benefits will be processed per statutory requirements" (brief)
   - Outstanding items: "Please return company property (ID badge, laptop, access card) by [DATE]"
   - Reference letter offer (optional): "A reference letter confirming your role and tenure will be provided upon request" (builds goodwill, reduces dispute risk)
   - Confidentiality reminder (if applicable): "Please note you remain bound by confidentiality obligations under your employment contract"
   - Signature: By authorized person (HR, director); avoid unsigned letters
5. **Tone & Litigation Risk Minimization**: (a) Avoid accusatory language (do not include detailed allegations in termination letter even if dismissal for cause—keep letter professional and neutral); (b) avoid admission of employer fault ("we've made mistakes managing your performance"); (c) avoid speculative language ("we expect you'll seek other employment"); (d) keep letter concise and factual; (e) ensure tone does not suggest malice or discrimination; (f) avoid statements that contradict later legal position (e.g., if wrongful dismissal claim filed, letter should not admit breach)
6. **Special Scenarios**: (a) **Redundancy/Retrenchment**: Letter should confirm retrenchment reason, reference MOM notification, outline severance package (gratuity, enhanced benefits if any); (b) **Gross Misconduct Dismissal**: Letter may be brief (misconduct specified in detail in separate investigative report, not in termination letter); summary dismissal implies no notice due; (c) **Probationary Termination**: Letter may briefly note probation status but should still observe notice/fairness procedures (see PROMPT 19); (d) **Mutual Agreement Termination**: If separation is agreed, termination letter should reference mutual termination agreement signed by both parties (evidences both parties agreed to termination)
7. **Document Preservation & Follow-Up**: Retain copy of termination letter in employee file; send via email (received confirmation) or hand-deliver with witness present; ensure final payment is processed on-time (failure to pay final paycheck by statutory deadline—next payday or 7 days—is breach of Section 38); confirm CPF settlement notification filed with CPFB

Context: Use when terminating employee, ensuring compliance with notice requirements and final payment calculations.
Difficulty: Intermediate
Best AI tool: Claude
Follow-up: PROMPT 3 (Retrenchment Gratuity Calculation) if termination is redundancy-related

---

**PROMPT 22 — Medical Leave & Illness Absence Management**

[EMPLOYEE NAME] has been absent from work due to [ILLNESS/CONDITION] from [START DATE] to [CURRENT DATE/ANTICIPATED END DATE]. Medical evidence: [DESCRIBE: medical certificates provided, diagnoses mentioned, sick leave balance]. The absence is [EXPECTED TO CONTINUE/HAS CONCLUDED]. Employer's concerns: [DESCRIBE: performance impact, coverage arrangements, return-to-work conditions, potential termination if prolonged].

Analyze employer obligations and return-to-work management:

1. **Statutory Leave Entitlements During Illness**: Under Section 43A of the Employment Act, employees are entitled to paid medical leave at no deduction in wage: (a) First 4 days per calendar year: at full pay (employer pay); days 5-8: at 50% pay (shared employer-employee); (b) Entitlement is 4 days per year for first year of employment, 8 days per year thereafter; (c) Medical certificates are required for absences exceeding 2 consecutive days or when employer requests (employer can require certificate for 1-day absences if requested in writing); (d) If employee exhausts medical leave entitlement, further leave is unpaid unless covered by annual leave or other policy
2. **Medical Certificate Requirements & Disputes**: (a) Certificate must be from approved medical provider (registered doctor, clinic, hospital; not traditional healer or unregistered provider); (b) Certificate should state nature of condition (if generic "unfit for work," may be insufficient), dates of medical treatment, and inability to work/recommendation for rest; (c) If employee submits questionable certificates (identical pattern recurring, suspiciously convenient timing), employer may require independent medical examination (Section 43A(4) permits this) at employer's expense to assess veracity and fitness for duty; (d) Dispute over certificate authenticity is grounds for non-acceptance, but must inform employee in writing of reason for rejection; (e) Excessive use of medical leave (e.g., every Friday) may indicate abuse; employer should counsel employee and document pattern; disciplinary action (warning) possible if abuse substantiated
3. **Fitness-to-Work Assessment & Return-to-Work**: (a) Before return after prolonged illness, employer may require employee to provide fitness-to-work medical clearance confirming employee is fit to resume full duties; (b) Employer may condition return on medical examination (at employer expense if required) confirming fitness and any work restrictions; (c) If employee is partially recovered with work restrictions (e.g., "no lifting," "restricted hours"), accommodate restrictions if reasonably practicable; failure to accommodate without legitimate business reason may constitute constructive dismissal or disability discrimination
4. **Termination Due to Prolonged Illness**: If employee is unable to return to work for extended period (weeks/months): (a) Timing: Under common law, after approximately 3-6 months of absence (depending on role and contractual circumstances), employer may argue employment is frustrated (employee's unavailability makes contract impossible to perform); frustration does not constitute dismissal per se, but may result in termination of employment; (b) Procedure: Before invoking frustration, employer should attempt accommodation (modified duties, retraining for different role if possible) to demonstrate good faith; (c) Statutory Considerations: If medical leave entitlements are exhausted and further absence is unpaid, employer may issue notice of termination for non-attendance (though dismissal for illness alone may be challenged as unfair if employer did not attempt accommodation); (d) Tax/Disability Considerations: If illness is work-related, may trigger WIC insurance claims or permanent disability assessment; if illness is disability-related, TAFEP guidelines recommend accommodation attempts before termination
5. **Workplace Safety & Health Dimensions**: If illness was work-related (occupational disease, workplace injury exacerbated condition): (a) Employer must report to MOM if serious injury/illness; (b) Workplace hazard may have caused illness (noise-induced hearing loss, chemical exposure, ergonomic injury)—investigate root cause and implement controls to prevent recurrence; (c) Retaliation against employee for reporting illness/seeking WIC claim is prohibited; (d) Discriminatory dismissal of employee on medical grounds may violate TAFEP if company has pattern of treating illness-related absences inconsistently across demographics
6. **Documentation & Communication**: (a) Keep detailed absence records (dates, medical certificates, reasons); (b) communicate proactively with employee during prolonged absence (maintain contact, explore return prospects, confirm accommodation possibilities); (c) provide written notice if intending to terminate due to prolonged absence (explain business impact, confirm no available alternative arrangement); (d) offer final opportunity for employee to confirm return date or anticipated return timeline; (e) if termination decision is made, observe proper notice period and final payment obligations

Context: Use when managing employee illness absences, assessing fitness-to-work, or considering termination due to prolonged incapacity.
Difficulty: Intermediate
Best AI tool: Claude
Follow-up: PROMPT 2 (Wrongful Dismissal Claim Analysis) if termination is disputed

---

**PROMPT 23 — Workplace Mental Health & Psychological Injury Claims**

[EMPLOYEE NAME] claims to have suffered psychological injury/mental health condition arising from [DESCRIBE: workplace stress/bullying/harassment/workload/management conflict]. The employee has: [DESCRIBE: sought counseling/medical treatment, requested accommodations, alleged work-life balance issues, reported stress-related symptoms]. The employer is concerned about: [DESCRIBE: liability exposure, accommodation requests, impact on other staff, potential legal claim].

Analyze employer obligations and liability exposure:

1. **Psychiatric Injury & Common Law Liability**: Under Singapore common law, employer can be liable for negligently causing psychological/psychiatric injury if: (a) Foreseeability: Employer should have foreseen that workplace conditions would cause psychological harm (recognized hazard: excessive workload, hostile environment, repeated bullying, inadequate support); (b) Breach of Duty: Employer failed to take reasonable steps to prevent foreseeable harm (failure to investigate complaints, inadequate grievance procedures, lack of mental health support); (c) Causation: Employee's psychiatric injury was caused by employer's breach (medical evidence linking workplace exposure to mental health condition); (d) Damage: Quantifiable harm (medical treatment costs, lost wages, pain & suffering). Successful claims are difficult because psychiatric injury causation must be clearly established; courts are cautious not to expand employer liability excessively
2. **Occupational Stress & WSH Act Considerations**: While psychiatric injury claims are uncommon, occupational stress may be addressed through WSH Act framework: (a) Employer has duty under Section 11 to conduct risk assessment for psychosocial hazards (workload, conflict, harassment, job insecurity); (b) if risk assessment identifies hazards, employer must implement control measures (workload management, conflict resolution procedures, mental health resources); (c) WSH Act does not explicitly cover mental health, but courts may extend interpretation to include psychological safety as aspect of "health"; (d) MOM guidance increasingly recognizes mental health as workplace safety concern
3. **Workplace Harassment & Bullying as Occupational Stress**: Distinct from general workplace stress, bullying/harassment creates liability: (a) Employer duty: Provide workplace free from harassment; establish clear grievance procedures; investigate complaints promptly; (b) Harassment definition: Unwelcome conduct (repeated criticism, exclusion, humiliation, unequal treatment) creating hostile environment; (c) Liability: Employer liable if harassment is by supervisor (employer has vicarious liability) or by co-worker (employer liable if negligently failed to prevent/respond); (d) Employee remedy: Damages for psychological injury caused by harassment; injunctive relief to stop harassment; compensation for medical treatment
4. **Duty of Care & Reasonable Accommodation**: (a) Employer has duty to accommodate employees with mental health conditions (disabilities recognized under TAFEP); (b) Reasonable accommodation examples: flexibility on work-from-home arrangements, reduced hours, quieter workspace, access to counseling services, modified deadlines; (c) Employer must engage with employee to understand specific needs and explore feasible accommodations; (d) Refusal to accommodate without legitimate business reason may constitute discrimination under TAFEP principles
5. **Mental Health Support & Preventive Measures**: To reduce liability exposure, employer should: (a) Provide Employee Assistance Program (EAP) offering confidential counseling; (b) educate managers on mental health awareness, recognizing stress signs, supporting struggling employees; (c) implement workload management practices (clear expectations, regular breaks, vacation encouragement); (d) establish psychologically safe culture (open dialogue about stress, non-punitive approach to mental health, destigmatization); (e) document all mental health-related conversations and accommodations provided
6. **Claims Process & Defenses**: If employee claims psychiatric injury: (a) Employer defenses: (i) injury was caused by personal factors (family issues, genetic predisposition) not workplace; (ii) employer took reasonable precautions (support services were available, feedback was constructive); (iii) medical causation unclear (expert psychiatric evidence disputed); (b) Employee must provide medical evidence (psychiatric diagnosis, nexus between workplace and condition); (c) timing: claim must be raised reasonably promptly (if injury occurred 2+ years ago and only now claimed, limitation period may bar claim or weakness of evidence suggested)
7. **Discrimination vs. Performance Management**: Distinguish between: (a) **Protected**: Employee with mental health condition receives accommodation/flexibility while remaining productive; (b) **Discriminatory**: Employee terminated/demoted solely because of mental health condition, without performance basis; (c) **Legitimate**: Employee performance is deficient (unrelated to mental health condition) and is managed through normal performance procedures; mental health condition does not shield employee from legitimate performance management, but accommodation should be explored first

Context: Use when addressing employee mental health concerns, managing bullying complaints, or assessing psychological injury liability.
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 14 (Sexual Harassment & Workplace Misconduct Investigation) if bullying/harassment involved

---

**PROMPT 24 — Performance Management Documentation & Capability Dismissal**

[EMPLOYEE NAME] (position: [TITLE], tenure: [YEARS]) has displayed [DESCRIBE: insufficient technical skills, recurring performance shortfalls, unmet KPIs, training failures]. Relevant performance issues include: [DESCRIBE SPECIFIC INCIDENTS WITH DATES]. The employee has: [DESCRIBE: received feedback, participated in training, been placed on performance improvement plan (PIP), been warned]. Current status: [DESCRIBE: no improvement, marginal improvement, performance remains below standard].

Develop a performance management strategy that protects against wrongful dismissal claims while enabling fair capability dismissal:

1. **Legal Framework for Capability Dismissal**: Under Singapore common law, employer can terminate for "capability" (inability to perform job due to lack of skill/competence) if: (a) **Fair Reason**: Employee performance is objectively deficient against agreed standards; (b) **Fair Procedure**: Employee received clear notice of standards, feedback on shortfalls, opportunity to improve, and reasonable support (training); (c) **Consistency**: Dismissal for capability is applied consistently (other similarly situated low performers not treated more favorably); (d) **Documentation**: Employer has contemporaneous records supporting performance concerns; (e) **Natural Justice**: Employee had opportunity to respond/explain performance issues. Dismissal for capability is legitimate ground for termination under Section 14 of Employment Act (but procedure must be fair)
2. **Performance Standards Clarity**: Start with documented expectations: (a) Review job description (updated if role has evolved); confirm employee understood core responsibilities; (b) establish objective KPIs (if possible—sales targets, error rates, project deadlines, quality metrics) or behavioral expectations (if role is less quantifiable); (c) communicate standards in writing (at onboarding, in PIP, in performance review); (d) distinguish between performance below expectations (grounds for improvement plan) vs. basic inability (grounds for dismissal if unchangeable)
3. **Performance Monitoring & Feedback System**: (a) **Frequency**: Regular performance discussions (monthly or quarterly depending on role); not just annual appraisals; (b) **Contemporaneous Documentation**: Document each conversation (date, feedback provided, employee's response, improvement areas identified, support offered); brief email summary post-meeting confirms conversation; (c) **Specific Examples**: Use factual examples ("In March project delivery was 2 weeks late due to incomplete requirements analysis") rather than general criticism ("Poor organization"); (d) **Forward Focus**: Feedback should be constructive and future-oriented (what needs to improve, how employer can help) rather than purely critical
4. **Performance Improvement Plan (PIP)**: If issues persist, implement formal PIP: (a) **Written PIP**: Document specific areas for improvement, measurable targets, timeline (typically 3-6 months), support/resources provided, review dates, and consequences if targets not met; (b) **Clarity**: PIP should not be ambiguous; employee must understand exactly what improvement is expected and by when; (c) **Regular Review**: Conduct PIP reviews at agreed intervals (monthly); document progress (or lack thereof); adjust support if needed; (d) **Success Criteria**: Define what constitutes "successful completion" (targets met, competency demonstrated, feedback improved); (e) **Documentation**: Keep detailed notes of PIP meetings and progress assessments; this becomes critical evidence if dismissal proceeds
5. **Training & Support Provision**: Demonstrate employer's good faith effort to help employee succeed: (a) **Training**: Provide relevant training (technical skills courses, coaching, mentoring) if identified as gap; (b) **Coaching/Mentoring**: Assign experienced colleague/manager to provide guidance; (c) **Resources**: Provide tools, information, time allocation needed to perform role; (d) **Feedback Quality**: Ensure feedback is helpful and development-focused, not just criticism; (e) **Document Support**: Record all training/support provided (attendance records, trainer confirmation, employee acknowledgment); if employee subsequently claims lack of support, documentation refutes claim
6. **Decision Point—Improvement vs. Termination**: After PIP period: (a) **Improvement Achieved**: Transition employee off PIP; provide positive feedback; continue monitoring to ensure sustained performance; (b) **Marginal Improvement**: Consider extension of PIP (clarify areas still needing work); avoid extension if becoming indefinite (limits employer's options); (c) **No Improvement**: If targets not met despite genuine support, dismissal is justified. Document this as final decision point
7. **Termination for Capability—Notice & Documentation**: If dismissal decision is made: (a) **Termination Notice**: Provide notice period as per contract (may be shorter notice justified for capability given extended improvement opportunity via PIP); (b) **Termination Letter**: State "your employment is terminated due to failure to meet performance standards outlined in [PIP dated X]"; reference specific shortfalls and support provided; (c) **Final Payment**: Calculate as per regular termination (salary, leave, gratuity if applicable—capability dismissal does not forfeit statutory entitlements); (d) **Practical Transition**: Plan hand-over of projects/responsibilities to mitigate business disruption
8. **Disputed Dismissal Defense Strategy**: If dismissed employee claims wrongful termination: (a) Rely on PIP documentation (demonstrates fair procedure, clear standards, specific feedback); (b) reference training records (shows support offered); (c) performance metrics (objective evidence of underperformance); (d) consistency evidence (if possible, show other low performers also managed through PIP/termination—avoids appearance of discriminatory selection); (e) employee's acknowledgment during PIP (signed PIP, performance review acknowledgments) strengthen defense
9. **Discriminatory Dismissal Risk**: Capability dismissal may be challenged as discriminatory if: (a) Selection for capability dismissal is disproportionately based on age (older workers fired for "lack of technological skills"), gender (women not meeting targets in sales), or nationality (foreign workers terminated for "cultural fit" issues); (b) similarly performing non-protected-group employees are given more opportunities or higher standards applied to protected group; (c) defense: apply standards equally, document application consistently, ensure diverse PIP selection

Context: Use when managing underperforming employees, implementing performance improvement plans, or preparing capability-based dismissal.
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 2 (Wrongful Dismissal Claim Analysis) if dismissal is subsequently disputed

---

**PROMPT 25 — Post-Employment Obligations & Restrictive Covenants Enforcement**

[EMPLOYEE NAME] recently departed [EMPLOYER NAME] (last employment date: [DATE], position: [TITLE], tenure: [YEARS]). The employee is now [DESCRIBE: joining competitor / starting own business / taking customer clients / using technology developed]. The employment contract contained [DESCRIBE: non-compete clause / non-solicitation clause / confidentiality clause / IP assignment clause].

Assess post-employment enforcement options and remedies available:

1. **Non-Solicitation Enforcement (Customers/Clients)**: If contract prohibits solicitation of clients for [TIMEFRAME]: (a) **Enforceability**: More enforceable than non-compete because narrower in scope (protects specific relationships, not all employment in field); (b) **Scope Definition**: "Customers/clients" should be specifically defined in contract (existing clients as of departure, clients served within last [X] months); (c) **Breach**: Solicitation means direct contact with client/customer offering competing services; if client voluntarily contacts departed employee, not breach (client-initiated contact permissible); (d) **Remedy**: If breach established, injunctive relief prevents further solicitation; damages claim for lost client revenue or loss of profit from diverted clients; (e) **Enforcement Timeline**: Non-solicitation period typically 6-12 months (reasonable; 3 years likely unenforceable); (f) **Good Faith**: Employer must have legitimate protectable interest (established client relationships, investment in client development, confidential client information)
2. **Non-Solicitation Enforcement (Employees)**: If contract prohibits employee from soliciting/recruiting other employees: (a) **Enforceability**: Narrower enforceability than non-compete; courts recognize employee mobility; (b) **Scope**: Usually enforceable only if protects senior employees or those with specialized training; overbroad prohibition on recruiting "any employee" may be unenforceable; (c) **Breach**: Direct recruitment (offering former colleague a job at new company); passive availability (if former colleague contacts departed employee) is not breach; (d) **Damages**: Lost employee (value of training, lost productivity, recruitment/replacement costs); (e) **Practical Challenge**: Difficult to enforce unless employee is visibly recruiting multiple staff members
3. **Confidential Information & Trade Secrets (Post-Employment Restraint)**: Post-employment, former employee remains bound by confidentiality obligations indefinitely (common law duty survives termination): (a) **Scope**: Information is confidential if: (i) not public domain, (ii) genuinely secret, (iii) treated as confidential by employer (labeled, restricted access, compartmentalized); (b) **Types**: Customer database, trade secrets, business strategy, pricing, source code, technical methods, financial information; (c) **Restraint Duration**: No time limit (indefinite protection for true trade secrets); unlike non-compete, confidentiality survives employment termination and extends to new employment; (d) **Enforcement**: Former employee cannot use/disclose confidential information even at competitor; if breach, employer may seek injunction preventing use/disclosure and damages (lost profits from diversion, competitor gains from using secrets, cost of remediation)
4. **Intellectual Property Assignment Post-Employment**: (a) **IP Created During Employment**: If contract assigns IP to employer, post-employment IP created by former employee likely remains employee's property (no ongoing assignment post-termination); however, if IP builds directly on pre-existing trade secrets, employer may claim rights; (b) **IP Created Using Employer Resources/Information**: If former employee uses confidential information or employer resources to develop IP in new role, employer may claim equitable interest in IP (unjust enrichment); (c) **Distinguishing Background vs. Foreground IP**: Former employee entitled to use general knowledge/skills (non-secret information); cannot use specific trade secrets/confidential information; (d) **Contract Clarity**: Ideal contracts distinguish: IP created during employment with employer resources (assigned to employer); IP created post-employment (employee's property); background IP/general knowledge (employee's to use)
5. **Remedies Framework & Enforcement Mechanics**: (a) **Injunctive Relief**: Interim injunction (obtainable urgently if serious issue to be tried + balance of convenience favors plaintiff + irreparable harm shown); final injunction (if breach established, restrains ongoing/future violations); (b) **Damages Claims**: Lost profits calculated as difference between what employer earned without breach vs. with breach (difficult to prove); competitor's gains (alternative basis—disgorged profits); (c) **Account of Profits**: In equity, instead of damages, employer can demand that wrongdoer account for profits earned using confidential information (employee must pay over profits to employer); (d) **Delivery Up**: Compels return of confidential documents/information; (e) **Declarations**: Court declares that information is confidential/trade secret and that former employee bound by confidentiality; serves as warning and basis for future enforcement
6. **Practical Enforcement Strategy**: (a) **Early Intervention**: Upon discovery of breach (employee joining competitor, using confidential information), act immediately (do not delay); (b) **Cease & Desist Letter**: Send formal letter from solicitor demanding cessation of breach, return of confidential materials, confirmation of compliance; often sufficient to stop breach without litigation; (c) **Evidence Gathering**: Document evidence of breach (former employee's LinkedIn profile showing similar role/customers, publicly available information on competitor's new services similar to employer's, former employee's communications indicating use of employer information); (d) **Interim Injunction Application**: If competitor intends to use confidential information, apply for interim injunction immediately (to court) restraining use pending full trial; (e) **Timeline**: Acts within weeks of discovery; delays weaken equitable remedies (laches doctrine—court may refuse injunction if unreasonable delay)
7. **Scope Limitations & Defenses**: (a) **Information No Longer Confidential**: If information has entered public domain (disclosed by third party, published, widely known in industry), confidentiality protection fails; (b) **General Knowledge**: If employee learned only general knowledge/skills (not specific secrets), use is permissible; burden on employer to prove information is protectable secret; (c) **Independent Development**: If employee can demonstrate knowledge/skill was independently developed (learned from public sources, own experience), confidentiality does not apply; (d) **Consent/Waiver**: If employer implicitly consented to use (overlooked breach, did not enforce against others), may be deemed waiver (weakens future enforcement)

Context: Use when former employee joins competitor, solicits clients/staff, or uses confidential information in new role.
Difficulty: Advanced
Best AI tool: Claude
Follow-up: PROMPT 9 (Non-Compete & Restraint of Trade Clause Enforceability) for non-compete specific analysis

---

## SECTION 5: SPECIALIZED AREAS & ADVANCED TOPICS

**PROMPT 26 — Domestic Worker Employment & Special Protections**

[EMPLOYER NAME] (referred to as "employer of domestic worker" or "major employer") employs [DOMESTIC WORKER NAME] from [COUNTRY OF ORIGIN] under a domestic worker employment arrangement. The domestic worker [DESCRIBE: works as live-in maid / caregiver / cook]. Issues: [DESCRIBE: alleged wage non-payment / poor working conditions / abuse allegations / contract disputes / MOM violations].

Analyze the special employment protections and obligations specific to domestic workers under Singapore law:

1. **Unique Legal Framework**: Domestic workers in Singapore fall partially outside Employment Act protection: (a) **Excluded from Employment Act**: Domestic workers are NOT covered by Employment Act provisions on maximum working hours, leave entitlements, statutory holidays, rest days—which are the core protections of Employment Act; (b) **Partial Coverage**: Domestic workers ARE covered by: Section 37 (minimum wage—currently SGD 730/month for overseas domestic workers, SGD 820/month from Feb 2024 onward with cost-of-living adjustments; Singapore citizens/permanent residents hired as domestic workers may have different entitlements); Section 23 (no unauthorized wage deductions); Sections related to unsafe working conditions, gratuity (if applicable), and wrongful dismissal; (c) **Special Regulation**: Domestic workers governed partly by Employment Act, partly by Ministry of Manpower (MOM) Employment of Foreign Domestic Worker (FDW) regulations and Tripartite Conditions of Employment (TCE) for FDWs
2. **Written Employment Contract Requirements**: (a) Mandatory written contract is required before FDW arrives in Singapore (form 23 or equivalent); contract must be in worker's native language + English; (b) Contract must specify: wages (monthly salary), rest days (minimum 1 per month mandatory per MOM guidelines, though common practice is 4 rest days per month), benefits (accommodation, food, medical), hours of work, duration of contract (typically 2 years), terms of repatriation, break of contract terms; (c) MOM provides standard contract template; use of significantly non-standard terms (especially onerous terms disadvantaging worker) may trigger MOM investigation; (d) Contract must be countersigned by employer and worker before employment begins; copy provided to worker
3. **Wages & Deduction Restrictions**: (a) **Minimum Wage**: As noted above, minimum monthly wage is SGD 730 (subject to annual upward review); wage must be paid in full each month without deduction except: (i) taxes (if applicable—rare for FDW below threshold); (ii) CPF contributions (if worker has opted for CPF coverage); (iii) authorized deductions with written consent (e.g., loan repayments); (b) **Prohibited Deductions**: Employer cannot deduct for: accommodation costs (room/board is separate from wage obligation and must be provided at employer's cost), meals, uniform, transportation, breakage, training, agency fees (these are employer's or agent's responsibility); (c) **Cash Payment**: Wages must be paid monthly, preferably by bank transfer (if FDW has account) or cash; payment delays are violation; (d) **Overstay Penalties**: If FDW overstays contract, no wage deduction is permitted; employer's remedy is to lodge overstay complaint with MOM (not wage deduction)
4. **Rest Days & Working Hours**: (a) **Rest Days**: Minimum 1 rest day per month (typically Sunday, or alternate day by agreement); mandatory rest day policy is weaker for domestic workers than for other employees (who have statutory entitlements); MOM guidelines recommend 4 rest days/month as best practice; (b) **Working Hours**: No statutory maximum working hours for FDWs (unlike regular employees' 44-hour week); however, MOM expects "reasonable hours" and investigates cases of excessive work (claims of 18-hour days without rest triggering concern); (c) **Flexibility**: Domestic work by nature is continuous (care for children, elderly); reasonable expectation is on-call availability; but employer must allow some personal time and rest
5. **Accommodation & Working Conditions**: (a) **Accommodation**: Employer must provide clean, safe living quarters (separate bed space, not sharing with employer family); employer costs (rent-equivalent, utilities) are not deducted from wage; (b) **Safety**: Employer responsible for providing safe working environment; equipment (vacuum cleaner, stove) must be maintained safely; (c) **Discipline & Abuse**: Any physical abuse, sexual harassment, withholding of food/medical care are criminal offenses under Penal Code; domestic workers particularly vulnerable to abuse (isolated work environment, language barriers, dependence on employer for housing/visa); MOM has heightened scrutiny of domestic worker abuse claims; (d) **Food & Healthcare**: Employer must provide adequate food and basic medical care; if worker requires medical treatment, employer must facilitate (no withholding due to cost); (e) **Privacy**: Worker entitled to basic privacy (e.g., no unauthorized access to phone, communications); excessive control and monitoring may constitute abuse/harassment
6. **Wrongful Dismissal & Contract Breach**: (a) **Termination**: Employer can terminate contract by providing notice per contract terms (typically 1-2 months' notice or notice period specified); if no notice period specified, common law default of 1 month applies; (b) **Grounds**: Dismissal must be for fair reason (gross misconduct, serious breach by worker); dismissal without reason is wrongful; (c) **Repatriation**: Upon termination (dismissal or end of contract), employer responsible for repatriation costs to worker's home country (airfare, visa cancellation); repatriation costs cannot be deducted from final wage; (d) **Severance**: Gratuity not typically payable to FDWs unless contract specifies (gratuity entitlement under Employment Act Section 71 requires 2+ years continuous service, which applies if contract is renewed); if contract renewed for 2+ years total service, gratuity becomes payable on final departure
7. **Complaints & MOM Enforcement**: (a) **Workers' Complaints**: FDWs can lodge complaints to MOM regarding: wage non-payment, abuse, contract breach, unsafe conditions; MOM investigates and can compel employer to pay arrears, impose fines, or cancel work permit (terminating employment); (b) **Employer Obligations**: Employers receiving complaints should cooperate with MOM investigations; failure to cooperate or obstruction results in additional penalties; (c) **Retaliation**: Employer cannot retaliate against FDW for lodging MOM complaint; retaliation is prohibited and may result in work permit cancellation; (d) **Agency Role**: If FDW hired through employment agent, agent may also be investigated if agent involvement in breach (wage fraud, misrepresentation); employer is primarily liable, agent is secondary
8. **Agency Relationship & Responsibilities**: (a) **Agent's Role**: Employment agents recruit FDWs, handle placement, initial orientation; agent typically receives commission from employer; (b) **Employer's Liability**: Employer is responsible for FDW's treatment regardless of agent involvement; employer cannot delegate statutory obligations to agent; (c) **Agent Involvement in Disputes**: If agent withheld portion of FDW's first month wage as "security deposit," this is prohibited and must be recovered; if agent misrepresented job scope/conditions, employer may have indemnity claim against agent (but remains liable to worker)
9. **Best Practices to Minimize Disputes**: (a) Use MOM-approved standard contract; avoid modifications that disadvantage worker; (b) pay wages promptly (never late); maintain payment records; (c) allow reasonable rest days and personal time; (d) address concerns/complaints promptly; treat worker with respect; (e) maintain cordial relationship and open communication; (f) provide access to communication (phone, internet) so worker can stay in touch with family; (g) facilitate medical care proactively; (h) if termination decided, provide notice and arrange repatriation; (i) maintain documentation (attendance records if any incidents, wage payment records) to defend against claims; (j) consider domestic worker insurance (covers medical expenses, repatriation if FDW injury)

Context: Use when employing domestic workers, addressing contract disputes, or responding to MOM complaints regarding domestic worker treatment.
Difficulty: Intermediate
Best AI tool: Claude
Follow-up: PROMPT 5 (MOM Inspection & Audit Preparation) if MOM investigation initiated

---

This completes the Employment Law section. File now contains 25 detailed prompts covering employment contract compliance, wrongful dismissal, MOM regulations, workplace safety, fair employment practices, dispute resolution, union matters, retrenchment, non-competes, IP disputes, probation management, bonuses, medical leave, mental health, performance management, post-employment obligations, and domestic worker protections.

---

