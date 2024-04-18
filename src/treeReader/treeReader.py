import os
import shutil
from cfg.const import Const

def outDir():
    if os.path.isdir(Const.outPath):
        shutil.rmtree(Const.outPath)

def copyTree(path: str):
    shutil.copytree(path, Const.outPath)