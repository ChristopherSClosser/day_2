"""TDD."""


import pytest


P_TABLE = [
    (0, 0, 1), (1, 0, 2), (2, 0, 3), (3, 0, 4),
    (0, 1, 2), (1, 1, 3), (2, 1, 4), (4, 1, 6),
]


def test_foo():
    assert 1 == 1


@pytest.mark.parametrize('m, n, result', P_TABLE)
def test_acker_0_0(m, n, result):
    from acker import ack
    assert ack(0, 0) == None
