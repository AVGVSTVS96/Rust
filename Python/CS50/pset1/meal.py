"""
Implement a program that prompts the user for a
time
Output whether its breakfast, lunch, or dinner time.
If its not time for a meal, output nothing.
"""

def main():
    time = input("What time is it? ")
    print(convert(time))


def convert(time):
    dot_time = time.replace(":", ".")
    float_time = float(dot_time)
    round_time = round(float_time, 1)
    return round_time

if __name__ == "__main__":
    main()
