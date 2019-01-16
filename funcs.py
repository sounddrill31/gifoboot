def splitter(gif, out):
    from PIL import Image
  # https://gist.github.com/revolunet/848913

    frame = Image.open(gif)
    n = 0
    while frame:
        frame.save(f'{out}/{n:04d}.png', 'PNG')
        n += 1
        try:
            frame.seek(n)
        except EOFError:
            break

    return out


def mirror(path):
    import os
    from shutil import copyfile

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


def desc(out, width, height, fps):
    import os

    parts = [i.name for i in os.scandir(out) if i.is_dir() and i.name.startswith('part')]
    with open(f'{out}/desc.txt', 'w') as txt:
        txt.write(f'{width} {height} {fps}\n')
        for i in parts:
            txt.write(f'p 0 0 {i}\n')

    return True
