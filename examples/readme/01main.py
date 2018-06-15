import sys
import os
import random
from io import StringIO
from csvresumable import DictReader

data = """
id,name
1,foo
2,bar
3,boo
"""

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--seed", default=0, type=int)
parser.add_argument("--resume", action="store_true")
args = parser.parse_args()

random.seed(int(os.environ.get("SEED", "0")))
for row in DictReader(StringIO(data), resume=args.resume):
    n = random.random()
    if n > 0.8:
        print("fail {}".format(n), file=sys.stderr)
        sys.exit(0)
    print("\t", row["name"])
print("finished")
