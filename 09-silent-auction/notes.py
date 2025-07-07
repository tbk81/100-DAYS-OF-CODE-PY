# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}

# for key in student_scores:
#     if student_scores[key] > 90:
#         student_grades[key] = "Outstanding"
#     elif 80 < student_scores[key] < 91:
#         student_grades[key] = "Exceeds Expectations"
#     elif 70 < student_scores[key] < 81:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"
# print(student_grades)

# '''
#  - Scores 91 - 100: Grade = "Outstanding" 
# - Scores 81 - 90: Grade = "Exceeds Expectations" 
# - Scores 71 - 80: Grade = "Acceptable"
# - Scores 70 or lower: Grade = "Fail"
# '''

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Struttgart", "Berlin"]
# }

# # print Lille
# print(travel_log["France"][1])

# nested_list = ["a", "b", ["c", "d"]]
# # print d
# print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Struttgart", "Berlin"],
        "total_visits": 5
    }
}

# print Lille
print(travel_log["France"]["cities_visited"][1])