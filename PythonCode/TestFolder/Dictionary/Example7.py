'''
Find Maximum Value
Given the dictionary marks = {"Alice": 88, "Bob": 95, "Charlie": 70}, find the student with the highest marks.
'''

marks = {"Alice": 88, "Bob": 95, "Charlie": 98}

print(max(marks, key=marks.get))
print(min(marks, key=marks.get))
