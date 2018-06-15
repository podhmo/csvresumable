from csvresumable import DictReader

files = ["a.csv", "b.csv"]
for f in files:
    r = DictReader(f)
    for row in r:
        do_something(row)
