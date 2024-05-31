#program that renames files ending in _X.png to _0X.png where X is a digit
# Usage: python namebyte.py

import os
import re
import sys

def namnbyt(mappe):
    filliste = os.listdir(mappe)
    filliste.sort()
    for filnamn in filliste:
        if filnamn.endswith(".png"):
            nytt_filnamn = re.sub(r"_(\d)\.png", r"_0\1.png", filnamn)
            if nytt_filnamn != filnamn:
                print(f"Renaming {filnamn} to {nytt_filnamn}")
                os.rename(os.path.join(mappe, filnamn), os.path.join(mappe, nytt_filnamn))

def filliste(mappe):
    filliste = os.listdir(mappe)
    filliste.sort()
    return filliste

if __name__ == "__main__":
    #namnbyt()
    mappe = r"C:\Users\78weikri\OneDrive - Akademiet Norge AS\KjemiOL\Fleirvalsoppgåver\\"
    directory_list = list()
    for root, dirs, files in os.walk(mappe, topdown=False):
        for name in dirs:
            directory_list.append(os.path.join(root, name))
    directory_list.sort()
    with open(mappe + "filliste.txt", "w") as f:
        for directory in directory_list:
            fillisten = filliste(directory)
            for fil in fillisten:
                if fil.endswith(".png"):
                    f.write(f"{fil}\n")
    print("Done")
            
