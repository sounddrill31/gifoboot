import os

def new_part(out):
    n = 0
    while os.path.exists(f'{out}/part{n}'):
        n += 1
    p = f'{out}/part{n}'
    os.makedirs(p)
    return p

def ratio(out):
    from PIL import Image
    with os.scandir(out) as files:
        for i in files:
            if i.is_dir() and i.name.startswith('part'):
                with os.scandir(i) as images:
                    for j in images:
                        if j.is_file() and j.name.endswith('.png'):
                            img = Image.open(j.path)
                            return img.size[0] / float(img.size[1])
    return None
    