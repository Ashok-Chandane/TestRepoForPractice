# 1. Create a dictionary of a student with name, age, and grade.
# 2. Print the student’s name.
# 3. Add a new key: “city”.
# 4. Loop through the dictionary and print all keys and values.

# 1. Create a dictionary of a student with name, age, and grade.
students = {
    101: {"name": "Stdnt1", "age": 17, "grade": 89.23},
    102: {"name": "Stdnt2", "age": 17, "grade": 97.34},
    103: {"name": "Stdnt3", "age": 16, "grade": 74.76},
    104: {"name": "Stdnt4", "age": 18, "grade": 61.78}
}

for key, value in students.items():
    print(f"{key} : {value['name']}'s age is {value['age']} and got {value['grade']}%")

students.update({105: {"name": "ABCD", "age": 17, "grade": 88.50}})

for key, value in students.items():
    print("{key} : {value['name']}'s age is {value['age']} and got {value['grade']}%")
