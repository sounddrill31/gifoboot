import os

def desc(out, width, height, fps):
    parts = []
    with os.scandir(out) as files:
        for i in files:
            if i.is_dir() and i.name.startswith('part'):
                parts.append(i.name)
    
    with open(f'{out}/desc.txt', 'w') as txt:
        txt.write(f'{width} {height} {fps}\n')
        for i in parts:
            txt.write(f'p 0 0 {i}\n')

    return True