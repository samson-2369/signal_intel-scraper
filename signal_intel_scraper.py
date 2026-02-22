import feedparser
from datetime import datetime
import os

# 1. Your Watchlist: Keywords & Specialized Feeds
# Optimized for ICS/OT, Satellite, and RF Security
keywords = [
    "satellite", "GNSS", "GPS", "spoofing", "jamming", 
    "ICS", "SCADA", "PLC", "modbus", "industrial", 
    "RF", "radio", "telemetry", "firmware", "physical layer",
    "zero-day", "exploit", "water sector", "energy grid"
]

feeds = [
    "https://therecord.media/feed/",
    "https://www.cyberscoop.com/feed/",
    "https://ics.sans.org/blog/feed/",          # Deep ICS/OT focus
    "https://www.dragos.com/feed/",             # Industrial threat intel
    "https://spacenews.com/feed/",              # Satellite industry
    "https://www.cisa.gov/cybersecurity-advisories.xml", # Govt alerts
    "https://krebsonsecurity.com/feed/",        # High-level security news
    "https://darkreading.com/rss.xml"           # General industry trends
]

def run_scraper():
    # Header with date for your Obsidian Article Feed
    date_str = datetime.now().strftime('%Y-%m-%d')
    report_content = f"# Signal Intelligence Report - {date_str}\n\n"
    
    found_articles = 0
    
    print(f"Starting scan for {date_str}...")

    # Process each feed
    for url in feeds:
        try:
            feed = feedparser.parse(url)
            source_name = feed.feed.title if 'title' in feed.feed else url
            
            for entry in feed.entries:
                # Check if keywords appear in title or summary
                title = entry.title if 'title' in entry else "No Title"
                summary = entry.summary if 'summary' in entry else ""
                
                content_to_check = (title + summary).lower()
                
                if any(key.lower() in content_to_check for key in keywords):
                    report_content += f"### [{title}]({entry.link})\n"
                    report_content += f"*Source: {source_name}*\n\n"
                    found_articles += 1
        except Exception as e:
            print(f"Could not reach {url}: {e}")

    if found_articles == 0:
        report_content += "_No specific keyword matches found in today's top stories._\n\n"

    # --- Research Notes Section ---
    # This section stays at the bottom for you to fill out in Obsidian
    report_content += "---\n"
    report_content += "## 📝 My Research Notes\n"
    report_content += "> Use this space to connect today's news to the 'When Software Meets the Physical World' series.\n\n"
    report_content += "### 💡 Key Takeaways\n- \n\n"
    report_content += "### 🛠️ Hardware/RF Connection\n- \n\n"
    report_content += "### 📝 Article Ideas\n- \n\n"
    report_content += "### ✅ To-Do\n- [ ] Fact-check this for the website\n- [ ] Archive relevant diagrams\n"

    # 2. Save with a unique date so your feed grows over time
    filename = f"report_{date_str}.md"
    
    with open(filename, "w") as f:
        f.write(report_content)
    
    print(f"Success! Generated {filename} with {found_articles} articles found.")

if __name__ == "__main__":
    run_scraper()