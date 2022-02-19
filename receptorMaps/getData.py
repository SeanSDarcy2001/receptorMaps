import numpy as np
from pathlib import Path

class load:
    """Parses the LED marker data."""

    def __init__(self, path: str):
        self.path = path
        with open(path, "r") as f:
            return NotImplementedError