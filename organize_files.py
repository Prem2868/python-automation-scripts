import os
import shutil

def organize_folder(path):
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            ext = filename.split('.')[-1]
            dest_folder = os.path.join(path, ext)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(os.path.join(path, filename), os.path.join(dest_folder, filename))

if __name__ == "__main__":
    path = input("Enter path to organize: ")
    organize_folder(path)
