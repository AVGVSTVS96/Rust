"""
Allow user to place order
Prompt for one item per line
After each input, print sum total of inputs so far
Input should be case insensitive, menu items Titlecased
When user inputs control-d, stop taking input
Read control-d with EOFerror exception
"""

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
