```console
make[1]: Entering directory '$HOME/my/csvresumable/examples/02recorder'
python main.py
----------------------------------------
DEBUG:csvresumable.recorder:create temporary file $HOME/.cache/py-resumable/tmp/tmpjaekt2q_
foo
bar
DEBUG:csvresumable.recorder:rename file $HOME/.cache/py-resumable/tmp/tmpjaekt2q_ -> $HOME/.cache/py-resumable/6fc56a312f7bef55d6e3a7d85b4196eb9bc7cb94.csv
RESUME=1 python main.py
----------------------------------------
DEBUG:csvresumable.loader:skip 'foo' (already used)
DEBUG:csvresumable.recorder:create temporary file $HOME/.cache/py-resumable/tmp/tmpbxa5jpcw
DEBUG:csvresumable.loader:skip 'bar' (already used)
DEBUG:csvresumable.recorder:rename file $HOME/.cache/py-resumable/tmp/tmpbxa5jpcw -> $HOME/.cache/py-resumable/6fc56a312f7bef55d6e3a7d85b4196eb9bc7cb94.csv
make[1]: Leaving directory '$HOME/my/csvresumable/examples/02recorder'
```
