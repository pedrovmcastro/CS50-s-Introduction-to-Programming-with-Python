# Working 9 to 5

"""
https://www.youtube.com/watch?v=UbxUSsFXYo4

Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock. Accordingly, instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”), wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post meridiem”, wherein “meridiem” means midday (i.e., noon).
Conversion Table

In a file called working.py, implement a function called convert that expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

    9:00 AM to 5:00 PM
    9 AM to 5 PM

Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    ...


...


if __name__ == "__main__":
    main()

Either before or after you implement convert in working.py, additionally implement, in a file called test_working.py, three or more functions that collectively test your implementation of convert thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_working.py

"""

import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    """
    Convert a time range from 12-hour format to 24-hour format.

    The input should be in one of the following formats:
    - "09:00 AM to 05:00 PM"
    - "9 AM to 5 PM"

    :param s: A string representing the time range.
    :return: A string representing the time range in 24-hour format (e.g., "09:00 to 17:00").
    :raises ValueError: If the input string does not match the expected format or if the time values are invalid.
    """
    if matches := re.search(r"^(\d\d?)(?::(\d\d))? (A|P)M to (\d\d?)(?::(\d\d))? (A|P)M$", s):
        # Unpack the groups in the pattern:
        hour1, min1, period1, hour2, min2, period2 = matches.groups()

        # Convert the hours and minutes from str to int:
        hour1, hour2 = int(hour1), int(hour2)
        if min1:
            min1 = int(min1)
        else:
            min1 = 0
        if min2:
            min2 = int(min2)
        else:
            min2 = 0

        # Check if the time values are valid:
        if hour1 > 12 or hour2 > 12 or hour1 == 0 or hour2 == 0 or min1 > 59 or min2 > 59:
            raise ValueError

        # Check the period and convert the hours to 24-hour format:
        if period1 == "P":
            if hour1 != 12:
                hour1 += 12
        else:
            if hour1 == 12:
                hour1 = 0
        if period2 == "P":
            if hour2 != 12:
                hour2 += 12
        else:
            if hour2 == 12:
                hour2 = 0

        # Return the time range in the new format:
        return f"{hour1:02}:{min1:02} to {hour2:02}:{min2:02}"

    # Raise ValueError if the input string doesn't match the expected format:
    else:
        raise ValueError


if __name__ == "__main__":
    main()
