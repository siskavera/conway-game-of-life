import numpy

def get_attractor_and_period(saved_states):
    last_state = saved_states[-1, :, :]

    i = -1  # TODO Throw if no duplicate
    for i in range(saved_states.shape[0]):
        if numpy.array_equal(last_state, saved_states[i, :, :]):
            break

    attractor = saved_states[i+1:, :, :]
    period = attractor.shape[0]

    return attractor, period

def has_duplicated_states(saved_states):
    n_saved = saved_states.shape[0]
    n_unique = numpy.unique(saved_states, axis=0).shape[0]

    return n_saved != n_unique