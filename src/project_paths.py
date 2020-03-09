import os
import pathlib
import uuid

PROJECT_ROOT = pathlib.Path(os.path.realpath(__file__)).parent
DATA_DIR = PROJECT_ROOT.parent.joinpath("data")
INITIAL_STATES = "initial_states"
MOVIE = "movie"
INTERACTIVE_PLOT = "interactive_plot"
VISUALISATION_TYPE_EXTENSION_MAP = {
    MOVIE: ".mp4",
    INTERACTIVE_PLOT: ".html"
}


def get_default_data_dir():
    return pathlib.Path(DATA_DIR).joinpath(str(uuid.uuid4()))


def ensure_data_dir_and_subdirs(data_dir):
    data_dir.mkdir(parents=True, exist_ok=True)

    data_dir.joinpath(INITIAL_STATES).mkdir(exist_ok=True)
    for visualisation_type in VISUALISATION_TYPE_EXTENSION_MAP.keys():
        data_dir.joinpath(visualisation_type).mkdir(exist_ok=True)
        data_dir.joinpath(visualisation_type).mkdir(exist_ok=True)
