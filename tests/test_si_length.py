from units.si import (
    length,
)
import pytest


@pytest.mark.parametrize(
    "unit,expected", (
        (length.Ym, 1e24),
        (length.Zm, 1e21),
        (length.Em, 1e18),
        (length.Pm, 1e15),
        (length.Tm, 1e12),
        (length.Gm, 1e9),
        (length.Mm, 1e6),
        (length.km, 1e3),
        (length.hm, 1e2),
        (length.dam, 10.0),
        (length.dm, 1e-1),
        (length.cm, 1e-2),
        (length.mm, 1e-3),
        (length.um, 1e-6),
        (length.nm, 1e-9),
        (length.pm, 1e-12),
        (length.fm, 1e-15),
        (length.am, 1e-18),
        (length.zm, 1e-21),
        (length.ym, 1e-24),
    )
)
def test_predefined_metre(unit, expected):
    assert unit.value == expected

