locations = {0: "Your sitting in front of a computer learning Python",
             1: "Your are standing at the end of a road before a small brick building",
             2: "Your are at the top of a hill",
             3: "You are inside the building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

words = {"NORTH": "N", "SOUTH": "S", "EAST": "E", "WEST": "W"}


loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits + " ").upper()
    print()

    if direction in exits[loc]:
        loc = exits[loc][direction]

    elif direction in words:
        print(words.items())
        loc = exits[loc][words[exits[loc][direction]]]

    else:
        print("You cannot go in that direction")