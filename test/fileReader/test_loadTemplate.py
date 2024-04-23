from fileReader.loadTemplate import loadTemplate

def loadTestTemplate(path):
    template = loadTemplate(path)
    assert(template.dictonary["🖨️"]=="print")
    assert(template.dictonary["0️⃣"]=="0")
    assert(template.dictonary["🛌"]=="sleep")

def test_loadTemplateNoEndLine():
    loadTestTemplate("test/rcs/skibidibidi.template")

def test_loadTemplateEndLine():
    loadTestTemplate("test/rcs/skibidibidiEndLine.template")