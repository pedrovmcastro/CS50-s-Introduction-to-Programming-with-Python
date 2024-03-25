import pytest
from seasons import get_date, life_minutes, num_to_words


def test_get_date_valid_format():
    assert get_date("2022-02-16") == ('2022', '02', '16')

def test_get_date_invalid_format():
    with pytest.raises(SystemExit, match="Invalid date"):
        get_date("invalid_date")

def test_life_minutes():
    assert life_minutes(2022, 2, 16) == 1051200

def test_num_to_words():
    assert num_to_words(1051200) == "One million, fifty-one thousand, two hundred"

