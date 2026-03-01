import feedparser
import os
import subprocess
from datetime import datetime

# --- CONFIGURATION: PATHS ---
OBSIDIAN_PATH = "/Users/jackcornell/Library/Mobile Documents/iCloud~md~obsidian/Documents/signal_intel-scraper"
WEB_ROOT = "/Users/jackcornell/Documents/GitHub/signal_intel-scraper"

# --- CONFIGURATION: IDENTITY & IP PROTECTION ---
AUTHOR = "Norris Cornell"
EMAIL = "npcornell@hotmail.com"  # Linked to your resume records
STATION_ID = "CORNELL SECURITY | PORTFOLIO & INTEL"

# --- CONFIGURATION: GROUNDED ABOUT ME ---
ABOUT_ME_HTML = f"""
<div class="norris-profile">
    <h2>{AUTHOR}</h2>
    <p><b>Specialist in Cyber-Physical Systems & ICS Signal Integrity</b></p>
    
    <p>I am a cybersecurity researcher and practitioner with nearly 20 years of hands-on experience 
    in electronics and industrial systems. My work sits at the intersection of physical-layer 
    security and critical infrastructure defense — approaching ICS/OT security from the sensor up, 
    not just the network down.</p>

    <p>As the author of the <b>"Inputs Lie"</b> research framework, I investigate how deterministic 
    logic in SCADA and ICS environments can be manipulated through physical-layer signal drift, 
    GNSS timing manipulation, and unverified external inputs. My research addresses a structural 
    blind spot in current security frameworks: critical infrastructure systems implicitly trust 
    external signals that can be manipulated below traditional detection thresholds by patient, 
    sophisticated adversaries.</p>

    <h3>Core Expertise</h3>
    <ul>
        <li><b>Physical-Layer Security:</b> GNSS/GPS timing vulnerabilities, RF signal integrity, and low signal-to-noise ratio attack detection in ICS/OT environments.</li>
        <li><b>Hardware Assurance:</b> 20 years of diagnostic experience with electronic systems, control circuits, and industrial protocols including Modbus and DNP3.</li>
        <li><b>ICS/OT Frameworks:</b> MITRE ATT&CK for ICS, NERC CIP, NIST 800-82, and Risk Management Framework (RMF).</li>
        <li><b>Identity & Access Management:</b> Technical lead for IAM programs in regulated financial and critical infrastructure-adjacent environments.</li>
    </ul>

    <h3>Research & Community</h3>
    <p>I am an active contributor to the ICS security community, presenting research on the 
    convergence of SIGINT, satellite cybersecurity, and ICS/OT security. I have presented 
    research such as "When Cyber Meets the Spectrum" at BSides Delaware and serve as a 
    long-term organizer and volunteer. Current research targets conference submission 
    to the ICS Cyber Security Conference or S4.</p>
</div>
"""

# --- CONFIGURATION: RSS FEEDS ---
FEEDS = {
    "SpaceNews (Satellite/GNSS)": "https://spacenews.com/feed/",
    "CyberScoop (ICS/Infrastructure)": "https://cyberscoop.com/feed/",
    "The Record (State Actors)": "https://therecord.media/feed/"
}

def scrape_intel():
    print(f"--- Starting Intelligence Scrape: {datetime.now()} ---")
    all_entries = []
    for source, url in FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:
            all_entries.append({
                "source": source, "title": entry.title,
                "link": entry.link, "summary": entry.get("summary", "No summary.")
            })
    return all_entries

def generate_web_pages(intel):
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # --- SHARED STYLING ---
    STYLE = """
    :root { --bg: #0d1117; --card: #161b22; --border: #30363d; --text: #c9d1d9; --accent: #58a6ff; --green: #3fb950; }
    body { font-family: -apple-system, sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 20px; line-height: 1.6; }
    .nav { display: flex; gap: 20px; border-bottom: 1px solid var(--border); padding-bottom: 15px; margin-bottom: 30px; font-size: 0.9rem; }
    .nav a { color: var(--accent); text-decoration: none; font-weight: bold; }
    .card { background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 20px; margin-bottom: 15px; }
    .title { display: block; color: #f0f6fc; font-weight: 600; text-decoration: none; margin: 10px 0; }
    .btn { display: inline-block; background: var(--green); color: #fff; text-decoration: none; padding: 12px 24px; border-radius: 6px; font-weight: 600; margin-top: 15px; }
    footer { text-align: center; font-size: 0.7rem; color: #484f58; margin-top: 50px; }
    @media (min-width: 768px) { body { max-width: 850px; margin: auto; } }
    """

    # --- 1. GENERATE INDEX.HTML (DASHBOARD) ---
    index_html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>{STATION_ID}</title><style>{STYLE}</style></head><body>
    <div class="nav"><a href="index.html">DASHBOARD</a><a href="research.html">RESEARCH HUB</a></div>
    {ABOUT_ME_HTML}
    <hr style="border: 0; border-top: 1px solid var(--border); margin: 40px 0;">
    <h3>Live Signal Intelligence</h3>
    """
    for item in intel:
        index_html += f"""<div class="card"><span style="color: var(--accent); font-size: 0.7rem; font-family: monospace;">{item['source']}</span>
        <a class="title" href="{item['link']}" target="_blank">{item['title']}</a><p style="color: #8b949e; font-size: 0.85rem;">{item['summary'][:200]}...</p></div>"""
    index_html += f"<footer>© 2026 {AUTHOR}. Powered by Custom OSINT Pipeline.</footer></body></html>"
    
    with open(os.path.join(WEB_ROOT, "index.html"), "w") as f: f.write(index_html)

    # --- 2. GENERATE RESEARCH.HTML (IP PROTECTED HUB) ---
    research_html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>RESEARCH | {AUTHOR}</title><style>{STYLE}</style></head><body>
    <div class="nav"><a href="index.html">DASHBOARD</a><a href="research.html">RESEARCH HUB</a></div>
    <h1>Technical Research & Whitepapers</h1>
    <div class="card">
        <div style="font-weight: bold; color: #fff; font-size: 1.2rem; margin-bottom: 10px;">Signal Manipulation in ICS: Why Traditional Security Fails at the Physics Layer</div>
        <p style="font-style: italic; color: #8b949e;"><b>Abstract:</b> Industrial control systems rely on deterministic assumptions that inputs follow physical laws. This research explores how "When Harmonics Become Attack Vectors," traditional security fails to detect signal drift manipulated below detection thresholds.</p>
        <div style="margin: 15px 0;"><strong style="font-size: 0.8rem; color: var(--accent);">TECHNICAL DEPTH:</strong>
            <ul style="font-size: 0.85rem; color: #8b949e;">
                <li>RF Signal Analysis & GNSS Timing Vulnerabilities</li>
                <li>Low Signal-to-Noise Ratio attack detection methodologies</li>
                <li>Physics-layer modeling of sensor harmonic distortion</li>
            </ul>
        </div>
        <a href="mailto:{EMAIL}?subject=Access Request: ICS Physics Paper" class="btn">Request Full Technical Annex (PDF)</a>
    </div>
    <footer>© 2026 {AUTHOR}. Novel research protected by cryptographic timestamping.</footer></body></html>"""
    
    with open(os.path.join(WEB_ROOT, "research.html"), "w") as f: f.write(research_html)

def generate_obsidian_log(intel):
    file_date = datetime.now().strftime("%Y-%m-%d")
    md_content = f"# Signal Intel Report: {file_date}\n\n"
    for item in intel:
        md_content += f"### {item['title']}\n**Source:** {item['source']}\n**Link:** {item['link']}\n\n> {item['summary']}\n\n---\n"
    
    with open(os.path.join(OBSIDIAN_PATH, f"Intel-{file_date}.md"), "w") as f: f.write(md_content)

def push_to_web():
    try:
        os.chdir(WEB_ROOT)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"Automated Update: {datetime.now().strftime('%Y-%m-%d')}"], check=True)
        subprocess.run(["git", "push", "origin", "master", "--force"], check=True)
        print(f"🟢 SUCCESS: {AUTHOR}'s Research Station is LIVE.")
    except Exception as e: print(f"❌ Deploy Failed: {e}")

if __name__ == "__main__":
    intel = scrape_intel()
    if intel:
        generate_web_pages(intel)
        generate_obsidian_log(intel)
        push_to_web()