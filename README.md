# Python File Organizer

A simple Python automation project that automatically organizes files into folders based on their extensions.

## Features

- Automatically categorizes files into Images, Documents, Audio, and Others.
- Creates category folders when needed.
- Prevents overwriting files with duplicate names.
- Handles file-moving errors using exception handling.
- Records successful moves, duplicate warnings, and errors using Python logging.
- Checks whether the source folder exists.

## Technologies Used

- Python
- pathlib
- shutil
- logging

## How to Run

1. Make sure Python is installed.
2. Download or clone this repository.
3. Create a folder named `Test-Files` in the project directory.
4. Place some test files inside `Test-Files`.
5. Run the command:

   `python File-Organizer.py`

The program will automatically organize the files into the appropriate folders.

## Supported File Types

| Category | Extensions |
|---|---|
| Images | .jpg, .png |
| Documents | .txt, .pdf |
| Audio | .mp3 |
| Others | All remaining extensions |

## Note

The program skips existing subfolders and does not overwrite files with duplicate names. The `Test-Files` folder and generated log file are excluded from Git tracking.