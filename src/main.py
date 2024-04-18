from treeReader import treeReader
import sys

def main():
    if len(sys.argv)==1:
        print("SkibidibidiPy by Yann Le Bezvoet - dev 1")
        print("\tUsage : skibidibidipy /path/to/skibidibidiPython/code")
        sys.exit()
    print("Strating preprocessing")
    print ('argument list', sys.argv)
    treeReader.outDir()
    treeReader.copyTree(sys.argv[1])

if __name__ == "__main__":
 main()