"""
implement a function called convert that accepts a str as input and returns that same input as emoji
implement a function called main that prompts the user for input, calls convert on that input, and prints the result
"""


def convert(string):
    new_string = string.replace(":)", "🙂")
    new_string = new_string.replace(":(", "🙁")
    return new_string


def main():
    string = input("Input: ")
    result = convert(string)
    print(result)


if __name__ == "__main__":
    main()
