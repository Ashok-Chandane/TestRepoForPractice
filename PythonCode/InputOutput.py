# 1. Ask the user for their name and greet them.
# 2. Ask for two numbers and print their sum.
# 3. Format a message like: "You are 25 years old and live in Paris.

# 1. Ask the user for their name and greet them.

name = input("May I know your name : ")

print(f"Hello {name} Welcome to Python World")

# 2. Ask for two numbers and print their sum.
num1 = int(input("Please enter number1 :"))
num2 = int(input("Please enter number2 :"))
print(f" {num1} + {num2} = ",num1+num2 )

# 3. Format a message like: "You are 25 years old and live in Paris.
age = int(input("Enter your age: "))
city = (input("Enter your city: "))

print(f"You are {age} years old and live in {city}.")