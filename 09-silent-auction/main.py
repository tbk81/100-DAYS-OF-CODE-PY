from art import logo

print(logo)


# def winner(my_dict):
#     high_bid = {"name": 0}
#     for key in my_dict:
#         if my_dict[key] > high_bid["name"]:
#             high_bid["name"] = my_dict[key]
#     print(high_bid)


auction_list = {}
auction_done = False
while not auction_done:
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: "))
    auction_list[name] = bid
    bidders = input("Other bidders, 'yes' or 'no'?: ").lower()
    if bidders == "no":
        high_bid = max(auction_list, key=auction_list.get)
        print(f"{high_bid} had the highest bid of ${auction_list[high_bid]}")
        auction_done = True
    elif bidders == "yes":
        print("\n"*100)
