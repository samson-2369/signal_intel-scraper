import feedparser
from datetime import datetime
import os

# PATHS
GITHUB_PATH = "/Users/jackcornell/Documents/GitHub/signal_intel-scraper"

# Watchlist: Specialized for RF, Satellite, and ICS
keywords = ["satellite", "GNSS", "GPS", "spoofing", "jamming", "ICS", "SCADA", "PLC", "modbus", "RF", "radio", "physical layer", "zero-day", "water sector", "energy grid"]

feeds = {
    "The Record": "https://therecord.media/feed/",
    "Cyberscoop": "https://www.cyberscoop.com/feed/",
    "SANS ICS": "https://ics.sans.org/blog/feed/",
    "Dragos": "https://www.dragos.com/feed/",
    "SpaceNews": "https://spacenews.com/feed/",
    "CISA Alerts": "https://www.cisa.gov/cybersecurity-advisories.xml"
}

def run_dual_scraper():
    date_str = datetime.now().strftime('%Y-%m-%d')
    print(f"🚀 Running Dual-Output Scraper for {date_str}...")

    # 1. Gather Data
    matches = []
    for name, url in feeds.items():
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                content = (entry.title + entry.get('summary', '')).lower()
                if any(key.lower() in content for key in keywords):
                    matches.append({"title": entry.title, "link": entry.link, "source": name})
        except: continue

    # 2. Generate Obsidian Markdown (Your Internal Workflow)
    md_content = f"# 📡 Signal Intel: {date_str}\n\n"
    for m in matches:
        md_content += f"### [{m['title']}]({m['link']})\n*Source: {m['source']}*\n\n"
    
    with open(os.path.join(GITHUB_PATH, f"report_{date_str}.md"), "w") as f:
        f.write(md_content)

    # 3. Generate Website HTML (Your Public Platform)
    html_content = f"""
    <html>
    <head>
        <style>
            body {{ font-family: sans-serif; line-height: 1.6; max-width: 800px; margin: auto; padding: 20px; background: #f4f4f4; }}
            .card {{ background: white; padding: 15px; margin-bottom: 10px; border-radius: 5px; border-left: 5px solid #2c3e50; }}
            h1 {{ color: #2c3e50; }}
            a {{ color: #3498db; text-decoration: none; font-weight: bold; }}
        </style>
    </head>
    <body>
        <h1>🛰️ Daily Signal Intelligence Briefing</h1>
        <p><i>Generated on {date_str} for Cornell Security Research</i></p>
    """
    for m in matches:
        html_content += f"""
        <div class="card">
            <h3>{m['title']}</h3>
            <p>Source: {m['source']}</p>
            <a href="{m['link']}" target="_blank">Read Full Report →</a>
        </div>
        """
    html_content += "</body></html>"

    with open(os.path.join(GITHUB_PATH, "daily_briefing.html"), "w") as f:
        f.write(html_content)
    
    print(f"✅ Done! Created Obsidian report and Website HTML in {GITHUB_PATH}")

if __name__ == "__main__":
    run_dual_scraper()