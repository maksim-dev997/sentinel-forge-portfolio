import os
import shutil

print("FILE ORGANIZER DEMO")

SOURCE_FOLDER = "demo_files"

TEXT_FOLDER = os.path.join(SOURCE_FOLDER, "TEXT")
IMAGE_FOLDER = os.path.join(SOURCE_FOLDER, "IMAGES")
PDF_FOLDER = os.path.join(SOURCE_FOLDER, "PDF")

os.makedirs(TEXT_FOLDER, exist_ok=True)
os.makedirs(IMAGE_FOLDER, exist_ok=True)
os.makedirs(PDF_FOLDER, exist_ok=True)

for filename in os.listdir(SOURCE_FOLDER):

    file_path = os.path.join(SOURCE_FOLDER, filename)

    if os.path.isdir(file_path):
        continue

    if filename.endswith(".txt"):

        shutil.move(
            file_path,
            os.path.join(TEXT_FOLDER, filename)
        )

    elif filename.endswith(".jpg") or filename.endswith(".png"):

        shutil.move(
            file_path,
            os.path.join(IMAGE_FOLDER, filename)
        )

    elif filename.endswith(".pdf"):

        shutil.move(
            file_path,
            os.path.join(PDF_FOLDER, filename)
        )

print("FILES ORGANIZED")
