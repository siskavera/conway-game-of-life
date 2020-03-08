import logging

import seaborn as sns
from matplotlib import pyplot as plt, animation


def create_movie(automata, n_steps, output_path):
    time_series = [state for state in automata.evolve_simple(n_steps)]
    fig = plt.figure()
    sns.heatmap(time_series[0], vmax=.8, square=True, cbar=False)

    def init():
        sns.heatmap(time_series[0], vmax=.8, square=True, cbar=False)

    def animate(i):
        data = time_series[i]
        sns.heatmap(data, vmax=.8, square=True, cbar=False)

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=20, repeat=False)
    logging.info("Saving video to %s" % output_path)
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=2, metadata=dict(artist='Me'), bitrate=1800)
    anim.save(output_path, writer=writer)