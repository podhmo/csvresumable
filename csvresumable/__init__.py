import operator
import csv
import os
import logging
import itertools
import tempfile
import atexit

logger = logging.getLogger(__name__)
RESUME = bool(os.environ.get("RESUME", ""))


def get_writename(filename, *, dir="."):
    return os.path.join(dir, ".resumable-{}".format(os.path.basename(filename)))


def DictReader(f, writename=None, resume=None, key=None, dir=".", *args, **kwargs):
    name = writename or get_writename(getattr(f, "name", None) or "unknown-{!r}".format(f))
    reader = csv.DictReader(f, *args, **kwargs)
    key = key or operator.itemgetter(reader.fieldnames[0])
    return Resumable(reader, name, resume=resume, key=key, dir=dir)


class Resumable:
    reader_factory = csv.reader
    writer_factory = csv.writer

    def __init__(self, reader, writename, *, resume=None, key=None, dir="."):
        self.reader = reader
        self.writename = writename
        self.dir = dir
        self.resume = resume or RESUME
        self.get_key = key or operator.itemgetter(0)

    def __getattr__(self, name):
        return getattr(self.reader, name)

    def __iter__(self):
        tmp_wf = tempfile.NamedTemporaryFile("w", delete=False, dir=self.dir)
        tmp_writer = self.writer_factory(tmp_wf)

        def rename_tempfile():
            tmp_wf.close()
            dirpath = os.path.dirname(self.writename)
            if dirpath:
                os.makedirs(dirpath, exist_ok=True)
            os.rename(tmp_wf.name, self.writename)

        atexit.register(rename_tempfile)

        rows = []
        reader_itr = iter(self.reader)

        get_key = self.get_key
        if self.resume and os.path.exists(self.writename):
            try:
                with open(self.writename) as rf:
                    r = self.reader_factory(rf)
                    for used in r:
                        rows.append(next(reader_itr))
                        k = get_key(rows[-1])
                        if k != used[0]:
                            break
                        rows.pop()
                        logger.debug("already used, skip: %s", k)
                        tmp_writer.writerow([k])
            except StopIteration as e:
                logger.debug("stop iteration %r", e)

        for row in itertools.chain(rows, reader_itr):
            retval = yield row
            if retval is None:
                tmp_writer.writerow([get_key(row)])


def concat_groupby(itrs, *, key, sort=True):
    itr = itertools.chain.from_iterable(itrs)
    if sort:
        itr = sorted(itr, key=key)
    return itertools.groupby(itr, key=key)
