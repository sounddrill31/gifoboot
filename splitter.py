from PIL import Image

# https://gist.github.com/revolunet/848913

def splitter(gif, out):
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
