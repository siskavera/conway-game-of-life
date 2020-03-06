import numpy
from src.conway import get_n_neighbours, get_next_state


def test_get_n_neighbours():
    # given
    test_state = numpy.array([[0, 1, 0, 0, 0],
                              [0, 1, 1, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 1, 1, 0, 0],
                              [1, 1, 1, 0, 0]])
    expected_n_neighbours = numpy.array([[4, 5, 5, 2, 1],
                                         [3, 3, 3, 1, 0],
                                         [3, 4, 5, 2, 0],
                                         [4, 5, 4, 2, 1],
                                         [3, 5, 4, 2, 1]])

    # when
    n_neighbours = get_n_neighbours(test_state)

    # then
    numpy.testing.assert_array_equal(expected_n_neighbours, n_neighbours)


def test_get_next_state():
    # given
    test_state = numpy.array([[0, 1, 0, 0, 0],
                              [0, 1, 1, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 1, 1, 0, 0],
                              [1, 1, 1, 0, 0]])

    expected_next_state = numpy.array([[0, 0, 0, 0, 0],
                                       [1, 1, 1, 0, 0],
                                       [1, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0],
                                       [1, 0, 0, 0, 0]])

    # when
    next_state = get_next_state(test_state)
    print(next_state)

    # then
    numpy.testing.assert_array_equal(expected_next_state, next_state)

