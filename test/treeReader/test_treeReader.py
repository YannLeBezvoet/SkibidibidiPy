from treeReader import treeReader
import os

def test_outDir():
    outDirExemplePath="test/rcs/codeExemple/outDirExemple"
    treeReader.outDir(outDirExemplePath)
    os.makedirs(outDirExemplePath)
    treeReader.outDir(outDirExemplePath)
    assert not os.path.exists(outDirExemplePath)

def test_copyTree():
    copyTreeExemple="test/rcs/codeExemple/copyTreeFolder"
    outCopyTree="test/rcs/codeExemple/outTreeFolder"
    treeReader.outDir(outCopyTree)
    treeReader.copyTree(copyTreeExemple, outCopyTree)
    assert os.path.isdir(outCopyTree)
    assert os.path.isdir(f"{outCopyTree}/copyTreeFolder")
    assert os.path.isfile(f"{outCopyTree}/copyTreeFile")
    assert os.path.isfile(f"{outCopyTree}/copyTreeFolder/copyTreeFile3")