import os
import requests

user_coin = input("Which coin do you want to check? ")
currency = input("Which currency do you want to check with? ")

api_key = os.getenv("CMC_API_KEY")

if not api_key:
    print("CMC_API_KEY is not set.")
    print("Set it in your environment before running the program.")
    raise SystemExit

api_url = f"https://pro-api.coinmarketcap.com/v2/simple/price?slug={user_coin}&convert={currency}"

headers = {
    "Accept": "application/json",
    "X-CMC_PRO_API_KEY": api_key
}

response = requests.get(api_url, headers=headers)
data = response.json()

price = data["data"][0]["quotes"][0]["price"]

print(f"{user_coin} is currently priced at {price} {currency.upper()}")
