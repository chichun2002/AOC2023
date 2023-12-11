file = open("input.txt", "r")
lines = file.readlines()


def KeyFunction(input):
    output = int(input[3])
    for value in input[0]:
        output *= 100
        if value == "A":
            output += 14
        elif value == "K":
            output += 13
        elif value == "Q":
            output += 12
        elif value == "J":
            output += 11
        elif value == "T":
            output += 10
        else:
            output += int(value)
    return output

hands = []
bets = []

for line in lines:
    line = line.split()
    hands.append([line[0], line[1], [line[0].count(card) for card in line[0]]])



for hand in hands:
    search = hand[2]
    if 5 in search:
        hand.append("7")
    elif 4 in search:
        hand.append("6")
    elif 3 in search and 2 in search:
        hand.append("5")
    elif 3 in search:
        hand.append("4")
    elif search.count(2) is 4:
        hand.append("3")
    elif 2 in search:
        hand.append("2")
    else:
        hand.append("1")

print(hands)

# for hand in hands:
#     print(KeyFunction(hand))

hands = sorted(hands, key=KeyFunction)

sum = 0
for i, hand in enumerate(hands):
    bet = int(hand[1])
    print(f"{bet} * {i+1}")
    sum += bet * (i+1)

print(sum)


