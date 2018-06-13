from csvresumable import DictReader, capture
import json
import logging
import sys

logging.basicConfig(level=logging.DEBUG)
sys.stderr.write("----------------------------------------\n")
with capture():
    with open("data.csv") as rf:
        r = DictReader(rf)
        for i, row in enumerate(r):
            print("start", row["id"])
            if i == 2:
                raise Exception("hmm")
            print(json.dumps(row))
            print("end", row["id"])
