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

print(data_numbers)
print(data_winning)

total = 0
for i, data in enumerate(data_numbers):
    value = ((len(set(data) & set(data_winning[i])))-1)
    if value >= 0:
        total +=2**value
    print(total)