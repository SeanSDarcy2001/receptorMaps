import logging
import click
from rich.logging import RichHandler
from rich.progress import track
from pathlib import Path
from receptorMaps import getData

FORMAT = "%(message)s"
logging.basicConfig(
    level="INFO",
    format=FORMAT,
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

log = logging.getLogger("friedBrains")

@click.command()
@click.option("-d", "--data-dir", default="data", help="Where the data is.")
@click.option("-o", "--output_dir", default="outputs", help="Where to store outputs.")
@click.option("-n", "--name", default="debug", help="Which experiment to run.")

def main(
    data_dir : str = "data", output_dir : str = "outputs", name : str = "debug"
) :
    data_dir = Path(data_dir).resolve()
    output_dir = Path(output_dir).resolve()
    if not output_dir.exists():
        output_dir.mkdir()
    pass


    maps = getData.load(data_dir / f"Problem4-BodyA.txt")

if __name__ == "__main()__" :
    main()