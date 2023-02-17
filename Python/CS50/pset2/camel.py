# implement a program that prompts the user
# for the name of a variable in camel case
# output the corresponding name in snake case

import re


def main():
    camel = input("camelCase: ")
    snake = split_camel(camel)
    lower_snake = [word.lower() for word in snake]
    print((lower_snake[0]) + "_" + (lower_snake[1]))


def split_camel(string):
    words = re.findall(r'[a-z]+|[A-Z][a-z]*', string)
    return words


if __name__ == "__main__":
    main()
