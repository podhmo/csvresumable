from csvresumable import DictReader
import logging
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--resume", action="store_true")
parser.add_argument("file", nargs="?", default="./data.csv")
args = parser.parse_args()
# logging.basicConfig(level=logging.DEBUG)

import sys; sys.stderr.write("----------------------------------------\n")
with open(args.file, "r") as rf:
    r = DictReader(rf, resume=args.resume)

    for i, row in enumerate(r):
        print(row)
        if i == 2:
            break
