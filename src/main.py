from treeReader import treeReader
import sys
from cfg.const import Const

def main():
    nbArg = len(sys.argv)
    if nbArg==1:
        print(Const.terminalUsage1)
        print(Const.terminalUsage2)
        sys.exit()
    elif nbArg != 3:
        print(f"{Const.terminalOneArg1}{nbArg - 1}{Const.terminalOneArg2}")
        sys.exit()
    print("Strating preprocessing")
    print ('argument list', sys.argv)
    treeReader.outDir()
    treeReader.copyTree(sys.argv[2])

if __name__ == "__main__":
 main()