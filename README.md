# gifoboot

This script converts GIF files to Android boot animations.
Requires PIL to be installed.

```
>>> python3 main.py --help
```
```
Usage: main.py [options] filename fps

Input a GIF file, get a bootanimation.zip of it.

Options:
  -h, --help            show this help message and exit
  -m, --mirror          mirror the gif so it will be a perfect loop
  -r RESOLUTION, --res=RESOLUTION
                        specify a resolution (only needs width, default is
                        1080)
```
For example:
```
>>> python3 main.py funny.gif 30
```
will output a `bootanimation.zip` with `funny.gif` running at 30 fps. By defalt the width is set to `1080`, that can be changed with `-r`. Sometimes it's nice to have a gif mirrored the other way around, so it will be a perfect loop, and you can do that with `-m`.

TODO:
- `-c` to set it to complete at least one loop
- `-f` to output a flashable file
- `-l` for landscape mode
- make fps optional
- check what is being input from cmdline
- windows compatibility

> Also, there's some stuff [here](https://rastamanjohn.gq/bootanimations/).
