import os

def crawl_folder(folder_path):
    """Loops through all files in the given folder and returns a list of file paths."""
    files = []
    
    for root, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            files.append(file_path)  # Store the full path

    return files

