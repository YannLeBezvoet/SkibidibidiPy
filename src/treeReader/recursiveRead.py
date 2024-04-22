import os
from fileReader import fileReader

def recursiveRead(path: str):
    ls = os.listdir(path)
    for element in ls:
        fullPath = f"{path}/{element}"
        if os.path.isdir(fullPath):
            recursiveRead(fullPath)
        elif os.path.isfile(fullPath):
            fileReader.readFile(fullPath)