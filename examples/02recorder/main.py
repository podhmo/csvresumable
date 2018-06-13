from csvresumable.recorder import Recorder
from csvresumable.name import get_identity


def iterate():
    yield "foo"
    yield "bar"


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    for row in Recorder(iterate(), writename=get_identity(), key=lambda x: x):
        print(row)
