from solution import Doors


def test_toogle():
    d = Doors(1)
    assert d._closed == {1, }
    assert d._open == set()
    d._toogle(1)
    assert d._closed == set()
    assert d._open == {1, }
