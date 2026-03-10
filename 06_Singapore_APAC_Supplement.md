# Singapore & APAC Legal AI Prompt Supplement
### Jurisdiction-Specific Prompts for Singapore Law Practice
### Optimised for Microsoft Copilot, Claude, ChatGPT & Legal AI Tools

---

> **Why this supplement exists:** Most AI prompt libraries are written for a US/UK legal context. Singapore law, procedure, and regulation differ in important ways. This supplement provides prompts tuned to the Singapore legal environment, covering the Rules of Court 2021, Singapore statutes, MAS regulation, PDPA, CPF, and other Singapore-specific frameworks.
>
> **Important note on AI and Singapore case law:** AI tools do not have access to eLitigation or the Singapore Law Watch database in real time. Always verify all case citations on the Supreme Court's lawnet.sg or through your law firm's database. Never cite a case in court documents without independent verification.
>
> ⚠ **Disclaimer:** These prompts are starting points only. Singapore law changes regularly. Always check the current version of any statute on sso.agc.gov.sg. Every output must be reviewed by a Singapore-qualified lawyer before use.

---

## Section A: Singapore Civil Procedure (Rules of Court 2021)

**PROMPT SG-A1 — Originating Claim Drafting**
Act as a litigation lawyer admitted in Singapore. I need to file an Originating Claim under the Rules of Court 2021. The claim is: [DESCRIBE — parties, cause of action, amount claimed]. Draft: 1. The Originating Claim in the format required by Form 8 (or the applicable form under the ROC 2021). 2. A brief summary of the statement of claim to accompany it. Note the applicable Division of the General Division (General, Intellectual Property, Technology & Construction, or other). Flag any aspects of my claim that may affect which Division or track it is filed in (the Simplified, General, or Complex Commercial List).

---

**PROMPT SG-A2 — Affidavit of Evidence-in-Chief (AEIC)**
Act as a Singapore litigation lawyer. Draft an Affidavit of Evidence-in-Chief (AEIC) for [WITNESS NAME], a [ROLE / OCCUPATION], for use in civil proceedings in the Singapore General Division of the High Court / State Courts [specify]. The witness will give evidence on the following facts: [LIST THE KEY FACTS IN CHRONOLOGICAL ORDER]. The AEIC should: be in the first person, comply with the AEIC requirements under the Rules of Court 2021, include a jurat, identify any facts stated on information and belief with the source, and include placeholders for exhibits ([EXHIBIT A], [EXHIBIT B] etc.). Note the difference between the witness's personal knowledge and hearsay.

---

**PROMPT SG-A3 — Case Management Conference Preparation**
Act as a Singapore litigation lawyer. I have a Case Management Conference (CMC) scheduled before the Registrar for [MATTER NAME]. The claim is for: [DESCRIBE]. The key issues in dispute are: [LIST]. Prepare a CMC checklist covering: 1. Documents I need to bring to the CMC. 2. Directions the Registrar is likely to give (discovery, exchange of AEICs, expert evidence, trial dates). 3. My client's preferred timeline and any constraints. 4. Any interlocutory applications I should flag. 5. Positions to take on discovery: what documents to request, scope of electronic discovery under the Singapore Electronic Discovery Practice Directions. Also draft a brief opening statement for the CMC.

---

**PROMPT SG-A4 — Costs — Party-and-Party Costs Submissions**
Act as a Singapore litigation lawyer. My client has succeeded in [PROCEEDINGS TYPE] in the [High Court / State Courts / Court of Appeal]. Draft submissions on costs covering: 1. The applicable costs framework (Scale of Costs in Appendix G of the ROC 2021 / costs on the indemnity basis). 2. A summary of work done and time spent justifying the costs claimed. 3. Any offers to settle made (including Calderbank letters or Part 36-equivalent offers) that should affect the costs order. 4. A response to the losing party's likely objections. 5. The costs order we are seeking (standard / indemnity basis, amount).

---

**PROMPT SG-A5 — State Courts vs High Court — Jurisdiction Analysis**
Act as a Singapore litigation lawyer. I have a dispute involving a claim of approximately [AMOUNT] for [TYPE OF CLAIM]. Advise on: 1. Whether the claim should be filed in the Magistrates' Court, District Court, or General Division of the High Court, and the applicable jurisdictional limits under the State Courts Act and Supreme Court of Judicature Act. 2. The advantages and disadvantages of each forum (costs regime, appeal rights, complexity of procedure). 3. Whether there are any specialist courts or panels that may be more appropriate (SICC, Technology and Construction, Intellectual Property Division). 4. Whether there is a risk of a costs penalty if the claim is brought in a higher court than necessary.

---

## Section B: Singapore Employment Law

**PROMPT SG-B1 — Singapore Employment Act Compliance Check**
Act as an employment lawyer specialising in Singapore law. My client employs [NUMBER] employees in Singapore. The workforce includes: [DESCRIBE — mixture of managers, executives, rank-and-file employees, foreign nationals on Employment Passes / S Passes / Work Permits]. Conduct an Employment Act compliance check covering: 1. Which employees are covered by the Employment Act (as amended 2019) and which provisions apply. 2. Working hours, overtime, and rest day requirements for covered employees. 3. Leave entitlements — annual leave, sick leave, maternity and paternity leave, childcare leave under the relevant Acts. 4. CPF contribution obligations — rates, deadlines, foreign employee levy. 5. Any common areas of non-compliance in [INDUSTRY]. 6. Tripartite guidelines relevant to our workforce.

---

**PROMPT SG-B2 — Fair Employment / Fair Consideration Framework**
Act as an employment lawyer in Singapore. My client company has [NUMBER] employees and is subject to the Fair Consideration Framework (FCF). We are about to hire for [ROLE]. Draft a compliance checklist covering: 1. The job advertising requirements on MyCareersFuture.sg before applying for an Employment Pass. 2. The FCF's requirements on fair and merit-based hiring. 3. What documentation we should keep to show we considered Singaporeans fairly. 4. The situations in which TAFEP may investigate and what triggers scrutiny. 5. What to do if we believe there is a genuine business case to hire a foreign national over a Singaporean candidate.

---

**PROMPT SG-B3 — Retrenchment — MOM Notification & Best Practices**
Act as an employment lawyer in Singapore. My client needs to retrench [NUMBER] employees due to [RESTRUCTURING / BUSINESS DOWNTURN / CLOSURE]. Produce a retrenchment compliance checklist under Singapore law covering: 1. MOM notification requirements — when and how to notify (employers with 10+ employees who retrench 5+ employees in any 6-month period must notify). 2. The retrenchment benefit: what the law requires vs. what the tripartite guidelines recommend. 3. Notice period and payment in lieu of notice under the Employment Act. 4. Outplacement — any obligations under current tripartite guidelines. 5. The selection process — criteria that are lawful and those that could be discriminatory. 6. CPF obligations during retrenchment. 7. Documentation — letters, separation agreements, records to retain. 8. Communication — what to say to affected employees, remaining staff, and MOM.

---

## Section C: Singapore Data Protection (PDPA)

**PROMPT SG-C1 — PDPA Compliance Gap Analysis**
Act as a Singapore data protection lawyer. Conduct a PDPA gap analysis for [ORGANISATION NAME], a [DESCRIBE — SME, MNC, public agency, licensed entity]. The organisation processes: [DESCRIBE PERSONAL DATA]. Current practices: [DESCRIBE]. Assess compliance against the PDPA's key obligations: 1. Consent obligation — is valid consent being obtained? Are deemed consent provisions used correctly? 2. Purpose limitation — is data only used for the purposes for which consent was given? 3. Notification obligation — is the collection, use and disclosure of data adequately notified to individuals? 4. Access and correction — do we have a process to handle requests within 30 business days? 5. Accuracy obligation — are data quality controls in place? 6. Protection obligation — are reasonable security arrangements in place? 7. Retention limitation — do we delete data when it is no longer needed? 8. Transfer limitation — how is overseas data transfer handled? 9. Data Breach Notification — do we have a breach response plan meeting PDPA requirements (mandatory notification within 3 business days for significant breaches)? For each obligation: Compliant / Partial / Gap. Recommended action.

---

**PROMPT SG-C2 — PDPA Data Breach Notification**
Act as a Singapore data protection officer. My organisation has discovered a personal data breach. Details: [DESCRIBE — nature of breach, data involved, number of individuals, date discovered, cause]. Under the PDPA's mandatory breach notification regime: 1. Is this breach notifiable to the PDPC? (Assess against the significant harm / significant scale thresholds). 2. What is the notification deadline? (3 business days from when we have reasonable grounds to believe it is a notifiable breach). 3. What information must be included in the PDPC notification? 4. Do we need to notify affected individuals? What must that notification say? 5. Draft the PDPC notification. 6. Draft the affected individual notification. 7. List the immediate containment steps we should be taking right now.

---

## Section D: Singapore Companies Act & Corporate Law

**PROMPT SG-D1 — Section 216 Minority Oppression Analysis**
Act as a Singapore company law specialist. My client is a minority shareholder and believes the majority has acted oppressively under Section 216 of the Companies Act 1967 (Cap. 50). The facts are: [DESCRIBE]. Advise on: 1. Whether the facts meet the threshold for Section 216 relief (oppression, disregard of interests, unfair discrimination, or prejudice). 2. The leading Singapore cases on Section 216 and how they apply here. 3. The remedies available under Section 216 (buyout order, injunction, winding up, other). 4. Whether a quasi-partnership argument applies and its significance. 5. Any defences the majority is likely to raise (legitimate majority rule, ratification). 6. Recommended litigation strategy.

*Note: Always verify Singapore case law on lawnet.sg or through your law firm's subscription database. Do not rely on AI-generated case citations without independent verification.*

---

**PROMPT SG-D2 — ACRA Filing Obligations Checklist**
Act as a Singapore corporate secretarial specialist. [COMPANY NAME] is a Singapore-incorporated private limited company. Generate an annual ACRA filing and compliance obligations checklist covering: 1. Annual Return filing (due date, information required, filing fee). 2. Financial statements — which companies must file financial statements with ACRA (XBRL requirements)? 3. AGM requirements or written resolution procedures for private companies exempt from AGM requirements. 4. Director and shareholder information updates — when must changes be notified to ACRA and within how many days? 5. Beneficial ownership and significant controllers register requirements. 6. Common penalties for late or missed filings. Present as a table with [Obligation | Deadline | Responsible Party | Penalty for Non-Compliance].

---

## Section E: Singapore Property Law

**PROMPT SG-E1 — Option to Purchase (OTP) Review**
Act as a Singapore conveyancing lawyer. Review the following Option to Purchase for a [HDB / private residential / commercial] property at [ADDRESS]: [PASTE KEY TERMS OR DESCRIBE]. Advise: 1. The key terms of the OTP (purchase price, option period, completion date, conditions). 2. Any unusual provisions compared to the standard Law Society Conditions of Sale or HDB standard form. 3. Any conditions that need to be satisfied before exercise of the option. 4. The timeline from grant of option to completion and the key milestones. 5. Stamp duty obligations and the applicable ABSD rate for this buyer. 6. Any caveats or encumbrances on the title I should be aware of. 7. Next steps after the option is exercised.

---

**PROMPT SG-E2 — HDB Transaction Checklist**
Act as a Singapore property lawyer. My client is purchasing an HDB resale flat at [ADDRESS]. Buyer: [DESCRIBE — Singapore citizen, SPR, foreigner, existing HDB ownership status]. Seller: [DESCRIBE]. Generate a step-by-step HDB resale transaction checklist covering: 1. Eligibility checks — HDB eligibility and any restrictions on purchase. 2. CPF usage — CPF housing grant eligibility and withdrawal requirements. 3. HDB Loan vs bank loan — key differences and HDB's Loan Eligibility Letter requirements. 4. Legal completion process — HDB resale portal, lawyer involvement, completion appointment. 5. Stamp duty — BSD, ABSD (if applicable). 6. Post-completion steps — keys, utilities, town council. Flag any issues specific to my client's circumstances.

---

## Section F: Singapore MAS & Financial Regulation

**PROMPT SG-F1 — Payment Services Act Licensing Assessment**
Act as a Singapore financial services regulatory lawyer. My client operates a [DESCRIBE BUSINESS — e.g. cryptocurrency exchange / payment gateway / remittance service / digital token platform]. Assess: 1. Whether my client's activities constitute a "payment service" under the Payment Services Act 2019. 2. Which licence class applies (Money-Changing, Standard Payment Institution, or Major Payment Institution). 3. The applicable thresholds that determine the licence class. 4. Key licensing conditions and ongoing compliance obligations. 5. Whether any exemption applies. 6. The timeline and key steps for applying for a licence. Note: flag if any new MAS notices or guidelines have updated these requirements, as the PSA framework is actively evolving.

---

*End of Singapore & APAC Supplement. This supplement should be used alongside the main prompt packs for Litigation, Corporate, Compliance, and In-House Counsel.*
