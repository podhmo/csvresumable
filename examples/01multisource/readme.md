```console
make[1]: Entering directory '$HOME/my/csvresumable/examples/01multisource'
python main.py
----------------------------------------
{"gid": "1", "rows": [{"id": "1", "name": "foo", "groupId": "1"}, {"id": "2", "name": "bar", "groupId": "1"}, {"id": "5", "name": "x", "groupId": "1"}, {"id": "1", "name": "foo", "groupId": "1"}]}
{"gid": "2", "rows": [{"id": "3", "name": "boo", "groupId": "2"}, {"id": "6", "name": "y", "groupId": "2"}]}
RESUME=1 python main.py
----------------------------------------
{"gid": "2", "rows": [{"id": "3", "name": "boo", "groupId": "2"}, {"id": "6", "name": "y", "groupId": "2"}]}
{"gid": "3", "rows": [{"id": "4", "name": "bee", "groupId": "3"}, {"id": "7", "name": "z", "groupId": "3"}]}
RESUME=1 python main.py
----------------------------------------
{"gid": "3", "rows": [{"id": "4", "name": "bee", "groupId": "3"}, {"id": "7", "name": "z", "groupId": "3"}]}
python main.py
----------------------------------------
{"gid": "1", "rows": [{"id": "1", "name": "foo", "groupId": "1"}, {"id": "2", "name": "bar", "groupId": "1"}, {"id": "5", "name": "x", "groupId": "1"}, {"id": "1", "name": "foo", "groupId": "1"}]}
{"gid": "2", "rows": [{"id": "3", "name": "boo", "groupId": "2"}, {"id": "6", "name": "y", "groupId": "2"}]}
make[1]: Leaving directory '$HOME/my/csvresumable/examples/01multisource'
```
