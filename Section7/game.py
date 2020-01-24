# Using split to create a more robust form of checking for if word contains
locations = {0: "Your sitting in front of a computer learning Python",
             1: "Your are standing at the end of a road before a small brick building",
             2: "Your are at the top of a hill",
             3: "You are inside the building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

# print(locations[0].split())
# print(locations[3].split(","))
# print(''.join(locations[0].split()))

exits = {0: {"Q": 0},
         1: {"W": 2, "2": 2, "E": 3, "3": 3, "N": 5, "5": 5, "4": 4, "S": 4, "Q": 0},
         2: {"N": 5, "5": 5, "Q": 0},
         3: {"W": 1, "1": 1, "Q": 0},
         4: {"N": 1, "1": 1, "W": 2, "2": 2, "Q": 0},
         5: {"W": 2, "2": 2, "S": 1, "1": 1, "Q": 0}}

words = {"QUIT": "Q", "NORTH": "N", "SOUTH": "S", "EAST": "E", "WEST": "W", "ROAD": "1", "HILL": "2", "BUILDING": "3", "VALLEY": "4", "FORREST": "5"}

namedExits = {1: {"2": 2, "3" : 3, "4" : 4, "5" : 5},
              2: {"5": 5},
              3: {"1": 1},
              4: {"1": 1, "2": 2},
              5: {"2": 2, "1": 1}}

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(namedExits[loc])

    direction = input("Available exits are " + availableExits + " ").upper()
    print()
    if len(direction) > 1:
        direct = direction.split()
        for word in direct:
            if word in words:
                direction = words[word]
                break

    if direction in allExits:
        loc = allExits[direction]

    else:
        print("You cannot go in that direction")