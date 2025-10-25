import os

def get_size(start_path='.'):
    """Return total size of directory including subdirectories."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it's a symbolic link
            if not os.path.islink(fp):
                try:
                    total_size += os.path.getsize(fp)
                except Exception as e:
                    print(f"Cannot access {fp}: {e}")
    return total_size

def human_readable_size(size, decimal_places=2):
    """Convert bytes to human-readable format."""
    for unit in ['B','KB','MB','GB','TB']:
        if size < 1024.0:
            return f"{size:.{decimal_places}f} {unit}"
        size /= 1024.0

def list_folders_with_size(path='.'):
    """List all folders in the path with their size."""
    for entry in os.scandir(path):
        if entry.is_dir():
            folder_size = get_size(entry.path)
            print(f"{entry.name:<40} → {human_readable_size(folder_size)}")

if __name__ == "__main__":
    target_path = input("Enter path to scan (default current folder): ").strip() or '.'
    list_folders_with_size(target_path)
