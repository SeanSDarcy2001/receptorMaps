from pathlib import Path
import logging as log
import json
import pickle

class saveData:

    def __init__(self, fname: str):
        self.fname = fname

    #save to directory
    def save(self, dic, output_dir: str = ".", pickled = False):
        newPath = Path.joinpath(output_dir, self.fname)
        if pickled:
            fileHandler = open(newPath, "w")
            print("Dumping with pickle:")
            pickle.dump(dic, fileHandler)
        with open(newPath, "w") as self.fname:
            json.dump(dic, self.fname)
