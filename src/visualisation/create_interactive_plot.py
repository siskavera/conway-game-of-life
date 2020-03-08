import numpy
import plotly.graph_objs as go

from src.visualisation.animation_config import PLOT_LAYOUT


def get_title(i_step, attractor_found):
    title = "Conway's Game of Life<br>"
    title += "Step {}".format(i_step)
    if attractor_found:
        title += ", System reached attractor"

    return title


def create_interactive_plot(automata, n_steps, output_path):
    x = numpy.arange(automata.state.shape[0])
    y = numpy.arange(automata.state.shape[1])

    data = [go.Heatmap(x=x, y=y, z=automata.state, showscale=False,
                       colorscale=[(0, "dimgrey"), (1, "gainsboro")],
                       zmin=0, zmax=1)]
    frames = [
        {
            "data": [{
                "z": state,
                "type": "heatmap",
            }],
            "layout": {
                "title": get_title(i, automata.attractor is not None)
            }
        } for i, state in enumerate(automata.evolve_and_check_for_attractor(n_steps))
    ]

    fig = go.Figure(data=data,
                     frames=frames,
                     layout=PLOT_LAYOUT)
    fig.write_html(output_path)
