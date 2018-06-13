from csvresumable import DictReader
import logging
logging.basicConfig(level=logging.DEBUG)

with open("./data.csv", "r") as rf:
    r = DictReader(rf)

    i = 0
    for row in r:
        print(row)
        if i == 3:
            break
        i += 1
