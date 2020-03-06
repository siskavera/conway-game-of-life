import numpy
import pytest

from src.attractor_helpers import get_max_period, has_duplicated_states


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