import logging
import click
from os import mkdir
from rich.logging import RichHandler
from rich.progress import track
from pathlib import Path
from cpcrCode import getData, saveData, generateDictionary
from neuromaps import transforms
import numpy as np

print("out of main")

FORMAT = "%(message)s"
logging.basicConfig(
    level="INFO",
    format=FORMAT,
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

log = logging.getLogger("receptorMaps")

@click.command()
@click.option("-d", "--data-dir", default="inputs", help="Where the data is.")
@click.option("-o", "--output_dir", default="outputs", help="Where to store outputs.")

def main(data_dir = "inputs", output_dir = "outputs") : 
    data_dir = Path(data_dir).resolve()
    output_dir = Path(output_dir).resolve()
    if not output_dir.exists():
        output_dir.mkdir()
    pass
    getter= getData(data_dir)
    maps = getter.getMaps()
    keys = getter.getKeys()
    #fsLR_tuples = []
    fsL_maps = []
    fsR_maps = []
    fsLR_maps = []
    for map in maps :
        transform = transforms.mni152_to_fslr(map, '32k')
        #fsLR_tuples.append(transform)
        fsL_maps.append(transform[0].agg_data())
        fsR_maps.append(transform[1].agg_data())
        fsLR_maps.append(np.concatenate(transform[0].agg_data(), transform[1].agg_data()))
    
    dictWriter1 = generateDictionary()
    dictWriter1.generate(keys, fsL_maps)
    leftHemi_maps = dictWriter1.returnDictionary()
    dictWriter2 = generateDictionary()
    dictWriter2.generate(keys, fsR_maps)
    rightHemi_maps = dictWriter2.returnDictionary()
    dictWriter3 = generateDictionary()
    dictWriter3.generate(keys, fsLR_maps)
    lr_maps = dictWriter3.returnDictionary()

    left_saver = saveData("fsLR32k_receptorMapDictionary_LEFT")
    left_saver.save(leftHemi_maps, output_dir)
    right_saver = saveData("fsLR32k_receptorMapDictionary_RIGHT")
    right_saver.save(rightHemi_maps, output_dir)
    lr_saver = saveData("fsLR32k_beliveau2017maps")
    lr_saver.save(lr_maps, output_dir)

if __name__ == "__main()__" :
    main()

main()