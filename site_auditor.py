import os
import requests
import shutil
from datetime import datetime

GITHUB_PATH = "/Users/jackcornell/Documents/GitHub/signal_intel-scraper"
ICLOUD_PATH = "/Users/jackcornell/Library/Mobile Documents/com~apple~CloudDocs/Obsidian/signal_intel-scraper"

def audit_site():
    target = "https://cornellsecurity.com"
    filename = "site_health_report.md"
    
    try:
        res = requests.get(target, timeout=10)
        status = "✅ Online" if res.status_code == 200 else f"❌ Error {res.status_code}"
    except Exception as e:
        status = f"❌ Offline (Error: {str(e)})"

    report = f"# 🌐 Website Health Report: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    report += f"- **Status:** {status}\n\n---"

    # Save to GitHub
    github_file = os.path.join(GITHUB_PATH, filename)
    with open(github_file, "w") as f:
        f.write(report)
    
    # Sync to iCloud
    try:
        shutil.copy(github_file, os.path.join(ICLOUD_PATH, filename))
        print(f"✅ Health Audit saved and synced to iCloud.")
    except Exception as e:
        print(f"⚠️ Health Audit saved locally, but sync failed: {e}")

if __name__ == "__main__":
    audit_site()