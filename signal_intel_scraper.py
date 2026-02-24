import feedparser
from datetime import datetime
import os

# THE FIXED PATH: Your local GitHub folder
VAULT_PATH = "/Users/jackcornell/Documents/GitHub/signal_intel-scraper"

# 1. Your Watchlist: Keywords & Specialized Feeds
keywords = [
    "satellite", "GNSS", "GPS", "spoofing", "jamming",
    "ICS", "SCADA", "PLC", "modbus", "industrial",
    "RF", "radio", "telemetry", "firmware", "physical layer",
    "zero-day", "exploit", "water sector", "energy grid"
]

feeds = {
    "The Record": "https://therecord.media/feed/",
    "Cyberscoop": "https://www.cyberscoop.com/feed/",
    "SANS ICS": "https://ics.sans.org/blog/feed/",
    "Dragos": "https://www.dragos.com/feed/",
    "SpaceNews": "https://spacenews.com/feed/",
    "CISA Alerts": "https://www.cisa.gov/cybersecurity-advisories.xml",
    "Krebs": "https://krebsonsecurity.com/feed/",
    "DarkReading": "https://darkreading.com/rss.xml"
}

def run_scraper():
    date_str = datetime.now().strftime('%Y-%m-%d')
    report_content = f"# 📡 Signal Intelligence Report: {date_str}\n\n"
    found_articles = 0

    print(f"🚀 Starting scan for {date_str}...")

    for name, url in feeds.items():
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                # Check if keywords appear in title or summary
                title = entry.get('title', '')
                summary = entry.get('summary', '')
                content_to_check = (title + summary).lower()
                
                if any(key.lower() in content_to_check for key in keywords):
                    report_content += f"### [{title}]({entry.link})\n"
                    report_content += f"*Source: {name}*\n\n"
                    found_articles += 1
        except Exception as e:
            print(f"⚠️ Could not reach {name}: {e}")

    if found_articles == 0:
        report_content += "*No specific keyword matches found in today's top stories.*\n"

    report_content += "\n---\n## 📝 My Research Notes\n> Use this space to connect today's news to the 'When Software Meets the Physical World' series.\n"
    
    # Save the file
    if not os.path.exists(VAULT_PATH):
        os.makedirs(VAULT_PATH)
    
    filename = f"report_{date_str}.md"
    full_path = os.path.join(VAULT_PATH, filename)
    
    with open(full_path, "w") as f:
        f.write(report_content)
    
    print(f"✅ Success! {found_articles} signals saved to Obsidian.")

if __name__ == "__main__":
    run_scraper()