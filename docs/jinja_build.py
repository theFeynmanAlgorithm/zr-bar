from staticjinja import Site
from pathlib import Path
from yaml import load, FullLoader

_DATA_FOLDER = "data"

def load_folder(path: Path):
    drinks = []
    drink_paths = sorted(path.glob('*.yaml'))
    for file in drink_paths:
        with open(file) as drink_file:
            drinks.append(load(drink_file, Loader=FullLoader))

    return drinks

if __name__ == '__main__':
    drink_context = {
        'classics': load_folder(Path(_DATA_FOLDER)/'classics'),
        'guest_favorites': load_folder(Path(_DATA_FOLDER)/'guest_favorites'),
        'zack_picks': load_folder(Path(_DATA_FOLDER)/'zack_picks'),
        'shots': load_folder(Path(_DATA_FOLDER)/'shots'),
    }
    site = Site.make_site(contexts=[('index.html', drink_context)])
    site.render(use_reloader=True)