valid = ["1","2","3","4","5","6","7","8","9","0","."]

file = open("input.txt", "r")
lines = file.readlines()

def search (grid, x, y):
    v = []
    for i, dx in enumerate(range(-1 if (x > 0) else 0, 2 if (x < len(grid)-1) else 1)):
        v.append([])
        for dy in range(-1 if (y > 0) else 0, 2 if (y < len(grid[0])-1) else 1):
            v[i].append([(dx+x),(dy+y)])
    return v


grid = []

for i, line in enumerate(lines):
    grid.append([])
    for character in line:
        if character != '\n':
            grid[i].append(character)
# print(len(grid))
# print(len(grid[0]))
# print(grid[9][9])
# print(search(grid,9,9))
symbollist = []
for i, line in enumerate(lines):
    # print(i)
    for j, char in enumerate(grid[i]):
        # print(j)
        # print(char)
        if char is "*":
            symbollist.append(search(grid,i,j))

print(symbollist)
gears = []

for symbol in symbollist:
    concat = []
    for row in symbol:
        concat += row
    prev = "n"
    count = 0
    print(concat)
    for value in concat:
        if grid[value[0]][value[1]].isdigit() and not prev.isdigit():
            count+=1
        prev = grid[value[0]][value[1]]
    print(count)
    if count > 1:
        gears.append(concat)
print(gears)
for gear in gears:
    row = []
    for pair in gear:
        row += grid[pair[0]][pair[1]]
    print(row)
total = 0 
for gear in gears:
    prev = "n"
    row = []
    values = []
    for pair in gear:
        # print(prev)
        row += grid[pair[0]][pair[1]]
        if grid[pair[0]][pair[1]].isdigit() and not prev.isdigit():
            print(grid[pair[0]][pair[1]])
            num = []
            for i in range(-2,3):
                num += grid[pair[0]][i+pair[1]]
                # print(num)
            if not num[int(len(num)/2)+1].isdigit():
                num = num[int(len(num)/2)-2] + num[int(len(num)/2)-1] + num[int(len(num)/2)]
            elif not num[int(len(num)/2)-1].isdigit():
                num = num[int(len(num)/2)] + num[int(len(num)/2)+1] + num[int(len(num)/2)+2]
            else:
                num = num[int(len(num)/2)-1] + num[int(len(num)/2)] + num[int(len(num)/2)+1]
            
            num = ''.join(c for c in num if c.isdigit())
            # print(num)
            values.append(int(num))
            
        prev = grid[pair[0]][pair[1]]

    product = 1
    for i in values:
         product = product * i
    
    total += product
    print(row)
# print(gears)
print(total)
# num1=0
# total = 0
# for i, value in enumerate(values):
#     if i % 2 == 0:
#         # print(value)
#         num1 = int(value)
#     else:
#         total += num1 * int(value)
# print(total)