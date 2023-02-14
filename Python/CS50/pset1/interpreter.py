"""
implement a program that prompts the user for an arithmetic expression and
then calculates and outputs the result as a floating-point value formatted
to one decimal place
users input will be formatted as x y z, with one space between x and y
and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
"""

expression = input("Expression: ")
words = expression.split()

if words[1] == "+":
    print(int(words[0]) + int(words[2]))

elif words[1] == "-":
    print(int(words[0]) - int(words[2]))

elif words[1] == "*":
    print(int(words[0]) * int(words[2]))

elif words[1] == "/":
    print(int(words[0]) / int(words[2]))
