# 1. Write a function that greets the user by name.
# 2. Write a function that adds two numbers and returns the sum.
# 3. Write a function that checks if a number is even or odd.

def greet(name="Sunny", greet="Guten Morgen"):
    print("Hello " + name + " " + greet)


greet("Sanika", "Welcome to Beautiful World my Sweetie")


def sum(num1, num2):
    return (num1+num2)


print(sum(5, 8))


def EvenOrOdd(num):
    if (num % 2 == 0):
        str = "Even"
    else:
        str = "Odd"

    return str


print(EvenOrOdd(8))
print(EvenOrOdd(17))
