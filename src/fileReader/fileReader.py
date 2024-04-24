from fileReader.loadTemplate import loadTemplate
class FileReader:
    def __init__(self, template: loadTemplate) -> None:
        self.template = template
    def readFile(self, path):
        file = open(path, 'r')
        content = file.read()
        for key, value in self.template.dictonary.items():
            content = content.replace(key, value)
        file.close()
        file = open(path, "w")
        file.write(content)