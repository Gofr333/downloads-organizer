# Downloads Organizer

A safe Python script that automatically organizes files in the user's **Downloads** folder based on their file extensions.

The organizer creates a complete preview before making any changes and requires explicit confirmation before moving files.

---

## Features

* Automatically detects the user's Downloads folder
* Organizes files by file extension
* Supports images, documents, videos, audio, archives, installers, code, game files, and many other formats
* Moves unknown file types to the `Other` folder
* Moves files without extensions to the `No Extension` folder
* Moves ambiguous file types to the `Review` folder
* Automatically handles duplicate filenames
* Never overwrites existing files
* Creates destination folders only when needed
* Does not move existing folders
* Does not extract archives
* Skips files that are still being downloaded
* Skips symbolic links
* Skips common Windows system files
* Skips the organizer script itself if it is located inside Downloads
* Creates one exact organization plan before making changes
* Requires confirmation using `MOVE <number>`
* Continues processing even if one file causes an error
* Displays scan and final organization statistics
* Uses only the Python standard library

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

# How to Use

## 1. Download the script

Download:

```text
organizer.py
```

from this GitHub repository.

You can save it anywhere, for example on your Desktop.

---

## 2. Open PowerShell in the script folder

Open the folder containing:

```text
organizer.py
```

Right-click inside the folder and select:

```text
Open in Terminal
```

You can also open PowerShell manually inside that folder.

---

## 3. Run the script

Type:

```powershell
python organizer.py
```

and press **Enter**.

If `python` does not work, try:

```powershell
py organizer.py
```

> It is recommended to run the script through PowerShell or another terminal instead of double-clicking the `.py` file.

---

## 4. Review the preview

The organizer first scans the Downloads folder and creates an exact plan.

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

The script also displays a scan summary:

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

## 5. Confirm the operation

After the preview, the organizer displays the number of files that will be moved.

Example:

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

## 6. Organization

After confirmation, the script executes the exact plan shown in the preview.

Example:

```text
[MOVED] photo.png -> Images/photo.png
[MOVED] invoice.pdf -> Documents/invoice.pdf
[MOVED] setup.exe -> Installers/setup.exe
[MOVED] modpack.7z -> Archives/modpack.7z
```

When finished, the organizer displays a summary:

```text
============================================================
ORGANIZATION SUMMARY
============================================================
Files planned:   4
Files moved:     4
Files not moved: 0
Errors:          0
```

---

# Safety

The organizer includes several safeguards before changing any files.

### Dry Preview

The script always shows the complete organization plan before moving anything.

### Explicit Confirmation

The user must type:

```text
MOVE <number>
```

For example:

```text
MOVE 25
```

### Existing Folders

Existing folders inside Downloads are left untouched.

### Active Downloads

Files that appear to still be downloading are skipped.

Examples include:

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

### System Files

Common Windows system files such as:

```text
desktop.ini
Thumbs.db
```

are skipped.

### Symbolic Links

Symbolic links are skipped to avoid accidentally modifying files outside the Downloads folder.

### Organizer Protection

If `organizer.py` itself is located inside the Downloads folder, the script will not move itself.

---

# Duplicate Files

Existing files are never intentionally overwritten.

If the destination already contains:

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

The organizer also reserves filenames while creating the preview, preventing two planned files from accidentally receiving the same destination.

---

# Archives

Archive files are only moved.

They are **never extracted or modified**.

Supported archive formats include:

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

The organizer supports categories such as:

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

Some ambiguous extensions are moved to:

```text
Review
```

so the user can decide what to do with them manually.

---

# Error Handling

If one file cannot be moved, the entire program does not stop.

Instead, the organizer displays an error:

```text
[ERROR] example.pdf: ...
```

and continues with the remaining files.

The final summary shows how many files were successfully moved and how many errors occurred.

---

# Requirements

* Python 3
* Windows

No additional Python packages are required.

The project uses only Python's standard library.

---

# Project Structure

```text
downloads-organizer/
├── organizer.py
├── README.md
└── .gitignore
```

---

# Quick Start

```text
1. Download organizer.py
2. Open its folder
3. Right-click → Open in Terminal
4. Run: python organizer.py
5. Review the preview
6. Type the requested MOVE <number> confirmation
7. Done
```

If `python` is not recognized, use:

```powershell
py organizer.py
```

---

# Disclaimer

Always review the preview before confirming the operation.

The project includes multiple safeguards, but keeping backups of important files is always recommended.

Use the script at your own responsibility.

---

# Author
GOFR
Created as a Python learning project and practical file automation tool.
