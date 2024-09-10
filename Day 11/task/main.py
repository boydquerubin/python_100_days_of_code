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

    first_round = random.choices(cards, k=2)
    for _ in first_round:
        score = sum(first_round)

    current_score = score

    print(f"Your cards: {first_round}, current score: {current_score}")



    # def player_cards():
    #     for num in cards:
    #         print(random.shuffle(cards))



    game_start = input("Type 'Y' to Hit and 'N' to Stand\n").lower()


if game_start == "n":
    print("Bye, have a wonderful day!")
