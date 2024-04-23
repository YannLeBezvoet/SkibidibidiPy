import os
import shutil
from cfg.const import Const

def outDir(Outpath=Const.outPath):
    if os.path.isdir(Outpath):
        shutil.rmtree(Outpath)

def copyTree(path, outPath=Const.outPath):
    shutil.copytree(path, outPath)