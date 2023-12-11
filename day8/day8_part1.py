file = open("input.txt", "r")
lines = file.readlines()

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

for line in lines[2:]:
    line = line.split()
    graph.append_node(line[0],line[2][1:-1],line[3][:-1])

node = "AAA"
steps = 0

# graph.print()

while node != "ZZZ":
    for char in lines[0][:-1]:
        if char == "R":
            node = graph.right(node)
        if char == "L":
            node = graph.left(node)
        steps += 1
        print(steps)
    
print(steps)