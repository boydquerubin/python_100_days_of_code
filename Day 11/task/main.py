#create a flowchart
#try solving without hints

import random

game_start = input("Do you want to play Blackjack? Type 'Y' or 'N' ").lower() #function inertia? or inception lol greeting disappears\n*20

current_score = 0
dealer_current_score = 0

if game_start == "y":
    print(f"\n"*20)

    import art
    print(art.logo)
    #Computer thinks Ace is only 11
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    hand = [] #empty array to show hand?
    dealer_hand = []

    first_round = random.choices(cards, k=2)
    hand.extend(first_round)
    current_score = sum(hand)

    print(f"Your cards: {first_round}, your current score: {current_score}")
    #computer's hand
    dealer_first_round = random.choices(cards, k=2)
    dealer_hand.extend(dealer_first_round)
    dealer_current_score = sum(dealer_hand)
    print(f"Dealer's hand: {dealer_hand}, Dealer's current score: {dealer_current_score}")


    if current_score <= 21:
        hit_or_stand = input("Type 'Y' to Hit and 'N' to Stand\n").lower()

        if hit_or_stand == "y":
            second_round = random.choices(cards, k=1)
            print(f"The dealer deals you a {second_round}.")
            hand.extend(second_round)
            current_score = sum(hand)
            print(f"Your cards: {hand}, your current score: {current_score}")

            dealer_second_round = random.choices(cards, k=1)
            dealer_hand.extend(dealer_second_round)
            dealer_current_score = sum(dealer_hand)
            print(f"Dealer's hand: {dealer_hand}, Dealer's current score: {dealer_current_score}")

            if current_score <= 21:
                hit_or_stand = input("Type 'Y' to Hit and 'N' to Stand\n").lower()
                #third round?
            elif current_score == 21:
                print(f"You hit {current_score}, You win!")
            else:
                print("You went over 21. Bust, you lose!")

        if hit_or_stand == "n":
            print(f"Your score is {current_score}.")
            print("Dealer's hand is: X")

    elif current_score == 21:
        print(f"Your cards: {hand}, your current score: {current_score}")
        print("Dealer's hand is: X")
        print(f"You hit {current_score}, You win!")
    else:
        print(f"Your cards: {hand}, your current score: {current_score}")
        print("Dealer's hand is: X")
        print("You went over 21. Bust, you lose!")

    if hit_or_stand == "n":
        print(f"Your score is {current_score}.")
        print("Dealer's hand is: X")



        #if score over 21 you lose

if game_start == "n":
    print("Bye, have a wonderful day!")
