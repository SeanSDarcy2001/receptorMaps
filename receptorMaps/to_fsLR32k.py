import numpy as np
from pathlib import Path
import neuromaps
from neuromaps import transforms

class Converter :

    def init(self, map) :
        self.MNImap = map

    def convert(self) :
        map = self.MNImap
	    #fsLR32k = neuromaps.transforms.mni152_to_fslr(map, '32k')
        #return fsLR32k