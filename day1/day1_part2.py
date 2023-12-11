def replaceid(line, id, text, num):
    out = line
    if line[id:id+len(text)] == text:
        # out = line[0:id] + str(num) + line[id+len(text):-1]
        return str(num)


f = open("input.txt", "r")
lines = f.readlines()
total = 0
for line in lines:
    new_line = []
    for id, character in enumerate(line):
        # print(character)
        if character == 'o':
            new_line.append(replaceid(line, id, "one", 1))
        if character == 't':
            new_line.append(replaceid(line, id, "two", 2))
            new_line.append(replaceid(line, id, "three", 3))
        if character == 'f':
            new_line.append(replaceid(line, id, "four", 4))
            new_line.append(replaceid(line, id, "five", 5))
        if character == 's':
            new_line.append(replaceid(line, id, "six", 6))
            new_line.append(replaceid(line, id, "seven", 7))
        if character == 'e':
            new_line.append(replaceid(line, id, "eight", 8))
        if character == 'n':
            new_line.append(replaceid(line, id, "nine", 9))
        if character.isdigit():
            new_line.append(character)
    # print(new_line)
    # new = line.replace("one","1")
    # line = line.replace("two","2")
    # line = line.replace("three","3")
    # line = line.replace("four","4")
    # line = line.replace("five","5")
    # line = line.replace("six","6")
    # line = line.replace("seven","7")
    # line = line.replace("eight","8")
    # line = line.replace("nine","9")
    output = [i for i in new_line if i != None]
    # print(output)
    # print(int(output[0] + output[-1]))
    total += int(output[0] + output[-1])

print(total)

