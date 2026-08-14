from pathlib import Path


# ==========================================
# SETTINGS
# ==========================================

DOWNLOADS_FOLDER = Path.home() / "Downloads"

# Files that usually mean a download is still in progress.
# They are skipped so the organizer does not interfere with active downloads.
ACTIVE_DOWNLOAD_SUFFIXES = {
    ".crdownload",
    ".part",
    ".partial",
    ".download",
}

# Common system files that should stay where they are.
SKIPPED_FILENAMES = {
    "desktop.ini",
    "thumbs.db",
}


FILE_TYPES = {

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
# HELPERS
# ==========================================

def get_folder_name(item):
    extension = item.suffix.lower()

    if not extension:
        return "No Extension"

    return FILE_TYPES.get(extension, "Other")


def get_unique_destination(item, destination_folder, reserved_paths):
    destination_path = destination_folder / item.name
    counter = 1

    while destination_path.exists() or destination_path in reserved_paths:
        new_name = f"{item.stem}_{counter}{item.suffix}"
        destination_path = destination_folder / new_name
        counter += 1

    return destination_path


def create_plan():
    plan = []
    reserved_paths = set()

    stats = {
        "folders_skipped": 0,
        "active_downloads_skipped": 0,
        "system_files_skipped": 0,
        "symlinks_skipped": 0,
        "self_skipped": 0,
        "planning_errors": 0,
    }

    script_path = Path(__file__).resolve()

    try:
        items = sorted(
            DOWNLOADS_FOLDER.iterdir(),
            key=lambda path: path.name.lower(),
        )
    except OSError as error:
        print(f"[ERROR] Could not read Downloads folder: {error}")
        return [], stats

    for item in items:
        try:
            # Never move the organizer itself if it is stored in Downloads.
            if item.resolve() == script_path:
                stats["self_skipped"] += 1
                continue

            # Skip symbolic links to avoid surprising changes outside Downloads.
            if item.is_symlink():
                stats["symlinks_skipped"] += 1
                continue

            # Existing folders are intentionally left untouched.
            if not item.is_file():
                stats["folders_skipped"] += 1
                continue

            # Skip common Windows system files.
            if item.name.lower() in SKIPPED_FILENAMES:
                stats["system_files_skipped"] += 1
                continue

            # Skip files that are probably still being downloaded.
            if (
                item.suffix.lower() in ACTIVE_DOWNLOAD_SUFFIXES
                or item.name.startswith("~$")
            ):
                stats["active_downloads_skipped"] += 1
                continue

            folder_name = get_folder_name(item)
            destination_folder = DOWNLOADS_FOLDER / folder_name

            # A file with the same name as a category folder would make
            # creating that folder impossible, so skip it safely.
            if destination_folder.exists() and not destination_folder.is_dir():
                stats["planning_errors"] += 1
                print(
                    f"[PLAN ERROR] Cannot use category '{folder_name}' because "
                    f"'{destination_folder.name}' already exists as a file."
                )
                continue

            destination_path = get_unique_destination(
                item,
                destination_folder,
                reserved_paths,
            )

            reserved_paths.add(destination_path)
            plan.append((item, destination_path, folder_name))

        except OSError as error:
            stats["planning_errors"] += 1
            print(f"[PLAN ERROR] {item.name}: {error}")

    return plan, stats


# ==========================================
# PREVIEW
# ==========================================

def show_preview(plan, stats):
    print()
    print("=" * 60)
    print("PREVIEW - NO FILES HAVE BEEN MOVED")
    print("=" * 60)
    print()

    for source, destination, folder_name in plan:
        print(
            f"[PLAN] {source.name} -> "
            f"{folder_name}/{destination.name}"
        )

    print()
    print("=" * 60)
    print("SCAN SUMMARY")
    print("=" * 60)
    print(f"Files planned:            {len(plan)}")
    print(f"Folders skipped:          {stats['folders_skipped']}")
    print(f"Active downloads skipped: {stats['active_downloads_skipped']}")
    print(f"System files skipped:     {stats['system_files_skipped']}")
    print(f"Symlinks skipped:         {stats['symlinks_skipped']}")
    print(f"Organizer skipped:        {stats['self_skipped']}")
    print(f"Planning errors:          {stats['planning_errors']}")


# ==========================================
# CONFIRMATION
# ==========================================

def confirm_run(file_count):
    expected_confirmation = f"MOVE {file_count}"

    print()
    print("=" * 60)
    print("WARNING")
    print("=" * 60)
    print()
    print(f"{file_count} file(s) will be moved inside your Downloads folder.")
    print("Archives will NOT be extracted.")
    print("Existing folders will NOT be moved.")
    print("Files still being downloaded will be skipped.")
    print()
    print(f'Type "{expected_confirmation}" to continue.')

    confirmation = input("> ").strip().upper()

    return confirmation == expected_confirmation


# ==========================================
# EXECUTION
# ==========================================

def execute_plan(plan):
    moved = 0
    errors = 0

    print()
    print("=" * 60)
    print("ORGANIZING FILES")
    print("=" * 60)
    print()

    for source, destination, folder_name in plan:
        try:
            # The preview and execution use the exact same plan.
            # If the source changed after preview, skip it rather than guessing.
            if not source.exists() or not source.is_file():
                errors += 1
                print(
                    f"[ERROR] {source.name}: source file is no longer available."
                )
                continue

            # If something created the approved destination after the preview,
            # do not overwrite it. The user can run the organizer again.
            if destination.exists():
                errors += 1
                print(
                    f"[ERROR] {source.name}: destination now exists "
                    f"({destination.name}). Run the organizer again."
                )
                continue

            destination.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            source.rename(destination)
            moved += 1

            print(
                f"[MOVED] {source.name} -> "
                f"{folder_name}/{destination.name}"
            )

        except OSError as error:
            errors += 1
            print(f"[ERROR] {source.name}: {error}")

    return moved, errors


# ==========================================
# FINAL SUMMARY
# ==========================================

def show_final_summary(planned, moved, errors):
    not_moved = planned - moved

    print()
    print("=" * 60)
    print("ORGANIZATION SUMMARY")
    print("=" * 60)
    print(f"Files planned:   {planned}")
    print(f"Files moved:     {moved}")
    print(f"Files not moved: {not_moved}")
    print(f"Errors:          {errors}")


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():
    print()
    print("=" * 60)
    print("DOWNLOADS ORGANIZER")
    print("=" * 60)

    if not DOWNLOADS_FOLDER.exists() or not DOWNLOADS_FOLDER.is_dir():
        print()
        print("Downloads folder was not found.")
        print(f"Expected location: {DOWNLOADS_FOLDER}")
        return

    print()
    print(f"Target folder: {DOWNLOADS_FOLDER}")

    # Scan only once and build an exact plan.
    plan, stats = create_plan()

    show_preview(plan, stats)

    if not plan:
        print()
        print("No files need to be organized.")
        return

    if not confirm_run(len(plan)):
        print()
        print("Operation cancelled.")
        print("No files were moved.")
        return

    moved, errors = execute_plan(plan)
    show_final_summary(len(plan), moved, errors)

    if errors == 0:
        print()
        print("Downloads folder organized successfully.")
    else:
        print()
        print("Finished with errors. Review the messages above.")


# ==========================================
# START PROGRAM
# ==========================================

if __name__ == "__main__":
    main()
