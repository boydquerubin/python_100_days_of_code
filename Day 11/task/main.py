#create a flowchart
#try solving without hints

import random

game_start = input("Do you want to play Blackjack? Type 'Y' or 'N' ").lower() #function inertia? or inception lol greeting disappears\n*20

current_score = 0

if game_start == "y":
    print(f"\n"*20)

    import art
    print(art.logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    hand = [] #empty array to show hand?

    first_round = random.choices(cards, k=2)

    current_score = sum(first_round)

    print(f"Your cards: {first_round}, current score: {current_score}")

    hit_or_stand = input("Type 'Y' to Hit and 'N' to Stand\n").lower()
    if hit_or_stand == "y":
        second_round = random.choices(cards, k=1)

        current_score = sum(first_round + second_round)
        print(f"Your cards: {first_round}{second_round}, current score: {current_score}")
        #if score over 23 you lose

if game_start == "n":
    print("Bye, have a wonderful day!")
