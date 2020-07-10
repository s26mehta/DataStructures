###################################################################################################
## Dropbox Interview: Output a list of lists that has the duplicates files in a path
##                    hierachy. The content is what makes the files duplicates not the
##                    file names. (Generate md4/md5 hash but to double check if the files
##                    are duplicates you can hash again.)
##                    If two files have same size and same hash code, they are probably equal.
##                    But there will still be a little chance these two files are different
##                   (except if file size is less than hash code size).
###################################################################################################

import os
import hashlib

values = dict()
duplicates = []
og_path = []
def get_duplicates(path):
    if len(og_path) == 0:
        og_path.append(path)

    for name in os.listdir(path):
        if os.path.isdir(name):
            get_duplicates(os.path.abspath(name))

        if os.path.isfile(name):
            hash = md5(name)
            if hash in values:
                values[hash].append(os.path.abspath(name))
            else:
                values[hash] = [os.path.abspath(name)]

    if path == og_path[0]:
        output_duplicates()

def output_duplicates():
    for key in values:
        if len(values[key])> 1:
            duplicates.append(values[key])

    print(duplicates)


def md5(name):
    hash_md5 = hashlib.md5()
    with open(name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# get_duplicates(os.getcwd())
