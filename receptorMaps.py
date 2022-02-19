import logging
import click
from os import mkdir
from rich.logging import RichHandler
from rich.progress import track
from pathlib import Path
from cpcrCode import getData, saveData, generateDictionary
from neuromaps import transforms

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
@click.option("-n", "--name", default="debug", help="Which experiment to run.")

def main(
    data_dir : str = "inputs", output_dir : str = "outputs", name : str = "debug"
) :
    data_dir = Path(data_dir).resolve()
    output_dir = Path(output_dir).resolve()
    if not output_dir.os.exists():
        output_dir.mkdir()
    pass


    maps = getData(data_dir).getMaps()
    keys = []
    fsLR_tuples = []
    #fsL_maps = []
    #fsR_maps = []
    for map in maps :
        transform = transforms.min152_to_fslr(map, '32k')
        fsLR_tuples.append(transform)
        #fsL_maps.append(transform[0].agg_data())
        #fsR_maps.append(transform[1].agg_data())
    
    dict = generateDictionary(keys, fsLR_tuples).generate()
    saver = saveData("fsLR32k_receptorMapDictionary")
    saver.save(dict, output_dir)


if __name__ == "__main()__" :
    main()