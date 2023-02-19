# program that removes all vowels from a string
# prompt the user for a string
# use a for loop to iterate through the string
# if the character is a vowel, replace it with an empty character
# print the string without vowels

def main():
    string = input("Input: ")
    string = remove_vowels(string)
    print(string)


def remove_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    for char in string:
        if char in vowels:
            string = string.replace(char, "")
    return string


if __name__ == "__main__":
    main()
