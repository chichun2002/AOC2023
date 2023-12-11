f = open("input.txt", "r")
lines = f.readlines()
# print(lines)
games = []
for line in lines:
    max_game = {'red' : 0, 'blue' : 0,'green' : 0}
    
    line = line[line.find(':')+1:-1]
    line = line.split()
    for id, word in enumerate(line):
        # print(word)
        if "blue" in word:
            max_game['blue'] = max(max_game['blue'],int(line[id-1]))
        if "red" in word:
            max_game['red'] = max(max_game['red'],int(line[id-1]))
        if "green" in word:
            max_game['green'] = max(max_game['green'],int(line[id-1]))
    games.append(max_game)

# red = int(input())
# green = int(input())
# blue = int(input())

# sum = 0
# for id, game in enumerate(games):
#     if red < game["red"]:
#         continue
#     if green < game["green"]:
#         continue
#     if blue < game["blue"]:
#         continue
#     sum += (id+1)
# print(sum)

sum = 0
for id, game in enumerate(games):
    sum += (game['red']*game["green"]*game["blue"])
print(sum)