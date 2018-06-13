```console
make[1]: Entering directory '$HOME/my/csvresumable/examples/04witherror'
python main.py || echo ""
----------------------------------------
DEBUG:csvresumable.recorder:create temporary file $HOME/.cache/py-resumable/tmp/tmphelnzntq
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
DEBUG:csvresumable.recorder:rename file $HOME/.cache/py-resumable/tmp/tmphelnzntq -> $HOME/.cache/py-resumable/beffc1e6485d0461cfa3059a1cd793c540e3b712.csv

RESUME=1 python main.py || echo ""
----------------------------------------
DEBUG:csvresumable.capture:replay start '$HOME/.cache/py-resumable/beffc1e6485d0461cfa3059a1cd793c540e3b712.capture'
DEBUG:csvresumable.capture:replay end
DEBUG:csvresumable.loader:skip '1' (already used)
DEBUG:csvresumable.recorder:create temporary file $HOME/.cache/py-resumable/tmp/tmpfbl35ur8
DEBUG:csvresumable.loader:skip '2' (already used)
start 1
{"id": "1", "name": "foo"}
end 1
start 2
{"id": "2", "name": "bar"}
end 2
start 3
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
DEBUG:csvresumable.recorder:rename file $HOME/.cache/py-resumable/tmp/tmpfbl35ur8 -> $HOME/.cache/py-resumable/beffc1e6485d0461cfa3059a1cd793c540e3b712.csv

make[1]: Leaving directory '$HOME/my/csvresumable/examples/04witherror'
```
