import argparse
import datetime
import logging
import os
import pathlib
import uuid
import warnings

import numpy
import pandas
from tqdm import tqdm

from src.cellular_automata.cellular_automata import CellularAutomata, AttractorNotFoundError

logging.basicConfig(level=logging.INFO)

DATA_DIR = pathlib.Path(os.path.realpath(__file__)).parent.parent.joinpath("data")
INITIAL_STATES_SUBDIR = "initial_states"


def get_data_dir(simulation_name):
    date_today = datetime.date.today().strftime("%Y-%m-%d")
    data_dir = pathlib.Path(DATA_DIR).joinpath(date_today).joinpath(simulation_name)
    data_dir.mkdir(parents=True)
    data_dir.joinpath(INITIAL_STATES_SUBDIR).mkdir()

    return data_dir


def run_simulations(automata_size, n_simulations, simulation_name):
    data_dir = get_data_dir(simulation_name)
    logging.info("Running {n} simulations on a {a}x{a} grid.".format(n=args.n_simulations, a=args.automata_size))
    logging.info("Results will be saved under {data_folder}.".format(data_folder=data_dir))

    automata = CellularAutomata(shape=(automata_size, automata_size))
    periods = []
    steps_to_reachs = []
    n_cells_alive = []
    n_not_reached_attractor = 0

    for i in tqdm(range(n_simulations)):
        automata.reset_state()

        initial_state = automata.state
        initial_state_file_name = data_dir.joinpath(INITIAL_STATES_SUBDIR).joinpath("initial_state_{}".format(i))
        numpy.save(initial_state_file_name, initial_state)

        try:
            automata.run_until_attractor_found(n_max_steps=200)
        except AttractorNotFoundError as err:
            warnings.warn(str(err))
            n_not_reached_attractor += 1
            continue

        periods.append(automata.attractor_period)
        steps_to_reachs.append(automata.attractor_found_after)
        mean_cells_alive = numpy.sum(numpy.mean(automata.attractor, axis=0))
        n_cells_alive.append(mean_cells_alive)

    results = pandas.DataFrame({"period": periods,
                                "steps_to_reach": steps_to_reachs,
                                "n_cells_alive": n_cells_alive})
    results.to_csv(os.path.join(data_dir, "summary.csv"))

    logging.info("Simulations finished.")
    if n_not_reached_attractor == 0:
        logging.info("All simulations reached an attractor \U0001F973")
    else:
        logging.warning("{} simulations did not reach an attractor.".format(n_not_reached_attractor))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Cellular Automata simulations.")
    parser.add_argument("-a", "--automata-size", type=int,
                        help="size of the automata state (a square grid)")
    parser.add_argument("-n", "--n_simulations", type=int,
                        help="number of simulations run")
    parser.add_argument("-s", "--simulation_name", type=str,
                        help="name of simulation, helped to determine data dir for results")

    parser.set_defaults(automata_size=6, n_simulations=100, simulation_name = str(uuid.uuid4()))
    args = parser.parse_args()

    run_simulations(args.automata_size, args.n_simulations, args.simulation_name)
