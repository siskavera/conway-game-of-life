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
logging.getLogger('matplotlib.animation').setLevel(logging.WARNING)  # This package is very verbose


def get_initial_state_path(data_dir, run_id):
    return pathlib.Path(data_dir).joinpath(INITIAL_STATES).joinpath("initial_state_{}.npy".format(run_id))


def get_output_path_for_simulated_input(data_dir, run_id, visualisation_type):
    dir = pathlib.Path(data_dir).joinpath(visualisation_type)
    output_path = dir.joinpath("{}_{}".format(visualisation_type, run_id)).with_suffix(
        VISUALISATION_TYPE_EXTENSION_MAP[visualisation_type])
    return str(output_path)


def get_output_path_for_custom_input(initial_state_path, visualisation_type):
    output_path = pathlib.Path(initial_state_path).with_suffix(VISUALISATION_TYPE_EXTENSION_MAP[visualisation_type])
    return str(output_path)


def run_single_simulation(initial_state_path, n_steps, movie_path, interactive_plot_path):
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
    automaton.run_until_attractor_found(n_steps)
    if automaton.attractor is not None:
        prop_cells_alive = numpy.sum(numpy.mean(automaton.attractor, axis=0)) / (
                automaton.attractor.shape[1] * automaton.attractor.shape[2])
        logging.info("Attractor found after {} steps, with periodicity {} and {} live cells on average".format(
            automaton.attractor_found_after, automaton.attractor_period, prop_cells_alive))

    if movie_path:
        logging.info("Creating %s and saving it to %s" % (MOVIE, movie_path))
        automaton.reset_state(initial_state)
        create_movie(automaton, n_steps, movie_path)

    if interactive_plot_path:
        logging.info("Creating %s and saving it to %s" % (INTERACTIVE_PLOT, interactive_plot_path))
        automaton.reset_state(initial_state)
        create_interactive_plot(automaton, n_steps, interactive_plot_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Cellular Automata simulations.")
    parser.add_argument("-d", "--data_dir", type=str,
                        help="data directory")
    parser.add_argument("-r", "--run_id", type=int,
                        help="ID of the run within a simulation")
    parser.add_argument("-i", "--initial_state_path", type=str,
                        help="Path to a custom initial state")
    parser.add_argument("-m", "--movie", action='store_true',
                        help="generate movie")
    parser.add_argument("-p", "--interactive_plot", action='store_true',
                        help="generate interactive plot")
    parser.add_argument("-n", "--n_steps", type=int,
                        help="number of steps to visualise")

    parser.set_defaults(run_id=1, visualisation_type="interactive_plot", n_steps=30)
    args = parser.parse_args()

    movie_path = None
    interactive_plot_path = None

    if (args.data_dir and args.run_id):
        initial_state_path = get_initial_state_path(args.data_dir, args.run_id)
        if args.movie:
            movie_path = get_output_path_for_simulated_input(args.data_dir, args.run_id, MOVIE)
        if args.interactive_plot:
            interactive_plot_path = get_output_path_for_simulated_input(args.data_dir, args.run_id, INTERACTIVE_PLOT)
    elif (args.initial_state_path):
        initial_state_path = args.initial_state_path
        if args.movie:
            movie_path = get_output_path_for_custom_input(args.initial_state_path, MOVIE)
        if args.interactive_plot:
            interactive_plot_path = get_output_path_for_custom_input(args.initial_state_path, INTERACTIVE_PLOT)
    else:
        raise Exception("Either initial_state_path or data_dir and run_id needs to be defined.")

    run_single_simulation(initial_state_path, args.n_steps, movie_path, interactive_plot_path)
