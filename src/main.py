from treeReader import treeReader
import sys
from cfg.const import Const
from treeReader import recursiveRead
from fileReader.fileReader import FileReader
from fileReader.loadTemplate import loadTemplate

def main():
    nbArg = len(sys.argv)
    if nbArg==1:
        print(Const.terminalUsage1)
        print(Const.terminalUsage2)
        sys.exit()
    elif nbArg != 3:
        print(f"{Const.terminalOneArg1}{nbArg - 1}{Const.terminalOneArg2}")
        sys.exit()
    print(Const.terminalMain1)
    treeReader.outDir()
    treeReader.copyTree(sys.argv[2])
    myTemplate = loadTemplate(sys.argv[1])
    myFileReader = FileReader(myTemplate)
    recursiveRead.recursiveRead(".out", myFileReader)
    print("Finish")
if __name__ == "__main__":
 main()