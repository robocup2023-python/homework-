import threading
import os

def rename_files(old_name, new_name):
    os.rename(old_name, new_name)

if __name__ == "__main__":
    path = 'Home'
    for file in  os.makedirs(path):
        t = threading.Thread(target=rename_files, args=(file, "new_" + file))
        t.start()