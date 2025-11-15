'''
Check Membership
Given names = ["Alice", "Bob", "Charlie", "David"], check if "Eve" is in the list. If not, add her.
'''

names = ["Alice", "Bob", "Charlie", "David"]
find_flag = False

print(names)

for name in names:
    if name is "Eve":
        find_flag = True

if find_flag is False:
    names.append("Eve")

print(names)

nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort()
print(nums)
nums.reverse()
print(nums)
