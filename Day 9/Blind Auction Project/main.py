import art
print(art.logo)
# TODO-1: Ask the user for input
bids = {}
while True:
    name = str(input("What is your name?: "))
    price = int(input("What is your bid?: "))

# TODO-2: Save data into dictionary {name: price}

    bids[name] = price

# TODO-3: Whether if new bids need to be added
    more_bids = input("Will there be others to bid? 'Yes' or 'No': ").lower()

    if more_bids == "no":
        break

    else:
        print("\n" * 20)

# TODO-4: Compare bids in dictionary
highest_bidder = max(bids, key=bids.get)
highest_bid = bids[highest_bidder]

print(f"The winner is: {highest_bidder}, with the highest bid: {highest_bid}")

# def find_highest_bidder(bidding_dictionary):
#     highest_bid = 0
#     for bidder in bidding_dictionary:
#         bid_amount = bidding_dictionary(bidder)
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#
#     print(f"The winner is {winner} with a bid of ${highest_bid}")