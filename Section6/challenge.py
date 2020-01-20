# locations = {0: "Your sitting in front of a computer learning Python",
#              1: "Your are standing at the end of a road before a small brick building",
#              2: "Your are at the top of a hill",
#              3: "You are inside the building, a well house for a small stream",
#              4: "You are in a valley beside a stream",
#              5: "You are in the forest"}
#
# exits = {0: {"Q": 0},
#          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#          2: {"N": 5, "Q": 0},
#          3: {"W": 1, "Q": 0},
#          4: {"N": 1, "W": 2, "Q": 0},
#          5: {"W": 2, "S": 1, "Q": 0}}
#
# words = {"QUIT": "Q", "NORTH": "N", "SOUTH": "S", "EAST": "E", "WEST": "W"}
#
# loc = 1
# while True:
#     availableExits = ", ".join(exits[loc].keys())
#     print(locations[loc])
#
#     if loc == 0:
#         break
#
#     direction = input("Available exits are " + availableExits + " ").upper()
#     print()
#
#     if direction in exits[loc]:
#         loc = exits[loc][direction]
#
#     elif direction in words:
#         direction = words.get(direction)
#
#         if direction in exits[loc]:
#             loc = exits[loc][direction]
#
#     else:
#         print("You cannot go in that direction")

# Another Variation that Takes into account all words
#
# locations = {0: "Your sitting in front of a computer learning Python",
#              1: "Your are standing at the end of a road before a small brick building",
#              2: "Your are at the top of a hill",
#              3: "You are inside the building, a well house for a small stream",
#              4: "You are in a valley beside a stream",
#              5: "You are in the forest"}
#
# exits = {0: {"Q": 0},
#          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#          2: {"N": 5, "Q": 0},
#          3: {"W": 1, "Q": 0},
#          4: {"N": 1, "W": 2, "Q": 0},
#          5: {"W": 2, "S": 1, "Q": 0}}
#
# words = {"QUIT": "Q", "NORTH": "N", "SOUTH": "S", "EAST": "E", "WEST": "W"}
#
# loc = 1
# while True:
#     availableExits = ", ".join(exits[loc].keys())
#     print(locations[loc])
#
#     if loc == 0:
#         break
#
#     direction = input("Available exits are " + availableExits + " ").upper()
#     print()
#     if len(direction) > 1:
#         for word in words:
#             if word in direction:
#                 direction = words[word]
#
#     if direction in exits[loc]:
#         loc = exits[loc][direction]
#
#     else:
#         print("You cannot go in that direction")


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
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

words = {"QUIT": "Q", "NORTH": "N", "SOUTH": "S", "EAST": "E", "WEST": "W"}

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits + " ").upper()
    print()
    if len(direction) > 1:
        direct = direction.split()
        for word in direct:
            if word in words:
                direction = words[word]
                break

    if direction in exits[loc]:
        loc = exits[loc][direction]

    else:
        print("You cannot go in that direction")