import os
import shutil
from datetime import datetime, timedelta

def run_archiver():
    # Define your paths
    report_folder = "."
    archive_path = "./Archive/Reports"
    
    # Create the archive folder if it doesn't exist
    if not os.path.exists(archive_path):
        os.makedirs(archive_path)

    # Calculate the cutoff date (30 days ago)
    cutoff = datetime.now() - timedelta(days=30)
    
    moved_count = 0
    for filename in os.listdir(report_folder):
        # Look for report files (e.g., report_2026-01-20.md)
        if filename.startswith("report_") and filename.endswith(".md"):
            try:
                # Extract date from filename
                file_date_str = filename.replace("report_", "").replace(".md", "")
                file_date = datetime.strptime(file_date_str, "%Y-%m-%d")
                
                if file_date < cutoff:
                    shutil.move(os.path.join(report_folder, filename), 
                                os.path.join(archive_path, filename))
                    moved_count += 1
            except Exception as e:
                print(f"Skipping {filename}: {e}")

    print(f"🧹 Cleanup complete. Moved {moved_count} old reports to Archive.")

if __name__ == "__main__":
    run_archiver()