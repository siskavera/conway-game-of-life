UPDATE_MENUS = [{
    "type": "buttons",
    "x": 0.25,
    "xanchor": "right",
    "y": 0,
    "yanchor": "top",
    "pad": {"r": 10, "t": 60},
    "direction": "left",
    "buttons": [
        {
            "label": "Play",
            "method": "animate",
            "args": [None, {"frame": {"duration": 500},
                            "fromcurrent": True, "transition": {"duration": 300,
                                                                "easing": "quadratic-in-out"}}]
        },
        {
            "label": "Pause",
            "method": "animate",
            "args": [[None], {"frame": {"duration": 0},
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
    "updatemenus": UPDATE_MENUS
}
SLIDERS = {
    "active": 0,
    "yanchor": "top",
    "xanchor": "left",
    "currentvalue": {
        "font": {"size": 20},
        "prefix": "#step:",
        "visible": True,
        "xanchor": "right"
    },
    "transition": {"duration": 300, "easing": "cubic-in-out"},
    "pad": {"b": 10, "t": 30},
    "len": 0.7,
    "x": 0.3,
    "y": 0,
    "steps": []
}