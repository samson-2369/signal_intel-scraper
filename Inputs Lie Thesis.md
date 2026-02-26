# Inputs Lie: How Trust Became the Primary Attack Surface in Critical Infrastructure

## Thesis Statement

Critical infrastructure systems operate on two layers of trust that adversaries are exploiting in tandem. At the protocol level, systems are architecturally designed to execute inputs they cannot authenticate — a design assumption from an era of isolated networks that persists in brownfield OT environments today. At the operational level, defenders assume that signals arriving through expected channels represent legitimate reality — an assumption adversaries exploit not only by injecting false inputs, but by silently observing accurate ones. Across GNSS, ICS/OT, and cyber-kinetic domains, the evidence is consistent: technical sophistication is not the primary driver of successful attacks against critical infrastructure. Trust is. Until defenders reframe their threat models around input verification at both layers, the attack surface will continue to expand regardless of investment in traditional perimeter controls.

---

## Abstract

_(200 words max — states the claim, the domains covered, and the defensive implication)_

---

## Chapter 1 — The Trust Architecture of Critical Infrastructure

Sets the foundation. Explains how industrial systems were designed in an era of assumed isolation and why that design philosophy persists in brownfield environments today. Introduces the two-layer trust framework — protocol-level and operational — and defines both for the reader. This chapter is the conceptual lens everything else gets read through.

### Key Points

- Historical design context: isolated networks, air-gap assumptions, pre-internet era protocols
- Why brownfield environments cannot simply retrofit authentication
- Defining protocol-level trust vs. operational trust
- Introduction of the "Inputs Lie" framework

### Sources / Research Notes

---

## Chapter 2 — Protocol-Level Trust: When the System Cannot Verify

GNSS and GPS spoofing. Modbus and unauthenticated command execution. FrostyGoop as the case study. The argument here is that these aren't bugs — they're design decisions that made sense in context and became liabilities when the context changed.

### Key Points

- GPS/GNSS: receivers trust positioning data they have no mechanism to authenticate
- Modbus TCP: no authentication, no encryption, no source verification by design
- FrostyGoop (January 2024): 600 apartment buildings, Lviv, Ukraine — heating controllers executed malicious Modbus commands because that is what Modbus does
- The design-to-liability pipeline: how isolation assumptions collapse when connectivity is introduced
- Brownfield constraint: you cannot cryptographically authenticate Modbus on 30-year-old PLCs that lack the compute resources to support it

### Sources / Research Notes

- BSides Delaware 2025 presentation: "When Cyber Meets the Spectrum"
- Dragos 9th Annual OT Cybersecurity Year in Review (2025)

---

## Chapter 3 — Operational Trust: When the Defender Cannot Verify

The harder and more original argument. Covers adversary behavior that exploits the defender's assumption that normal-looking traffic is legitimate traffic. Introduces passive access as an attack surface — the argument that read-only OT access extracts operational value without manipulating anything.

### Key Points

- KAMACITE: systematic reconnaissance of U.S. industrial devices, mapping control loops that govern physical processes
- VOLTZITE: manipulating engineering workstations, dumping configuration files and alarm data, investigating what inputs cause processes to stop
- AZURITE: targeting engineering workstations, exfiltrating alarm data and configuration files — operational intelligence about what systems trust and when they respond
- The passive adversary problem: an attacker who only watches is still extracting value
- 82% of organizations lack clear criteria for when operational anomalies should trigger cyber investigations (Dragos)
- 30% of incident response cases began with unexplained operational issues asset owners couldn't diagnose
- Losing exclusive view of operational reality is itself a security failure

### Sources / Research Notes

- Dragos 9th Annual OT Cybersecurity Year in Review (2025)

---

## Chapter 4 — The Cyber-Kinetic Convergence

Ukraine as the culminating case study. Both trust layers intersect in their most consequential application. The SCADA feedback loop. Observation as a weapon. The grid as a targeting sensor.

### Key Points

- The Record (February 23, 2026): Ukrainian officials warning that cyberattacks on the energy grid are being used to guide and refine kinetic missile strikes
- Persistent OT access as a real-time intelligence collection platform, not just a stepping stone to a future cyberattack
- The SCADA feedback loop: when a missile strikes a substation, the SCADA system sees it — breakers trip, frequency anomalies propagate, grid self-healing logic activates — and an adversary watching that telemetry in real time sees exactly what went dark, how the system responded, and where residual capacity remains
- The attacker's observational advantage compounds with every strike: they are learning while the defender is responding
- KAMACITE pre-positioning as the prerequisite: persistent footholds that survive detection cycles
- The defensive asymmetry problem: the attacker who can watch your grid's real-time response knows things your own analysts haven't correlated yet
- This is the Inputs Lie framework in its most lethal application — the infrastructure is functioning as designed, reporting reality faithfully, and that is the problem

### Sources / Research Notes

- The Record, February 23, 2026
- Dragos threat group tracking: KAMACITE, ELECTRUM

---

## Chapter 5 — Defensive Implications

Split along the two-layer trust framework. Protocol-level and operational-level recommendations. Closes with the argument that perimeter defense is insufficient as a primary strategy when the attack surface is trust itself.

### Protocol-Level Recommendations

- OT network monitoring and anomaly detection calibrated against documented baselines of normal operations
- Network segmentation: limiting lateral movement between IT and OT environments
- Unidirectional gateways where feasible
- Dragos vulnerability framework: 3% require immediate action, 71% addressable at next maintenance cycle, 27% don't warrant remediation — triage matters
- Accept that you cannot retrofit authentication into brownfield protocols; focus on detection over prevention

### Operational-Level Recommendations

- Telemetry access control: treat read access to OT telemetry as a security-relevant permission, not a low-severity finding
- Passive adversary threat modeling: explicitly model the attacker who does not manipulate anything
- Establish clear criteria for when operational anomalies trigger cyber investigations
- Retain transient network data long enough to reconstruct events after the fact
- Detection capabilities for when Modbus commands go to registers they shouldn't, at frequencies that don't match normal operations, from sources not previously observed

### The Reframing Argument

- Perimeter defense asks: did anything get in?
- Input verification asks: who else can verify what my systems are seeing?
- These are different questions with different answers and different defensive postures

### Sources / Research Notes

- Dragos 9th Annual OT Cybersecurity Year in Review (2025)

---

## Conclusion — Reframing the Threat Model

Returns to the thesis. Makes the case that the question defenders need to be asking isn't "did anything get in" but "who else can verify what my systems are seeing." The two-layer trust framework as a practical reorientation for defenders, not just an analytical observation.

### Closing Question

How many adversaries currently have read access to your infrastructure's truth?

---

## Appendices

### Appendix A — Threat Group Reference Table

|Group|Nexus|Domain|Relevant TTPs|Framework Relevance|
|---|---|---|---|---|
|KAMACITE|Russia / GRU|Energy / Grid|Control loop mapping, persistent access, network reconnaissance|Operational trust — mapping what inputs stop processes|
|VOLTZITE|Unknown|Energy / ICS|Engineering workstation manipulation, config file exfiltration|Operational trust — passive access extracting intelligence|
|AZURITE|Unknown|Energy / OT|Engineering workstation targeting, alarm data theft|Operational trust — stealing operational intelligence|
|SYLVANITE|Unknown|Initial Access|Edge device exploitation, access handoff to Stage 2|Protocol-level trust — weaponizing before patches deploy|
|PYROXENE|Unknown|Supply Chain|Social engineering, fake LinkedIn recruiter profiles, wiper malware|Operational trust — long-term patience before kinetic action|
|ELECTRUM|Russia|Energy|Coordinated attacks on distributed energy resources|Both layers — Ukraine grid, cyber-kinetic convergence|

### Appendix B — Protocol Trust Assumption Reference

|Protocol|Year Designed|Authentication|Encryption|Primary Vulnerability|
|---|---|---|---|---|
|Modbus TCP|1979|None|None|Any device on network can send commands|
|DNP3|1990|Optional (rarely deployed)|None by default|Replay attacks, spoofed commands|
|GPS/GNSS|1970s|None (civilian)|None (civilian)|Signal spoofing, meaconing|
|_(Add others as research develops)_|||||

### Appendix C — Citations and Further Reading

- Dragos 9th Annual OT Cybersecurity Year in Review (2025)
- The Record, February 23, 2026 — Ukrainian grid cyberattack reporting
- BSides Delaware 2025 — "When Cyber Meets the Spectrum" (Cornell)
- _(Add as research develops)_

---

## Writing Notes

- Target length: 8,000–12,000 words excluding appendices
- Chapter 3 is the most original contribution — passive access as attack surface is underliterature
- Chapter 4 is the most timely — Ukraine reporting gives it immediate relevance
- Chapter 5 is what makes this actionable for the target audience
- Target audience: cleared contractors, utility defenders, ICS/OT security practitioners, research roles (NLR, national labs, DOE)
- Publication: CornellSecurity.com standalone, with potential for conference submission (S4, ICS-CERT) after initial publication