# Downloads Organizer

A safe and simple Python script that automatically organizes files in the user's Downloads folder based on their file extensions.

The script includes a dry-run preview and requires explicit confirmation before moving any files.

## Features

- Automatically detects the user's Downloads folder
- Organizes files by file extension
- Supports images, documents, videos, audio files, archives, installers, code files, game files, and more
- Moves unknown file types to the `Other` folder
- Moves files without extensions to the `No Extension` folder
- Handles duplicate filenames automatically
- Creates destination folders only when needed
- Does not move existing folders
- Does not extract archives
- Includes a safe dry-run preview
- Requires the user to type `MOVE` before making changes

## Example

Before:

```text
Downloads/
├── photo.png
├── invoice.pdf
├── movie.mp4
├── setup.exe
├── modpack.7z
└── unknown.xyz
```

After:

```text
Downloads/
├── Images/
│   └── photo.png
│
├── Documents/
│   └── invoice.pdf
│
├── Videos/
│   └── movie.mp4
│
├── Installers/
│   └── setup.exe
│
├── Archives/
│   └── modpack.7z
│
└── Other/
    └── unknown.xyz
```

## Safety

The script performs a dry run before making any changes.

Example:

```text
[DRY RUN] photo.png -> Images/photo.png
[DRY RUN] invoice.pdf -> Documents/invoice.pdf
[DRY RUN] modpack.7z -> Archives/modpack.7z
```

No files are moved during the preview.

Before performing the actual operation, the script asks the user to type:

```text
MOVE
```

Any other input cancels the operation.

## Duplicate Files

If a file with the same name already exists in the destination folder, the script creates a new unique filename.

Example:

```text
photo.png
photo_1.png
photo_2.png
photo_3.png
```

Existing files are not overwritten.

## Archives

Archive files such as:

```text
.zip
.rar
.7z
.tar
.gz
```

are only moved to the `Archives` folder.

They are never extracted or modified.

## Requirements

- Python 3
- Windows

The project uses only Python's standard library, so no additional Python packages are required.

## Usage

Clone or download the repository.

Open a terminal inside the project folder and run:

```bash
python organizer.py
```

The script will display a preview of the planned operations.

Review the preview carefully.

If you want to continue, type:

```text
MOVE
```

Otherwise, enter anything else to cancel.

## Project Structure

```text
downloads-organizer/
├── organizer.py
├── README.md
└── .gitignore
```

## Disclaimer

Always review the dry-run preview before confirming the operation.

Although the script includes safeguards against filename conflicts, it is recommended to keep backups of important files.

## Author

Created as a Python learning project and practical file automation tool.