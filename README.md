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

### Running notebooks
There are two alternatives:
1. Run `start_jupyter_lab.sh`
2. Manually
    1. Activate your virtual environment
    2. Run jupyter lab (`jupyter lab`), with the project root to its path

### Running simulations
`PYTHONPATH="./" python src/run_simulations.py `