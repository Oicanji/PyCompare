import pathlib
import os

dirname_root = pathlib.Path(__file__).parent.parent.resolve()

class Config:
    ROOT_PATH = dirname_root
    FILES = os.path.join(dirname_root, 'files')
    VERSION = open(os.path.join(dirname_root,".version")).read()
