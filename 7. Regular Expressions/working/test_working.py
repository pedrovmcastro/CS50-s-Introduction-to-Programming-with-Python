import pytest
from working import convert


def test_valid_input_1_format_am_to_pm():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_valid_input_2_format_am_to_pm():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_valid_input_3_format_pm_to_am():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"


def test_valid_input_4_format_am_to_am():
    assert convert("12:30 AM to 8:50 AM") == "00:30 to 08:50"


def test_invalid_str_format_1():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60")


def test_invalid_str_format_2():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")


def test_invalid_str_format_3():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00")


def test_invalid_values():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
