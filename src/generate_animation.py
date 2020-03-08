import logging

import numpy

from src.visualisation.create_animation import create_animation
from src.cellular_automata.cellular_automata import CellularAutomata


logging.basicConfig(level=logging.INFO)


def generate_visualisation(path_to_initial_state):
    logging.info("Loading initial state from %s" % path_to_initial_state)
    initial_state = numpy.load(path_to_initial_state)
    automata = CellularAutomata(initial_state=initial_state)

    create_animation(automata, 10, output_path)


if __name__ == "__main__":
    file_name = "../data/2020-03-07/turbine/initial_states/initial_state_0.npy"
    generate_visualisation(output_path)

