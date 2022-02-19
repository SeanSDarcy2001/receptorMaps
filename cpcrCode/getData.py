import numpy as np
from pathlib import Path

class getData:
    """Parses the LED marker data."""

    def __init__(self, path: str):
        self.MNImaps = []
        self.keys = []
        self.path = path
        print("we get here")
        fileList = Path(path).glob('**/*.gz')
        for file in fileList:
            print(file)
            self.MNImaps.append(file)
            self.keys.append(str(file))

    def getMaps(self) :
        print("we called get maps")
        return self.MNImaps

    def getKeys(self) :
        return self.keys
    