import random

print(r'''   ___                       _____ _                __                 _               
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   
                                                                                       ''')
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# range 1, 100
number = random.randint(1, 100)

attempts = 10

if difficulty == "easy":
    print(f"You have {attempts} attempts remaining to guess the number.")
    attempt1 = int(input("Make a guess: "))
    # while loop here? How do I shorten this code?
    if attempt1 > number:
        print("Too high.\nGuess again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")

        # attempt2 = int(input("Make a guess: "))
        # if attempt2 > number:
        #     print("Too high.\nGuess again.")
        #     attempts -= 1
        #     print(f"You have {attempts} attempts remaining to guess the number.")
        #     attempt2 = int(input("Make a guess: "))



        if attempts == 0:

    # if attempt1 > number:
    #     print("Too high.\nGuess again.")
    #     attempts -= 1
    #     print(f"You have {attempts} attempts remaining to guess the number.")
    #     is there a way to make this more concise?
    # when am i going to finish this?

if difficulty == "hard":
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
    input("Make a guess: ")

def my_function():
    print("create new function")