amount = int(input("How many expenses do you want to enter?: "))

expenses = []
total = 0
highest_price = 0
highest_item = None
category_totals = {}

for _ in range(amount):
    item = str(input("What item do you want to add?: "))
    price = int(input("Whats the price of said item?: "))
    category = str(input("Whats the category of said item?: "))

    expense = {
        "item": item,
        "price": price,
        "category": category
    }

    expenses.append(expense)
    total = total + price

for expense in expenses:
    print(expense["item"], expense["price"], expense["category"])

    if expense["category"] in category_totals:
        category_totals[expense["category"]] = category_totals[expense["category"]] + expense["price"]
    else:
        category_totals[expense["category"]] = expense["price"]

    if expense["price"] > highest_price:
        highest_price = expense["price"]
        highest_item = expense["item"]

for category in category_totals:
    print(category, category_totals[category])

average = total / amount

print(category_totals)
print(f"The average cost is {average:.2f}.")
print(f"Total expenses: {total}")
print(f"Highest price: {highest_item} at {highest_price}")
