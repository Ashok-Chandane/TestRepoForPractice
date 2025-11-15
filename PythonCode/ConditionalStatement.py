# 1. Ask for a number and tell if it’s positive, negative, or zero.
# 2. Check if a user’s age is old enough to vote (18+).
# 3. Ask for a password and check if it matches a preset one.

# 1. Ask for a number and tell if it’s positive, negative, or zero.

num = int(input("Enter a number > "))

if (num > 0):
    print("It's a Positive Number.")
elif (num < 0):
    print("It's a Negative Number.")
else:
    print("It's a Zero.")

# 2. Check if a user’s age is old enough to vote (18+).
age = int(input("Enter a Age > "))

if age >= 18:
    print("You are Eligible to Vote")
else:
    print("You are NOT Eligible to Vote")

# 3. Ask for a password and check if it matches a preset one.
password = "Qwer1234"

user_input = input("Please Enter your Password > ")

if password == user_input:
    print("Welcome to your Account")
else:
    print("Wrong Password")
