import numpy


def get_n_neighbours(state):
    n_neighbours = numpy.roll(state, 1, axis=0)
    n_neighbours = n_neighbours + numpy.roll(state, 1, axis=1)
    n_neighbours = n_neighbours + numpy.roll(state, -1, axis=0)
    n_neighbours = n_neighbours + numpy.roll(state, -1, axis=1)

    return n_neighbours


def survives(previous_state, n_neighbours):
    if previous_state and (n_neighbours == 2 or n_neighbours == 3):
        return True
    if not previous_state and n_neighbours == 3:
        return True
    return False


def get_next_state(state):
    n_neighbours = get_n_neighbours(state)

    new_state = [1 if survives(previous_state, n_neighbours) else 0
                 for previous_state, n_neighbours
                 in zip(state.flatten(), n_neighbours.flatten())]
    new_state = numpy.reshape(new_state, state.shape)
    return new_state
