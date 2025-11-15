'''
List Slicing
Given nums = [10, 20, 30, 40, 50, 60, 70], print the first three elements, the last two, and the middle three.
'''

nums = [10, 20, 30, 40, 50, 60, 70]

print(nums[:3])
print(nums[-2:])
print(nums[:4:2])

mid_index = len(nums) // 2

print(nums[mid_index - 1: mid_index + 2])
