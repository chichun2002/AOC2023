file = open("input.txt", "r")
lines = file.readlines()

data_numbers = []
data_winning = []

for line in lines:
    line = line.split(":")
    line = line[1].split("|")
    numbers = line[0].split()
    winning = line[1].split()
    data_numbers.append(numbers)
    data_winning.append(winning)

multipliers = []
for data in data_numbers:
    multipliers.append(1)

print(multipliers)
for i, data in enumerate(data_numbers):
    value = (len(set(data) & set(data_winning[i])))
    print(value)
    for j in range(value):
        print(j)
        multipliers[i+j+1] += (1*multipliers[i])
        print(multipliers)

print(sum(multipliers))