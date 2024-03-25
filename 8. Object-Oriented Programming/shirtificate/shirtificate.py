# CS50 Shirtificate

"""
Suppose that you’d like to implement a CS50 “shirtificate,” a PDF with an image of an I took CS50 t-shirt, shirtificate.png, customized with a user’s own name.

In a file called shirtificate.py, implement a program that prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar to this one for John Harvard, with these specifications:

    The orientation of the PDF should be Portrait.
    The format of the PDF should be A4, which is 210mm wide by 297mm tall.
    The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
    The shirt’s image should be centered horizontally.
    The user’s name should be on top of the shirt, in white text.

All other details we leave to you. You’re even welcome to add borders, colors, and lines. Your shirtificate needn’t match John Harvard’s precisely. And no need to wrap long names across multiple lines.

Before writing any code, do read through fpdf2’s tutorial to learn how to use it. Then skim fpdf2’s API (application programming interface) to see all of its functions and parameters therefor.

No need to submit any PDFs with your code. But, if you would like, you’re welcome (but not expected) to share a shirtificate with your name on it in any of CS50’s communities!
"""

from fpdf import FPDF

name = input("Name: ")

# Creating a pdf object:
pdf = FPDF()
pdf.add_page()

# Creating the header:
pdf.set_font("helvetica", size=48)
pdf.cell(0, 20, new_x="LMARGIN", new_y="NEXT")
pdf.cell(text="CS50 Shirtificate", center=True)
pdf.cell(0, 40, new_x="LMARGIN", new_y="NEXT")

# Placing the shirt and the phrase:
pdf.set_font("helvetica", size=24)
pdf.set_text_color(255, 255, 255)
pdf.image("shirtificate.png", w=190, h=190)
pdf.set_xy(0, 132)
pdf.cell(text= f"{name} took CS50", center=True)
pdf.output("shirtificate.pdf")
