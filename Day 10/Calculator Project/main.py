def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

first_number = int(input("Type your first number "))
math_op = input("Choose your mathematical operator (a choice of '+', '-', '*' or '/') ")
second_number = int(input("Type your second number "))

# print(operations["*"](4,8))

# while True:
#     if math_op == "+":
#         (operations["*"](first_number, second_number)
#     if math_op == "-":
#         (operations["*"](first_number, second_number)
#     if math_op == "*":
#         (operations["*"](first_number, second_number)
#     if math_op == "/":
#         (operations["*"](first_number, second_number)

# operations["*"]

# for operate in operations:
#     if