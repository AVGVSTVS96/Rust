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
    if len(s) < 2 or len(s) > 6:
        return False
    elif not s[:2].isalpha():
        return False
    elif s.isalnum() and s[-2:].isdigit() or not s.isalnum():  # TODO needs fixing
        return True
    else:
        return False

#    if s[:2].isdigit():
#        return False
#    if s.isalnum() and s[-2:].isdigit() or not s.isalnum():
#        return True


"""       *This code works*
if s[:2].isalpha() and 2 <= len(s) <= 6:
    if len(s) > 2 and not s[:-2].isalpha():  
        return False                        
    return True
return False
"""

if __name__ == '__main__':
    main()
