from pathlib import Path
import logging as log
import json

class saveData:

    def __init__(self, fname: str):
        self.fname = fname

    #save to directory
    def save(self, dic, output_dir: str = "."):
        newPath = Path.joinpath(output_dir, self.fname)
        with open(newPath, "w") as self.fname:
            json.dump(dic, self.fname)
