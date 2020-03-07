import warnings

import numpy

from src.conway.conway import get_next_state
from src.cellular_automata.saved_state_helpers import has_duplicated_states, get_attractor_and_period_from_saved_states


class CellularAutomata():
    def __init__(self, shape=None, initial_state=None):
        if initial_state is not None and shape is not None:
            if shape != initial_state.shape:
                warnings.warn("Shape provided %s does not match shape of initial state provided %s."
                              "Provided shape will be ignored."
                              % (shape, initial_state.shape))

        if initial_state is not None:
            self.state = initial_state
        elif shape is not None:
            self._initialize_random(shape)
        else:
            raise ValueError("Provide either shape or initial state to Cellular Automata")

        self.max_period = 2**(self.state.shape[0]*self.state.shape[1])
        self.rule = get_next_state
        self.attractor = None
        self.attractor_period = None
        self.attractor_found_after = None

    def reset_state(self, state=None):
        self.attractor = None
        self.attractor_period = None
        self.attractor_found_after = None

        if state is None:
            self._initialize_random(self.state.shape)
        else:
            self.state = state

    def _initialize_random(self, shape):
        self.state = numpy.random.randint(2, size=shape)

    def evolve_and_check_for_attractor(self, n_max_steps, stop_when_attractor_found=False):
        max_period = self.max_period
        saved_states = numpy.array([self.state])
        i = 0

        for i in range(n_max_steps):
            yield self.state
            self.state = self.rule(self.state)

            saved_states = numpy.concatenate([saved_states,
                                              numpy.reshape(self.state, (1, self.state.shape[0], self.state.shape[1]))],
                                             axis=0)

            # On a grid of 6, we'd run into memory problems before we get here, but still :)
            if saved_states.shape[2] == max_period:
                saved_states = numpy.delete(saved_states, 0, 2)

            if has_duplicated_states(saved_states):
                attractor, period = get_attractor_and_period_from_saved_states(saved_states)
                self.attractor = attractor
                self.attractor_period = period
                self.attractor_found_after = i

                if stop_when_attractor_found:
                    return
                else:
                    break

        for state in self.evolve_simple(n_max_steps-i):
            yield state

    def run_until_attractor_found(self, n_max_steps=100):
        for _ in self.evolve_and_check_for_attractor(n_max_steps, True):
            pass

    def evolve_simple(self, n_max_steps):
        for i in range(n_max_steps):
            yield self.state
            self.state = self.rule(self.state)
