programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# print(programming_dictionary["Function"])

programming_dictionary["Loop"] = "The action of doing something over and over again."

empty_dictionary = {}

# programming_dictionary = {}
# print(programming_dictionary)

programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

    student_scores = {
        'Harry': 88,
        'Ron': 78,
        'Hermione': 95,
        'Draco': 75,
        'Neville': 60
    }

    student_grades = {}

    for score in student_scores:
        if student_scores[score] in range(91, 100):
            student_grades[score] = "Outstanding"
        elif student_scores[score] in range(81, 90):
            student_grades[score] = "Exceeds Expectations"
        elif student_scores[score] in range(71, 80):
            student_grades[score] = "Acceptable"
        else:
            student_grades[score] = "Fail"

    print(student_grades)