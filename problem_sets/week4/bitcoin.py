import requests
import sys

if len(sys.argv) < 2 or len(sys.argv) > 2:
    sys.exit(1)

user_input = sys.argv[1]

try:
    number = float(user_input)

except ValueError:
    sys.exit(f"Error: '{user_input}' is not a valid number.")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=8120cb2caa66294c299440c2138d1680b269a3640d2f065e25cb09316a33ae37")

    value = response.json()["data"]["priceUsd"]
    price = float(value)

    total = number * price

    print(f"${total:,.4f}")

except requests.RequestException:
    sys.exit("Error fetching data from CoinCap API")




