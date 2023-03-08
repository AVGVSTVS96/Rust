"""
TODO Implement a program that prompts the user for items, one per line, until the user inputs control-d
TODO Then output the user’s grocery list in all uppercase, sorted alphabetically by item
TODO Prefix each line with the number of times the user inputted that item. No need to pluralize the items.
TODO Treat the user’s input case-insensitively.
"""

# prompt for input
items_count = {}
while True:
    try:
        item = input()
    except EOFError:
        break
    else:
        item = item.lower()
        if item in items_count:
            items_count[item] += 1
        else:
            items_count[item] = 1

for item in sorted(items_count.keys()):
    count = items_count[item]
    print(f"{count} {item.upper()}")
