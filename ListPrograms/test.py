students = {
    "Rahul": [80, 90, 85],
    "Priya": [95, 92, 98],
    "Amit": [75, 85, 80]
}

subjects = ("Maths", "Science", "English")

for roll_no, (name, marks) in enumerate(students.items(), start=1):
    print("\nRoll No:", roll_no)
    print("Name:", name)

    for subject, mark in zip(subjects, marks):
        print(subject, ":", mark)