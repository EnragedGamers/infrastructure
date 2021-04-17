#!/usr/bin/python

# Namecheap Python version: 2.6.6 (WTF IT SUCKS)
import os
import bz2
import glob

ignore = [
    __file__,
    'robot.txt',
    '.htaccess',
    '.ftpquota'
]

print('[compress] Starting to compress files...')

for root, subdirs, files in os.walk('fastdl.enragedgamers.net'):
    for file in files:
        if file in ignore: continue
        path = os.path.join(root, file)
        if os.path.splitext(file)[1] == '.bz2': continue
        print('[compress] Compressing {0}...'.format(file))
        with open(path, 'rb+') as f: # compress the binary data and write to a new file
            new = path + '.bz2'
            compress = bz2.compress(f.read())
            if not os.path.exists(new): # create a new file name.ext.bz2
                with open(new, 'a+'):
                    os.utime(new, None)
            with open(new, 'wb') as n:
                n.write(compress)
