readme:
	kamidana readme.md.j2 -a kamidana.additionals.reader | sed 's/^RESUME=/$$ RESUME=/g; s/^python /$$ python /g;' | grep -v make | tee readme.md

00:
	SEED=0 python 00main.py
	SEED=1 RESUME=1 python 00main.py
	SEED=2 RESUME=1 python 00main.py
	SEED=5 python 00main.py

01:
	SEED=0 python 01main.py
	SEED=1 python 01main.py --resume
	SEED=2 python 01main.py --resume
	SEED=5 python 01main.py
