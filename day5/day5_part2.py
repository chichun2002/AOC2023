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

# for map in maps:
#     print(map)

# print([int(x) for map in maps for entry in map for x in entry])

print(seeds)

seed_history = []
seed_history.append(seeds)

# print(map)

# for id, map in enumerate(maps):
#     # print(map)
#     seeds = []
#     for i, seed in enumerate(seed_history[id]):
#         for item in map:

#             if seed >= item[1] and seed <= (item[1] + item[2]):
#                 seeds.append(item[0]+(seed-item[1]))
#                 break
#         else:
#             seeds.append(seed)
#     seed_history.append(seeds)

# print(min(seed_history[-1]))
# # print (len(maps))