# 1. Print numbers from 1 to 10 using a for loop.
# 2. Print even numbers from 1 to 20.
# 3. Use a while loop to count down from 5 to 1.
# 4. Ask the user for a number and print its multiplication table.

for i in range(1, 11):
    print(i)

for i in range(2, 21, 2):
    print(i)

i = 5
while i:
    print(i)
    i -= 1

num = int(input("Enter a Number > "))

for i in range(1, 11):
    print(num*i)
