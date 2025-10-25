import os
from pathlib import Path
from collections import defaultdict

def scan_files(base_path: Path):
    """
    Recursively scans the given directory for files
    and returns a mapping of file extensions → list of file names.
    """
    file_map = defaultdict(list)
    all_files = []

    # Walk through all files and subdirectories
    for root, _, files in os.walk(base_path):
        for file in files:
            file_path = Path(root) / file
            all_files.append(file_path)

    print(f"🔍 Scanned {len(all_files)} files under: {base_path}\n")

    # Group by file extension
    for file_path in all_files:
        ext = file_path.suffix.lower() or "NO_EXT"
        file_map[ext].append(str(file_path))

    return file_map


def print_summary(file_map):
    """
    Prints the grouped file map in a compact format.
    """
    print("\n📂 File Type Summary (Tiny Format)")
    print("=" * 60)

    for ext, files in sorted(file_map.items()):
        print(f"{ext:10s} → {len(files)} files")

    print("=" * 60)
    print(f"Total categories: {len(file_map)}")


if __name__ == "__main__":
    # Change base_dir to the folder you want to scan (or leave as current)
    base_dir = Path.home()  # your home directory
    # base_dir = Path("/Users/yourname/Documents")  # optional specific folder

    file_map = scan_files(base_dir)
    print_summary(file_map)
