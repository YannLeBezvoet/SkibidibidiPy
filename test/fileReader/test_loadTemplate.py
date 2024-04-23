from fileReader.loadTemplate import loadTemplate

def test_loadTemplate():
    template = loadTemplate("test/rcs/skibidibidi.template")
    assert(template.dictonary["🖨️"]=="print")
    assert(template.dictonary["0️⃣"]=="0")
    assert(template.dictonary["🛌"]=="sleep")