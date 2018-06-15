```console
make[1]: Entering directory '$HOME/my/csvresumable/examples/02recorder'
python main.py
----------------------------------------
DEBUG:csvresumable.recorder:create temporary file $HOME/.cache/py-resumable/tmp/tmpkuo5t58k
foo
bar
DEBUG:csvresumable.recorder:rename file $HOME/.cache/py-resumable/tmp/tmpkuo5t58k -> $HOME/.cache/py-resumable/05cb957a0f761eaedda42f148f15a3d04b461072.csv
RESUME=1 python main.py
----------------------------------------
DEBUG:csvresumable.loader:skip 'foo' (already used)
DEBUG:csvresumable.recorder:create temporary file $HOME/.cache/py-resumable/tmp/tmpka5s4cku
DEBUG:csvresumable.loader:skip 'bar' (already used)
DEBUG:csvresumable.recorder:rename file $HOME/.cache/py-resumable/tmp/tmpka5s4cku -> $HOME/.cache/py-resumable/05cb957a0f761eaedda42f148f15a3d04b461072.csv
make[1]: Leaving directory '$HOME/my/csvresumable/examples/02recorder'
```
