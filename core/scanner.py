import os
from core.hashing import get_file_hash

def scan_folder(folder_path):

    hashes = {}
    duplicates = []

    for root, _, files in os.walk(folder_path):

        for file in files:

            path = os.path.join(root, file)
            file_hash = get_file_hash(path)

            if file_hash in hashes:
                duplicates.append(path)

            else:
                hashes[file_hash] = path

    return duplicates