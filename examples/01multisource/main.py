import json
import csv
import itertools
import csvresumable


def iterate():
    files = ["data/users1.csv", "data/users2.csv"]
    readers = [csv.DictReader(open(f)) for f in files]
    return csvresumable.concat_groupby(readers, key=lambda x: x["groupId"])

import sys; sys.stderr.write("----------------------------------------\n")
itr = csvresumable.iterate(iterate())
for gid, rows in itertools.islice(itr, 2):
    print(json.dumps({"gid": gid, "rows": list(rows)}))

