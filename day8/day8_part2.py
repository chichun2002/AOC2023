import numpy as np
from math import gcd

file = open("input.txt", "r")
lines = file.readlines()

def lcm(a,b):
    return int(abs(a*b) / gcd(a,b))

class Graph:
    def __init__(self):
        self.nodes = {}
        self.start = None

    def append_node(self, node, left, right):
        if self.nodes == {}:
            self.start = node
        self.nodes.update({node : [left, right]})
    
    def right(self, input):
        return self.nodes[input][1]
            
    def left(self, input):
        return self.nodes[input][0]
    
    def print(self):
        print(self.nodes)
    
graph = Graph()

starts = []

for line in lines[2:]:
    line = line.split()
    graph.append_node(line[0],line[2][1:-1],line[3][:-1])
    if line[0][-1] == "A":
        starts.append(line[0])

print(starts)


current_nodes = starts.copy()

phase = [0 for i in range(len(current_nodes))]

steps = 0

# while all(node[-1] != "Z" for node in current_nodes):
#     print(current_nodes)
#     for char in lines[0][:-1]:
#         for i, node in enumerate(current_nodes):
#             if char == "R":
#                 current_nodes[i] = graph.right(node)
                
#             if char == "L":
#                 current_nodes[i] = graph.left(node)

#         steps += 1
#     if all(node == "XXX" for node in current_nodes):
#         break

# print(steps)

flag = False
count = 0
while flag == False:
    for char in lines[0][:-1]:
        # print(lines[0][:-1])
        # print(f"changing chars{char}")
        for i, node in enumerate(current_nodes):
            # print(f"{char} {node}")
            if char == "R":
                node = graph.right(node)
                current_nodes[i] = node
                
            if char == "L":
                node = graph.left(node)
                current_nodes[i] = node

            if node[-1] == "Z" and phase[i] == 0:
                phase[i] = count + 1
        count += 1
        # print(current_nodes)
        if all(i != 0 for i in phase):
            break
    else:
        continue
    break
        # if count > 100:
        #     flag = True
print(phase)

multiple = 1
for i in phase:
    multiple = lcm(multiple, i)

print(multiple)

# node = "AAA"
# steps = 0

# # graph.print()

# while node != "ZZZ":
#     for char in lines[0][:-1]:
#         if char == "R":
#             node = graph.right(node)
#         if char == "L":
#             node = graph.left(node)
#         steps += 1
#         print(steps)
    
# print(steps)

