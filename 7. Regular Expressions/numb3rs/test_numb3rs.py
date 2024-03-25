from numb3rs import validate

def test_valid_ip():
    assert validate("127.0.0.1") == True

def test_valid_ip_255():
    assert validate("255.255.255.255") == True

def test_invalid_ip_greater():
    assert validate("512.512.512.512") == False

def test_invalid_ip_one_greater():
    assert validate("1.2.3.1000") == False

def test_invalid_ip_one_right():
    assert validate("255.256.256.256") == False

def test_invalid_ip_str():
    assert validate("cat") == False

def test_invalid_ip_first():
    assert validate("256.255.255.255") == False

def test_invalid_ip_less():
    assert validate("8.8.8") == False

def test_invalid_ip_more():
    assert validate("10.10.10.10.10") == False

def test_invalid_ip_letters():
    assert validate("2001:0db8:85a3:000") == False
