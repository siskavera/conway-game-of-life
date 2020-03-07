import logging
import pathlib

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import seaborn as sns

from src.cellular_automata.cellular_automata import CellularAutomata


logging.basicConfig(level=logging.INFO)


def generate_movie(path_to_initial_state):
    logging.info("Loading initial state from %s" % path_to_initial_state)
    initial_state = np.load(path_to_initial_state)
    file_name = pathlib.Path(path_to_initial_state).stem
    output_path = pathlib.Path(path_to_initial_state).parent.parent.joinpath("plots").joinpath("{}.mp4".format(file_name))
    output_path.parent.mkdir(exist_ok=True)

    automata = CellularAutomata(initial_state=initial_state)
    time_series = [state for state in automata.evolve_simple(20)]

    fig = plt.figure()
    sns.heatmap(time_series[0], vmax=.8, square=True, cbar=False)

    def init():
        sns.heatmap(time_series[0], vmax=.8, square=True, cbar=False)

    def animate(i):
        data = time_series[i]
        sns.heatmap(data, vmax=.8, square=True, cbar=False)

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=20, repeat = False)

    logging.info("Saving video to %s" % output_path)
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=2, metadata=dict(artist='Me'), bitrate=1800)
    anim.save(output_path, writer=writer)


if __name__ == "__main__":
    file_name = "../data/2020-03-07/turbine/initial_states/initial_state_0.npy"
    generate_movie(file_name)

