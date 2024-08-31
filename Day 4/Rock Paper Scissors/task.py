import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_paper_scissors = [rock, paper, scissors]

computer_choice = random.randint(0, 2)

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if player_choice == 0:
    print(rock_paper_scissors[0])
    print(f"Computer chose: {computer_choice}\n")

    if computer_choice == 1:
        print(rock_paper_scissors[1])
        print("You lose!")
    elif computer_choice == 0:
        print(rock_paper_scissors[0])
        print("It's a draw!")
    else:
        print(rock_paper_scissors[2])
        print("You win!")

elif player_choice == 1:
    print(rock_paper_scissors[1])
    print(f"Computer chose: {computer_choice}\n")

    if computer_choice == 2:
        print("You lose!")
        print(rock_paper_scissors[2])
    elif computer_choice == 1:
        print("It's a draw!")
        print(rock_paper_scissors[1])
    else:
        print("You win!")
        print(rock_paper_scissors[0])

elif player_choice == 2:
    print(rock_paper_scissors[2])
    print(f"Computer chose: {computer_choice}\n")

    if computer_choice == 0:
        print("You lose!")
        print(rock_paper_scissors[0])
    elif computer_choice == 2:
        print("It's a draw!")
        print(rock_paper_scissors[2])
    else:
        print("You win!")
        print(rock_paper_scissors[1])

else:
    print("You can't follow instructions. You lose!")


# print(rock_paper_scissors[random_i])