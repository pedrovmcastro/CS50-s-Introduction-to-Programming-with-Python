from um import count

def test_beginning_of_sentence():
    assert count("Um, thanks") == 1


def test_middle_of_sentence():
    assert count("hello, um, world") == 1


def test_end_of_sentence():
    assert count("thanks, um") == 1


def test_single_um():
    assert count("Um") == 1


def test_middle_of_word():
    assert count("Um, thanks for the album, um") == 2

