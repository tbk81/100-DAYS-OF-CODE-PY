student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif 80 < student_scores[key] < 91:
        student_grades[key] = "Exceeds Expectations"
    elif 70 < student_scores[key] < 81:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
# for key in student_scores:
#     student_grades[key] = student_scores[key]/100
print(student_grades)

'''
 - Scores 91 - 100: Grade = "Outstanding" 
- Scores 81 - 90: Grade = "Exceeds Expectations" 
- Scores 71 - 80: Grade = "Acceptable"
- Scores 70 or lower: Grade = "Fail"
'''