import numpy

from src.conway import get_next_state
from src.attractor_helpers import get_max_period, get_attractor_and_period, has_duplicated_states

N_MAX_STEPS = 5


def find_attractor(state):
    max_period = get_max_period(state)
    saved_states = numpy.array([state])

    for i in range(N_MAX_STEPS):
        print("")
        print("LOOP")
        print(state)
        print(saved_states)

        state = get_next_state(state)

        saved_states = numpy.concatenate([saved_states,
                                          numpy.reshape(state, (1, state.shape[0], state.shape[1]))],
                                         axis=0)

        if saved_states.shape[2] == max_period:
            saved_states = numpy.delete(saved_states, 0, 2)

        if has_duplicated_states(saved_states):
            return get_attractor_and_period(saved_states)
