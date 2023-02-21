"""Program prompts user for vanity plate and
   outputs "Valid" these requirements are met:
    # String must begin with 2 letters
    # Minimum 2 characters, maximum 6
    # Numbers must only come at the end
    # No periods, spaces or punctuation
"""
# TODO Stop punctuation marks from being allowed

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[:2].isalpha() and 2 <= len(s) <= 6:
        if len(s) > 2 and not s[:-2].isalpha():  # TODO s[:-2] slices last 2 chars off string
            return False                         # TODO s[-2:] only looks at the last 2 chars
        return True
    return False


if __name__ == '__main__':
    main()
