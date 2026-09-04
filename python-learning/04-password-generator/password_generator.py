import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"

amount = int(input("How many characters should the password have?: "))

password = ""

for _ in range(amount):
    password += random.choice(characters)

print(f"Your password is: {password}")
