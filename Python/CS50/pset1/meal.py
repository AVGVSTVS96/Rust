# Implement a program that prompts the user for a time
# Output whether its breakfast, lunch, or dinner time
# If not time for a meal, output nothing.


def main():
    time = input("What time is it? ")
    float_time = convert(time)

    if 7.0 <= float_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= float_time <= 13.0:
        print("lunch time")
    elif 18.0 <= float_time <= 19.0:
        print("dinner time")
    else:
        pass


def convert(time):  # converts time to float w/ 1 decimal place
    dot_time = time.replace(":", ".")
    float_time = float(dot_time)
    round_time = round(float_time, 1)
    return round_time


if __name__ == "__main__":
    main()
