class loadTemplate:
    def __init__(self, templatePath: str) -> None:
        self.dictonary = {}
        file = open(templatePath)
        content = file.read()
        content = content.split("\n")
        for line in content:
            if "|" in line:
                splitedLine = line.split("|")
                self.dictonary[splitedLine[0]] = splitedLine[1]