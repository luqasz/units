from units import si
import pytest


def test_unit_str():
    m = si.AbstractUnit(15.0, 'g')
    assert str(m) == '1.5 dag'


def test_unit_add():
    assert si.AbstractUnit(1, 'm') + si.AbstractUnit(1000, 'm') == si.AbstractUnit(1001, 'm')


def test_unit_lt():
    assert si.AbstractUnit(1, 'm') < si.AbstractUnit(1001, 'm')


def test_unit_gt():
    assert si.AbstractUnit(10, 'm') > si.AbstractUnit(1, 'm')


def test_unit_sub():
    assert si.AbstractUnit(10, 'm') - si.AbstractUnit(1, 'm') == si.AbstractUnit(9, 'm')


def test_unit_mul():
    assert si.AbstractUnit(10, 'm') * 100 == si.AbstractUnit(1000, 'm')


def test_unit_eq():
    assert si.AbstractUnit(10, 'm') == si.AbstractUnit(10, 'm')


def test_unit_ne():
    assert si.AbstractUnit(1, 'm') != si.AbstractUnit(10, 'm')


def test_unit_float():
    assert float(si.AbstractUnit(1, 'm')) == 1.0


def test_unit_is_hashable():
    assert hash(si.AbstractUnit(10, 'm'))

