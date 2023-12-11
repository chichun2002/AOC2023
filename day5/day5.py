import numpy as np

file = open("input.txt", "r")
lines = file.readlines()

maps = []
store = []

for id, line in enumerate(lines):
    
    if any(char.isdigit() for char in line)  and id > 1:
        out = [int(x) for x in line.split()]
        store.append(out)
    
    if "seeds:" in line:
        seeds = [int(x) for x in line.split()[1:]]
        print(f"seeds {seeds}")
    if "seed-to-soil map:" in line:
        store = []
    if "soil-to-fertilizer map:" in line:
        maps.append(store)
        store = []
    if "fertilizer-to-water map:" in line:
        maps.append(store)
        store = []
    if "water-to-light map:" in line:
        maps.append(store)
        store = []
    if "light-to-temperature map:" in line:
        maps.append(store)
        store = []
    if "temperature-to-humidity map:" in line:
        maps.append(store)
        store = []
    if "humidity-to-location map:" in line:
        maps.append(store)
        store = []
maps.append(store)

range_list = []
for i, seed in enumerate(seeds):
    if i % 2 == 0:
        range_list.append([seed,seed+seeds[i+1]])



# print(maps[0])

ranges = []
ranges.append(range_list)

print(ranges)

for i, map in enumerate(maps):
    print("new_map")
    range_list = []

    for range in ranges[i]:
        
        old_range = range.copy()
        new_range = range.copy()
        # print(range)

        for transform in map:
            new_range = range.copy()
            old_range = range.copy()
            if range[0] >= transform[1] and range[0] <= transform[1]+transform[2]-1:
                
                new_range[0] = transform[0]+(range[0]-transform[1])
                if range[1] <= transform[1]+transform[2]-1:
                    new_range[1] = transform[0]+(range[1]-transform[1])
                    range = [0,0]
                else:
                    new_range[1] = transform[0]+(transform[2])
                    range = [(transform[1]+transform[2]),range[1]]

            elif range[1] <= transform[1]+transform[2]-1 and range[1] >= transform[1]:
                
                new_range[1] = transform[0]+(range[1]-transform[1])
                if range[0] >= transform[1]:
                    new_range[0] = transform[0]+(range[0]-transform[1])
                    range = [0,0]
                else:
                    new_range[0] = transform[0]
                    range = [range[0],(transform[1]-1)]

            elif range[0] <= transform[1] and range[1] >= transform[1]+transform[2]-1:
                new_range = [transform[0],transform[0]+transform[2]]
                temp_range = range.copy()
                print(f"branches create {[temp_range[0],transform[1]-1]} {[transform[1] + transform[2],temp_range[1]]}")
                ranges[i].append([temp_range[0],transform[1]-1])
                ranges[i].append([transform[1] + transform[2],temp_range[1]])
                range = [0,0]

            if new_range != old_range:
                range_list.append(new_range.copy())
            print(f"{old_range} mapped to {new_range} given {transform} debug creation {range}")

            if range == [0,0]:
                break
        
        if new_range == old_range:
            range_list.append(old_range.copy())

    ranges.append(range_list.copy())
    # print(f"apended {range_list}")

print("\n")
for range in ranges:
    print(range)
    print("\n")

print(min(value[0] for value in ranges[-1]))