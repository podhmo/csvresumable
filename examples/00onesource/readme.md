```console
make[1]: Entering directory '$HOME/my/csvresumable/examples/00onesource'
python main.py
----------------------------------------
DEBUG:csvresumable.recorder:create temporary file $HOME/.cache/py-resumable/tmp/tmpcowitrsv
OrderedDict([('id', '1'), ('name', 'a')])
OrderedDict([('id', '2'), ('name', 'b')])
OrderedDict([('id', '3'), ('name', 'c')])
OrderedDict([('id', '4'), ('name', 'e')])
DEBUG:csvresumable.recorder:rename file $HOME/.cache/py-resumable/tmp/tmpcowitrsv -> $HOME/.cache/py-resumable/7ad970258066905b768424602c585c4f8453b597.csv
RESUME=1 python main.py
----------------------------------------
DEBUG:csvresumable.loader:skip '1' (already used)
DEBUG:csvresumable.recorder:create temporary file $HOME/.cache/py-resumable/tmp/tmpptyt7toe
DEBUG:csvresumable.loader:skip '2' (already used)
DEBUG:csvresumable.loader:skip '3' (already used)
OrderedDict([('id', '4'), ('name', 'e')])
OrderedDict([('id', '5'), ('name', 'f')])
DEBUG:csvresumable.recorder:rename file $HOME/.cache/py-resumable/tmp/tmpptyt7toe -> $HOME/.cache/py-resumable/7ad970258066905b768424602c585c4f8453b597.csv
RESUME=1 python main.py
----------------------------------------
DEBUG:csvresumable.loader:skip '1' (already used)
DEBUG:csvresumable.recorder:create temporary file $HOME/.cache/py-resumable/tmp/tmpq652xb2u
DEBUG:csvresumable.loader:skip '2' (already used)
DEBUG:csvresumable.loader:skip '3' (already used)
DEBUG:csvresumable.loader:skip '4' (already used)
DEBUG:csvresumable.loader:skip '5' (already used)
DEBUG:csvresumable.recorder:rename file $HOME/.cache/py-resumable/tmp/tmpq652xb2u -> $HOME/.cache/py-resumable/7ad970258066905b768424602c585c4f8453b597.csv
python main.py
----------------------------------------
DEBUG:csvresumable.recorder:create temporary file $HOME/.cache/py-resumable/tmp/tmpnxcqye46
OrderedDict([('id', '1'), ('name', 'a')])
OrderedDict([('id', '2'), ('name', 'b')])
OrderedDict([('id', '3'), ('name', 'c')])
OrderedDict([('id', '4'), ('name', 'e')])
DEBUG:csvresumable.recorder:rename file $HOME/.cache/py-resumable/tmp/tmpnxcqye46 -> $HOME/.cache/py-resumable/7ad970258066905b768424602c585c4f8453b597.csv
make[1]: Leaving directory '$HOME/my/csvresumable/examples/00onesource'
```
