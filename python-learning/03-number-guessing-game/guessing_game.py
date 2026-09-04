import random

while True:
    difficulty = input("Choose a difficulty (Easy, Medium, Hard): ").lower()

    if difficulty == "easy":
        maximum = 50
        attempts = 5
    elif difficulty == "medium":
        maximum = 100
        attempts = 10
    elif difficulty == "hard":
        maximum = 500
        attempts = 15
    else:
        print("Invalid difficulty.")
        continue

    number = random.randint(1, maximum)
    print(f"I'm thinking of a number between 1 and {maximum}.")

    won = False

    while attempts > 0:
        guess = int(input("Guess the number: "))

        if guess == number:
            print("Correct!")
            won = True
            break
        elif guess < number:
            print("The number is higher.")
        else:
            print("The number is lower.")

        attempts -= 1
        print(f"Attempts left: {attempts}")

    if not won:
        print(f"You lost. The number was {number}.")

    restart = input("Play again? (y/n): ").lower()

    if restart != "y":
        break
