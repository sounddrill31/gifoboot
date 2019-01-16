def splitter(gif, out):
    from collections import Counter
    from PIL import Image, ImageSequence

    f = Image.open(gif)
    n = 0
    d = []
    for frame in ImageSequence.Iterator(f):
        n += 1
        d.append(frame.info['duration'])
        frame.save(f'{out}/{n:04d}.png', 'PNG')
    fps = None
    c = Counter(d)
    m = c.most_common(2)
    if len(m) == 1 or m[0][1] >= (n/4)*3:
        fps = int(1000 / m[0][0])

    return out, fps


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
