import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime

VAULT_PATH = "/Users/jackcornell/Documents/GitHub/signal_intel-scraper"
TARGET_SITE = "https://cornellsecurity.com"

def get_links(url):
    links = set()
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        for a in soup.find_all('a', href=True):
            full_url = urljoin(url, a['href'])
            if TARGET_SITE in full_url:
                links.add(full_url)
    except Exception as e:
        print(f"Error reading {url}: {e}")
    return links

def audit_site():
    start_time = datetime.now()
    all_links = get_links(TARGET_SITE)
    broken_links = []
    working_count = 0

    print(f"🚀 Starting audit of {TARGET_SITE}...")

    for link in list(all_links)[:15]: # Checking top 15 links for speed
        try:
            res = requests.head(link, allow_redirects=True, timeout=5)
            if res.status_code >= 400:
                broken_links.append((link, res.status_code))
            else:
                working_count += 1
        except:
            broken_links.append((link, "TIMEOUT/ERROR"))

    report_content = f"# 🌐 Website Health Report: {datetime.now().strftime('%Y-%m-%d')}\n\n"
    report_content += f"### 📊 Quick Stats\n"
    report_content += f"- **Links Checked:** {len(all_links)}\n"
    report_content += f"- **Working:** ✅ {working_count}\n"
    report_content += f"- **Broken:** ❌ {len(broken_links)}\n\n"
    
    report_content += "### 🛠️ Maintenance To-Do List\n"
    if broken_links:
        for link, code in broken_links:
            report_content += f"- [ ] Fix link: {link} (Error: {code})\n"
    else:
        report_content += "- [x] No broken links found! Site is healthy.\n"

    report_content += f"\n---\n*Audit completed in {datetime.now() - start_time}*"

    full_path = os.path.join(VAULT_PATH, "site_health_report.md")
    with open(full_path, "w") as f:
        f.write(report_content)
    print(f"✅ Audit complete! Report saved to Obsidian.")

if __name__ == "__main__":
    audit_site()