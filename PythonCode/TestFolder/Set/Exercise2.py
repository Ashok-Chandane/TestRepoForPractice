
subjects1 = {"python", "C++", "java", "python", "javascript"}
subjects2 = {"java", "python", "java", "C++", "C"}

print(subjects1)
print(subjects2)

print(f"Unique subjects are : {subjects1.union(subjects2)}")
print(f"Total number of classrooms required are: {len(subjects1.union(subjects2))}")