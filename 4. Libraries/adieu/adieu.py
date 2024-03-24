# Adieu, Adieu

"""
https://www.youtube.com/watch?v=Qy9_lfjQopU&t=4s

In The Sound of Music, there’s a song sung largely in English, So Long, Farewell, with these lyrics, wherein “adieu” means “goodbye” in French:

    Adieu, adieu, to yieu and yieu and yieu

Of course, the line isn’t grammatically correct, since it would typically be written (with an Oxford comma) as:

    Adieu, adieu, to yieu, yieu, and yieu

To be fair, “yieu” isn’t even a word; it just rhymes with “you”!

In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and
names with

commas and one and, as in the below:

    Adieu, adieu, to Liesl
    Adieu, adieu, to Liesl and Friedrich
    Adieu, adieu, to Liesl, Friedrich, and Louisa
    Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

Hints

    Note that the inflect module comes with quite a few methods, per pypi.org/project/inflect. You can install it with:

    pip install inflect
"""

names = []
while True:
    try:
        name = input('Name: ')
    except EOFError:
        break
    names.append(name)

print('Adieu, adieu, to ', end='')
if len(names) == 1:
    print(names[0])
elif len(names) == 2:
    print(f'{names[0]} and {names[1]}')
else:
    for name in names[:-1]:
        print(f'{name}, ', end='')
    print(f'and {names[-1]}')
    