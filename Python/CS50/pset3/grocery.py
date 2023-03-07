"""
TODO Implement a program that prompts the user for items, one per line, until the user inputs control-d
TODO Then output the user’s grocery list in all uppercase, sorted alphabetically by item
TODO Prefix each line with the number of times the user inputted that item. No need to pluralize the items.
TODO Treat the user’s input case-insensitively.
"""

# prompt for input
items = ""
while True:
    try:
        items = input().upper()
    except EOFError:
        break

# print all uppercase
for item in items:
    print("")
