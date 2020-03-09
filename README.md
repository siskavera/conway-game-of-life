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
    2. Run jupyter lab (`jupyter lab`), with the `src` folder added to its path
    (e.g. `PYTHONPATH=$(pwd)/src jupyter lab` when run from project root)

There are two notebooks:
1. `Attractors.ipynb`: Simplistic analysis of generated simulations
2. `SimpleVisualisation.ipynb`: Simple visualisation of a single simulation, with self-actualising plots.

### Running simulations with random initial conditions
The script `src/run_simulations.py` can run an arbitrary number of simulations with random
initial conditions (each cell initialised uniformly at random).

The program takes the following command line arguments:
* `-d`/`--data_dir`: Directory to save the data to. Obligatory.
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

 #### Execution
 1. Activate your virtual environment e.g. `source venv/bin/activate`
 2. Execute the script. e.g. `python src/run_simulations.py -d data/sample_run -n 100`

### Run and visualise single simulation
The script `src/run_single_simulation.py` can generate visualisations for initial states from a
simulation or custom defined initial states.

The program takes the following command line arguments:
* `-d`/`--data_dir`: Directory of the simulation.
* `-r`/`--run_id`: ID of the run in the simulation. Default: 1
* `-i`/`--initial_state_path`: Path to a custom initial state.
* `-n`/`--n_steps`: Number of steps to run. Default: 30
* `-m`/`--movie`: Generate movie (mp4). Default: `False`
* `-p`/`--interactive_plot`: Generate interactive plot (html). Default: `False`

 At least one of `data_dir` and `initial_state_path` needs to be provided. `data_dir` takes precedence.
 
 In case `data_dir` is provided, the visualisation will be saved in the corresponding subfolder
 (`video` or `interactive-plot`). In case `initial_state_path` is provided, it will be saved in the
 same folder.
 
 #### Execution
 1. Activate your virtual environment e.g. `source venv/bin/activate`
 2. Execute the script. e.g. `python src/run_single_simulation.py -d data/sample_run -p  -n 50`
 
 ### Run test suite
 1. Activate your virtual environment. e.g. `source venv/bin/activate`
 2. Change to `src`
 3. Execute all tests: `python -m pytest`
 
 *Note: Only the core components (cellular automata and evolution rule for Conway's Game of Life)
 are covered with unit tests.*