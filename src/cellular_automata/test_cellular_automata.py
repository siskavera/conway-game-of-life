import numpy
from unittest.mock import patch

import pytest

from src.cellular_automata import cellular_automata


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


@patch.object(cellular_automata, "get_next_state")
class TestGetAttractor():
    def test_fixed_point(self, mock_get_next_state):
        test_state = numpy.zeros([2, 3])
        test_ca = cellular_automata.CellularAutomata(initial_state=test_state)
        mock_get_next_state.return_value = numpy.zeros([2, 3])

        expected_attractor = numpy.zeros([1, 2, 3])
        expected_period = 1

        test_ca.run_until_attractor_found()

        numpy.testing.assert_array_equal(test_ca.attractor, expected_attractor)
        assert test_ca.attractor_period == expected_period

    def test_attractor_cycle(self, mock_get_next_state):
        test_ca = cellular_automata.CellularAutomata(initial_state=numpy.zeros([2, 2]))
        mock_get_next_state.side_effect = [
            numpy.array([[0, 1], [1, 1]]),
            numpy.array([[1, 1], [1, 1]]),
            numpy.array([[0, 1], [0, 1]]),
            numpy.array([[0, 1], [1, 1]])
        ]

        expected_attractor = numpy.array([
            [[1, 1], [1, 1]],
            [[0, 1], [0, 1]],
            [[0, 1], [1, 1]],
        ])
        expected_period = 3

        test_ca.run_until_attractor_found()

        numpy.testing.assert_array_equal(test_ca.attractor, expected_attractor)
        assert test_ca.attractor_period == expected_period


@patch.object(cellular_automata, "get_next_state")
def test_evolve_simple(mock_get_next_state):
    expected_states = [
        numpy.array([[0, 1], [1, 1]]),
        numpy.array([[1, 1], [1, 1]]),
        numpy.array([[0, 1], [0, 1]]),
        numpy.array([[0, 1], [1, 1]])
    ]

    test_ca = cellular_automata.CellularAutomata(initial_state=expected_states[0])
    mock_get_next_state.side_effect = expected_states[1:]

    for i, state in enumerate(test_ca.evolve_simple(3)):
        numpy.testing.assert_array_equal(expected_states[i], state)


@patch.object(cellular_automata, "get_next_state")
def test_evolve_and_check_for_attractor(mock_get_next_state):
    expected_states = [
        numpy.array([[0, 1], [1, 1]]),
        numpy.array([[1, 1], [1, 1]]),
        numpy.array([[0, 1], [0, 1]]),
        numpy.array([[0, 1], [1, 1]]),
        numpy.array([[1, 1], [1, 1]]),
        numpy.array([[0, 1], [0, 1]]),
        numpy.array([[0, 1], [1, 1]]),
        numpy.array([[1, 1], [1, 1]]),
        numpy.array([[0, 1], [0, 1]]),
        numpy.array([[0, 1], [1, 1]]),
    ]
    expected_attractor = numpy.array([
        [[1, 1], [1, 1]],
        [[0, 1], [0, 1]],
        [[0, 1], [1, 1]],
    ])
    expected_period = 3

    test_ca = cellular_automata.CellularAutomata(initial_state=expected_states[0])
    mock_get_next_state.side_effect = expected_states[1:]

    for i, state in enumerate(test_ca.evolve_and_check_for_attractor(8)):
        numpy.testing.assert_array_equal(expected_states[i], state)

    numpy.testing.assert_array_equal(test_ca.attractor, expected_attractor)
    assert test_ca.attractor_period == expected_period
    assert test_ca.attractor_found_after == 2


def test_get_max_period():
    test_ca = cellular_automata.CellularAutomata((2, 2))

    assert test_ca.max_period == 16

