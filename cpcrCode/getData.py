import numpy as np
from pathlib import Path

class getData:
    """Parses the LED marker data."""

    def __init__(self, path: str):
        self.MNImaps = []
        self.keys = []
        self.path = path
        fileList = Path(path).glob('**/*.gz')
        for file in fileList:
            self.MNImaps.append(file)
            self.keys.append(str(file))

    def getMaps(self) :
        return self.MNImaps

    def getKeys(self) :
        return self.keys
    