```console
make[1]: Entering directory '$HOME/my/csvresumable/examples/00onesource'
python main.py
----------------------------------------
DEBUG:csvresumable.recorder:create temporary file $HOME/.cache/py-resumable/tmp/tmpqyt0prow
OrderedDict([('id', '1'), ('name', 'a')])
OrderedDict([('id', '2'), ('name', 'b')])
OrderedDict([('id', '3'), ('name', 'c')])
OrderedDict([('id', '4'), ('name', 'e')])
DEBUG:csvresumable.recorder:rename file $HOME/.cache/py-resumable/tmp/tmpqyt0prow -> $HOME/.cache/py-resumable/5186ed011fc55484df5ac8fdd929c174136938a0.csv
RESUME=1 python main.py
----------------------------------------
DEBUG:csvresumable.loader:skip '1' (already used)
DEBUG:csvresumable.recorder:create temporary file $HOME/.cache/py-resumable/tmp/tmp2hytgsbo
DEBUG:csvresumable.loader:skip '2' (already used)
DEBUG:csvresumable.loader:skip '3' (already used)
OrderedDict([('id', '4'), ('name', 'e')])
OrderedDict([('id', '5'), ('name', 'f')])
DEBUG:csvresumable.recorder:rename file $HOME/.cache/py-resumable/tmp/tmp2hytgsbo -> $HOME/.cache/py-resumable/5186ed011fc55484df5ac8fdd929c174136938a0.csv
RESUME=1 python main.py
----------------------------------------
DEBUG:csvresumable.loader:skip '1' (already used)
DEBUG:csvresumable.recorder:create temporary file $HOME/.cache/py-resumable/tmp/tmpgb1y2p7b
DEBUG:csvresumable.loader:skip '2' (already used)
DEBUG:csvresumable.loader:skip '3' (already used)
DEBUG:csvresumable.loader:skip '4' (already used)
DEBUG:csvresumable.loader:skip '5' (already used)
DEBUG:csvresumable.recorder:rename file $HOME/.cache/py-resumable/tmp/tmpgb1y2p7b -> $HOME/.cache/py-resumable/5186ed011fc55484df5ac8fdd929c174136938a0.csv
python main.py
----------------------------------------
DEBUG:csvresumable.recorder:create temporary file $HOME/.cache/py-resumable/tmp/tmprrvynp1e
OrderedDict([('id', '1'), ('name', 'a')])
OrderedDict([('id', '2'), ('name', 'b')])
OrderedDict([('id', '3'), ('name', 'c')])
OrderedDict([('id', '4'), ('name', 'e')])
DEBUG:csvresumable.recorder:rename file $HOME/.cache/py-resumable/tmp/tmprrvynp1e -> $HOME/.cache/py-resumable/5186ed011fc55484df5ac8fdd929c174136938a0.csv
make[1]: Leaving directory '$HOME/my/csvresumable/examples/00onesource'
```
