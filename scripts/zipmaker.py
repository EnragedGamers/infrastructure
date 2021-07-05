# zipmaker.py - EnragedGamers
# made by @gabyfle <gabyfle@enragedgamers.net>
# working with Python 2.6.6 (yeah, namecheap servers sucks)

import sys
import os
import zipfile

compressed = [".tar", ".gz", ".bz2", ".zip", ".7z"]

def build_zip(name, walk):
    zf = zipfile.ZipFile(name + ".zip", "w")
    for dir, _, files in os.walk(walk):
        if dir == walk + "/archives": continue # it's the archives folder so don't put it in the actual archive (infinite loop ?)
        zf.write(dir)
        for filename in files:
            if os.path.splitext(filename)[1] in compressed: continue # this file is a compressed one so skip
            zf.write(os.path.join(dir, filename))
    zf.close()

def main(game, version):
    games = ["csgo", "tf2"]
    if not game in games:
        print("[ZipMaker] The game \"" + str(game) + "\" is unknown.")
        sys.exit(1)

    path = game + "/archives/"
    filename = version + ".zip"

    if os.path.exists(path + filename):
        print("[ZipMaker] This version already exists, do you want to overwrite the existing one ? (Y/N)")
        response = input()
        if not response in ["Y", "y", "Yes", "YES", "yes"]:
            print("[ZipMaker] Aborting.")
            sys.exit(0)

    build_zip(path + version, game)

if len(sys.argv) < 3:
    print("[ZipMaker] Missing argument. Aborting.")
    sys.exit(1)

game, version = sys.argv[1], sys.argv[2]
main(game, version)

# we're not checking whether or not the /csgo/ path is existing but wdk since it'll be used by people knowing what they're doing
