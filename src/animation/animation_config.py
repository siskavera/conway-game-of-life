UPDATE_MENUS = [{
    'type': 'buttons',
    "x": 0.2,
    "xanchor": "right",
    "y": 0,
    "yanchor": "top",
    "pad": {"r": 10, "t": 40},
    "direction": "left",
    'buttons': [
        {
            'label': 'Play',
            'method': 'animate',
            'args': [None, {"fromcurrent": True}]
        },
        {
            'label': 'Pause',
            'method': 'animate',
            'args': [[None], {"frame": {"duration": 0, "redraw": False},
                              "mode": "immediate",
                              "transition": {"duration": 0}}]
        }
    ],
}]
PLOT_LAYOUT = {
    "title": {
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top",
        "pad": {"r": 10, "t": 87},
    },
    "font": {
        "family": "Courier New, monospace",
        "size": 14,
        "color": "#7f7f7f"
    },
    "width": 800,
    "height": 800,
    'updatemenus': UPDATE_MENUS
}