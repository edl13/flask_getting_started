import pytest


def test_dist():
    from server import getDis

    a = [0, 1]
    b = [3.5, -9.9]

    dis = getDis(a, b)
    assert dis == pytest.approx(9.56347217)
