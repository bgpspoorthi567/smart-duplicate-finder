import os

def calculate_storage_saved(duplicate_files):
    total_bytes = sum(os.path.getsize(f) for f in duplicate_files if os.path.exists(f))
    return total_bytes / (1024 * 1024)
