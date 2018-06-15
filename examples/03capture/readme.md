```console
make[1]: Entering directory '$HOME/my/csvresumable/examples/03capture'
python main.py
----------------------------------------
DEBUG:csvresumable.recorder:create temporary file $HOME/.cache/py-resumable/tmp/tmpgu0jz9mt
OrderedDict([('id', '1'), ('name', 'foo')])
OrderedDict([('id', '2'), ('name', 'bar')])
OrderedDict([('id', '3'), ('name', 'boo')])
DEBUG:csvresumable.recorder:rename file $HOME/.cache/py-resumable/tmp/tmpgu0jz9mt -> $HOME/.cache/py-resumable/d4c0fe049bdb214c3e165473603b358097588660.csv
RESUME=1 python main.py
----------------------------------------
DEBUG:csvresumable.capture:replay start '$HOME/.cache/py-resumable/618e4e5dbe4cc34a9679f9b3b9ec4edd5bf6c27d.capture'
OrderedDict([('id', '1'), ('name', 'foo')])
OrderedDict([('id', '2'), ('name', 'bar')])
OrderedDict([('id', '3'), ('name', 'boo')])
DEBUG:csvresumable.capture:replay end
DEBUG:csvresumable.loader:skip '1' (already used)
DEBUG:csvresumable.recorder:create temporary file $HOME/.cache/py-resumable/tmp/tmpeyppvdj5
DEBUG:csvresumable.loader:skip '2' (already used)
OrderedDict([('id', '3'), ('name', 'boo')])
OrderedDict([('id', '4'), ('name', 'yoo')])
DEBUG:csvresumable.recorder:rename file $HOME/.cache/py-resumable/tmp/tmpeyppvdj5 -> $HOME/.cache/py-resumable/d4c0fe049bdb214c3e165473603b358097588660.csv
make[1]: Leaving directory '$HOME/my/csvresumable/examples/03capture'
```
