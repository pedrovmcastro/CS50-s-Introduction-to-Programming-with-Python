from twttr import shorten

def test_lowercase():
    assert shorten('twitter') == 'twttr'

def test_uppercase():
    assert shorten('TWITTER') == 'TWTTR'

def test_numbers():
    assert shorten('tw1tt3r') == 'tw1tt3r'

def test_punctuation():
    assert shorten('twitter.com') == 'twttr.cm'

