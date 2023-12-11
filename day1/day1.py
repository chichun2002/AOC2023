f = open("input.txt", "r")
lines = f.readlines()
total = 0
for line in lines:
    output = [i for i in line if i.isdigit()]
    total += int(output[0] + output[-1])

print(total)