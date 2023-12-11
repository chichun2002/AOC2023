def search(grid, x, y):
    grid_x = len(grid) - 1
    grid_y = len(grid[0]) - 1
    
    search = []

    vector = [[1,1],[1,0],[1,-1],[0,1],[0,-1],[-1,1],[-1,0],[-1,-1]]
    for coord in vector:
        dx = x+coord[0]
        dy = y+coord[1]

        # print(f"x {dx} {grid_x}")
        # print(f"y {dy} {grid_y}")

        if dx > grid_x or dx < 0 or dy > grid_y or dy < 0:
            # print("flag")
            continue
        
        if grid[dx][dy] == "*":
            search.append([dx,dy])
    
    return search


file = open("input.txt","r")
lines = file.readlines()

grid = []

for i, line in enumerate(lines):
    grid.append([])
    for character in line:
        if character != '\n':
            grid[i].append(character)

# print(grid)
# print(search(grid, 10, 9))

number_gears = []
number = ""
gears = []

for x, line in enumerate(grid):
    if number and gears:
                number_gears.append([number,gears])
    number = ""
    gears = []

    for y, character in enumerate(line):
        if character.isdigit():
            number += character

            gear_search = search(grid,x,y)

            if gear_search:
                print(gear_search[0])
                for gear in gear_search:
                    if gear not in gears:
                        gears += [gear] 
        else:
            if number and gears:
                number_gears.append([number,gears])
            number = ""
            gears = []

print(number_gears)

def number_search(data, coord):
    numbers = []
    for number in data:
        if coord in number[1]:
            numbers.append(number[0])
    return numbers
    
total = 0
for x, line in enumerate(grid):
    for y, character in enumerate(line):
        if character == "*":
            numbers = number_search(number_gears, [x,y])
            print(numbers)
            if len(numbers) == 2:
                total += (int(numbers[0]) * int(numbers[1]))
print(total)