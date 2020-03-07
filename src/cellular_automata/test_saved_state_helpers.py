import numpy
import pytest

from src.cellular_automata.saved_state_helpers import has_duplicated_states, get_attractor_and_period_from_saved_states


@pytest.mark.parametrize(
    "test_saved_states,duplicated",
    [
        (numpy.array([
            [[1, 0], [1, 0]],
            [[1, 0], [0, 0]],
            [[1, 0], [1, 0]]
        ]), True),
        (numpy.array([
            [[1, 0], [1, 0]],
            [[1, 0], [0, 0]],
            [[0, 0], [1, 0]]
        ]), False)
    ]
)
def test_has_duplicated_states_duplicated(test_saved_states, duplicated):
    assert has_duplicated_states(test_saved_states) == duplicated


@pytest.mark.parametrize(
    "test_saved_states,expected_attractor,expected_period",
    [
        (numpy.array([
            [[0, 0], [0, 0]],
            [[1, 0], [0, 0]],
            [[1, 0], [1, 0]],
            [[1, 0], [0, 0]],
            [[1, 0], [1, 0]]
        ]),
         numpy.array([
             [[1, 0], [0, 0]],
             [[1, 0], [1, 0]]
         ]), 2),
    ]
)
def test_get_attractor_and_period(test_saved_states, expected_attractor, expected_period):
    attractor, period = get_attractor_and_period_from_saved_states(test_saved_states)

    numpy.testing.assert_array_equal(expected_attractor, attractor)
    assert expected_period == period