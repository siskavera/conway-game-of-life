import numpy


def get_max_period(state):
    n, m = state.shape
    return n*m


def has_duplicated_states(saved_states):
    n_saved = saved_states.shape[0]
    n_unique = numpy.unique(saved_states, axis=0).shape[0]

    return n_saved != n_unique


def get_attractor_and_period(saved_states):
    return [[[]]], 0