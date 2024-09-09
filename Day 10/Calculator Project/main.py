import art
print(art.logo)

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

result = None

while True:
    if result is None:
        first_number = float(input("Enter the first number: "))
    else:
        first_number = result

    math_op = input("Choose your mathematical operator (a choice of '+', '-', '*' or '/') ")
    while math_op not in operations:
        math_op = input("Invalid input. Please choose '+', '-', '*' or '/' ")

    second_number = float(input("Enter the second number: "))

    if math_op == "/" and second_number == 0:
        print("Error: Division by zero is undefined.")
    else:
        result = operations[math_op](first_number, second_number)
        print(f"{first_number} {math_op} {second_number} = {result}")

    keep_going = input("would you like to continue? (yes/no)\n").lower()
    if keep_going == "yes":
        break
    """Learn about function recursions here"""

print("Thank you for using the calculator, goodbye!")

