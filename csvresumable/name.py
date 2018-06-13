import os.path
import sys
import hashlib


def get_identity(
    argv=sys.argv, prefix=".resumable-", suffix=".csv", encoding="utf-8", hasher=hashlib.sha1
):
    """
    get_identity('main')
    '.resumable-f58ccb5f55e806673664c8e5c56515d07790df41.csv'
    """
    sha1 = hasher("@".join(argv).encode(encoding))
    return "{}{}{}".format(prefix, sha1.hexdigest(), suffix)


def with_decoration(filepath, *, prefix):
    """
    >>> with_decoration('./foo/bar.txt', prefix='super-')
    './foo/super-bar.txt'
    """
    d = os.path.dirname(filepath)
    b, ext = os.path.splitext(os.path.basename(filepath))
    return os.path.join(d, "{}{}{}".format(prefix, b, ext))
