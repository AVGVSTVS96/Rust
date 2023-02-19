# program that calculates the change input to reach 50 cents
# prompt the user to insert a coin
# after each coin input print the coin amount and the remaining due
# only accept 5, 10, 25 cent inputs


amount_due = 50
cents = 0
accepted_inputs = [5, 10, 25]

while cents < 50:
    print(f"Amount Due: {amount_due - cents}")
    coin_input = int(input("Insert Coin: "))
    if coin_input in accepted_inputs:
        cents += coin_input

if cents == 50:
    print("Change Owed: 0")

