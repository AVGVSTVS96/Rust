"""Program prompts user for vanity plate and
   outputs "Valid" these requirements are met:
    # String must begin with 2 letters
    # Minimum 2 characters, maximum 6
    # Numbers must only come at the end
    # No periods, spaces or punctuation
"""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[:2].isalpha():
        return False
    if not s.isalnum():
        return False
    has_letters = any(c.isalpha() for c in s)
    has_digits = any(c.isdigit() for c in s)
    if has_digits and has_letters:
        if s[-2:].isdigit() and s[-2] != "0":
            return True
        else:
            return False
    elif has_digits:
        return False
    else:
        return True


if __name__ == '__main__':
    main()
