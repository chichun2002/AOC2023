file = open("input.txt", "r")
lines = file.readlines()

print(lines)

time = []
record = []

times = [int(line) for line in lines[0].split()[1:]]
records = [int(line) for line in lines[1].split()[1:]]

new_records_list = []

for id, time in enumerate(times):

    new_records = 0

    for i in range(time+1):
        distance = (i*(time-i))
        if distance > records[id]:
            new_records += 1

    new_records_list.append(new_records)

print(new_records_list)

product = 1

for item in new_records_list:
    product *= item

print(product)