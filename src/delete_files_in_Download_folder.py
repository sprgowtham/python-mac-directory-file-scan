import os
import time
from pathlib import Path

# Set the path to your Downloads folder
downloads_path = Path.home() / "Downloads"

# Prompt user for cutoff date
cutoff_input = input("Enter cutoff date (DD-MON-YYYY, e.g., 25-OCT-2025): ")

try:
    cutoff_timestamp = time.mktime(time.strptime(cutoff_input, "%d-%b-%Y"))
except ValueError:
    print("Invalid date format. Please use DD-MON-YYYY (e.g., 25-OCT-2025).")
    exit(1)

# List files to be deleted
files_to_delete = []

for file in downloads_path.iterdir():
    if file.is_file():
        file_mtime = file.stat().st_mtime  # Last modification time
        if file_mtime < cutoff_timestamp:
            files_to_delete.append(file)

# Print files found
if files_to_delete:
    print(f"Files before {cutoff_input}:")
    for f in files_to_delete:
        print(f"  {f.name}")
else:
    print(f"No files found before {cutoff_input}.")

# Ask user if they want to delete the files
confirm = input("Do you want to delete these files? (y/n): ").lower()
if confirm == 'y':
    for f in files_to_delete:
        f.unlink()  # Deletes the file
    print("Files deleted successfully.")
else:
    print("No files were deleted.")
