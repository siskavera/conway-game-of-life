import numpy
from unittest.mock import patch, MagicMock

import pytest

from src import cellular_automata


class TestInit():
    def test_no_arguments(self):
        with pytest.raises(ValueError):
            cellular_automata.CellularAutomata()

    def test_shape_only(self):
        test_ca = cellular_automata.CellularAutomata(shape=(2,3))

        assert (2,3) == test_ca.state.shape
        assert set(numpy.unique(test_ca.state)).issubset({0,1})

    def test_initial_state(self):
        initial_state = numpy.random.randint(2, size=(3, 3))

        test_ca = cellular_automata.CellularAutomata(initial_state=initial_state)

        assert (3, 3) == test_ca.state.shape
        numpy.testing.assert_array_equal(initial_state, test_ca.state)

    def test_state_and_initial_state(self):
        initial_state = numpy.random.randint(2, size=(3, 3))

        test_ca = cellular_automata.CellularAutomata(initial_state=initial_state, shape=(5,6))

        assert (3, 3) == test_ca.state.shape
        numpy.testing.assert_array_equal(initial_state, test_ca.state)


@patch.object(cellular_automata, "get_next_state", MagicMock(return_value=numpy.zeros([2, 3])))
def test_find_attractor():
    test_ca = cellular_automata.CellularAutomata((2, 3))
    test_state = numpy.zeros([2, 3])

    expected_attractor = numpy.zeros([1, 2, 3])
    expected_period = 1

    attractor, period = test_ca.find_attractor(test_state)

    numpy.testing.assert_array_equal(attractor, expected_attractor)
    assert period == expected_period


def test_get_max_period():
    test_ca = cellular_automata.CellularAutomata((2, 2))

    assert test_ca.max_period == 16

