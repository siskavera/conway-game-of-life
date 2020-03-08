# Modeling homework
## Solutions

#### What possible attractors are there in this system?

There are two main types of attractors in finite-state systems: fixed points and cycles.
A fixed point is a state mapped to itself, while a cycle is a finite number of states that
are visited in a sequence.
In this system, both of these appear.

The attractors also differ in terms of the number of cells alive. There is a trivial fixed point
where all cells are dead.

#### Which attractor is most likely to manifest if we initialize the system randomly?
In this system, the most likely attractor was the state where all cells are dead. In a trial run
with 10.000 simulations with random initial states (state for each cell chosen uniformly at random),
about 64% ended up in this state.


#### Is there an initial condition which produces a state after the 100 billionth iteration of the simulation, that is not part of any attractor?
No. 

The number of possible states for a 6x6 grid with binary states is `2^(6*6)=68719476736`,
just above 68 billion. Therefore, the system must have visited a state at least twice after 100 billion
steps. Since Conway's Game of Life is a Markov process (the next state only depends on the current one),
this would mean that the sequence of states after the second visit of a state are exactly the same as
after the first one. Thus the system will keep iterating the states between these two visits,
which by definiton means that it reached an attractor.