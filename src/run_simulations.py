import argparse
import logging
import os
import uuid
import warnings

import numpy
import pandas
from tqdm import tqdm

from src.cellular_automata.cellular_automaton import CellularAutomaton, AttractorNotFoundError
from src.data_dir import get_data_dir, INITIAL_STATES, ensure_data_dir_and_subdirs

logging.basicConfig(level=logging.INFO)


def run_simulations(automata_size, n_simulations, simulation_name):
    data_dir = get_data_dir(simulation_name)
    ensure_data_dir_and_subdirs(simulation_name)

    logging.info("Running {n} simulations on a {a}x{a} grid.".format(n=args.n_simulations, a=args.automata_size))
    logging.info("Results will be saved under {data_folder}.".format(data_folder=data_dir))

    automata = CellularAutomaton(shape=(automata_size, automata_size))
    periods = []
    steps_to_reachs = []
    n_cells_alive = []
    n_not_reached_attractor = 0

    for i in tqdm(range(n_simulations)):
        automata.reset_state()

        initial_state = automata.state
        initial_state_file_name = data_dir.joinpath(INITIAL_STATES).joinpath("initial_state_{}".format(i))
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
    parser.add_argument("-a", "--automata_size", type=int,
                        help="size of the automata state (a square grid)")
    parser.add_argument("-n", "--n-_imulations", type=int,
                        help="number of simulations run")
    parser.add_argument("-s", "--simulation_name", type=str,
                        help="name of simulation, determines data dir")

    parser.set_defaults(automata_size=6, n_simulations=100, simulation_name = str(uuid.uuid4()))
    args = parser.parse_args()

    run_simulations(args.automata_size, args.n_simulations, args.simulation_name)
