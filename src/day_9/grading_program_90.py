# Grading Program

# My solution 2:

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for scores in student_scores:
    if int(student_scores[scores]) >= 91 and int(student_scores[scores]) <= 100:
        student_grades[scores] = "Outstanding"

    elif int(student_scores[scores]) >= 81 and int(student_scores[scores]) <= 91:
        student_grades[scores] = "Exceeds Expectations"

    elif int(student_scores[scores]) >= 71 and int(student_scores[scores]) <= 80:
        student_grades[scores] = "Acceptable"

    else:
        student_grades[scores] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)


# instructors solution:

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"

    elif score > 80:
        student_grades[student] = "Exceeds Expectations"

    elif score > 70:
        student_grades[student] = "Acceptable"

    else:
        student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)