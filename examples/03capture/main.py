import itertools
from csvresumable import capture, DictReader
import logging

print("-")
logging.basicConfig(level=logging.DEBUG)
with capture():
    with open("data.csv") as rf:
        r = DictReader(rf)
        for row in itertools.islice(r, 3):
            print(row)
