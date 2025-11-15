user_input = int(input("Input number : "))
Fact = 1

for i in range(user_input, 1, -1):
    Fact *= i

print(f"Factorial = {Fact}")
