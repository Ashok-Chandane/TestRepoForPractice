'''
Exercise 2: Counting Words

Given the list:

words = ["apple", "banana", "apple", "orange", "banana", "apple"]


👉 Task:
Create a dictionary that counts how many times each word appears.
Expected output:

{'apple': 3, 'banana': 2, 'orange': 1}


(Hint: use a loop and an if-else statement, or dict.get())
'''

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
inventory = {}

for index in words:
    if index in inventory:
        inventory[index] += 1
    else:
        inventory[index] = 1

print(inventory)
