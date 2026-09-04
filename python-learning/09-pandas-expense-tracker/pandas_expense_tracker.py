import pandas as pd

expenses = [
    {"item": "Example 1", "price": 400, "category": "Food"},
    {"item": "Example 2", "price": 200, "category": "Gaming"},
    {"item": "Example 3", "price": 100, "category": "Food"},
    {"item": "Example 4", "price": 25, "category": "Other"}
]

df = pd.DataFrame(expenses)

print(df)

print(f"Average price: {df['price'].mean():.2f}")
print(f"Total price: {df['price'].sum()}")
print(f"Highest price: {df['price'].max()}")

highest_expense = df.loc[df["price"].idxmax()]
print("Highest expense:")
print(highest_expense)
