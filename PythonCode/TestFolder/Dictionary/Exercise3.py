'''
Exercise 3: Nested Dictionary

Create a dictionary of students and their grades:

students = {
    "Alice": {"math": 85, "science": 90},
    "Bob": {"math": 78, "science": 83},
    "Charlie": {"math": 92, "science": 88}
}


👉 Tasks:

Print Alice’s science grade.

Add a new student "Diana" with math=89 and science=91.

Increase Bob’s math score by 5.

Print all student names using a loop.
'''

students = {
    "Alice": {"math": 85, "science": 90},
    "Bob": {"math": 78, "science": 83},
    "Charlie": {"math": 92, "science": 88}
}

print(students["Alice"]["science"])

students.update({"Diana": {"math": 89, "science": 91}})

for name in students:
    print(name)
