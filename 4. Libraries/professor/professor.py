# Little Professor

"""
One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math problems for David to solve. For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. If the toy were to display 4 + 1 = , David would (hopefully) answer with 5. If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

In a file called professor.py, implement a program that:

    Prompts the user for a level, 

. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with

    digits. No need to support operations other than addition (+).
    Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
    The program should ultimately output the user’s score: the number of correct answers out of 10.

Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

import random


def main():
    ...


def get_level():
    ...


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()

Hints

    Note that you can raise an exception like ValueError with code like:

    raise ValueError

    Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html.

"""

import random


def main():
    level = get_level()
    score = 0

    # External loop for the 10 questions
    for _ in range(10):
        n1, n2 = generate_integer(level), generate_integer(level)
        ans = n1 + n2

        # Inner loop for the 3 attempts
        correct = False
        for i in range(3):
            user_ans = input(f'{n1} + {n2} = ')
            try:
                user_ans = int(user_ans)
            except ValueError:
                pass
            if ans != user_ans:
                print('EEE')
            else:
                correct = True  # Indicative boolean variable
                break

        if not correct:
            print(f'{n1} + {n2} = {ans}')
        else:
            score += 1

    print(f'Score: {score}')


def get_level():
    while True:
        try:
            n = int(input('Level: '))
            if n < 1 or n > 3:
                raise ValueError
        except ValueError:
            pass
        else:
            return n


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
