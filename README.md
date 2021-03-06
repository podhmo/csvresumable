# cssresumable

Adding tiny resume function for your csv reading iterator.

## examples

00main.py

```python
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

```

resuming until success.

```console
SEED=0 python 00main.py
fail 0.420571580830845
	 foo
	 bar
SEED=1 RESUME=1 python 00main.py
fail 0.13436424411240122
SEED=2 RESUME=1 python 00main.py
	 boo
finished
SEED=5 python 00main.py
	 foo
	 bar
	 boo
finished

```

or setting with `resume` option (run this script, such as `python 01main.py --resume`)

```diff
--- 00main.py	2018-06-16 04:19:51.573578443 +0900
+++ 01main.py	2018-06-16 04:20:04.760554103 +0900
@@ -4,17 +4,23 @@
 from io import StringIO
 from csvresumable import DictReader
 
-data = """\
+data = """
 id,name
 1,foo
 2,bar
 3,boo
 """
 
+import argparse
+parser = argparse.ArgumentParser()
+parser.add_argument("--seed", default=0, type=int)
+parser.add_argument("--resume", action="store_true")
+args = parser.parse_args()
+
 random.seed(int(os.environ.get("SEED", "0")))
-for row in DictReader(StringIO(data)):
+for row in DictReader(StringIO(data), resume=args.resume):
     n = random.random()
-    if n < 0.5:
+    if n > 0.8:
         print("fail {}".format(n), file=sys.stderr)
         sys.exit(0)
     print("\t", row["name"])

```

### with multi files

```python
from csvresumable import DictReader

files = ["a.csv", "b.csv"]
for f in files:
    r = DictReader(f)
    for row in r:
        do_something(row)

```

## more

- [examples/01multisource](examples/01multisource)
