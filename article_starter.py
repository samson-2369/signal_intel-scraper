import os
from datetime import datetime

def create_article_draft():
    date_str = datetime.now().strftime('%Y-%m-%d')
    # 1. Setup metadata for your website (SEO)
    title = input("Enter the working title of your article: ")
    slug = title.lower().replace(" ", "-")
    filename = f"draft_{date_str}_{slug}.md"

    # 2. Try to find your latest research notes to include them
    research_context = ""
    latest_report = f"report_{date_str}.md"
    
    if os.path.exists(latest_report):
        with open(latest_report, 'r') as f:
            content = f.read()
            if "## 📝 My Research Notes" in content:
                research_context = content.split("## 📝 My Research Notes")[-1]

    # 3. Create the Article Template
    template = f"""---
title: "{title}"
date: {date_str}
series: "When Software Meets the Physical World"
status: draft
---

# {title}

## Introduction
> Write your hook here. Connect the digital vulnerability to the physical impact.

## The Signal
{research_context if research_context else "*(No research notes found for today. Run the scraper first!)*"}

## Technical Deep Dive
## The Impact
## Conclusion
- [ ] Add internal links to cornellsecurity.com
- [ ] Verify diagrams/images are in the folder
"""

    with open(filename, "w") as f:
        f.write(template)
    
    print(f"\n🚀 Success! Draft created: {filename}")
    print("Open it in Obsidian to start writing.")

if __name__ == "__main__":
    create_article_draft()