import logging

import numpy

from src.animation.create_animation import create_animation
from src.cellular_automata.cellular_automata import CellularAutomata


logging.basicConfig(level=logging.INFO)


def generate_movie(path_to_initial_state):
    logging.info("Loading initial state from %s" % path_to_initial_state)
    initial_state = numpy.load(path_to_initial_state)
    automata = CellularAutomata(initial_state=initial_state)

    fig = create_animation(initial_state, automata, 10)
    fig.write_html("fig.html", auto_open=True)


if __name__ == "__main__":
    file_name = "../data/2020-03-07/turbine/initial_states/initial_state_0.npy"
    generate_movie(file_name)

