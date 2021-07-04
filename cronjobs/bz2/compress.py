#!/usr/bin/python

# Namecheap Python version: 2.6.6 (WTF IT SUCKS)
import os
import sys
import bz2

import time

ignore = [ # files to ignore
    __file__,
    'robot.txt',
    '.htaccess',
    '.ftpquota',
    '.gitignore'
]

ext_ignore = [ # file extensions that shouldn't be compressed
    '.html',
    '.css',
    '.js',
    '.py',
    '.bz2'
]

filename = 'last_compression'
delay = 24 * 3600

if os.path.exists(filename):
    print('[compress] Checking latest compression timestamp...')
    with open(filename, 'r') as f:
        if float(f.readline()) - time.time() <= delay:
            sys.exit('[compress] Aborting file compression.')
else:
    with open(filename, 'w') as f:
        f.write(str(time.time()))


print('[compress] Starting to compress files...')

for root, subdirs, files in os.walk('fastdl.enragedgamers.net'):
    for file in files:
        if file in ignore: continue
        if os.path.splitext(file)[1] in ext_ignore: continue

        path = os.path.join(root, file)
        
        print('[compress] Compressing {0}...'.format(file))

        with open(path, 'rb+') as f: # compress the binary data and write to a new file
            new = path + '.bz2'
            compress = bz2.compress(f.read())
            if not os.path.exists(new): # create a new file name.ext.bz2
                with open(new, 'a+'):
                    os.utime(new, None)
            with open(new, 'wb') as n:
                n.write(compress)
 