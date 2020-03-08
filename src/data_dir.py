import os
import pathlib


DATA_DIR = pathlib.Path(os.path.realpath(__file__)).parent.parent.joinpath("data")
INITIAL_STATES = "initial_states"
MOVIE = "movie"
INTERACTIVE_PLOT = "interactive_plot"
VISUALISATION_TYPE_EXTENSION_MAP = {
    MOVIE: "mp4",
    INTERACTIVE_PLOT: "html"
}


def get_data_dir(simulation_name):
    data_dir = pathlib.Path(DATA_DIR).joinpath(simulation_name)

    return data_dir


def ensure_data_dir_and_subdirs(simulation_name):
    data_dir = get_data_dir(simulation_name)

    data_dir.mkdir(parents=True, exist_ok=True)

    data_dir.joinpath(INITIAL_STATES).mkdir(exist_ok=True)
    for visualisation_type in VISUALISATION_TYPE_EXTENSION_MAP.keys():
        data_dir.joinpath(visualisation_type).mkdir(exist_ok=True)
        data_dir.joinpath(visualisation_type).mkdir(exist_ok=True)
