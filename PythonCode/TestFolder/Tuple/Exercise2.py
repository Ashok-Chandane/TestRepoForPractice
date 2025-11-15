'''
Tuple indexing
Given the tuple colors = ("red", "green", "blue", "yellow", "purple"), print the second and last elements.
Using the same colors tuple, print the first three elements and then the last two.
'''

colors = ("red", "green", "blue", "yellow", "purple")

for item in colors:
    print(item)

print(colors[1], colors[-1])

print(colors[:3], colors[-2:])

found = 0

for color in colors:
    if color is "orange":
        found = 1
        break
if found is True:
    print("Found")
else:
    print("Not Found")
