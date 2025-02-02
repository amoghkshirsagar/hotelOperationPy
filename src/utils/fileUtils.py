import json

def writeJson(fileName: str, data):
        with open(fileName, 'w') as f:
            json.dump(data, f)

def readJson(fileName: str):
    with open(fileName, 'r') as f:
        fileContent = json.load(f)
        return fileContent
