import datetime
import os
import pathlib
import uuid

import numpy
import pandas

from src.cellular_automata.cellular_automata import CellularAutomata

DATA_DIR = pathlib.Path(os.path.realpath(__file__)).parent.parent.joinpath("data")


def run_simulations(automata_size, n_simulations, data_folder):
    automata = CellularAutomata(shape=(automata_size, automata_size))
    periods = []
    steps_to_reachs = []
    n_cells_alive = []

    for i in range(n_simulations):
        simulation_dir = pathlib.Path(data_folder).joinpath(str(i))
        simulation_dir.mkdir()

        automata.reset_state()
        initial_state = automata.state
        initial_state_file_name = simulation_dir.joinpath("initial_state")
        numpy.save(initial_state_file_name, initial_state)

        automata.run_until_attractor_found(n_max_steps=200)

        periods.append(automata.attractor_period)
        steps_to_reachs.append(automata.attractor_found_after)
        mean_cells_alive = numpy.sum(numpy.mean(automata.attractor, axis=0))
        n_cells_alive.append(mean_cells_alive)

    results = pandas.DataFrame({"period": periods,
                                "steps_to_reach": steps_to_reachs,
                                "n_cells_alive": n_cells_alive})
    results.to_csv(os.path.join(data_folder, "summary.csv"))


if __name__ == "__main__":
    automata_size = 6
    n_simulations = 10

    simulation_id = str(uuid.uuid4())
    date_today = datetime.date.today().strftime("%y-%m-%d")
    data_folder = pathlib.Path(DATA_DIR).joinpath(date_today).joinpath(simulation_id)
    data_folder.mkdir(parents=True)

    run_simulations(automata_size, n_simulations, data_folder)