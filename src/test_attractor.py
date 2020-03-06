import numpy
import pytest

from src.attractor import get_max_period, find_attractor, has_duplicated_states





def test_find_attractor():
    test_state = numpy.zeros(3)

    find_attractor(test_state)


