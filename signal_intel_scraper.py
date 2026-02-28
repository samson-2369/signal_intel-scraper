import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# --- CONFIGURATION ---
GITHUB_PATH = "/Users/jackcornell/Documents/GitHub/signal_intel-scraper/"
HTML_FILE = os.path.join(GITHUB_PATH, "daily_briefing.html")
OBSIDIAN_FILE = os.path.join(GITHUB_PATH, f"Daily_Intel_{datetime.now().strftime('%Y-%m-%d')}.md")

FEEDS = {
    "Cyberscoop": "https://cyberscoop.com/feed/",
    "SpaceNews": "https://spacenews.com/feed/",
    "The Record": "https://therecord.media/feed/"
}

def get_intel():
    all_reports = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    for source, url in FEEDS.items():
        try:
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, "lxml-xml")
            items = soup.find_all("item")[:5] 
            for item in items:
                all_reports.append({
                    "source": source,
                    "title": item.title.text,
                    "link": item.link.text
                })
        except Exception as e:
            print(f"⚠️ Error fetching {source}: {e}")
    return all_reports

def generate_outputs(reports):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # HTML GENERATION
    html = f"<html><head><style>body{{font-family:sans-serif;max-width:800px;margin:auto;padding:20px;overflow-y:auto;height:100vh;}}.card{{background:white;padding:20px;margin-bottom:15px;border-left:6px solid #2c3e50;box-shadow:0 2px 5px rgba(0,0,0,0.1);}}</style></head><body><h1>📡 Daily Intel - {now}</h1>"
    for r in reports:
        html += f"<div class='card'><b>{r['source']}</b><h3>{r['title']}</h3><a href='{r['link']}'>Read More →</a></div>"
    html += "</body></html>"
    # OBSIDIAN GENERATION
    md = f"# 🛰️ Daily Intel - {now}\n\n"
    for r in reports:
        md += f"### {r['title']}\n- Source: {r['source']}\n- [Link]({r['link']})\n\n"
    with open(HTML_FILE, "w") as f: f.write(html)
    with open(OBSIDIAN_FILE, "w") as f: f.write(md)
    print(f"✅ Success! Dashboard updated and Obsidian report created at {now}")

if __name__ == "__main__":
    intel = get_intel()
    if intel: generate_outputs(intel)