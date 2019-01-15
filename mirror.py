import os
from shutil import copyfile

def mirror(path):
    files = os.listdir(path)
    ext = os.path.splitext(files[0])[-1]
    for i in files:
        files[files.index(i)] = os.path.splitext(i)[0]
    files.sort(reverse=True)
    n, l = int(files[0]), len(files[0])
    files = files[1:-1]

    for i in files:
        n += 1
        copyfile(f'{path}/{i}{ext}', f'{path}/{n:0{l}d}{ext}')
