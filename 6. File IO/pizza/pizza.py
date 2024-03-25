# Pizza Py

"""
Perhaps the most popular place for pizza in Harvard Square is Pinocchio’s Pizza & Subs, aka Noch’s, known for its Sicilian pizza, which is “a deep-dish or thick-crust pizza.”

Students tend to buy pizza by the slice, but Pinocchio’s also has whole pizzas on its menu too, per this CSV file of Sicilian pizzas, sicilian.csv, below:

Sicilian Pizza,Small,Large
Cheese,$25.50,$39.95
1 item,$27.50,$41.95
2 items,$29.50,$43.95
3 items,$31.50,$45.95
Special,$33.50,$47.95

See regular.csv for a CSV file of regular pizzas as well.

Of course, a CSV file isn’t the most customer-friendly format to look at. Prettier might be a table, formatted as ASCII art, like this one:

+------------------+---------+---------+
| Sicilian Pizza   | Small   | Large   |
+==================+=========+=========+
| Cheese           | $25.50  | $39.95  |
+------------------+---------+---------+
| 1 item           | $27.50  | $41.95  |
+------------------+---------+---------+
| 2 items          | $29.50  | $43.95  |
+------------------+---------+---------+
| 3 items          | $31.50  | $45.95  |
+------------------+---------+---------+
| Special          | $33.50  | $47.95  |
+------------------+---------+---------+

In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist, the program should instead exit via sys.exit.
Hints

    Recall that the csv module comes with quite a few methods, per docs.python.org/3/library/csv.html, among which are reader, per docs.python.org/3/library/csv.html#csv.reader, and DictReader, per docs.python.org/3/library/csv.html#csv.DictReader.
    Note that open can raise a FileNotFoundError, per docs.python.org/3/library/exceptions.html#FileNotFoundError.
    Note that the tabulate package comes with just one function, per pypi.org/project/tabulate. You can install the package with:

    pip install tabulate
"""

import sys
import csv
from tabulate import tabulate

# Testing the command-line arguments:
if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

# Testing if the file exists:
try:
    with open(sys.argv[1]) as file:
        pass
except FileNotFoundError:
    sys.exit("File does not exist")

table = []

# Reading the csv file:
with open(sys.argv[1]) as file:
    reader = csv.reader(file)
    for row in reader:
        table.append([row[0], row[1], row[2]])

# Creating the table with tabulate
print(tabulate(table, headers="firstrow", tablefmt="grid"))
