import argparse
import logging
import pathlib

import numpy as np

from src.cellular_automata.cellular_automaton import CellularAutomaton
from src.data_dir import INITIAL_STATES, VISUALISATION_TYPE_EXTENSION_MAP, MOVIE, INTERACTIVE_PLOT
from src.visualisation.create_interactive_plot import create_interactive_plot
from src.visualisation.create_movie import create_movie

logging.basicConfig(level=logging.INFO)


def get_path_to_initial_state(data_dir, run_id):
    return pathlib.Path(data_dir).joinpath(INITIAL_STATES).joinpath("initial_state_{}.npy".format(run_id))


def get_output_path(data_dir, run_id, visualisation_type):
    if visualisation_type not in VISUALISATION_TYPE_EXTENSION_MAP.keys():
        raise ValueError("Invalid visualisation type {}. "
                         "Valid values are movie or interactive_plot".format(visualisation_type))

    dir = pathlib.Path(data_dir).joinpath(visualisation_type)
    output_path = dir.joinpath("{}_{}.{}".format(visualisation_type, run_id, VISUALISATION_TYPE_EXTENSION_MAP[visualisation_type]))
    return str(output_path)


def get_visualisation_creator(visualisation_type):
    if visualisation_type == MOVIE:
        return create_movie
    elif visualisation_type == INTERACTIVE_PLOT:
        return create_interactive_plot


def generate_visualisation(data_dir, run_id, visualisation_type, n_steps):
    path_to_initial_state = get_path_to_initial_state(data_dir, run_id)
    output_path = get_output_path(data_dir, run_id, visualisation_type)
    visualisation_creator = get_visualisation_creator(visualisation_type)

    logging.info("Loading initial state from %s" % path_to_initial_state)
    initial_state = np.load(path_to_initial_state)

    automaton = CellularAutomaton(initial_state=initial_state)
    if visualisation_type == MOVIE:
        visualisation_creator(automaton, n_steps, output_path)
    elif visualisation_type == INTERACTIVE_PLOT:
        visualisation_creator(automaton, n_steps, output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Cellular Automata simulations.")
    parser.add_argument("-d", "--data_dir", type=str,
                        help="data directory")
    parser.add_argument("-r", "--run_id", type=int,
                        help="ID of the run within a simulation")
    parser.add_argument("-t", "--visualisation_type", type=str,
                        help="visualisation type: movie or interactive_plot")
    parser.add_argument("-n", "--n_steps", type=int,
                        help="number of steps to visualise")

    parser.set_defaults(run_id=1, visualisation_type="interactive_plot", n_steps=30)
    args = parser.parse_args()

    generate_visualisation(args.data_dir, args.run_id, args.visualisation_type, args.n_steps)
