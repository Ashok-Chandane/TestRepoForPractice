# 1. Create a list of 5 favorite foods.
# 2. Print the first and last items.
# 3. Add a new food and remove one.
# 4. Loop through the list and print each item.

food = ["A", "B", "C", "D", "E"]

print(food)

print(food[0], food[-1])

food.append("F")

print(food)

food.remove("C")

print(food)

for item in food:
    print(item)
