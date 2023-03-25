# gifoboot

This script converts GIF files to Android boot animations.
Requires [Pillow](https://github.com/python-pillow/Pillow) to be installed:
```
$ pip install Pillow
```
To use, run for example:
```
$ python3 main.py ./persona-persona4.gif
```
This will output a `bootanimation.zip` of `persona-persona4.gif`. Framerate is set automatically, but can be set manually with `-f`. By defalt the width is set to `1080`, that can be changed with `-r`. Sometimes it's nice to have the `gif` mirrored the other way around, so it will be a perfect loop, and you can do that with `-m`.

TODO:
- `-c` to set it to complete at least one loop
- `-l` for landscape mode
- output a flashable file
- check what is being input from cmdline
- windows compatibility

> Also, there's some stuff [here](https://rastamanjohn.gq/bootanimations/).
> And thanks to @Lonami for all the help in the comments!

Credits to [tenor](https://tenor.com/view/persona-persona4-adachi-tohru-adachi-adachy-gif-22275551) for persona-persona4.gif
