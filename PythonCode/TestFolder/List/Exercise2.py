'''
Append and Insert
Start with an empty list. Add numbers 1 to 5 using .append(), then insert the number 10 at index 2.
'''

my_list = []

for i in range(1, 6, 1):
    my_list.append(i)

print(my_list)
my_list.insert(2,10)
print(my_list)

