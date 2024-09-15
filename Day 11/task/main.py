#ace handling
#improve dealer card drawing logic
#debug player hit or stand flow
#simplify dealer win/loss condition
#prevent redundancy
#
# import random
#
# game_start = input("Do you want to play Blackjack? Type 'Y' or 'N' ").lower() #function inertia? or inception lol greeting disappears\n*20
#
# current_score = 0
# dealer_current_score = 0
#
# if game_start == "y":
#     print(f"\n"*20)
#
#     import art
#     print(art.logo)
#     #Computer thinks Ace is only 11
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
#     hand = [] #empty array to show hand?
#     dealer_hand = []
#
#     first_round = random.choices(cards, k=2)
#     hand.extend(first_round)
#     current_score = sum(hand)
#
#     print(f"Your cards: {first_round}, your current score: {current_score}")
#     #computer's hand
#     dealer_first_round = random.choices(cards, k=2)
#     dealer_hand.extend(dealer_first_round)
#     dealer_current_score = sum(dealer_hand)
#     print(f"Dealer's hand: {dealer_hand}, Dealer's current score: {dealer_current_score}")
#
#     hit_or_stand = input("Type 'Y' to Hit and 'N' to Stand\n").lower()
#
#     # attempt to redraw for dealer
#     if dealer_current_score < 21 and dealer_current_score > 2:
#         dealer_second_round = random.choices(cards, k=1)
#         dealer_hand.extend(dealer_second_round)
#         dealer_current_score = sum(dealer_hand)
#         if dealer_current_score < 21:
#             print(f"Dealer hits again. Dealer's hand: {dealer_hand}, Dealer's current score: {dealer_current_score}")
#             if dealer_current_score < 21 and dealer_current_score > 13:
#                 dealer_second_round = random.choices(cards, k=1)
#                 dealer_hand.extend(dealer_second_round)
#                 dealer_current_score = sum(dealer_hand)
#
#                 if dealer_current_score <= 21:
#                     print(f"Dealer's hand: {dealer_hand}, Dealer's current score: {dealer_current_score}, dealer wins.")
#                 else:
#                     print(f"Dealer's hand: {dealer_hand}, Dealer's current score: {dealer_current_score}, dealer bust.")
#         else:
#             print("test1")
#             #print(f"Dealer hits again. Dealer's hand: {dealer_hand}, Dealer's current score: {dealer_current_score}")
#
#     if hit_or_stand == "n":
#         if current_score > dealer_current_score:
#             print(f"Your score is {current_score}. Dealer's score is: {dealer_current_score}. You win!!!")
#         if dealer_current_score > current_score and dealer_current_score > 21:
#             print(f"Your score is {current_score}. Dealer's score is: {dealer_current_score}. Dealer Bust, you win!!!")
#         if dealer_current_score > current_score and dealer_current_score < 21:
#             print(f"Your score is {current_score}. Dealer's score is: {dealer_current_score}. Dealer wins.")
#         # compare_scores = max(current_score, dealer_current_score)
#         # if compare_scores <= 21:
#         #     print(f"Your score is {current_score}. Dealer's score is: {dealer_current_score}. {compare_scores} wins!")
#
#     if current_score <= 21:
#         # hit_or_stand = input("Type 'Y' to Hit and 'N' to Stand\n").lower()
#         if hit_or_stand == "y":
#             second_round = random.choices(cards, k=1)
#             print(f"The dealer deals you a {second_round}.")
#             hand.extend(second_round)
#             current_score = sum(hand)
#             print(f"Your cards: {hand}, your current score: {current_score}")
#
#             dealer_second_round = random.choices(cards, k=1)
#             dealer_hand.extend(dealer_second_round)
#             dealer_current_score = sum(dealer_hand)
#             print(f"Dealer's hand: {dealer_hand}, Dealer's current score: {dealer_current_score}")
#
#             if current_score <= 21:
#                 hit_or_stand = input("Type 'Y' to Hit and 'N' to Stand\n").lower()
#                 #third round?
#             elif current_score == 21:
#                 print(f"You hit {current_score}, You win!")
#             else:
#                 print("You went over 21. Bust, you lose!")
#
#         if hit_or_stand == "n":
#             print(f"Your score is {current_score}.")
#             print("Dealer's hand is: X")
#
#     if current_score == 21:
#         print(f"Your cards: {hand}, your current score: {current_score}")
#         print("Dealer's hand is: X")
#         print(f"You hit {current_score}, You win!")
#     if current_score > 21:
#         print(f"Your cards: {hand}, your current score: {current_score}")
#         print("Dealer's hand is: X")
#         print("You went over 21. Bust, you lose!")
#
#     if hit_or_stand == "n":
#         # if the dealer's hand is under 21, make it draw another card
#         # if it is close to 20, make it not draw any more cards
#         print(f"Your score is {current_score}. Dealer's score is: {dealer_current_score}.")
#
#         #if score over 21 you lose
#
# if game_start == "n":
#     print("Bye, have a wonderful day!")

import random


def handle_ace(hand, current_score):
    """Adjust for ace being 1 or 11 based on the current score."""
    if 11 in hand and current_score > 21:
        current_score -= 10
    return current_score


def dealer_logic(dealer_hand, dealer_current_score):
    """Dealer keeps hitting if score is less than 17."""
    while dealer_current_score < 17:
        dealer_hand.append(random.choice(cards))
        dealer_current_score = sum(dealer_hand)
        dealer_current_score = handle_ace(dealer_hand, dealer_current_score)
        print(f"Dealer's hand: {dealer_hand}, Dealer's current score: {dealer_current_score}\n")
    return dealer_current_score


def compare_scores(player_score, dealer_score):
    """Determine the winner."""
    if player_score > 21:
        print("You went over 21. Bust, you lose!\n")
    elif dealer_score > 21:
        print(f"Dealer busts! You win with {player_score}.\n")
    elif player_score > dealer_score:
        print(f"You win with {player_score} against dealer's {dealer_score}.\n")
    elif dealer_score > player_score:
        print(f"Dealer wins with {dealer_score} against your {player_score}.\n")
    else:
        print(f"It's a draw! Both have {player_score}.\n")


game_start = input("Do you want to play Blackjack? Type 'Y' or 'N': ").lower()

if game_start == "y":
    print(f"\n" * 20)

    while True:
        import art

        print(art.logo)

        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        # Initial setup
        player_hand = random.choices(cards, k=2)
        dealer_hand = random.choices(cards, k=2)

        player_score = sum(player_hand)
        dealer_score = sum(dealer_hand)

        player_score = handle_ace(player_hand, player_score)
        dealer_score = handle_ace(dealer_hand, dealer_score)

        print(f"Your cards: {player_hand}, current score: {player_score}\n")
        print(f"Dealer's first card: {dealer_hand[0]}\n")

        # Player's hit or stand loop
        while player_score < 21:
            hit_or_stand = input("Type 'Y' to Hit or 'N' to Stand: ").lower()
            if hit_or_stand == 'y':
                player_hand.append(random.choice(cards))
                player_score = sum(player_hand)
                player_score = handle_ace(player_hand, player_score)
                print(f"Your cards: {player_hand}, current score: {player_score}\n")
            else:
                break

        # Dealer logic (dealer must hit until >= 17)
        if player_score <= 21:
            dealer_score = dealer_logic(dealer_hand, dealer_score)

        # Compare scores and determine the result
        print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}\n")
        compare_scores(player_score, dealer_score)

        keep_going = input("Would you like to keep playing? Type 'Y' or 'N': ").lower()
        if keep_going == "n":
            print("Bye, have a wonderful day!")
            break

elif game_start == "n":
    print("Bye, have a wonderful day!")
