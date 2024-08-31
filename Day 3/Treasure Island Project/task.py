print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Dungeon Treasure. ")
print("Your mission is to find the treasure and escape the dungeon. \n")

import random

def perception():
    return random.randint(1, 100)

part_one = input("Enter the dungeon? Y or N \n").lower()

if part_one == "y":
    print("You enter the dungeon. \n")
elif part_one == "n":
    print("Game over. You go back to your mundane life. \n")
else:
    input("Invalid input. \n")

part_two = input("You keep walking forward until you reach a fork in the dungeon. "
                 "Do you go left or right? \n").lower()

if part_two == "left":
    print("There is a skeleton warrior holding a sword and a shield. Prepare to fight! \n")
    skeleton_one = input("Type F to attack. ").lower()
    if skeleton_one == "F":
        print("The skeleton dies. \n")
    else:
        print("You fumble your weapon, the skeleton strikes. \n")
        print("Game over. \n")
elif part_two == "right":
    print("You find a door. ")

part_three = input("Would you like to enter? Y or N \n").lower()

if part_three == "y":
    print("You enter the door. You find three chests. \n")
    part_three_chests = input("Which one do you decide to open? Left, Middle, or Right? \n").lower()

    if part_three_chests == "left":
        print("You open the chest. It's empty. \n")
        left_chest = input("Type R for a perception check. \n").lower()

        if left_chest == "r":
            perception_result = perception()
            print(f"You rolled {perception_result}! \n")

            if perception_result > 50:
                print("You notice a hidden compartment in the chest. You find a magic sword! ")
            else:
                print("You notice nothing out of the ordinary.")

        else:
            print("Invalid input. Game breaks.")
elif part_three == "n":
    print("You turn around, suddenly you see a skeleton warrior holding a sword and shield.")
    print("You reach for your sword, but you fumble your weapon, and the skeleton strikes. \n")
    print("Game over. \n")