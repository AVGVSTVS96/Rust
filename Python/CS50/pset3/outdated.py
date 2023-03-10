"""
TODO: Add loop to prompt user again if date is invalid
"""

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

date_endian = input("Date: ").title()

# split input
split_date = date_endian.replace(",", " ").replace("/", " ").split()

# get month
month = split_date[0]
if month.isalpha():
    if month in months:
        month_number = f"{months[month]:02}"
elif month.isnumeric():
    if int(month) in months.values():
        month_number = f"{int(month):02}"

# get day
day = str(split_date[1])

# get year
year = str(split_date[2])

print(year, month_number, day, sep="-")
