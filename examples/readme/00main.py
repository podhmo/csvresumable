import sys
import os
import random
from io import StringIO
from csvresumable import DictReader

data = """\
id,name
1,foo
2,bar
3,boo
"""

random.seed(int(os.environ.get("SEED", "0")))
for row in DictReader(StringIO(data)):
    n = random.random()
    if n < 0.5:
        print("fail {}".format(n), file=sys.stderr)
        sys.exit(0)
    print("\t", row["name"])
print("finished")
