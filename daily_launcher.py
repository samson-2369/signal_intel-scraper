import subprocess
import os

# Your verified home base
BASE_DIR = "/Users/jackcornell/Documents/GitHub/signal_intel-scraper"

def run_daily_ops():
    # 1. Run the Intelligence Scraper
    print("🛰️ Gathering Signals...")
    scraper_path = os.path.join(BASE_DIR, "signal_intel_scraper.py")
    subprocess.run(["/usr/bin/python3", scraper_path])

    # 2. Run the Site Auditor
    print("🌐 Auditing Website...")
    auditor_path = os.path.join(BASE_DIR, "site_auditor.py")
    subprocess.run(["/usr/bin/python3", auditor_path])

    print("✅ All daily reports generated and synced to Obsidian!")

if __name__ == "__main__":
    run_daily_ops()