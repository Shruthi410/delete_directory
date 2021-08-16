import os, shutil

dir = 'TicTacToeTests'
delete_list = []
for files in os.listdir(dir):
    path = os.path.join(dir, files)
    try:
        shutil.rmtree(path)
    except OSError:
        os.remove(path)
    delete_list.append(path)

print(f"Deleted files: {delete_list}")
