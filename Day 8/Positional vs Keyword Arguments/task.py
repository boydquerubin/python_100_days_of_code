# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

# def greet_with(name, location):
#     print(f"Hello, {name}")
#     print(f"You said you're from {location}?")

# greet_with("Joe", "Texas")

def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"You said you're from {location}?")

greet_with(location="Texas", name="Joe")


# def calculate_love_score(name1, name2):
#     print(f"The first person's name is: {name1}")
#     print(f"The second person's name is: {name2}")
#
#     true = "TRUE".lower()
#     love = "LOVE".lower()
#     combined_names = name1.lower() + name2.lower()
#
#     true_score = 0
#     love_score = 0
#
#     for letter in true:
#         letter_count = combined_names.count(letter)
#         true_score += letter_count
#         print(letter + f" occurs {letter_count} times")
#     print(f"Total TRUE score = {true_score}")
#
#     for letter in love:
#         letter_count = combined_names.count(letter)
#         love_score += letter_count
#         print(letter + f" occurs {letter_count} times")
#     print(f"Total LOVE score = {love_score}")
#
#     print(f"Love Score = {true_score}{love_score}")
#
#
# calculate_love_score("Joe", "Julie")


def calculate_love_score(name1, name2):
    true = "TRUE".lower()
    love = "LOVE".lower()
    combined_names = name1.lower() + name2.lower()

    true_score = 0
    love_score = 0

    for letter in true:
        letter_count = combined_names.count(letter)
        true_score += letter_count

    for letter in love:
        letter_count = combined_names.count(letter)
        love_score += letter_count

    print(f"{true_score}{love_score}")


calculate_love_score("Joe", "Julie")