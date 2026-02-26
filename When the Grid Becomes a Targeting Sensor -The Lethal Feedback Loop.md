---
title: "When the Grid Becomes a Targeting Sensor: The Lethal Feedback Loop"
date: 2026-02-23
series: When Software Meets the Physical World
status: Ready to Publish
publish date:
Document type: LinkedIn article
---

# Ukraine Energy Grid attacks and inputs lie

## Introduction
> Write your hook here. Connect the digital vulnerability to the physical impact.

## The Signal

> Use this space to connect today's news to the 'When Software Meets the Physical World' series.

### 💡 Key Takeaways
- APT activity is proving the inputs lie framework is more than theory, it's op

### 🛠️ Hardware/RF Connection
- 

### 📝 Article Ideas
- Ukraine energy grid attacks article will become a follow-up post from hte Dragos Year in Review article
The article sites that attackers aren’t necessarily after an immediate outage but mapping how quickly defenders respond. It’s part of a broader strategy 

The attackers are seeking information on how quickly does this fail and how long it takes to repair


### ✅ To-Do
- [ ] Fact-check this for the website
- [ ] Archive relevant diagrams


## Technical Deep Dive
## The Impact
## Conclusion
- [ ] Add internal links to cornellsecurity.com
- [ ] Verify diagrams/images are in the folder

---

---

**When the Grid Becomes a Targeting Sensor: The Lethal Feedback Loop**

Ukrainian officials are now warning that persistent OT access is being used to guide missile strikes in real time. An adversary watching SCADA telemetry sees exactly what went dark after a strike, how the grid responded, and where residual capacity remains. The infrastructure is functioning as designed. That's the problem.

New reporting from The Record (February 23, 2026) describes cyberattacks on Ukraine's energy grid being used not as the primary weapon — but as an intelligence collection platform operating in real time, correcting aim for the next kinetic salvo.

Persistent access isn't a stepping stone to a future cyberattack. It's a spotter.

**The SCADA Feedback Loop**

Industrial telemetry is the nervous system of critical infrastructure — the continuous stream of signals that tells operators how their systems are breathing. Breaker statuses. Frequency deviations. Load distributions. Every ping is a data point about the physical state of the world.

For an adversary with persistent read access to OT networks, that same telemetry stream becomes a battle damage assessment tool.

When a missile strike takes down a substation, the SCADA system sees it happen. Breakers trip. Frequency anomalies propagate. The grid's self-healing logic activates and begins rerouting power. The attacker watching that telemetry in real time sees exactly what went dark, how the system responded, and where residual capacity remains. They're using the grid's own sensors to correct aim for the next salvo.

This is the Inputs Lie framework in its most lethal application. The infrastructure is functioning exactly as designed — collecting accurate data about its own physical state and reporting it faithfully. The problem is who else is reading those reports.

**The Verification Gap**

The Inputs Lie series is built on a premise that keeps proving itself across domains: industrial systems act on signals they cannot verify.

GPS receivers trust positioning data they have no mechanism to authenticate. PLCs execute commands that arrive structurally valid but may originate from an adversary. In Ukraine, the same logic applies in reverse — the SCADA system is faithfully reporting reality, but that reality is now being consumed by an actor using it to refine physical targeting.

But this case exposes something the earlier examples didn't fully surface: the blind spot isn't always about feeding false data into a system. Sometimes it's about losing exclusive view of the truth.

When a defender loses control of who can observe their operational reality, they haven't just lost data confidentiality. They've lost the asymmetry that makes defense possible. The attacker who can watch your grid's real-time response to a strike knows things your own analysts won't have correlated yet — which feeders rerouted, which substations absorbed load, where the system is now stressed. That observational advantage compounds with every subsequent strike. The defender is responding. The attacker is learning.

KAMACITE — tracked extensively by Dragos targeting energy sector OT environments — has demonstrated exactly this pre-positioning behavior: stealing network diagrams, mapping operational dependencies, establishing persistent footholds that survive detection cycles. The Ukraine reporting suggests that access, once established, doesn't sit idle.

**What This Means for Defenders**

We have to stop treating cyber and physical as separate line items on a risk register.

If you are defending a utility, your network monitoring isn't only about preventing a digital blackout. It's about denying an adversary the sensory capability they need to facilitate physical destruction. An attacker with read-only access to your OT telemetry is still extracting operational value — not by manipulating your systems, but by watching them.

The threat model has to account for observation as an attack surface. Not every intrusion that doesn't manipulate anything is benign. Passive access to real-time industrial telemetry, in the right geopolitical context, is reconnaissance with kinetic consequences.

The lesson Ukraine is making impossible to ignore: losing exclusive view of your own operational reality isn't a data breach. It's a targeting advantage handed to whoever is watching.

How many adversaries currently have read access to your infrastructure's truth?

---

_Part of the ongoing Inputs Lie series. Previous entries cover GNSS spoofing, ICS protocol trust assumptions, and the Dragos 2025 OT Year in Review._



ANNOUNCEMENT POST

Ukrainian officials confirmed it this week.

Cyberattacks on the energy grid aren't just causing blackouts.

They're guiding missile strikes.

An adversary with persistent OT access watches SCADA telemetry in real time. When a missile hits a substation, they see exactly what went dark, how the grid rerouted, and where residual capacity remains.

The infrastructure is functioning as designed.
That's the problem.

This is the Inputs Lie framework in its most lethal application — and it changes the threat model for every utility defender in the room.

Read-only access to your OT telemetry isn't a low-severity finding.
In the right geopolitical context, it's a targeting advantage.

New article: When the Grid Becomes a Targeting Sensor: The Lethal Feedback Loop



#CriticalInfrastructure #OTSecurity #ICS #SCADA #InputsLie #GridSecurity #CyberPhysical