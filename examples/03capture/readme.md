```console
make[1]: Entering directory '$HOME/my/csvresumable/examples/03capture'
python main.py
----------------------------------------
DEBUG:csvresumable.recorder:create temporary file $HOME/.cache/py-resumable/tmp/tmp65wv8f88
OrderedDict([('id', '1'), ('name', 'foo')])
OrderedDict([('id', '2'), ('name', 'bar')])
OrderedDict([('id', '3'), ('name', 'boo')])
DEBUG:csvresumable.recorder:rename file $HOME/.cache/py-resumable/tmp/tmp65wv8f88 -> $HOME/.cache/py-resumable/dcda6905a8a5de5304710262d26dd56a2c5403f7.csv
RESUME=1 python main.py
----------------------------------------
DEBUG:csvresumable.capture:replay start '$HOME/.cache/py-resumable/dcda6905a8a5de5304710262d26dd56a2c5403f7.capture'
DEBUG:csvresumable.capture:replay end
DEBUG:csvresumable.loader:skip '1' (already used)
DEBUG:csvresumable.recorder:create temporary file $HOME/.cache/py-resumable/tmp/tmpcus8zc9x
DEBUG:csvresumable.loader:skip '2' (already used)
OrderedDict([('id', '1'), ('name', 'foo')])
OrderedDict([('id', '2'), ('name', 'bar')])
OrderedDict([('id', '3'), ('name', 'boo')])
OrderedDict([('id', '3'), ('name', 'boo')])
OrderedDict([('id', '4'), ('name', 'yoo')])
DEBUG:csvresumable.recorder:rename file $HOME/.cache/py-resumable/tmp/tmpcus8zc9x -> $HOME/.cache/py-resumable/dcda6905a8a5de5304710262d26dd56a2c5403f7.csv
make[1]: Leaving directory '$HOME/my/csvresumable/examples/03capture'
```
