
collection = {1, 2, 3, 4, 1, 2}

print(collection)

print(type(collection))

for i in range(1, 10, 1):
    collection.add(i)

print(collection)

for i in range(1, 10, 1):
    if i % 2 == 0:
        collection.remove(i)

print(collection)
print(len(collection))
collection.pop(3)

collection2 = set()

for i in range(ord('A'), ord('Z') + 1):
    collection2.add(chr(i))

print(collection2)
print(len(collection2))