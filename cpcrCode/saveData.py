from pathlib import Path
import logging as log
import json

class saveData:

    def __init__(self, fname: str):
        self.fname = fname

    #save to directory
    def save(self, dic, output_dir: str = "."):
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        with open(output_dir / self.fname, "w") as file:
            json.dump(dic, file)
            file.write(str(self.fname))

        log.info(f"Saved output to {output_dir / self.fname}")