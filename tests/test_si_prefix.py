from units.si import prefix
import pytest


def prefix_id(pref):
    if isinstance(pref, prefix.Prefix):
        return pref.name


@pytest.mark.parametrize(
    "pref,exp",
    (
        (prefix.yotta, 24),
        (prefix.zetta, 21),
        (prefix.exa, 18),
        (prefix.peta, 15),
        (prefix.tera, 12),
        (prefix.giga, 9),
        (prefix.mega, 6),
        (prefix.kilo, 3),
        (prefix.hecto, 2),
        (prefix.deca, 1),
        (prefix.none, 0),
        (prefix.deci, -1),
        (prefix.milli, -3),
        (prefix.centi, -2),
        (prefix.micro, -6),
        (prefix.nano, -9),
        (prefix.pico, -12),
        (prefix.atto, -18),
        (prefix.femto, -15),
        (prefix.zepto, -21),
        (prefix.yocto, -24),
    ),
    ids=prefix_id,
)
def test_prefix_mul(pref, exp):
    assert pref * 1 == pow(10, exp)


@pytest.mark.parametrize(
    "pref,exp",
    (
        (prefix.yotta, 24),
        (prefix.zetta, 21),
        (prefix.exa, 18),
        (prefix.peta, 15),
        (prefix.tera, 12),
        (prefix.giga, 9),
        (prefix.mega, 6),
        (prefix.kilo, 3),
        (prefix.hecto, 2),
        (prefix.deca, 1),
        (prefix.none, 0),
        (prefix.deci, -1),
        (prefix.milli, -3),
        (prefix.centi, -2),
        (prefix.micro, -6),
        (prefix.nano, -9),
        (prefix.pico, -12),
        (prefix.atto, -18),
        (prefix.femto, -15),
        (prefix.zepto, -21),
        (prefix.yocto, -24),
    ),
    ids=prefix_id,
)
def test_prefix_float_cast(pref, exp):
    assert float(pref) == float(pow(10, exp))

