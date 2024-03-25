import pytest
from jar import Jar

def test_init():
    with pytest.raises(ValueError, match="Invalid capacity"):
        print(Jar(-1))
    jar = Jar(10)
    assert jar.capacity == 10 and jar.size == 0
    jar = Jar()
    assert jar.capacity == 12 and jar.size == 0
    jar.deposit(5)
    assert jar.capacity == 12 and jar.size == 5
    jar.withdraw(3)
    assert jar.capacity == 12 and jar.size == 2


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(10)
    assert jar.size == 11
    with pytest.raises(ValueError, match="Exceeds capacity"):
        jar.deposit(10)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5
    jar.withdraw(4)
    assert jar.size == 1
    with pytest.raises(ValueError, match="Not enough cookies"):
        jar.withdraw(10)

