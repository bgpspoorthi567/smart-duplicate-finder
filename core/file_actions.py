import os
import shutil

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)

def move_file(path, destination="duplicates_backup"):
    os.makedirs(destination, exist_ok=True)
    shutil.move(path, os.path.join(destination, os.path.basename(path)))
