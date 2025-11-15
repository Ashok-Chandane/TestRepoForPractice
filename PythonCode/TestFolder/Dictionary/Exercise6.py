'''
Dictionary of Lists
Create a dictionary named scores where keys are subject names (e.g., "Math", "Science") and values are lists of scores.
Example: {"Math": [90, 85, 88]}

Find Maximum Value
Given the dictionary marks = {"Alice": 88, "Bob": 95, "Charlie": 70}, find the student with the highest marks.

Merge Dictionaries
'''

scores = {
    "Math": [88, 92, 60, 83],
    "Science": [78, 98, 60, 59],
    "History": [45, 71, 83, 92],
    "English": [54, 65, 71, 36]
}

for keys, values in scores.items():
    print(keys, max(values))
    print(keys, min(values))
