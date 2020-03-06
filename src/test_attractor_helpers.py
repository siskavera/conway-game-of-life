import numpy
import pytest

from src.attractor_helpers import get_max_period, has_duplicated_states, get_attractor_and_period


def test_get_max_period():
    test_state = numpy.zeros([2, 3])

    assert 6 == get_max_period(test_state)


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
    assert duplicated == has_duplicated_states(test_saved_states)

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
    attractor, period = get_attractor_and_period(test_saved_states)

    numpy.testing.assert_array_equal(expected_attractor, attractor)
    assert expected_period == period
