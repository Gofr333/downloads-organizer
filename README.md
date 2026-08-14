# Downloads Organizer

A safe Windows file organizer written in Python. It scans the user's **Downloads** folder, creates an exact preview, and moves files into categories only after explicit confirmation.

## Download for Windows

**Recommended for most users:** download the ready-to-run Windows executable from the latest release:

[Download DownloadsOrganizer.exe](https://github.com/Gofr333/downloads-organizer/releases/latest/download/DownloadsOrganizer.exe)

No Python installation is required when using the `.exe` version.

## Quick Start

1. Download `DownloadsOrganizer.exe` using the link above.
2. Double-click `DownloadsOrganizer.exe`.
3. Review the complete preview. No files have been moved yet.
4. The program will show how many files are planned, for example:

```text
Type "MOVE 15" to continue.
```

5. Type the exact confirmation shown by the program:

```text
MOVE 15
```

6. Review the final summary.

Any other confirmation cancels the operation.

> The executable is currently unsigned. Windows may display a security/reputation warning for software that has not been code-signed. If you do not trust the binary, do not bypass the warning; review the source code and run `organizer.py` with Python instead.

## Features

- Detects the Windows Downloads folder, including common redirected locations
- Organizes files by extension
- Supports images, documents, spreadsheets, presentations, videos, audio, archives, installers, code, game files, and many other formats
- Moves unknown extensions to `Other`
- Moves files without extensions to `No Extension`
- Moves ambiguous extensions to `Review`
- Creates one exact plan before changing anything
- Requires confirmation using `MOVE <number>`
- Handles duplicate filenames automatically
- Does not intentionally overwrite existing files
- Creates destination folders only when needed
- Leaves existing folders untouched
- Does not extract archives
- Skips files that appear to still be downloading
- Skips symbolic links
- Skips common Windows system files
- Protects the running organizer itself, including the packaged `.exe`
- Continues processing if an individual file causes an error
- Displays scan and final statistics
- Uses only Python's standard library at runtime

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
├── Documents/
│   └── invoice.pdf
├── Videos/
│   └── movie.mp4
├── Installers/
│   └── setup.exe
├── Archives/
│   └── modpack.7z
└── Other/
    └── unknown.xyz
```

## Safety

### Exact preview

The organizer scans the Downloads folder once and creates the plan that will be executed after confirmation.

Example:

```text
============================================================
PREVIEW - NO FILES HAVE BEEN MOVED
============================================================

[PLAN] photo.png -> Images/photo.png
[PLAN] invoice.pdf -> Documents/invoice.pdf
[PLAN] setup.exe -> Installers/setup.exe
```

### Explicit confirmation

If 3 files are planned, the program asks for:

```text
MOVE 3
```

The number must match the current plan.

### Duplicate protection

If `photo.png` already exists in the destination folder, the organizer looks for a free name:

```text
photo.png
photo_1.png
photo_2.png
```

### Active downloads

Files with temporary download extensions are skipped, including:

```text
.crdownload
.part
.partial
.download
```

Temporary Microsoft Office files beginning with `~$` are also skipped.

### Archives

Archives are moved only. They are never extracted by this program.

Examples include:

```text
.zip
.rar
.7z
.tar
.gz
```

## Categories

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

## Run From Source

Developers and users who prefer to inspect and run the Python source can clone the repository:

```powershell
git clone https://github.com/Gofr333/downloads-organizer.git
cd downloads-organizer
python organizer.py
```

If `python` is not recognized on Windows, try:

```powershell
py organizer.py
```

Running from source requires Python 3. No third-party runtime packages are required.

## Windows Executable Build

The repository contains a GitHub Actions workflow that builds `DownloadsOrganizer.exe` on a Windows runner using PyInstaller.

The generated executable is not committed to the source branch. Release binaries are attached to GitHub Releases instead.

### Create a new release

After committing and pushing your changes, create and push a version tag:

```powershell
git tag v1.0.0
git push origin v1.0.0
```

GitHub Actions will then:

1. Start a Windows build environment.
2. Install Python and PyInstaller.
3. Build `DownloadsOrganizer.exe`.
4. Generate a SHA-256 checksum.
5. Create a GitHub Release for the tag.
6. Attach the executable and checksum to that release.

The workflow can also be started manually from the **Actions** tab. A manual run creates a downloadable workflow artifact but does not create a GitHub Release.

## Verify the Download

Each release includes:

```text
DownloadsOrganizer.exe
DownloadsOrganizer.sha256
```

On Windows, the executable checksum can be calculated with:

```powershell
Get-FileHash .\DownloadsOrganizer.exe -Algorithm SHA256
```

Compare the displayed hash with the value in `DownloadsOrganizer.sha256` from the same release.

## Project Structure

```text
downloads-organizer/
├── .github/
│   └── workflows/
│       └── build-release.yml
├── organizer.py
├── README.md
└── .gitignore
```

## Requirements

### Ready-to-run executable

- Windows
- Python is **not** required

### Running from source

- Windows
- Python 3

## Disclaimer

Always review the preview before confirming an operation. The project includes multiple safeguards, but keeping backups of important files is recommended.

Use the program at your own responsibility.

## Author

Created as a Python learning project and practical file automation tool.
