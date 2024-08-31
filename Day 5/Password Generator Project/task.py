import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

new_list = []

for _ in range(nr_letters):
    random_letter = random.choice(letters)
    new_list.append(random_letter)

for _ in range(nr_numbers):
    random_number = random.choice(numbers)
    new_list.append(random_number)

for _ in range(nr_symbols):
    random_symbol = random.choice(symbols)
    new_list.append(random_symbol)

print(new_list)
random.shuffle(new_list)
print(new_list)

password = ""
for character in new_list:
    password += character

print("Your new password is: " + password)
