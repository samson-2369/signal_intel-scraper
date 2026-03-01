# Cornell Security — cornellsecurity.com

Personal website and research portfolio of **Norris Cornell**, Specialist in Cyber-Physical Systems & ICS Signal Integrity.

## About

This repository hosts the source for [cornellsecurity.com](https://cornellsecurity.com) — a professional site featuring original research, technical white papers, and field analysis on ICS/OT security and critical infrastructure defense.

## Research Focus

- **Physical-Layer Security** — GNSS/GPS timing vulnerabilities, RF signal integrity, and sub-threshold attack detection in ICS/OT environments
- **Cyber-Physical Systems** — Security at the intersection of digital control logic and physical infrastructure
- **ICS/OT Frameworks** — MITRE ATT&CK for ICS, NERC CIP, NIST 800-82, RMF
- **"Inputs Lie" Framework** — Original research on how deterministic ICS logic can be manipulated through unverified external inputs

## Tools in This Repository

The following scripts are part of an open-source intelligence collection and analysis toolkit developed for monitoring the ICS/cybersecurity/critical infrastructure landscape:

| Script | Description |
|---|---|
| `signal_intel_scraper.py` | Aggregates and parses security news from curated sources |
| `archiver.py` | Archives daily intelligence reports for longitudinal analysis |
| `article_starter.py` | Scaffolds article drafts from raw intelligence inputs |
| `site_auditor.py` | Monitors site health and content integrity |
| `weekly_digest.py` | Compiles weekly intelligence summaries |

## Site Structure

```
/
├── index.html          # Homepage
├── about.html          # Bio and expertise
├── research.html       # White papers and frameworks
├── blog.html           # Field notes and analysis
├── contact.html        # Speaking and collaboration
├── css/style.css       # Stylesheet
├── CNAME               # Custom domain config
└── robots.txt          # Crawler policy
```

## Copyright

© 2026 Norris Cornell. All Rights Reserved.

All research, written content, and frameworks published on this site and in this repository are the intellectual property of Norris Cornell. The intelligence-collection scripts are provided for educational and research purposes. No written content may be reproduced or redistributed without prior written permission.
