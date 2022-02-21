
person = {
    "name": "baraka",
    "email": "baraka@gmail.com",
    "phone": "+(254) 7 123 456 76"
}

# access values
print(person['email'])
print(person.get('email'))
print(person.get('email34', "garry@gmail.com"))

# setting values
person['age'] = 35

# re-assign values
person['name'] = "Bob"


# empty dict
# person = {}

# loop through a dictionary
for key in person:
    print(f"'{key}'==>{person[key]}")

# Day 9.1 exercise
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 63
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    grade = ""
    if score > 90:
        grade = "Outstanding"
    elif score > 80:
        grade = "Exceeds expectations"
    elif score > 70:
        grade = "Acceptable"
    else:
        grade = "Fair"
    student_grades[student] = grade


print(student_grades)
