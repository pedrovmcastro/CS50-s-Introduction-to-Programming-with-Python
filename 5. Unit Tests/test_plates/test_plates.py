from plates import is_valid


def test_smaller_length():
    assert is_valid("A") == False


def test_bigger_length():
    assert is_valid("AAAAAAA") == False


def test_start_with_letters():
    assert is_valid("50") == False


def test_punctuation():
    assert is_valid("CS.50") == False


def test_first_number():
    assert is_valid("CS05") == False


def test_middle_numbers():
    assert is_valid("AAA50AA") == False


def test_correct_plate():
    assert is_valid("CS50") == True
