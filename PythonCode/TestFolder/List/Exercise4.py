'''
List Comprehension
Create a list of squares of numbers from 1 to 10 using list comprehension.
'''

squares = []

for index in range(1, 11):
    squares.append(index**2)

print(squares)

for index in range(1, 11):
    # This shifts existing content to next memory indices [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    # squares.insert(index-1, index**3)
    # This replace content on existing memory [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
    squares[index-1] = index**3

print(squares)
