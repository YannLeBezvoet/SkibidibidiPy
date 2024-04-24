import os
from fileReader.fileReader import FileReader

def recursiveRead(path, myfileReader):
    ls = os.listdir(path)
    for element in ls:
        fullPath = f"{path}/{element}"
        if os.path.isdir(fullPath):
            recursiveRead(fullPath, myfileReader)
        elif os.path.isfile(fullPath):
            myfileReader.readFile(fullPath)
