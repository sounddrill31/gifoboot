# gifoboot

This script converts GIF files to Android boot animations.
Requires [Pillow](https://github.com/python-pillow/Pillow) to be installed:
```
$ pip install Pillow
```
To use, run for example:
```
$ python3 main.py ./funny.gif 30
```
This will output a `bootanimation.zip` with `funny.gif` running at 30 fps. By defalt the width is set to `1080`, that can be changed with `-r`. Sometimes it's nice to have the `gif` mirrored the other way around, so it will be a perfect loop, and you can do that with `-m`.

TODO:
- `-c` to set it to complete at least one loop
- `-f` to output a flashable file
- `-l` for landscape mode
- make fps optional
- check what is being input from cmdline
- windows compatibility

> Also, there's some stuff [here](https://rastamanjohn.gq/bootanimations/).
> And thanks to @Lonami for all the help in the comments!
