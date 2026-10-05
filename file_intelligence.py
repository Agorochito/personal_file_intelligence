import os
import hashlib


# ---------- FUNCTIONS ----------

def calculate_file_hash(full_path):
    hash_object = hashlib.sha256()

    with open(full_path, "rb") as f:
        hash_object.update(f.read())

    return hash_object.hexdigest()


def get_valid_folder():
    while True:
        user_folder_path = input("Enter a folder path: ")

        if os.path.isdir(user_folder_path):
            return user_folder_path
        else:
            print("This is not a valid folder path.")


def find_duplicates(hashes):
    duplicates = []

    for value in hashes.values():
        if len(value) >= 2:
            duplicates.append(value)

    return duplicates


def categorize_file(extension, categories):
    for category, extensions in categories.items():
        if extension in extensions:
            return category

    return "Others"


def format_size(size_in_bytes):
    if size_in_bytes < 1024:
        return f"{size_in_bytes} bytes"

    elif size_in_bytes < 1024 * 1024:
        return f"{round(size_in_bytes / 1024, 2)} KB"

    elif size_in_bytes < 1024 * 1024 * 1024:
        return f"{round(size_in_bytes / 1024 / 1024, 2)} MB"

    else:
        return f"{round(size_in_bytes / 1024 / 1024 / 1024, 2)} GB"


# ---------- FILE CATEGORIES ----------

categories = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif",
        ".bmp", ".tiff"
    ],

    "Documents": [
        ".pdf", ".doc", ".docx", ".txt",
        ".ppt", ".pptx", ".xls", ".xlsx"
    ],

    "Code": [
        ".py", ".java", ".c", ".cpp",
        ".js", ".html", ".css", ".rb", ".php"
    ],

    "Videos": [
        ".mp4", ".avi", ".mov", ".mkv",
        ".flv", ".wmv"
    ]
}


# ---------- GET FOLDER ----------

user_folder_path = get_valid_folder()


# ---------- ANALYSIS VARIABLES ----------

python_files = 0
pdf_files = 0
text_files = 0

file_count = 0
folder_count = 0
skipped_files = 0

total_size = 0

current_largest = 0
largest_file = None

hashes = {}

category_count = {
    "Images": 0,
    "Documents": 0,
    "Code": 0,
    "Videos": 0,
    "Others": 0
}


# ---------- ANALYZE FOLDER RECURSIVELY ----------

for current_folder, folders, files in os.walk(user_folder_path):

    folder_count += len(folders)

    for file in files:

        full_path = os.path.join(current_folder, file)

        try:
            # ---------- FILE SIZE ----------

            file_size = os.path.getsize(full_path)


            # ---------- FILE HASH ----------

            hex_val = calculate_file_hash(full_path)


            # The file was successfully analyzed,
            # so now update our statistics.

            file_count += 1
            total_size += file_size


            # ---------- FILE EXTENSION ----------

            extension = os.path.splitext(file)[1].lower()


            # ---------- FILE CATEGORY ----------

            category = categorize_file(extension, categories)
            category_count[category] += 1


            # ---------- SPECIFIC FILE TYPES ----------

            if extension == ".py":
                python_files += 1

            elif extension == ".pdf":
                pdf_files += 1

            elif extension == ".txt":
                text_files += 1


            # ---------- DUPLICATE DETECTION ----------

            if hex_val in hashes:
                hashes[hex_val].append(full_path)

            else:
                hashes[hex_val] = [full_path]


            # ---------- LARGEST FILE ----------

            if file_size > current_largest:
                current_largest = file_size
                largest_file = full_path


        except PermissionError:
            skipped_files += 1
            print("Skipped unreadable file:", full_path)


# ---------- FIND DUPLICATES ----------

duplicates = find_duplicates(hashes)


# ---------- CLEANUP INTELLIGENCE ----------

recoverable_space = 0

for group in duplicates:

    try:
        duplicate_size = os.path.getsize(group[0])
        redundant_copies = len(group) - 1

        recoverable_space += duplicate_size * redundant_copies

    except PermissionError:
        pass


# ---------- FILE INTELLIGENCE REPORT ----------

print("\n========== FILE INTELLIGENCE REPORT ==========")

print("\nFolder:", os.path.basename(user_folder_path))


# ---------- OVERVIEW ----------

print("\nOVERVIEW")

print("Files analyzed:", file_count)
print("Folders:", folder_count)
print("Files skipped:", skipped_files)
print("Total Size:", format_size(total_size))


# ---------- CATEGORIES ----------

print("\nCATEGORIES")

for category, count in category_count.items():
    print(category, ":", count)


# ---------- SPECIFIC FILE TYPES ----------

print("\nSPECIFIC FILE TYPES")

print("Python files:", python_files)
print("PDF files:", pdf_files)
print("Text files:", text_files)


# ---------- LARGEST FILE ----------

print("\nLARGEST FILE")

if largest_file is not None:
    print("Name:", os.path.basename(largest_file))
    print("Size:", format_size(current_largest))

else:
    print("No files found.")


# ---------- DUPLICATES ----------

print("\nDUPLICATES")

print("Duplicate Groups:", len(duplicates))

if len(duplicates) == 0:
    print("No duplicate files found.")

else:
    for group in duplicates:

        print("\nDuplicate group:")

        for duplicate_file in group:
            print("-", duplicate_file)


# ---------- CLEANUP INTELLIGENCE ----------

print("\nCLEANUP INTELLIGENCE")

if recoverable_space > 0:
    print(
        "Potential duplicate storage that could be recovered:",
        format_size(recoverable_space)
    )

else:
    print("No recoverable duplicate storage found.")


print("\n==============================================")
    
