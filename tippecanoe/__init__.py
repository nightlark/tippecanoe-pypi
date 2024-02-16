import os
import subprocess
import sys

try:
    from ._version import __version__, __version_tuple__
except ModuleNotFoundError:
    __version__ = ""
    __version_tuple__ = ()

BIN_DIR = os.path.join(os.path.dirname(__file__), "bin")


def _program(name: str, *args):
    return subprocess.call([os.path.join(BIN_DIR, name)] + list(args))


def tippecanoe():
    raise SystemExit(_program("tippecanoe", *sys.argv[1:]))


def tile_join():
    raise SystemExit(_program("tile-join", *sys.argv[1:]))


def tippecanoe_decode():
    raise SystemExit(_program("tippecanoe-decode", *sys.argv[1:]))


def tippecanoe_enumerate():
    raise SystemExit(_program("tippecanoe-enumerate", *sys.argv[1:]))


def tippecanoe_json_tool():
    raise SystemExit(_program("tippecanoe-json-tool", *sys.argv[1:]))


def tippecanoe_overzoom():
    raise SystemExit(_program("tippecanoe-overzoom", *sys.argv[1:]))
