import requests as requests

print("Welcome to the currency converter!")
is_on = True


def get_input():
    currency_from = input("Which currency would you like to convert from? ").upper()
    currency_to = input("Which currency would you like to convert to? ").upper()
    amount = int(input(f"How much {currency_from} would you like to convert to {currency_to}? "))
    return currency_from, currency_to, amount

def convert(currency_from, currency_to, amount):
    url = f"https://v6.exchangerate-api.com/v6/03aa8fc4f315c8609ad8281c/pair/{currency_from}/{currency_to}/{amount}"
    data = requests.get(url).json()
    converted_amount = data["conversion_result"]
    return converted_amount

while is_on:
    currency_from, currency_to, amount = get_input()
    converted_amount = convert(currency_from, currency_to, amount)
    print (f"{amount} {currency_from} is {converted_amount} {currency_to}")
    replay = input("Would you like to do another conversion? Y/N ").lower()
    if replay == "n":
        is_on = False