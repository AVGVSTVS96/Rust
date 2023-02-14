"""
implement a program that prompts the user
for the answer to the Great Question of Life,
the Universe and Everything

output Yes if the user inputs 42 or (case-insensitively)
forty-two or forty two. Otherwise output No.
"""

answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
if answer.lower() == "forty-two" or answer.lower() == "forty two" or answer == "42":
    print("Yes")
else:
    print("No")
    