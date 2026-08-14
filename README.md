# Downloads Organizer

A safe and simple Windows application that automatically organizes files inside your **Downloads** folder based on their file extensions.

The program creates a complete preview before moving anything and requires explicit confirmation before making changes.

## Download

### Recommended

Download the latest Windows version from:

**[Latest Release](https://github.com/Gofr333/downloads-organizer/releases/latest)**

Download:

```text
DownloadsOrganizer.exe
```

Then simply double-click the file to start the organizer.

**Python is not required when using the `.exe` version.**

---

## Quick Start

1. Download `DownloadsOrganizer.exe` from the latest GitHub Release.
2. Double-click `DownloadsOrganizer.exe`.
3. Review the organization preview.
4. Type the requested `MOVE <number>` confirmation.
5. Press Enter.
6. Done.

Example:

```text
25 file(s) will be moved inside your Downloads folder.

Type "MOVE 25" to continue.
```

To continue:

```text
MOVE 25
```

Any other input cancels the operation.

---

## Features

* Automatically detects the user's Downloads folder
* Organizes files by file extension
* Supports many common file formats
* Moves unknown file types to `Other`
* Moves files without extensions to `No Extension`
* Moves ambiguous file types to `Review`
* Automatically handles duplicate filenames
* Does not intentionally overwrite existing files
* Creates destination folders only when needed
* Does not move existing folders
* Does not extract archives
* Skips files that are still being downloaded
* Skips symbolic links
* Skips common Windows system files
* Prevents the application from moving itself
* Creates an exact organization plan before moving files
* Requires confirmation using `MOVE <number>`
* Continues processing if an individual file causes an error
* Displays scan and final organization statistics
* Uses only Python's standard library in the source version
* Available as a standalone Windows executable

---

## Example

### Before

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

### After

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

# How It Works

When the application starts, it scans the Downloads folder and creates an organization plan.

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

At this stage:

```text
NO FILES HAVE BEEN MOVED
```

The application also displays a scan summary:

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

Before moving anything, the application requires explicit confirmation.

Example:

```text
4 file(s) will be moved inside your Downloads folder.

Type "MOVE 4" to continue.
```

To approve the operation:

```text
MOVE 4
```

The number must match the number displayed by the program.

Anything else cancels the operation:

```text
Operation cancelled.
No files were moved.
```

---

# Safety

Downloads Organizer includes several safeguards designed to make file organization predictable and safer.

## Preview Before Changes

The application always displays the complete organization plan before moving files.

No files are moved during the preview.

## Exact Confirmation

The user must confirm using:

```text
MOVE <number>
```

For example:

```text
MOVE 37
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

Symbolic links are skipped to reduce the risk of modifying files outside the Downloads folder.

## Self Protection

The organizer does not move its own executable or Python script when running from the Downloads folder.

---

# Duplicate Files

Existing files are not intentionally overwritten.

If this file already exists:

```text
photo.png
```

the organizer searches for a free filename:

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

Filename reservations are also created during the planning stage, preventing multiple planned files from receiving the same destination.

---

# Archives

Archive files are only moved.

They are **never extracted or modified**.

Supported formats include:

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

Example:

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

Downloads Organizer supports categories including:

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

Unknown extensions are moved to:

```text
Other
```

Files without an extension are moved to:

```text
No Extension
```

Ambiguous extensions are moved to:

```text
Review
```

so they can be checked manually.

---

# Error Handling

If a file cannot be moved, the application does not stop the entire organization process.

Instead, it displays an error:

```text
[ERROR] example.pdf: ...
```

and continues with the remaining files.

At the end, a summary is displayed:

```text
============================================================
ORGANIZATION SUMMARY
============================================================
Files planned:   125
Files moved:     124
Files not moved: 1
Errors:          1
```

---

# Windows Security Notice

The Windows executable is currently not digitally signed.

Because of this, Windows SmartScreen or antivirus software may display a warning when running a newly downloaded release.

The complete Python source code is available in this repository for inspection.

If you do not want to run the executable, you can run the Python source version instead.

---

# Verify the Download

Releases may also contain:

```text
DownloadsOrganizer.sha256
```

This file contains the SHA-256 checksum of the executable.

You can calculate the checksum yourself in PowerShell:

```powershell
Get-FileHash .\DownloadsOrganizer.exe -Algorithm SHA256
```

Compare the generated hash with the value provided in:

```text
DownloadsOrganizer.sha256
```

They should match.

---

# Run From Source

Developers and users who prefer running the Python source can download or clone the repository.

Clone:

```powershell
git clone https://github.com/Gofr333/downloads-organizer.git
```

Enter the project folder:

```powershell
cd downloads-organizer
```

Run:

```powershell
python organizer.py
```

If `python` is not recognized:

```powershell
py organizer.py
```

## Source Requirements

* Python 3
* Windows

No additional Python packages are required to run `organizer.py`.

---

# Project Structure

```text
downloads-organizer/
├── .github/
│   └── workflows/
│       └── build-release.yml
│
├── organizer.py
├── README.md
└── .gitignore
```

### `organizer.py`

Contains the main Downloads Organizer application.

### `.github/workflows/build-release.yml`

Automatically builds the Windows executable for releases using GitHub Actions.

### `README.md`

Project documentation.

### `.gitignore`

Prevents unnecessary development and build files from being committed.

---

# Releases

Windows releases are built automatically.

A release contains:

```text
DownloadsOrganizer.exe
DownloadsOrganizer.sha256
```

`DownloadsOrganizer.exe` is the standalone Windows application.

`DownloadsOrganizer.sha256` can be used to verify the integrity of the downloaded executable.

---

# Disclaimer

Always review the preview before confirming the operation.

Although Downloads Organizer includes multiple safeguards, keeping backups of important files is recommended.

Use the application at your own responsibility.

---

# Author

Created as a Python learning project and practical Windows file automation tool.
