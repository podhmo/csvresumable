from csvresumable.recorder import Recorder
from csvresumable.loader import Loader


def iterate():
    yield "foo"
    yield "bar"


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    for row in Loader(iterate(), Recorder(), key=lambda x: x):
        print(row)
