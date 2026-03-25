rates = {"USD": 1, "EUR": 0.92, "INR": 82.5}

amount = float(input("Enter amount in USD: "))
currency = input("Convert to (EUR/INR): ").upper()

if currency in rates:
    converted = amount * rates[currency]
    print(f"{amount} USD = {converted} {currency}")
else:
    print("Currency not supported")
