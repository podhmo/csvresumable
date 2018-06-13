from logging import getLogger as get_logger
import atexit
import os.path
import csv
import tempfile
from .langhelpers import reify

logger = get_logger(__name__)


class Recorder:
    writer_factory = csv.writer

    def __init__(self, iterator, *, writename, key, dir=".", register=atexit.register):
        self.iterator = iterator
        self.writename = writename
        self.register = register
        self.key = key
        self.dir = dir
        self._wf = None

    @reify
    def writer(self):
        self._wf = tempfile.NamedTemporaryFile("w", delete=False, dir=self.dir)
        logger.debug("create temporary file %s", self._wf.name)
        self.register(self.finalize)
        return self.writer_factory(self._wf)

    def __iter__(self):
        return self

    def __next__(self):
        row = next(self.iterator)
        self.writer.writerow([self.key(row)])
        return row

    def finalize(self):
        if self._wf is None:
            return
        self._wf.close()
        dirpath = os.path.dirname(self.writename)
        if dirpath:
            os.makedirs(dirpath, exist_ok=True)
        logger.debug("rename file %s -> %s", self._wf.name, self.writename)
        os.rename(self._wf.name, self.writename)