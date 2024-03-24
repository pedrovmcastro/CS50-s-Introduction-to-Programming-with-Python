# Guessing Game

"""
I’m thinking of a number between 1 and 100…
What is it?

In a file called game.py, implement a program that:

    Prompts the user for a level, 

. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and

    , inclusive, using the random module.
    Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
        If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
        If the guess is larger than that integer, the program should output Too large! and prompt the user again.
        If the guess is the same as that integer, the program should output Just right! and exit.

Hints

    Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html.
"""

from random import randint

def get_int(prompt):
    while True:
        try:
            return int(input(f'{prompt}: '))
        except ValueError:
            pass

lv, guess = get_int('Level'), get_int('Guess')
num = randint(1, lv)

while guess != num:
    if guess > num:
        print('Too large!')
        guess = get_int('Guess')
    elif guess < num or guess < 1:
        print('Too small!')
        guess = get_int('Guess')

print('Just Right!')
