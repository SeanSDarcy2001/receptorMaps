from pathlib import Path
import re

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
            fileName = str(file)
            try:
                found = re.search('/inputs/(.+?).nii', fileName).group(1)
                print(found)
            except AttributeError:
                pass
            self.keys.append(found)

    def getMaps(self) :
        print("we called get maps")
        return self.MNImaps

    def getKeys(self) :
        return self.keys
    