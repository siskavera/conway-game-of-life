import argparse
import logging
import pathlib

import numpy
import numpy as np

from src.cellular_automata.cellular_automaton import CellularAutomaton
from src.data_dir import INITIAL_STATES, VISUALISATION_TYPE_EXTENSION_MAP, MOVIE, INTERACTIVE_PLOT
from src.visualisation.create_interactive_plot import create_interactive_plot
from src.visualisation.create_movie import create_movie

logging.basicConfig(level=logging.INFO)


def get_initial_state_path(data_dir, run_id):
    return pathlib.Path(data_dir).joinpath(INITIAL_STATES).joinpath("initial_state_{}.npy".format(run_id))


def get_output_path(data_dir, run_id, visualisation_type):
    if visualisation_type not in VISUALISATION_TYPE_EXTENSION_MAP.keys():
        raise ValueError("Invalid visualisation type {}. "
                         "Valid values are movie or interactive_plot".format(visualisation_type))

    dir = pathlib.Path(data_dir).joinpath(visualisation_type)
    output_path = dir.joinpath("{}_{}{}".format(visualisation_type, run_id, VISUALISATION_TYPE_EXTENSION_MAP[visualisation_type]))
    return str(output_path)


def get_visualisation_creator(visualisation_type):
    if visualisation_type == MOVIE:
        return create_movie
    elif visualisation_type == INTERACTIVE_PLOT:
        return create_interactive_plot


def generate_visualisation(initial_state_path, output_path, visualisation_type, n_steps):
    visualise = get_visualisation_creator(visualisation_type)

    logging.info("Loading initial state from %s" % initial_state_path)
    try:
        initial_state = np.load(initial_state_path)
    except ValueError:
        try:
            initial_state = numpy.loadtxt(initial_state_path)
        except ValueError:
            try:
                initial_state = numpy.loadtxt(initial_state_path, delimiter=",")
            except ValueError:
                logging.error("Invalid input file %s provided. Only binary files in Numpy format and"
                              "space or comma-separated text files are supported." % initial_state_path)
                raise

    automaton = CellularAutomaton(initial_state=initial_state)
    logging.info("Creating %s and saving it to %s" % (visualisation_type, output_path))
    if visualisation_type == MOVIE:
        visualise(automaton, n_steps, output_path)
    elif visualisation_type == INTERACTIVE_PLOT:
        visualise(automaton, n_steps, output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Cellular Automata simulations.")
    parser.add_argument("-d", "--data_dir", type=str,
                        help="data directory")
    parser.add_argument("-r", "--run_id", type=int,
                        help="ID of the run within a simulation")
    parser.add_argument("-i", "--initial_state_path", type=str,
                        help="Path to a custom initial state")
    parser.add_argument("-t", "--visualisation_type", type=str,
                        help="visualisation type: movie or interactive_plot")
    parser.add_argument("-n", "--n_steps", type=int,
                        help="number of steps to visualise")

    parser.set_defaults(run_id=1, visualisation_type="interactive_plot", n_steps=30)
    args = parser.parse_args()

    if (args.data_dir and args.run_id):
        initial_state_path = get_initial_state_path(args.data_dir, args.run_id)
        output_path = get_output_path(args.data_dir, args.run_id, args.visualisation_type)
    elif (args.initial_state_path):
        initial_state_path = args.initial_state_path
        output_path = pathlib.Path(initial_state_path).with_suffix(VISUALISATION_TYPE_EXTENSION_MAP[args.visualisation_type])
        output_path = str(output_path)
    else:
        raise Exception("Either initial_state_path or data_dir and run_id needs to be defined.")

    generate_visualisation(initial_state_path, output_path, args.visualisation_type, args.n_steps)
