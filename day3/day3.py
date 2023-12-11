f = open("input.txt", "r")
lines = f.readlines()
# print(len(lines))
# print(len(lines[0]))


def search(matrix, x, y):
    list = []
    for i in range(3):
        for j in range(3):
            intx = max(x-1+i, 0)
            inty = max(y-1+j, 0)
            intx = min(intx, len(matrix)-1)
            inty = min(inty, len(matrix[0])-1)
            list.append(matrix[intx][inty])

    return list

matrix = []

for i, line in enumerate(lines):
    matrix.append([])
    for character in line:
        if character != '\n':
            matrix[i].append(character)

symbols = ["1","2","3","4","5","6","7","8","9","0","."]
store = []
digit = []
for x, i in enumerate(matrix):
    # print(i)
    for y, j in enumerate(i):
        
        # continue
        # print(x)
        if j.isdigit():
            digit.append(j)
            
            if not all(t in symbols for t in search(matrix, x, y)):
                   digit.append(True)
        else:
            if digit != []:
                store.append(digit)
            digit=[]
        # print(store)
# print(search(matrix, 0, 0))
# print(store)
# for line in lines:
sum = 0
for entry in store:
    if True in entry:
        
        l = [i for i in entry if type(i)==str]
        output = ""
        for value in l:
            output += value
        # print(output)
        sum += int(output)

print(sum)

