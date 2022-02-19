from pathlib import Path
import logging as log
import json

class saveData:

    def __init__(self, fname: str):
        self.fname = fname

    #save to directory
    def save(self, dic, output_dir: str = "."):
        with open(output_dir, "w") as self.fname:
            json.dump(dic, self.fname)

        log.info(f"Saved output to {output_dir / self.fname}")