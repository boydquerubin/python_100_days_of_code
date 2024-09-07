def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


print(format_name("AnGEla", "YU"))

print(format_name(input("What is your first name? "), input("What is your last name? ")))

# def is_leap_year(year):
#     if year % 400 == 0:
#         return True
#     if year % 100 == 0:
#         return False
#     if year % 4 == 0:
#         return True
#     return False
#
# print(is_leap_year(2000))
# print(is_leap_year(1900))
# print(is_leap_year(2024))
# print(is_leap_year(2023))
# print(is_leap_year(1989))