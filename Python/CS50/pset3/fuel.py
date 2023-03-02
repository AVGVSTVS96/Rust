"""
- Prompt user for fraction (x/y)
- Output percentage as integer
- If percentage < 1 output E
- If percentage > 99 output F

# If x or y != integer (or) x > y (or) y == 0, prompt again
# Handle ValueError and ZeroDivisionError
"""


def prompt():
    global x, y
    while True:
        try:
            fuel_fraction = input("Fraction: ")
            x, y = fraction_split = fuel_fraction.split("/")
            x = int(x)
            y = int(y)
            if y == 0 or x > y:
                continue
            else:
                break
        except ValueError:
            print("Input Integers")
        except ZeroDivisionError:
            print("Y must not be 0")


def convert_percent():
    percentage = (x / y) * 100
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(round(percentage), "%", sep="")


def main():
    # Get and evaluate input
    prompt()
    # Get percentage
    convert_percent()


if __name__ == '__main__':
    main()
