import os, shutil

home_path = os.path.expanduser('~')

dir1 = os.path.join(home_path, r'Users/vajroprd/Library/Developer/Xcode/DerivedData')
dir2 = os.path.join(home_path, r'Users/vajroprd/Library/Developer/Xcode/Archieves')
dir3 = os.path.join(home_path, r'Library/Caches/')
dir4 = os.path.join(home_path, r'Library/Application Support/')


dirs = [dir1, dir2, dir3, dir4]


for dir in dirs:
    delete_list = []
    for files in os.listdir(dir):
        path = os.path.join(dir, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)
        delete_list.append(path)

    print(f"Deleted files: {delete_list}")
    
