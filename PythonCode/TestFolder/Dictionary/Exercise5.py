'''
Create a Dictionary
Create a dictionary named student with keys: "name", "age", and "grade".
Assign any values you like.

Access Values
From the student dictionary, print only the value of "grade".

Add a Key-Value Pair
Add a new key "subject" with the value "Math" to the student dictionary.

Update a Value
Change the "grade" value to "A+".

Delete a Key
Remove the key "age" from the student dictionary.

Check for Key
Write a condition to check if "subject" exists in the student dictionary and print a message.

Iterate Through Dictionary
Print all the keys and values in the student dictionary in the format:
key: value
'''

student = {
    "name": "A",
    "age": 19,
    "grade": 'A'
}

print(student)
print(student["grade"])
student["Subject"] = "Math"
print(student)
student["grade"] = "A+"
print(student)
student.pop("age")
print(student)

if "Subject" in student:
    print(f"Subject available is : {student['Subject']}")
else:
    print("No")
