'''
Combine Lists
Combine list1 = [1,2,3] and list2 = [4,5,6] into a single list in two different ways.
'''

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined_list = []
# combined_list = list1 + list2

combined_list = list1
combined_list.extend(list2)
print(combined_list)
