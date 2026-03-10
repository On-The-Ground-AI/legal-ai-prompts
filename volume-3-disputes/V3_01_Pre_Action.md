# Legal AI Prompt Library: V3_01 Pre-Action & Case Planning

*This file has been updated with principles from the **Prompt Engineering for Lawyers (2nd Edition)** guide by the **Singapore Academy of Law (SAL)** and **Microsoft Singapore** (2025). Improvements include: source-grounding, chain-of-thought, structured output formats, and pinpoint reference requirements. The SAL guide also contributed Singapore-specific litigation prompts (affidavit/SOC inconsistency analysis, witness credibility, ENE submissions) — see V7_07_SAL_Singapore_Prompt_Guide.md.*

**Before using any prompt:** Add your role/context ("I am a lawyer acting for [PARTY] in a [jurisdiction] matter"), restrict analysis to the documents provided, and verify all case citations independently.

---

## SECTION A: INITIAL CASE ASSESSMENT

### PROMPT ID: PA-001
**TITLE:** Strength of Case Assessment
**FULL TEXT:** I am a lawyer acting for [PARTY] in a [jurisdiction] matter. Analyse the strength of our case concerning [BRIEF FACTUAL SUMMARY] where we are claiming [TYPE OF CLAIM] against [DEFENDANT]. Think through this step-by-step. Evaluate the merits based on: (1) strength of legal basis, (2) evidence quality and availability, (3) witness credibility and availability, (4) documentary evidence support, and (5) defendant's likely defences. Provide a percentage likelihood of success and key vulnerabilities. Restrict analysis to the facts and documents provided — do not make assumptions about evidence not described.
**CONTEXT:** Used after initial client consultation to determine whether to proceed
**DIFFICULTY:** Intermediate
**FOLLOW-UP:** What are the top three risks to success? What additional evidence would strengthen our position?

---

### PROMPT ID: PA-002
**TITLE:** Cause of Action Analysis
**FULL TEXT:** I am a lawyer acting for [PARTY] in a [jurisdiction] matter. Identify and analyse all potential causes of action arising from the following circumstances: [DETAILED FACTUAL NARRATIVE]. Think through this step-by-step. For each viable cause of action, specify: (1) required elements, (2) which elements are satisfied by the facts provided, (3) which elements are problematic, (4) applicable statutes or common law principles (with citations), and (5) jurisdiction-specific considerations. Rank by viability. Restrict analysis to the facts provided — note any factual gaps that would affect viability. Verify all cited cases and statutory provisions before use.
**CONTEXT:** Early case analysis phase; client seeking maximum claim options
**DIFFICULTY:** Intermediate to Advanced
**FOLLOW-UP:** Which cause of action offers the strongest damages claim? Are any causes of action mutually exclusive or cumulative?

---

### PROMPT ID: PA-003
**TITLE:** Limitation Period Compliance Check
**FULL TEXT:** I am a lawyer acting for [PARTY] in a [jurisdiction] matter. Determine the applicable limitation period for a claim of [TYPE OF CLAIM] arising from [BRIEF FACTUAL DESCRIPTION]. Key dates: [DATE OF INCIDENT/LOSS], [DATE OF DISCOVERY], [CURRENT DATE]. Think through this step-by-step. Identify: (1) the governing statute with citation, (2) the limitation period length, (3) any extension provisions that apply, (4) the expiry date, (5) risk mitigation steps if close to expiry. Consider the "date of knowledge" test where applicable. Cite specific statutory provisions — verify all citations before use.
**CONTEXT:** Avoiding claims becoming time-barred; urgent case intake
**DIFFICULTY:** Intermediate
**FOLLOW-UP:** If we're within 6 months of limitation, what steps should we take immediately? Are there any extension grounds available?

---

### PROMPT ID: PA-004
**TITLE:** Evidence Gap Analysis
**FULL TEXT:** I am a lawyer acting for [PARTY] in a [jurisdiction] matter. We have the following evidence available regarding our claim for [TYPE OF CLAIM]: [LIST EXISTING EVIDENCE]. Identify: (1) critical evidence gaps that could harm our case, (2) evidence that must be preserved urgently, (3) evidence likely held by the defendant or third parties, (4) feasibility of obtaining missing evidence, (5) impact of each gap on claim strength, and (6) evidence preservation steps needed before action commences. Present findings in a table with columns: Evidence Gap | Impact on Claim (HIGH/MEDIUM/LOW) | Source | Preservation/Acquisition Steps. Restrict analysis to the evidence described — do not assume other evidence exists.
**CONTEXT:** Pre-action investigation phase; evidence preservation deadline approaching
**DIFFICULTY:** Intermediate
**FOLLOW-UP:** Should we send a preservation notice? What is the cost-benefit of investigating each gap further?

---

### PROMPT ID: PA-005
**TITLE:** Forum & Jurisdiction Selection
**FULL TEXT:** I am a lawyer advising [PARTY] on a [jurisdiction] dispute. We are considering litigation for [TYPE OF CLAIM] in the amount of [ESTIMATED DAMAGES]. The parties are located in [PARTY LOCATIONS] and the contract/tort is connected to [RELEVANT CONNECTIONS]. Think through this step-by-step. Analyse: (1) proper forum (court level, tribunal), (2) jurisdictional grounds available, (3) forum non conveniens risks, (4) competing jurisdiction claims, (5) enforcement implications, and (6) strategic advantages/disadvantages of each forum option. Present as a comparison table. Cite applicable rules of court or statutes — verify all citations before use.
**CONTEXT:** Case planning phase; cross-border disputes
**DIFFICULTY:** Advanced
**FOLLOW-UP:** If the defendant challenges jurisdiction, what is our strongest argument? What is the cost difference between forums?

---

### PROMPT ID: PA-006
**TITLE:** Preliminary Damages Estimate
**FULL TEXT:** I am a lawyer advising [PARTY] on a damages claim in a [jurisdiction] matter. Provide a preliminary damages estimate for our claim concerning [TYPE OF LOSS/INJURY]. The loss occurred on [DATE] and includes: [SPECIFY LOSS CATEGORIES — e.g., direct losses, lost profits, injury, reputational harm]. Think through this step-by-step. Calculate: (1) quantifiable losses with supporting calculations, (2) applicable heads of damage, (3) mitigation obligations, (4) reasonableness and causation factors, (5) applicable discount/interest rates, and (6) a range of low to high recovery. Restrict analysis to the facts and figures provided — clearly note any assumptions made. Present as a structured table.
**CONTEXT:** Initial settlement negotiations; damages-focused claims
**DIFFICULTY:** Intermediate to Advanced
**FOLLOW-UP:** Which damages component is most defensible? What expert evidence would strengthen our damages case?

---

## SECTION B: PRE-ACTION CORRESPONDENCE

### PROMPT ID: PA-007
**TITLE:** Letter of Demand (Formal Pre-Action Notice)
**FULL TEXT:** Draft a formal letter of demand on behalf of [CLIENT NAME] to [DEFENDANT NAME/ENTITY] regarding [SUBJECT MATTER]. The letter should: (1) clearly state the claim and amount demanded, (2) specify the factual basis with dates and key events, (3) identify the legal basis (statute, common law, contract term), (4) detail the loss suffered with supporting calculations, (5) state the deadline for payment (typically 14-28 days), (6) warn of legal action/costs consequences, and (7) reference any attached documentary support. Maintain a professional but firm tone.
**CONTEXT:** First formal communication; opens pre-litigation period
**DIFFICULTY:** Intermediate
**FOLLOW-UP:** Should we offer a discount for early settlement? How should we handle a partial response?

---

### PROMPT ID: PA-008
**TITLE:** Cease & Desist Letter
**FULL TEXT:** Draft a cease and desist letter on behalf of [CLIENT NAME] to [INFRINGING PARTY] regarding [SPECIFIC INFRINGING CONDUCT - e.g., trademark use, patent infringement, defamation]. The letter must: (1) identify the specific intellectual property or right being infringed, (2) describe the infringing conduct with specific examples and dates, (3) establish [CLIENT]'s rights and prior ownership, (4) demand immediate cessation of the conduct, (5) specify timeframe for compliance (typically 10-14 days), (6) warn of legal action and damages, (7) identify potential statutory damages available, and (8) reference relevant law. Be direct and unambiguous.
**CONTEXT:** IP disputes; urgent action needed to establish damages claims
**DIFFICULTY:** Intermediate
**FOLLOW-UP:** What evidence should we gather to prove notice if we proceed to court? Should we register the IP right before sending?

---

### PROMPT ID: PA-009
**TITLE:** Pre-Action Protocol Letter
**FULL TEXT:** Prepare a pre-action protocol compliant letter from [CLIENT] to [DEFENDANT] regarding [CLAIM TYPE] under [APPLICABLE CIVIL PROCEDURE RULES/PROTOCOL]. The letter must: (1) set out concisely the claim including key facts, (2) specify the sum claimed (if quantifiable) with detailed breakdown, (3) identify the legal basis, (4) enclose supporting documents proving the claim, (5) set out a reasonable deadline for response (typically 14-28 days per rules), (6) indicate willingness to negotiate/mediate, (7) warn of costs consequences of non-compliance, and (8) comply with all procedural requirements (e.g., pre-action disclosure requests). Include a response template.
**CONTEXT:** Mandatory before court filing in many jurisdictions; cost management
**DIFFICULTY:** Intermediate
**FOLLOW-UP:** What should we do if the defendant doesn't respond by the deadline? Can we extract admissions from their response letter?

---

### PROMPT ID: PA-010
**TITLE:** Without Prejudice Settlement Communication
**FULL TEXT:** Draft a settlement proposal letter marked "WITHOUT PREJUDICE" from [CLIENT] to [OPPOSING PARTY] regarding the dispute concerning [CLAIM SUMMARY]. Include: (1) acknowledgment of the dispute, (2) settlement proposal with specific terms including payment amount and schedule, (3) any non-monetary conditions (admission, apology, injunction), (4) reference to costs to date and potential future exposure, (5) mediator/expert involvement if applicable, (6) deadline for acceptance (typically 7-21 days), (7) statement that letter cannot be used as evidence if negotiations fail, and (8) indication of binding nature if accepted. Balance commercial reasonableness with firmness.
**CONTEXT:** Mid-stage settlement negotiations; position advancement
**DIFFICULTY:** Intermediate
**FOLLOW-UP:** Should we escalate this to senior management on their side? What fallback position should we prepare?

---

### PROMPT ID: PA-011
**TITLE:** Response to Demand Letter
**FULL TEXT:** Draft a response to the demand letter received from [CLAIMANT] dated [DATE] demanding [AMOUNT] for [CLAIMED LOSS]. The response should: (1) acknowledge receipt and provide reference information, (2) deny or admit specific allegations clearly, (3) explain disputed facts with our version of events, (4) identify legal defenses (limitation, contributory negligence, novation, etc.), (5) challenge quantum (reduce claimed damages), (6) disclose counterclaims if any exist, (7) indicate willingness or refusal to settle and on what basis, (8) set out our position on liability and quantum separately, and (9) propose next steps. Keep a professional tone while advancing our position.
**CONTEXT:** Defensive correspondence; shifting negotiation dynamic
**DIFFICULTY:** Intermediate
**FOLLOW-UP:** Should we make a counter-offer? What admissions should we avoid in this letter?

---

### PROMPT ID: PA-012
**TITLE:** Calderbank Offer (Settlement Offer Letter)
**FULL TEXT:** Draft a Calderbank offer (structured settlement offer without prejudice but usable on costs) from [CLIENT] to [OPPONENT] on the dispute regarding [CLAIM SUMMARY] for amount of [SETTLEMENT AMOUNT] on the following terms: [SPECIFY TERMS - payment schedule, releases, non-admission clause if applicable]. The letter should: (1) clearly mark it as a Calderbank offer, (2) specify it is made without admitting liability, (3) state the offer validity period (typically 21+ days per rules), (4) reference costs exposure if offer not beaten at trial, (5) detail the settlement mechanics, (6) include any conditions, and (7) confirm it will be presented to the court on costs if proceedings commence and offer is not improved upon.
**CONTEXT:** Structured settlement negotiations; cost management tool
**DIFFICULTY:** Advanced
**FOLLOW-UP:** What happens if they beat our offer at trial? Should we make a higher open offer simultaneously?

---

## SECTION C: SETTLEMENT & NEGOTIATION

### PROMPT ID: PA-013
**TITLE:** Settlement Proposal with Financial & Non-Monetary Terms
**FULL TEXT:** Prepare a comprehensive settlement proposal from [CLIENT] to [OPPOSING PARTY] for the [CLAIM TYPE] dispute. Include: (1) settlement amount broken into components (liability admission %, specific heads of damage, interest), (2) payment schedule and security arrangements, (3) non-monetary terms (apology statement, retraction, injunction, reference clause), (4) release and waiver scope (what claims are covered/excluded), (5) confidentiality provisions, (6) regulatory/reporting obligations, (7) post-settlement compliance matters, (8) dispute resolution for future disagreements, (9) cost allocation between parties, and (10) deadline for acceptance with indication of costs consequences.
**CONTEXT:** Comprehensive settlement negotiations; resolving multi-faceted disputes
**DIFFICULTY:** Advanced
**FOLLOW-UP:** What are our walk-away points on each term? Should we prioritize payment amount or non-monetary terms?

---

### PROMPT ID: PA-014
**TITLE:** Mediation Position Statement (Party Statement)
**FULL TEXT:** Prepare a position statement for mediation from [CLIENT] regarding [DISPUTE SUMMARY] to be submitted to [MEDIATOR NAME/ORGANIZATION]. Include: (1) our version of key disputed facts with supporting timeline, (2) legal basis for the claim clearly articulated, (3) our damages/losses calculation with supporting detail, (4) acknowledgment of opponent's position and merits, (5) realistic assessment of litigation risks/costs, (6) settlement parameters (realistic range, bottom line, priority outcomes), (7) acknowledgment of common ground where possible, (8) explanation of any relationship/reputational factors, and (9) genuine proposals for resolution. Keep tone conciliatory while firm on essential points. Include exhibits.
**CONTEXT:** Mediation preparation; facilitating realistic settlement discussion
**DIFFICULTY:** Intermediate
**FOLLOW-UP:** Should we provide a different range to the mediator versus the other party? What additional authority might help the mediator?

---

### PROMPT ID: PA-015
**TITLE:** Settlement Agreement Draft
**FULL TEXT:** Draft a settlement agreement between [CLAIMANT NAME] and [DEFENDANT NAME] to resolve [DISPUTE DESCRIPTION]. The agreement must include: (1) recitals confirming the dispute, (2) settlement amount and payment terms (timing, method, security), (3) full scope release of claims (specify what is released and excluded), (4) admission/liability clause (whether admission is made or explicitly denied), (5) confidentiality/non-disclosure obligations, (6) non-disparagement clause, (7) post-settlement conduct obligations, (8) dispute resolution for future disagreements arising from settlement, (9) insurance/indemnity provisions if relevant, (10) termination and survival clauses, (11) tax/regulatory considerations, and (12) execution mechanics. Ensure balance between parties' interests.
**CONTEXT:** Final settlement documentation; closing transaction
**DIFFICULTY:** Advanced
**FOLLOW-UP:** Should we include a clawback provision? What escrow arrangements are appropriate?

---

### PROMPT ID: PA-016
**TITLE:** Cost-Benefit Analysis: Settlement vs. Litigation
**FULL TEXT:** Conduct a detailed cost-benefit analysis comparing settling the [CLAIM TYPE] dispute for [SETTLEMENT AMOUNT] versus proceeding to full litigation. Analyze: (1) estimated litigation costs (legal fees, expert witnesses, court fees) through to trial, (2) time investment and business disruption, (3) likelihood of success at trial (percentage), (4) potential recovery at trial (best case, likely case, worst case), (5) impact of loss on business/reputation, (6) enforceability and collection risks post-judgment, (7) insurance implications, (8) opportunity costs, (9) settlement certainty versus trial unpredictability, and (10) financial break-even analysis. Provide clear recommendation with supporting rationale.
**CONTEXT:** Major decision point; senior management input required
**DIFFICULTY:** Advanced
**FOLLOW-UP:** What additional information would change our recommendation? What is our BATNA (Best Alternative to Negotiated Agreement)?

---

### PROMPT ID: PA-017
**TITLE:** Structured Settlement Options Analysis
**FULL TEXT:** Analyze structured settlement options available for the [CLAIM TYPE] involving [INJURED PARTY/TYPE OF LOSS]. Consider: (1) lump sum versus periodic payment arrangements, (2) tax implications of each structure, (3) structured investment options (annuities, trusts, escrow), (4) inflation adjustment provisions, (5) longevity risk considerations (if personal injury), (6) flexibility for future changes, (7) creditor protection aspects, (8) regulatory compliance requirements, (9) insurance/guarantee mechanisms, and (10) total cost of each option versus present value analysis. Provide recommendations balancing certainty, tax efficiency, and affordability.
**CONTEXT:** High-value settlements; personal injury claims
**DIFFICULTY:** Advanced
**FOLLOW-UP:** What are the insurance implications? Are there government-backed structured settlement schemes available?

---

### PROMPT ID: PA-018
**TITLE:** Negotiation Strategy Memorandum
**FULL TEXT:** Prepare a confidential negotiation strategy memo for [CLIENT] regarding settlement of [DISPUTE SUMMARY]. Include: (1) negotiation objectives (priority, essential, desirable outcomes), (2) walk-away positions on key issues, (3) information asymmetries and hidden information, (4) their likely BATNA and reservation price, (5) negotiation phases and expected sequence, (6) anchor positions to propose, (7) concession strategy and trade-offs to offer, (8) response strategies to their anticipated positions, (9) personality/decision-making profile of key decision-makers on their side, (10) timing considerations and pressure points, and (11) contingency plans. Include specific conversation openers and phrases to use.
**CONTEXT:** Complex multi-issue negotiations; high-value disputes
**DIFFICULTY:** Advanced
**FOLLOW-UP:** Who should lead the negotiation from our side? When should we involve senior management?

---

## SECTION D: CASE PLANNING

### PROMPT ID: PA-019
**TITLE:** Litigation Budget & Cost Estimate
**FULL TEXT:** Prepare a detailed litigation budget and cost estimate for [CLIENT] pursuing a [CLAIM TYPE] claim for [ESTIMATED DAMAGES] against [DEFENDANT]. Break down costs into: (1) legal fees (hourly rates by seniority level, estimated hours per phase - investigation, pleadings, disclosure, expert reports, trial), (2) counsel fees if applicable, (3) expert witness fees (numbers, specialties, rates), (4) court fees and filing costs, (5) disbursements (translation, medical records, travel), (6) insurance costs (litigation insurance, professional indemnity), (7) contingency buffer (15-20% for unknowns), and (8) cost recovery prospects. Provide estimates for: best case (early settlement), likely case (pre-trial), worst case (trial + appeal). Include cash flow projections and funding recommendations.
**CONTEXT:** Budget approval; funding structure planning
**DIFFICULTY:** Advanced
**FOLLOW-UP:** What cost-saving measures can we implement? Should we seek litigation insurance or third-party funding?

---

### PROMPT ID: PA-020
**TITLE:** Litigation Timeline & Milestones
**FULL TEXT:** Develop a detailed litigation timeline and key milestones for [CLAIM TYPE] litigation likely to proceed in [RELEVANT COURT/JURISDICTION]. Establish critical dates for: (1) pleading phase (notice of claim, defence, reply timeline under rules), (2) disclosure/discovery deadlines, (3) expert report exchange, (4) pre-trial applications and hearing dates, (5) settlement conference/mediation, (6) trial preparation phase, (7) trial dates (estimate duration), (8) judgment delivery and appeal period, (9) enforcement phase if necessary. Include: dependencies between phases, critical path items, statutory requirements, and procedural rules affecting timing. Identify risks to timeline and contingencies.
**CONTEXT:** Project planning; stakeholder communication
**DIFFICULTY:** Intermediate
**FOLLOW-UP:** What are the longest lead time items? Where can we save time if settlement negotiations progress?

---

### PROMPT ID: PA-021
**TITLE:** Evidence Preservation Memorandum
**FULL TEXT:** Prepare an evidence preservation memo to [CLIENT/RELEVANT PARTIES] regarding the [INCIDENT/TRANSACTION] dated [DATE]. Identify and specify preservation obligations for: (1) documentary evidence (emails, contracts, invoices, communications), (2) physical evidence (products, equipment, premises condition), (3) electronic evidence (servers, phones, backup systems, metadata), (4) witness statements and testimony availability, (5) expert evidence sources, (6) video/photographic evidence, (7) financial records, (8) expert reports and analyses. Include: (a) specific items to preserve, (b) custodians responsible, (c) storage/retention method, (d) confidentiality protections, (e) legal privilege considerations, (f) applicable legal holds, and (g) penalties for destruction. Set out regular verification procedures.
**CONTEXT:** Immediately following incident; preventing spoliation claims
**DIFFICULTY:** Intermediate
**FOLLOW-UP:** Should we send a formal preservation notice to the other side? What sanctions apply for breaching this preservation obligation?

---

### PROMPT ID: PA-022
**TITLE:** Witness Identification & Assessment
**FULL TEXT:** Identify and assess all potential witnesses for the [CLAIM TYPE] dispute involving [PARTIES/SUBJECT MATTER]. For each witness, specify: (1) name, role, and availability, (2) knowledge of key facts (timeline, causation, damages), (3) credibility assessment (bias, accuracy, communication skills), (4) anticipated testimony areas, (5) consistency with documentary evidence, (6) potential hostile/neutral/favorable status, (7) interview priority ranking, (8) factual versus expert witness designation, (9) accessibility (location, cooperation likely), and (10) legal obligations (employment, NDA, privilege issues). Create a witness dependency map showing information interdependencies. Recommend interview sequence.
**CONTEXT:** Investigation phase; statement gathering
**DIFFICULTY:** Intermediate
**FOLLOW-UP:** Which witnesses are most critical to prove our key allegations? Should we secure witness statements now or wait?

---

### PROMPT ID: PA-023
**TITLE:** Document Collection & Disclosure Plan
**FULL TEXT:** Develop a document collection and disclosure plan for [CLIENT] in the [CLAIM TYPE] matter. Include: (1) identification of all document custodians (individuals, departments, systems), (2) document types to be collected (emails, contracts, financial records, communications, audio/video), (3) document sources and locations (servers, email archives, cloud storage, filing systems), (4) search terms and keywords for retrieval, (5) date ranges of relevant documents, (6) collection methodology (forensic imaging, email export, manual gathering), (7) document organization and classification system, (8) privilege review and legal hold processes, (9) redaction protocols, (10) disclosure timing and phases, and (11) cost and resource requirements. Include quality control and completeness verification procedures.
**CONTEXT:** Pre-disclosure phase; managing document volume
**DIFFICULTY:** Intermediate to Advanced
**FOLLOW-UP:** How will we identify privileged documents? What is our strategy for responding to opponent's document requests?

---

### PROMPT ID: PA-024
**TITLE:** Expert Identification & Engagement Plan
**FULL TEXT:** Prepare an expert identification and engagement plan for [CLAIM TYPE] litigation. For each expert needed, specify: (1) expertise field required (e.g., engineering, accounting, medicine), (2) specific questions to be answered, (3) candidate experts with credentials assessment, (4) engagement methodology (retainer, project fees), (5) estimated costs and timeline, (6) expert report schedule (when due, format requirements), (7) expert availability for cross-examination/trial, (8) privilege protection mechanisms, (9) instructions to be given, (10) process for expert conferences with opponent's experts, and (11) backup expert identification. Consider court rules for expert disclosure and declaration requirements in relevant jurisdiction.
**CONTEXT:** Complex technical/specialist claims; liability/causation/damages proof
**DIFFICULTY:** Advanced
**FOLLOW-UP:** Should we appoint a single joint expert or party-appointed experts? What is the fee estimate for each expert?

---

### PROMPT ID: PA-025
**TITLE:** Funding Assessment & Options Analysis
**FULL TEXT:** Conduct a funding assessment and options analysis for the [CLAIM TYPE] matter with estimated litigation costs of [ESTIMATED COST RANGE]. Evaluate available funding options: (1) internal funding/cash reserves impact, (2) insurance coverage (professional indemnity, litigation insurance), (3) litigation finance/third-party funding availability and terms, (4) contingency fee arrangements with counsel, (5) after-the-event (ATE) insurance feasibility, (6) alternative fee arrangements (fixed fees, success fees, capped fees), (7) cost awards expected from opponent if successful, (8) impact on cash flow and working capital, (9) funder requirements and performance metrics, and (10) total cost of capital under each option. Provide comparative analysis with break-even scenarios for each funding method.
**CONTEXT:** Financial planning; access to justice considerations
**DIFFICULTY:** Advanced
**FOLLOW-UP:** Which funding option is most cost-efficient? What are the hidden costs of third-party litigation funding?

---

### PROMPT ID: PA-026
**TITLE:** Pre-Litigation Risk Assessment & Mitigation
**FULL TEXT:** Conduct a comprehensive pre-litigation risk assessment for [CLIENT] regarding the [CLAIM TYPE] dispute. Identify and assess: (1) liability risks (strength of opponent's claims, threshold defenses), (2) quantum risks (damages valuation disputes, mitigation obligations), (3) procedural risks (limitation periods, standing issues, requirement steps missed), (4) evidence risks (witness availability, documentary gaps, privilege issues), (5) expert risks (expert unavailability, opinion gaps), (6) financial risks (recovery ability, enforceability), (7) reputational/business risks (public proceedings, settlement publicity), (8) regulatory/compliance risks, (9) insurance implications, and (10) alternative dispute resolution feasibility. For each risk, assess probability (high/medium/low), impact, and mitigation strategies. Provide overall risk rating.
**CONTEXT:** Pre-action decision-making; comprehensive risk management
**DIFFICULTY:** Advanced
**FOLLOW-UP:** Which risks are most material? What is our contingency plan for each high-risk item?

---

*End of V3_01: Pre-Action & Case Planning*
*Total Prompts: 26*
