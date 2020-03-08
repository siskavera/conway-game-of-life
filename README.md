# Conway's Game of Life

This project simulates Conway's Game of Life and explores its possible attractors.

## Structure
Simulation code is under `src` and exploratory notebooks are under `notebooks`.

## Getting Started

### Prerequisites
* Python 3.5+
* pip
* virtualenv (alternatively Conda, pipenv, ...)

Tested with Python 3.7 under Ubuntu 18.04

### Setting up virtual environment
There are two alternatives:
1. Run `set_env.sh`
2. Manually
    1. Create a new virtual environment using your preferred tool
    2. Install packages in `requirements.txt` in your enviroment

### Notebooks
There are two alternatives to run Jupyter lab:
1. Run `start_jupyter_lab.sh`
2. Manually
    1. Activate your virtual environment
    2. Run jupyter lab (`jupyter lab`), with the project root to its path

There are two notebooks:
1. `Attractors.ipynb`: Simplistic analysis of generated simulations
2. `SimpleVisualisation.pynb`: Simple visualisation of a single simulation, with self-actualising plots.

### Running simulations with random initial conditions
The script `src/run_simulations.py` can run an arbitrary number of simulations with random
initial conditions (each cell initialised uniformly at random). The script requires that the
project root is in the Python path (e.g. `PYTHONPATH="./" python src/run_simulations.py ...` 
from a Linux terminal).

The program takes the following command line arguments:
* `-d`/`-data_dir`: Directory to save the data to. Obligatory.
* `-a`/`--automata_size`: Size of the automata state (square grid). Default: 6
* `-n`/`--n_simulations`: Number of simulations to run. Default: 100

The program generates the following outputs:
```
data_dir
+-- summary.csv
+-- initial_states
|   +-- initial_state_0.npy
|   +-- initial_state_1.npy
|   +-- ...
+-- interactive_plot
+-- movie
```
`summary.csv`: Summary table of the attractors found:
* Length of period
* Number of steps it took to reach the attractor
* Number of cells alive in the attractor (for cyclic attractors, averaged over the whole cycle)

`initial_states`: All initial states are stored as numpy arrays here.

`interactive_plot`: Folder for future interactive plots generated for chosen runs.

`movie`: Folder for future movies generated for chosen runs.

### Run and visualise single simulation
The script `src/run_single_simulation.py` can generate visualisations for initial states from a
simulation or custom defined initial states. The script requires that the project root is in the 
Python path (e.g. `PYTHONPATH="./" python src/run_single_simulation.py.py ...`  from a Linux terminal).

The program takes the following command line arguments:
* `-d`/`-data_dir`: Directory of the simulation.
* `-r`/`-run_id`: ID of the run in the simulation. Default: 1
* `-i`/`-initial_state_path`: Path to a custom initial state.
* `-n`/`--n_steps`: Number of steps to run. Default: 30
* `-m`/`--movie`: Generate movie (mp4). Default: `False`
* `-p`/`--interactive_plot`: Generate interactive plot (html). Default: `False`

 At least one of `data_dir` and `initial_state_path` needs to be provided. `data_dir` takes precedence.
 
 In case `data_dir` is provided, the visualisation will be saved in the corresponding subfolder
 (`video` or `interactive-plot`). In case `initial_state_path` is provided, it will be saved in the
 same folder.