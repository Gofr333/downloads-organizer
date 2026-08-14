from pathlib import Path


# ==========================================
# SETTINGS
# ==========================================

downloads_folder = Path.home() / "Downloads"


file_types = {

    # ==========================================
    # IMAGES
    # ==========================================

    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".webp": "Images",
    ".bmp": "Images",
    ".tiff": "Images",
    ".tif": "Images",
    ".svg": "Images",
    ".ico": "Images",
    ".heic": "Images",
    ".heif": "Images",
    ".avif": "Images",
    ".jfif": "Images",

    # Camera RAW
    ".raw": "Images",
    ".cr2": "Images",
    ".cr3": "Images",
    ".nef": "Images",
    ".arw": "Images",
    ".dng": "Images",
    ".orf": "Images",
    ".rw2": "Images",

    # ==========================================
    # DOCUMENTS
    # ==========================================

    ".pdf": "Documents",
    ".txt": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".odt": "Documents",
    ".rtf": "Documents",
    ".pages": "Documents",
    ".tex": "Documents",
    ".md": "Documents",

    # ==========================================
    # SPREADSHEETS
    # ==========================================

    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".xlsm": "Spreadsheets",
    ".ods": "Spreadsheets",
    ".csv": "Spreadsheets",
    ".tsv": "Spreadsheets",

    # ==========================================
    # PRESENTATIONS
    # ==========================================

    ".ppt": "Presentations",
    ".pptx": "Presentations",
    ".pps": "Presentations",
    ".ppsx": "Presentations",
    ".odp": "Presentations",

    # ==========================================
    # VIDEOS
    # ==========================================

    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".wmv": "Videos",
    ".flv": "Videos",
    ".webm": "Videos",
    ".mpeg": "Videos",
    ".mpg": "Videos",
    ".m4v": "Videos",
    ".3gp": "Videos",
    ".mts": "Videos",
    ".m2ts": "Videos",
    ".vob": "Videos",

    # ==========================================
    # AUDIO
    # ==========================================

    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    ".aac": "Audio",
    ".ogg": "Audio",
    ".m4a": "Audio",
    ".wma": "Audio",
    ".opus": "Audio",
    ".aiff": "Audio",
    ".mid": "Audio",
    ".midi": "Audio",

    # ==========================================
    # ARCHIVES
    # Files are only moved - never extracted
    # ==========================================

    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".gzip": "Archives",
    ".bz2": "Archives",
    ".xz": "Archives",
    ".tgz": "Archives",
    ".tbz": "Archives",
    ".tbz2": "Archives",
    ".txz": "Archives",
    ".cab": "Archives",
    ".ace": "Archives",
    ".zst": "Archives",

    # ==========================================
    # INSTALLERS
    # ==========================================

    ".exe": "Installers",
    ".msi": "Installers",
    ".msix": "Installers",
    ".msixbundle": "Installers",
    ".appx": "Installers",
    ".appxbundle": "Installers",

    # Android
    ".apk": "Installers",
    ".xapk": "Installers",
    ".apks": "Installers",
    ".aab": "Installers",

    # Linux
    ".deb": "Installers",
    ".rpm": "Installers",
    ".appimage": "Installers",

    # macOS
    ".pkg": "Installers",
    ".dmg": "Installers",

    # ==========================================
    # DISK IMAGES
    # ==========================================

    ".iso": "Disk Images",
    ".img": "Disk Images",
    ".vhd": "Disk Images",
    ".vhdx": "Disk Images",
    ".vmdk": "Disk Images",
    ".qcow": "Disk Images",
    ".qcow2": "Disk Images",
    ".cue": "Disk Images",

    # ==========================================
    # EBOOKS
    # ==========================================

    ".epub": "Ebooks",
    ".mobi": "Ebooks",
    ".azw": "Ebooks",
    ".azw3": "Ebooks",
    ".fb2": "Ebooks",
    ".djvu": "Ebooks",

    # ==========================================
    # FONTS
    # ==========================================

    ".ttf": "Fonts",
    ".otf": "Fonts",
    ".woff": "Fonts",
    ".woff2": "Fonts",
    ".eot": "Fonts",

    # ==========================================
    # SUBTITLES
    # ==========================================

    ".srt": "Subtitles",
    ".sub": "Subtitles",
    ".ass": "Subtitles",
    ".ssa": "Subtitles",
    ".vtt": "Subtitles",

    # ==========================================
    # CODE
    # ==========================================

    ".py": "Code",
    ".pyw": "Code",
    ".pyi": "Code",
    ".ipynb": "Code",

    ".html": "Code",
    ".htm": "Code",
    ".css": "Code",
    ".js": "Code",
    ".jsx": "Code",
    ".tsx": "Code",
    ".vue": "Code",
    ".svelte": "Code",

    ".java": "Code",
    ".c": "Code",
    ".h": "Code",
    ".cpp": "Code",
    ".hpp": "Code",
    ".cs": "Code",
    ".go": "Code",
    ".rs": "Code",
    ".php": "Code",
    ".rb": "Code",
    ".swift": "Code",
    ".kt": "Code",
    ".kts": "Code",
    ".scala": "Code",
    ".lua": "Code",
    ".pl": "Code",
    ".r": "Code",
    ".dart": "Code",
    ".asm": "Code",
    ".sql": "Code",
    ".sh": "Code",
    ".bat": "Code",
    ".cmd": "Code",
    ".ps1": "Code",

    # ==========================================
    # JAVA / MODS
    # ==========================================

    ".jar": "Java",

    # ==========================================
    # DATA
    # ==========================================

    ".json": "Data",
    ".xml": "Data",
    ".yaml": "Data",
    ".yml": "Data",
    ".toml": "Data",
    ".parquet": "Data",
    ".feather": "Data",

    # ==========================================
    # DATABASES
    # ==========================================

    ".db": "Databases",
    ".sqlite": "Databases",
    ".sqlite3": "Databases",
    ".mdb": "Databases",
    ".accdb": "Databases",

    # ==========================================
    # CONFIGURATION FILES
    # ==========================================

    ".ini": "Configs",
    ".cfg": "Configs",
    ".conf": "Configs",
    ".config": "Configs",
    ".properties": "Configs",

    # ==========================================
    # LOGS
    # ==========================================

    ".log": "Logs",

    # ==========================================
    # BACKUPS / TEMPORARY FILES
    # ==========================================

    ".bak": "Backups",
    ".backup": "Backups",
    ".old": "Backups",

    ".tmp": "Temporary",

    # ==========================================
    # TORRENTS
    # ==========================================

    ".torrent": "Torrents",

    # ==========================================
    # SHORTCUTS
    # ==========================================

    ".lnk": "Shortcuts",
    ".url": "Shortcuts",

    # ==========================================
    # CERTIFICATES
    # ==========================================

    ".pem": "Certificates",
    ".crt": "Certificates",
    ".cer": "Certificates",
    ".p12": "Certificates",
    ".pfx": "Certificates",
    ".pub": "Certificates",

    # ==========================================
    # 3D MODELS
    # ==========================================

    ".stl": "3D Models",
    ".obj": "3D Models",
    ".fbx": "3D Models",
    ".gltf": "3D Models",
    ".glb": "3D Models",
    ".dae": "3D Models",
    ".blend": "3D Models",

    # ==========================================
    # CAD
    # ==========================================

    ".dwg": "CAD",
    ".dxf": "CAD",
    ".step": "CAD",
    ".stp": "CAD",
    ".iges": "CAD",
    ".igs": "CAD",

    # ==========================================
    # DESIGN
    # ==========================================

    ".psd": "Design",
    ".psb": "Design",
    ".ai": "Design",
    ".eps": "Design",
    ".xcf": "Design",
    ".kra": "Design",
    ".afdesign": "Design",
    ".afphoto": "Design",

    # ==========================================
    # MEDIA PROJECTS
    # ==========================================

    ".prproj": "Media Projects",
    ".aep": "Media Projects",
    ".veg": "Media Projects",
    ".drp": "Media Projects",
    ".aup": "Media Projects",
    ".aup3": "Media Projects",

    # ==========================================
    # MODS / GAME FILES
    # ==========================================

    ".mcpack": "Mods",
    ".mcaddon": "Mods",
    ".mcworld": "Mods",
    ".mcstructure": "Mods",
    ".mrpack": "Mods",
    ".litematic": "Mods",
    ".schematic": "Mods",
    ".schem": "Mods",
    ".package": "Mods",
    ".ts4script": "Mods",

    ".pak": "Game Files",

    # ==========================================
    # GAME SAVES
    # ==========================================

    ".sav": "Game Saves",
    ".save": "Game Saves",

    # ==========================================
    # ROMS / EMULATION
    # ==========================================

    ".nes": "ROMs",
    ".snes": "ROMs",
    ".gba": "ROMs",
    ".gb": "ROMs",
    ".gbc": "ROMs",
    ".nds": "ROMs",
    ".cia": "ROMs",
    ".nsp": "ROMs",
    ".xci": "ROMs",
    ".wad": "ROMs",
    ".rvz": "ROMs",
    ".wbfs": "ROMs",

    # ==========================================
    # 3D PRINTING
    # ==========================================

    ".gcode": "3D Printing",
    ".3mf": "3D Printing",

    # ==========================================
    # EMAIL
    # ==========================================

    ".eml": "Emails",
    ".msg": "Emails",
    ".mbox": "Emails",

    # ==========================================
    # CALENDAR / CONTACTS
    # ==========================================

    ".ics": "Calendar",
    ".vcf": "Contacts",

    # ==========================================
    # AMBIGUOUS EXTENSIONS
    # These can represent different file types,
    # so they are moved to Review.
    # ==========================================

    ".ts": "Review",
    ".key": "Review",
    ".bin": "Review",
    ".3ds": "Review",
}


# ==========================================
# ORGANIZER
# ==========================================

def organize_files(dry_run=True):

    for item in downloads_folder.iterdir():

        # Skip folders - organize files only
        if item.is_file():

            # Get the file extension
            extension = item.suffix.lower()

            # File without an extension
            if not extension:
                folder_name = "No Extension"

            # Known or unknown extension
            else:
                folder_name = file_types.get(
                    extension,
                    "Other"
                )

            # Build destination paths
            destination_folder = downloads_folder / folder_name
            destination_path = destination_folder / item.name

            # Handle duplicate file names
            if destination_path.exists():

                counter = 1

                while destination_path.exists():

                    new_name = (
                        f"{item.stem}_{counter}{item.suffix}"
                    )

                    destination_path = (
                        destination_folder / new_name
                    )

                    counter += 1

            # ==========================================
            # DRY RUN MODE
            # ==========================================

            if dry_run:

                print(
                    f"[DRY RUN] "
                    f"{item.name} -> "
                    f"{folder_name}/{destination_path.name}"
                )

            # ==========================================
            # ACTUAL FILE MOVING
            # ==========================================

            else:

                # Create destination folder if needed
                destination_folder.mkdir(
                    parents=True,
                    exist_ok=True
                )

                # Move the file
                item.rename(destination_path)

                print(
                    f"[MOVED] "
                    f"{destination_path.name} -> "
                    f"{folder_name}"
                )


# ==========================================
# CONFIRMATION
# ==========================================

def confirm_run():

    print()
    print("=" * 50)
    print("WARNING")
    print("=" * 50)

    print(
        "This script will move files "
        "inside your Downloads folder."
    )

    print()
    print("Archives will NOT be extracted.")
    print("Existing folders will NOT be moved.")
    print()
    print('Type "MOVE" to continue.')

    confirmation = input("> ").strip().upper()

    return confirmation == "MOVE"


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():

    print()
    print("=" * 50)
    print("DOWNLOADS ORGANIZER")
    print("=" * 50)

    # Check if Downloads exists
    if not downloads_folder.exists():
        print()
        print("Downloads folder was not found.")
        print(downloads_folder)
        return

    print()
    print(f"Target folder: {downloads_folder}")

    print()
    print("=" * 50)
    print("PREVIEW")
    print("=" * 50)
    print()

    # Safe preview
    organize_files(dry_run=True)

    # Ask for confirmation
    if confirm_run():

        print()
        print("=" * 50)
        print("ORGANIZING FILES")
        print("=" * 50)
        print()

        organize_files(dry_run=False)

        print()
        print("=" * 50)
        print("DONE")
        print("=" * 50)

        print()
        print("Your Downloads folder has been organized.")

    else:

        print()
        print("Operation cancelled.")
        print("No files were moved.")


# ==========================================
# START PROGRAM
# ==========================================

if __name__ == "__main__":
    main()