'''
Exercise 4: Dictionary Comprehension

Given a list of numbers:

numbers = [1, 2, 3, 4, 5]


👉 Task:
Create a dictionary where the keys are numbers and the values are their squares.
Expected output:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''

numbers = [1, 2, 3, 4, 5]

squares = {}

for index in numbers:
    squares[index] = (index*index)
    print(f"{index}:{index*index}")

print(squares)
