def calculated_age(current_year, user_year):
    return current_year - user_year

current_year = 2027
user_year = int(input("What year are you born in?"))
print(f"Your age is {calculated_age(current_year,user_year)}")
