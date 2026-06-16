import os
import shutil
from datetime import datetime

print("BACKUP MANAGER DEMO")

SOURCE_DIR = "source_data"
BACKUP_DIR = "backups"

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

backup_name = f"backup_{timestamp}"

destination = os.path.join(
    BACKUP_DIR,
    backup_name
)

os.makedirs(
    destination,
    exist_ok=True
)

copied_files = 0

for filename in os.listdir(SOURCE_DIR):

    source_file = os.path.join(
        SOURCE_DIR,
        filename
    )

    if os.path.isfile(source_file):

        shutil.copy2(
            source_file,
            destination
        )

        copied_files += 1

total_size = 0

for root, dirs, files in os.walk(destination):

    for file in files:

        file_path = os.path.join(
            root,
            file
        )

        total_size += os.path.getsize(
            file_path
        )

with open(
    "report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write(
        "BACKUP MANAGER REPORT\n\n"
    )

    report.write(
        f"Backup folder: {backup_name}\n"
    )

    report.write(
        f"Files copied: {copied_files}\n"
    )

    report.write(
        f"Total size: {total_size} bytes\n"
    )

print("BACKUP CREATED")
print("REPORT CREATED")
