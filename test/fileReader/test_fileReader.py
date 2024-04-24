from fileReader.fileReader import FileReader
from fileReader.fileReader import loadTemplate
import os

def test_fileReader():
    path = "test/rcs/fileReaderExample"
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            os.rmdir(path)
    file = open(path, 'x')
    content1 = "🖨️(\"HelloWorld\")\n"
    content2 = "🖨️(\"5️⃣❓\")"
    file.writelines([content1, content2])
    file.close()
    myTemplate = loadTemplate("test/rcs/skibidibidi.template")
    myFileReader = FileReader(myTemplate)
    myFileReader.readFile(path)
    file = open(path, 'r')
    lines = file.read()
    lines = lines.split("\n")
    assert lines[0] == "print(\"HelloWorld\")"
    assert lines[1] == "print(\"5?\")"
    os.remove(path)