# for number in range(1, 10, 3):
#     print(number)

# var = 0
# for number in range(1, 101):
#     var += number
#
# print(var)
#
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)


# glass1 = "milk"
# glass2 = "juice"
# glass3 = glass1
# glass1 = glass2
# glass2 = glass3
#
# print(glass1)
# print(glass2)