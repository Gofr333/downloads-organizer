# Downloads Organizer

A safe and simple Python tool that automatically organizes files inside your **Downloads** folder based on their file extensions.

The organizer creates a preview before moving anything and requires explicit confirmation before making changes.

## Features

* Automatically detects the user's Downloads folder
* Organizes files by file extension
* Supports images, documents, videos, audio, archives, installers, code files, game files, and many other formats
* Moves unknown file types to the `Other` folder
* Moves files without extensions to the `No Extension` folder
* Moves ambiguous file types to the `Review` folder
* Automatically handles duplicate filenames
* Never intentionally overwrites existing files
* Creates destination folders only when needed
* Does not move existing folders
* Does not extract archives
* Skips files that are still being downloaded
* Skips symbolic links
* Skips common Windows system files
* Skips the organizer script itself
* Creates an exact organization plan before moving files
* Requires confirmation using `MOVE <number>`
* Continues working if an individual file causes an error
* Displays scan and final organization statistics
* Uses only Python's standard library

---

# Quick Start

## 1. Download the project

Download the repository from GitHub.

After extracting it, the folder should contain:

```text
downloads-organizer/
├── organizer.py
├── run_organizer.bat
├── README.md
└── .gitignore
```

## 2. Start the organizer

Double-click:

```text
run_organizer.bat
```

That's it.

The launcher will automatically try to start the organizer using Python.

You do not need to manually open PowerShell.

---

# Using the Organizer

After starting `run_organizer.bat`, the program scans your Downloads folder.

It then displays a preview of the planned operations.

Example:

```text
============================================================
PREVIEW - NO FILES HAVE BEEN MOVED
============================================================

[PLAN] photo.png -> Images/photo.png
[PLAN] invoice.pdf -> Documents/invoice.pdf
[PLAN] setup.exe -> Installers/setup.exe
[PLAN] modpack.7z -> Archives/modpack.7z
```

At this stage, no files have been moved.

The program also displays a summary:

```text
============================================================
SCAN SUMMARY
============================================================
Files planned:            4
Folders skipped:          5
Active downloads skipped: 1
System files skipped:     1
Symlinks skipped:         0
Organizer skipped:        0
Planning errors:          0
```

---

# Confirmation

Before moving any files, the organizer requires confirmation.

For example:

```text
4 file(s) will be moved inside your Downloads folder.

Type "MOVE 4" to continue.
```

To continue, type exactly:

```text
MOVE 4
```

The number must match the number displayed by the program.

Any other input cancels the operation.

Example:

```text
Operation cancelled.
No files were moved.
```

---

# Example

Before:

```text
Downloads/
├── photo.png
├── invoice.pdf
├── movie.mp4
├── setup.exe
├── modpack.7z
├── unknown.xyz
└── notes
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
├── Other/
│   └── unknown.xyz
│
└── No Extension/
    └── notes
```

---

# Safety

The organizer includes several safeguards.

## Preview

The script always shows the exact organization plan before moving files.

No files are moved during the preview.

## Explicit Confirmation

The user must confirm using:

```text
MOVE <number>
```

For example:

```text
MOVE 25
```

## Existing Folders

Existing folders inside Downloads are not moved.

## Active Downloads

Files that appear to still be downloading are skipped.

Examples:

```text
.crdownload
.part
.partial
.download
```

Temporary Microsoft Office files beginning with:

```text
~$
```

are also skipped.

## Windows System Files

Common Windows system files such as:

```text
desktop.ini
Thumbs.db
```

are skipped.

## Symbolic Links

Symbolic links are skipped to avoid accidentally affecting files outside the Downloads folder.

## Organizer Protection

If `organizer.py` itself is located inside the Downloads folder, the script will not move itself.

---

# Duplicate Files

Existing files are not intentionally overwritten.

If this file already exists:

```text
photo.png
```

the organizer creates a unique filename:

```text
photo_1.png
photo_2.png
photo_3.png
```

Example:

```text
Images/
├── photo.png
├── photo_1.png
└── photo_2.png
```

The organizer also reserves filenames while creating the preview, preventing planned files from receiving the same destination.

---

# Archives

Archive files are only moved.

They are never extracted or modified.

Examples:

```text
.zip
.rar
.7z
.tar
.gz
.gzip
.bz2
.xz
.tgz
.tbz
.tbz2
.txz
.cab
.ace
.zst
```

For example:

```text
Downloads/modpack.7z
```

becomes:

```text
Downloads/Archives/modpack.7z
```

The contents of the archive remain unchanged.

---

# File Categories

The organizer supports categories including:

```text
Images
Documents
Spreadsheets
Presentations
Videos
Audio
Archives
Installers
Disk Images
Ebooks
Fonts
Subtitles
Code
Java
Data
Databases
Configs
Logs
Backups
Temporary
Torrents
Shortcuts
Certificates
3D Models
CAD
Design
Media Projects
Mods
Game Files
Game Saves
ROMs
3D Printing
Emails
Calendar
Contacts
Review
Other
No Extension
```

Unknown file extensions are moved to:

```text
Other
```

Files without extensions are moved to:

```text
No Extension
```

Ambiguous file extensions are moved to:

```text
Review
```

---

# Error Handling

If one file cannot be moved, the entire program does not stop.

Instead, the organizer displays an error and continues processing the remaining files.

Example:

```text
[ERROR] example.pdf: ...
```

The final summary shows how many files were moved successfully and how many errors occurred.

---

# Manual Start

If you prefer not to use the Windows launcher, you can run the Python script manually.

Open PowerShell or another terminal inside the project folder and run:

```powershell
python organizer.py
```

If `python` is not recognized, try:

```powershell
py organizer.py
```

---

# Python Requirement

The organizer requires:

```text
Python 3
Windows
```

No additional Python packages are required.

The project uses only Python's standard library.

If Python is missing, `run_organizer.bat` will display an error instead of immediately closing.

---

# Project Structure

```text
downloads-organizer/
├── organizer.py
├── run_organizer.bat
├── README.md
└── .gitignore
```

`organizer.py` contains the main application.

`run_organizer.bat` provides an easier way to start the application on Windows.

`README.md` contains the project documentation.

`.gitignore` tells Git which unnecessary files should not be uploaded.

---

# Disclaimer

Always review the preview before confirming the operation.

Although the organizer includes multiple safety mechanisms, keeping backups of important files is recommended.

Use the program at your own responsibility.

---

# Author

Created as a Python learning project and practical file automation tool.
