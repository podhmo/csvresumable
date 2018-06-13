import operator
import csv
import itertools
from csvresumable.loader import Loader
from csvresumable.recorder import Recorder


def DictReader(f, writename=None, resume=None, key=None, dir=".", *args, **kwargs):
    reader = csv.DictReader(f, *args, **kwargs)
    recorder = Recorder(name=writename, dir=dir)
    return _DictReaderWrapper(reader, recorder=recorder, resume=resume, key=key)


class _DictReaderWrapper:
    def __init__(self, reader, *, recorder, resume=None, key=None, dir="."):
        self.reader = reader
        self.key = key or operator.itemgetter(reader.fieldnames[0])
        self.loader = Loader(self.reader, recorder, key=self.key, resume=resume)

    def __getattr__(self, name):
        return getattr(self.reader, name)

    def __iter__(self):
        return iter(self.loader)


def iterate(iterator, *, writename=None, resume=None, key=None, dir="."):
    recorder = Recorder(name=writename, dir=dir)
    key = key or (lambda x: x)
    return Loader(iterator, recorder=recorder, resume=resume, key=key)


def concat_groupby(itrs, *, key, sort=True):
    itr = itertools.chain.from_iterable(itrs)
    if sort:
        itr = sorted(itr, key=key)
    return itertools.groupby(itr, key=key)
