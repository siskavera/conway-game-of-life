# Modeling homework

## Task
Your task is to create and analyze [Game of Life](https://en.wikipedia.org/wiki/Conway's_Game_of_Life) simulations on a 6x6 grid. 
The grid is folded to a toroid shape, so the squares on the top edge are neighboring 
the squares on the bottom edge and the squares on the left edge are neighboring the squares on the right. 

An attractor is either a state of the system that persists indefinitely or a sequence of states 
that is repeated in the same order indefinitely.

The program you write should be able to:
* run a simulation with a user defined starting condition
* display the results of the simulation
* determine if the simulation has reached an attractor

Run simulations and analyze their results to answer the following questions:
* What possible attractors are there in this system?
* Which attractor is most likely to manifest if we initialize the system randomly?
* Is there an initial condition which produces a state after the 100 billionth iteration of the simulation, that is not part of any attractor?
