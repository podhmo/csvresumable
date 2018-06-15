```console
make[1]: Entering directory '$HOME/my/csvresumable/examples/04witherror'
python main.py || echo ""
----------------------------------------
DEBUG:csvresumable.recorder:create temporary file $HOME/.cache/py-resumable/tmp/tmpg6snnoru
start 1
{"id": "1", "name": "foo"}
end 1
start 2
{"id": "2", "name": "bar"}
end 2
start 3
Traceback (most recent call last):
  File "main.py", line 14, in <module>
    raise Exception("hmm")
Exception: hmm
DEBUG:csvresumable.recorder:rename file $HOME/.cache/py-resumable/tmp/tmpg6snnoru -> $HOME/.cache/py-resumable/06bec8bf4d2c531ff8c0661f42d81a332a4111b7.csv

RESUME=1 python main.py || echo ""
----------------------------------------
DEBUG:csvresumable.capture:replay start '$HOME/.cache/py-resumable/5b77ff96da7011386579707d00d130b83e12741d.capture'
start 1
{"id": "1", "name": "foo"}
end 1
start 2
{"id": "2", "name": "bar"}
end 2
start 3
DEBUG:csvresumable.capture:replay end
DEBUG:csvresumable.loader:skip '1' (already used)
DEBUG:csvresumable.recorder:create temporary file $HOME/.cache/py-resumable/tmp/tmpn7595soe
DEBUG:csvresumable.loader:skip '2' (already used)
start 3
{"id": "3", "name": "boo"}
end 3
start 4
{"id": "4", "name": "hoi"}
end 4
start 5
Traceback (most recent call last):
  File "main.py", line 14, in <module>
    raise Exception("hmm")
Exception: hmm
DEBUG:csvresumable.recorder:rename file $HOME/.cache/py-resumable/tmp/tmpn7595soe -> $HOME/.cache/py-resumable/06bec8bf4d2c531ff8c0661f42d81a332a4111b7.csv

make[1]: Leaving directory '$HOME/my/csvresumable/examples/04witherror'
```
