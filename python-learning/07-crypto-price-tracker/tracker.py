import requests
import time
import keyboard
import os

user_coin = input("Which coin do you want to check? ")
currency = input("Which currency do you want to check with? ")
interval = int(input("How often should the price be checked (in seconds)? "))

api_key = os.getenv("CMC_API_KEY")

if not api_key:
    print("CMC_API_KEY is not set.")
    raise SystemExit

api_url = f"https://pro-api.coinmarketcap.com/v2/simple/price?slug={user_coin}&convert={currency}"

headers = {
    "Accept": "application/json",
    "X-CMC_PRO_API_KEY": api_key
}

file = open("prices.csv", "w")

run = True

while run:
    response = requests.get(api_url, headers=headers)
    data = response.json()

    price = data["data"][0]["quotes"][0]["price"]
    timestamp = data["status"]["timestamp"]

    description = f"{user_coin} is currently priced at {price}, {timestamp}\n"

    print(description)
    file.write(description)
    file.flush()

    for _ in range(interval * 10):
        time.sleep(0.1)

        if keyboard.is_pressed("ENTER"):
            run = False
            break

file.close()
