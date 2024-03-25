# Re-requesting a Vanity Plate

"""
https://www.youtube.com/watch?v=mQZmCJUSC6g

In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it does not, but main is only called if the value of __name__ is "__main__":

def main():
    ...


def is_valid(s):
    ...


if __name__ == "__main__":
    main()

Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_plates.py

Hints

    Be sure to include

    import plates

    or

    from plates import is_valid

    atop test_plates.py so that you can call is_valid in your tests.
    Take care to return, not print, a bool in is_valid. Only main should call print.

"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check the maximum and minimum length
    if len(s) < 2 or len(s) > 6:
        return False

    # Check if it starts with two letter
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Check that there are no periods, spaces, or punctuation marks
    for char in s:
        if not char.isalnum():
            return False

    # Check if the first number is non-zero
    first_num = 1
    for char in s:
        if char.isdigit():
            first_num = int(char)
            break
    if first_num == 0:
        return False

    # Check that there are no numbers in the middle of the plate
    num = False
    for char in s:
        if char.isdigit():
            num = True
        if char.isalpha() and num:
            return False
    return True


if __name__ == "__main__":
    main()
