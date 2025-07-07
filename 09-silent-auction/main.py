from art import logo
print(logo)

def winner(dict):
    high_bid = {"name": 0}
    for key in dict:
        if dict[key] > high_bid["name"]:
            high_bid["name"] = dict[key]
    print(high_bid)

auction_list = {}
auction_done = False
while not auction_done:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    auction_list[name] = bid
    bidders = input("Other bidders, 'yes' or 'no'?: ").lower()
    if bidders == "no":
        auction_done = True

print(auction_list)
winner(auction_list)
