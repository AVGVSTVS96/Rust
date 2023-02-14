"""
# implement a program that prompts the user for a greeting.
# If the greeting starts with “hello”, output $0.
# If the greeting starts with an “h” (but not “hello”), output $20.
# Otherwise, output $100. Ignore any leading whitespace in the users greeting,
#   and treat the users greeting case-insensitively.
"""

greeting = input("Greeting: ")
greeting.strip().lower()
if greeting.startswith("hello") is True:
    print("$0")
elif greeting.startswith("h") is True:
    print("$20")
else:
    print("$100")
