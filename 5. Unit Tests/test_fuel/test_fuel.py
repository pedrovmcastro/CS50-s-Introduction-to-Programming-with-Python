import pytest
from fuel import convert, gauge


def test_3_quarters():
    assert gauge(convert('3/4')) == '75%'


def test_1_quarter():
    assert gauge(convert('1/4')) == '25%'


def test_4_quarters():
    assert gauge(convert('4/4')) == 'F'


def test_0_quarters():
    assert gauge(convert('0/4')) == 'E'


def test_denominator_zero():
    with pytest.raises(ZeroDivisionError):
        gauge(convert('4/0'))


def test_str():
    with pytest.raises(ValueError):
        gauge(convert('three/four'))


def test_float():
     with pytest.raises(ValueError):
        gauge(convert('1.5/four'))


def test_x_greater_than_y():
     with pytest.raises(ValueError):
        gauge(convert('5/4'))


def test_1_100():
    assert gauge(convert('1/100')) == 'E'


def test_99_100():
    assert gauge(convert('99/100')) == 'F'
