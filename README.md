# Personal File Intelligence Tool

## About

Personal File Intelligence Tool is a Python program that helps users analyze the contents of folders on their device. By entering a folder path, users receive a report showing the number of files and subfolders, file categories, total storage size, and the largest file found.

The tool recursively scans subfolders and uses SHA-256 hashing to detect duplicate files, even when the files have different names or are located in different directories. It also provides cleanup intelligence by calculating how much storage space could potentially be recovered by removing unnecessary duplicate copies.

## Features

- Recursively scans folders and subfolders
- Counts files and folders
- Categorizes files as images, documents, code, videos, or other types
- Calculates total storage usage
- Identifies the largest file
- Detects duplicate files using SHA-256 hashing
- Groups duplicate files even when they have different names
- Calculates potential storage that can be recovered from duplicate files
- Skips inaccessible files instead of stopping the entire scan
- Displays file sizes in bytes, KB, MB, or GB

## How It Works

The program begins by asking the user to enter the path of a folder they want to analyze. Before starting the analysis, it checks whether the provided path points to a valid directory.

Once a valid folder is provided, the program recursively scans the folder and its subfolders. As files are discovered, it counts them and organizes them into categories such as images, documents, code, videos, and other file types based on their extensions.

During the scan, the program calculates the size of each file and keeps track of the total storage being used. It also compares file sizes throughout the scan to determine the largest file in the selected directory.

For duplicate detection, the program generates a SHA-256 hash for each file. Files with identical contents produce the same hash, allowing the program to detect duplicates even when those files have different names or are stored in different subfolders.

After duplicate groups are identified, the program calculates how many copies are redundant and estimates how much storage space could potentially be recovered while keeping one copy of each file.

Finally, the collected information is displayed in a File Intelligence Report containing an overview of the folder, file categories, specific file types, the largest file, duplicate groups, and potential recoverable storage.

## Technologies Used

- Python
- `os` module for file system navigation and file information
- `hashlib` module for SHA-256 file hashing
- Git for version control

## Running the Program

Make sure Python 3 is installed on your computer.

Clone or download this repository and open a terminal inside the project folder.

Run the program with:

```bash
python3 file_intelligence.py
```

When prompted, enter the path of the folder you want to analyze.

The program will scan the selected directory and display the File Intelligence Report in the terminal.

## Example Report

```text
========== FILE INTELLIGENCE REPORT ==========

Folder: Example Folder

OVERVIEW
Files analyzed: 12
Folders: 3
Files skipped: 0
Total Size: 18.42 MB

CATEGORIES
Images : 3
Documents : 5
Code : 2
Videos : 1
Others : 1

SPECIFIC FILE TYPES
Python files: 2
PDF files: 3
Text files: 1

LARGEST FILE
Name: presentation.pdf
Size: 7.31 MB

DUPLICATES
Duplicate Groups: 1

Duplicate group:
- /Example Folder/notes.txt
- /Example Folder/School/notes_copy.txt

CLEANUP INTELLIGENCE
Potential duplicate storage that could be recovered: 24.5 KB
```

## Future Improvements

Possible future improvements include:

- Exporting analysis results to a file
- Allowing users to choose which duplicate files to remove
- Adding more detailed file categories
- Providing additional storage cleanup insights
- Building a graphical user interface