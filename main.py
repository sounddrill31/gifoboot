import os
from sys import argv
from optparse import OptionParser
from tempfile import TemporaryDirectory
from zipfile import ZipFile, ZIP_STORED

from funcs import splitter, mirror, desc
from other import new_part, ratio

usage = 'usage: %prog [options] filename fps'
description = 'Input a GIF file, get a bootanimation.zip of it.'
prsr = OptionParser(usage=usage, description=description)

prsr.add_option(
    '-f',
    '--fps',
    default = -1,
    dest    = 'fps',
    type    = 'int',
    action  = 'store',
    help    = 'specify a framerate (by default it will try to get it automatically, if it fails it will ask for manual input)',
)
prsr.add_option(
    '-m',
    '--mirror',
    default = False,
    dest    = 'mirror',
    action  = 'store_true',
    help    = 'mirror the gif so it will be a perfect loop'
)
prsr.add_option(
    '-r',
    '--res',
    default = 1080,
    dest    = 'res',
    type    = 'int',
    action  = 'store',
    metavar = 'RESOLUTION',
    help    = 'specify a resolution (only needs width, default is 1080)'
)

(options, args) = prsr.parse_args()

with TemporaryDirectory() as out:
    gif = args[0]
    px, fps = splitter(gif, new_part(out))
    if options.mirror:
        mirror(px)
    w, h = options.res, int(options.res / ratio(out))
    if options.fps != -1:
        fps = options.fps
    elif fps is None:
        fps = int(input("Couldn't detect framerate, please enter it now: "))
    else:
        print(f'Detected framerate: {fps}')
    desc(out, w, h, fps)

    with ZipFile('bootanimation.zip', 'w', ZIP_STORED) as zp:
        for root, dirs, files in os.walk(out):
            for file in files:
                p = f'{root}/{file}'
                arcp = '/'.join(p.split('/')[3:])
                zp.write(p, arcp)
