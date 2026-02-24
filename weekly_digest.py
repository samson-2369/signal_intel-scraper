import os
from datetime import datetime, timedelta

def run_weekly_digest():
    today = datetime.now()
    week_ago = today - timedelta(days=7)
    
    digest_content = f"# 🗓️ Weekly Signal Digest: {week_ago.strftime('%Y-%m-%d')} to {today.strftime('%Y-%m-%d')}\n\n"
    all_titles = []

    # 1. Collect all report files from the last 7 days
    for i in range(8):
        check_date = (today - timedelta(days=i)).strftime('%Y-%m-%d')
        filename = f"report_{check_date}.md"
        
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                content = f.read()
                # Find the article titles
                lines = content.split('\n')
                titles = [line for line in lines if line.startswith('### [')]
                all_titles.extend(titles)

    # 2. Summarize findings
    digest_content += f"### 📊 Total Signals Detected: {len(all_titles)}\n\n"
    digest_content += "### 🏆 Top Headlines This Week\n"
    for title in all_titles[:10]: # Show the most recent 10
        digest_content += f"{title}\n"

    digest_content += "\n---\n## 🧠 Recommendation\n"
    digest_content += "> Based on this volume, you should consider a 'Physical Layer' deep dive into the most recurring topic above."

    with open("weekly_digest_report.md", "w") as f:
        f.write(digest_content)
    print("✅ Weekly Digest generated in Obsidian.")

if __name__ == "__main__":
    run_weekly_digest()