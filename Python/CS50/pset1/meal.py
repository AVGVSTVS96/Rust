"""
Implement a program that prompts the user for a
time
Output whether its breakfast, lunch, or dinner time.
If its not time for a meal, output nothing.
"""

def main():
    time = input("What time is it? ")
    float_time = convert(time)

    if float_time >= 7.0 or float_time <= 8.0:
        print("breakfast time")
    elif float_time >= 12.0 or float_time <= 13.0:
        print("lunch time")
    elif float_time>= 18.0 or float_time <= 19.0:
        print("dinner time")
    else:
        pass

def convert(time):
    dot_time = time.replace(":", ".")
    float_time = float(dot_time)
    round_time = round(float_time, 1)
    return round_time

if __name__ == "__main__":
    main()
