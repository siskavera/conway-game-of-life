import logging
import pathlib

import numpy as np

from src.cellular_automata.cellular_automata import CellularAutomata
from src.visualisation.create_movie import create_movie

logging.basicConfig(level=logging.INFO)


def generate_movie(path_to_initial_state):
    logging.info("Loading initial state from %s" % path_to_initial_state)
    initial_state = np.load(path_to_initial_state)

    file_name = pathlib.Path(path_to_initial_state).stem
    output_path = pathlib.Path(path_to_initial_state).parent.parent.joinpath("plots").joinpath("{}.mp4".format(file_name))
    output_path.parent.mkdir(exist_ok=True)

    automata = CellularAutomata(initial_state=initial_state)
    create_movie(automata, 10, output_path)


if __name__ == "__main__":
    file_name = "../data/2020-03-07/turbine/initial_states/initial_state_0.npy"
    generate_movie(file_name)

