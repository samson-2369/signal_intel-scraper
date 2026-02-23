import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from datetime import datetime

# CONFIGURATION
TARGET_SITE = "https://cornellsecurity.com"
REPORT_NAME = "site_health_report.md"

def get_links(url):
    """Finds all internal and external links on a page."""
    links = set()
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        for a in soup.find_all('a', href=True):
            full_url = urljoin(url, a['href'])
            links.add(full_url)
    except Exception as e:
        print(f"Error reading {url}: {e}")
    return links

def audit_site():
    print(f"🚀 Starting audit of {TARGET_SITE}...")
    start_time = datetime.now()
    
    # We'll just check the homepage and the links it finds for this 'rusty' version
    all_links = get_links(TARGET_SITE)
    broken_links = []
    working_count = 0

    for link in all_links:
        try:
            # We use a 'HEAD' request to be fast (just check the status, don't download everything)
            res = requests.head(link, allow_redirects=True, timeout=5)
            if res.status_code >= 400:
                broken_links.append((link, res.status_code))
            else:
                working_count += 1
        except:
            broken_links.append((link, "TIMEOUT/ERROR"))

    # Generate Markdown Report
    report_content = f"# 🌐 Website Health Report: {datetime.now().strftime('%Y-%m-%d')}\n\n"
    report_content += f"### 📊 Quick Stats\n"
    report_content += f"- **Links Checked:** {len(all_links)}\n"
    report_content += f"- **Working:** ✅ {working_count}\n"
    report_content += f"- **Broken:** ❌ {len(broken_links)}\n\n"

    report_content += "## 🛠️ Maintenance To-Do List\n"
    if broken_links:
        for link, code in broken_links:
            report_content += f"- [ ] Fix link: {link} (Error: {code})\n"
    else:
        report_content += "- [x] No broken links found! Great job maintaining the site.\n"

    report_content += f"\n---\n*Audit completed in {datetime.now() - start_time}*"

    with open(REPORT_NAME, "w") as f:
        f.write(report_content)
    
    print(f"✅ Audit complete! Report saved to {REPORT_NAME}")

if __name__ == "__main__":
    audit_site()