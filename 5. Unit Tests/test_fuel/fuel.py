# Refueling

"""
In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:

    convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
    gauge expects an int and returns a str that is:
        "E" if that int is less than or equal to 1,
        "F" if that int is greater than or equal to 99,
        and "Z%" otherwise, wherein Z is that same int.

def main():
    ...


def convert(fraction):
    ...


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()

Then, in a file called test_fuel.py, implement two or more functions that collectively test your implementations of convert and gauge thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_fuel.py

Hints

    Be sure to include

    import fuel

    or

    from fuel import convert, gauge

    atop test_fuel.py so that you can call convert and gauge in your tests.
    Take care to return, not print, an int in convert and a str in gauge. Only main should call print.
    Note that you can raise an exception like ValueError with code like:

    raise ValueError

    Note that you can check with pytest whether a function has raised an exception, per docs.pytest.org/en/latest/how-to/assert.html#assertions-about-expected-exceptions.
"""

def main():
    frac = input("Fraction: ")
    per = convert(frac)
    gau = gauge(per)
    print(gau)


def convert(fraction):
    x, y = fraction.split("/")
    try:
        x, y = int(x), int(y)
    except ValueError:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError

    return round((x/y)*100)


def gauge(percentage):
    if percentage >= 99 and percentage <= 100:
        return 'F'
    elif percentage <= 1 and percentage >= 0:
        return 'E'
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
