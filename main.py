import os
from sys import argv
from optparse import OptionParser
from tempfile import TemporaryDirectory
from zipfile import ZipFile, ZIP_STORED

from other import new_part, ratio
from splitter import splitter
from mirror import mirror
from desc import desc

usage = 'usage: %prog [options] filename fps'
description = 'Input a GIF file, get a bootanimation.zip of it.'
prsr = OptionParser(usage=usage, description=description)

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
    gif, fps = args[0], args[1]
    p0 = splitter(gif, new_part(out))
    if options.mirror:
        mirror(p0)
    w, h = options.res, int(options.res / ratio(out))
    desc(out, w, h, fps)

    with ZipFile('bootanimation.zip', 'w', ZIP_STORED) as zp:
        for root, dirs, files in os.walk(out):
            for file in files:
                p = f'{root}/{file}'
                arcp = '/'.join(p.split('/')[3:])
                zp.write(p, arcp)
