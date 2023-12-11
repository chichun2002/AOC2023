file = open("input.txt", "r")
lines = file.readlines()


def KeyFunction(input):
    output = int(input[2])
    for value in input[0]:
        output *= 100
        if value == "A":
            output += 14
        elif value == "K":
            output += 13
        elif value == "Q":
            output += 12
        elif value == "J":
            output += 1
        elif value == "T":
            output += 10
        else:
            output += int(value)
    return output

hands = []
bets = []

for line in lines:
    line = line.split()
    hands.append([line[0], line[1]])

for hand in hands:
    hand_copy = hand[0]
    hand_no_joker = hand_copy.replace("J", "")
    if len(hand_no_joker) > 0:
        hand_replaced_joker = hand_copy.replace("J", max(set(hand_no_joker), key=hand_no_joker.count))
    else:
        hand_replaced_joker = hand_copy
    
    search = [hand_replaced_joker.count(card) for card in hand_replaced_joker]
    
    

    if 5 in search:
        hand.append("7")
    elif 4 in search:
        hand.append("6")
    elif 3 in search and 2 in search:
        hand.append("5")
    elif 3 in search:
        hand.append("4")
    elif search.count(2) == 4:
        hand.append("3")
    elif 2 in search:
        hand.append("2")
    else:
        hand.append("1")

    print(f"JOKERS {hand[0].count('J')} original {hand[0]} replaced {hand_replaced_joker} search {search} rank {hand[2]} no_jokers is {hand_no_joker}")

# for hand in hands:
#     search = hand[2]
    
#     joker_count = 
    
#     hand_copy = hand[0]
#     hand_copy = hand_copy.replace("J", "")

#     hand_no_joker = [hand_copy, line[1], [hand_copy.count(card) for card in hand_copy]]

#     search2 = list(set(search))
#     search2.sort()
    
    
#     # print(search2)

#     # if joker_count == 5:
#     #     largest_set = joker_count
#     # elif max(hand[0]) == "J":
#     #     if len(search2) == 1:
#     #         largest_set = joker_count + search2[-1]
#     #     else:
#     #         largest_set = joker_count + search2[-2]
#     # else:
#     #     largest_set = joker_count + max(search)

#     # joker_count

#     if joker_count == 5:
#         largest_set = 5
#     else:
#         largest_set = joker_count + max(hand_no_joker[2])
    
#     print(f"largest set{largest_set}")
    
#     if largest_set == 5:
#         hand.append("7")
#     elif largest_set == 4:
#         hand.append("6")
    
#     elif largest_set == 3 and hand_no_joker[2].count(2) == 4:
#         hand.append("5")
    
#     elif largest_set == 3:
#         hand.append("4")
    
#     elif search.count(2) == 4:
#         hand.append("3")
    
#     elif largest_set == 2:
#         hand.append("2")
#     else:
#         hand.append("1")
    
#     print(f"{hand} joker count {joker_count} {hand_no_joker}")

# print(hands)

# for hand in hands:
#     print(KeyFunction(hand))

hands = sorted(hands, key=KeyFunction)

sum = 0
for i, hand in enumerate(hands):
    bet = int(hand[1])
    # print(f"{bet} * {i+1}")
    sum += bet * (i+1)

print(sum)


