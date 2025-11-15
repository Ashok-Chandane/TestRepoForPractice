list1 = [1, 2, 2, 1]
list2 = list1.copy()
list1.reverse()

if list1 == list2:
    print("Palindrom")
else:
    print("Not a Palindrom")
