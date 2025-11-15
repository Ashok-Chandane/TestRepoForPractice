'''
Create and Print
Create a list of 5 fruits and print the second and last elements.
'''

fruits = ["banana", "mango", "strawberry", "melon", "guava"]

print(fruits)
fruits.remove('guava')
print(fruits)
fruits.clear()
print(fruits)
fruits = ["banana", "mango", "strawberry", "melon", "guava"]
print(fruits)
fruits.sort(reverse=3)
print(fruits)
print(fruits.index('melon'))
fruits.insert(10, 'orange')
print(fruits)
print(fruits.index('orange'))
