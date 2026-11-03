import shutil
import logging
from pathlib import Path

logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    encoding="utf-8",
)


folder = Path("Test-Files")


images_folder = folder / "Images"
other_folder = folder / "Others"
documents_folder = folder / "Documents"
audio_folder = folder / "Audio"


def create_folders():

    images_folder.mkdir(exist_ok=True)
    other_folder.mkdir(exist_ok=True)
    documents_folder.mkdir(exist_ok=True)
    audio_folder.mkdir(exist_ok=True)


def move_file(source, destination):
    if destination.exists():
        logging.warning(f"{source.name} already exists")
        print("File already exists")
    else:
        try:
            shutil.move(str(source), str(destination))
            logging.info(f"{source.name} moved to {destination.parent.name}")
            print(source.name, "->", destination.parent.name)
        except OSError as e:
            logging.error(f"Failed to move {source.name}: {e}")
            print("Error", e)


def organize_files():
    for file in folder.iterdir():
        if not file.is_file():
            continue

        suffix = file.suffix.lower()

        if suffix in [".png", ".jpg"]:
            move_file(file, images_folder / file.name)

        elif suffix in [".txt", ".pdf"]:
            move_file(file, documents_folder / file.name)

        elif suffix in [".mp3"]:
            move_file(file, audio_folder / file.name)

        else:
            move_file(file, other_folder / file.name)


if folder.is_dir():
    create_folders()
    organize_files()
else:
    print("Error: Test-Files folder not found")
