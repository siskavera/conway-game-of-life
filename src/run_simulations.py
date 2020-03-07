import argparse
import datetime
import os
import pathlib
import uuid
import warnings

import numpy
import pandas
from tqdm import tqdm

from src.cellular_automata.cellular_automata import CellularAutomata, AttractorNotFoundError

DATA_DIR = pathlib.Path(os.path.realpath(__file__)).parent.parent.joinpath("data")


def run_simulations(automata_size, n_simulations, data_folder):
    automata = CellularAutomata(shape=(automata_size, automata_size))
    periods = []
    steps_to_reachs = []
    n_cells_alive = []

    for i in tqdm(range(n_simulations)):
        simulation_dir = pathlib.Path(data_folder).joinpath(str(i))
        simulation_dir.mkdir()

        automata.reset_state()
        initial_state = automata.state
        initial_state_file_name = simulation_dir.joinpath("initial_state")
        numpy.save(initial_state_file_name, initial_state)

        try:
            automata.run_until_attractor_found(n_max_steps=200)
        except AttractorNotFoundError as err:
            warnings.warn(str(err))
            continue

        periods.append(automata.attractor_period)
        steps_to_reachs.append(automata.attractor_found_after)
        mean_cells_alive = numpy.sum(numpy.mean(automata.attractor, axis=0))
        n_cells_alive.append(mean_cells_alive)

    results = pandas.DataFrame({"period": periods,
                                "steps_to_reach": steps_to_reachs,
                                "n_cells_alive": n_cells_alive})
    results.to_csv(os.path.join(data_folder, "summary.csv"))


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

    date_today = datetime.date.today().strftime("%y-%m-%d")
    data_folder = pathlib.Path(DATA_DIR).joinpath(date_today).joinpath(args.simulation_name)
    data_folder.mkdir(parents=True)

    run_simulations(args.automata_size, args.n_simulations, data_folder)