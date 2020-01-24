#Shelve like a dictionary is unordered, but on some systems will return the dict alphabetical
import shelve
#
# with shelve.open("bike2") as bike:
#     bike["Make"] = "Honda"
#     bike["model"] = "CB 750"
#     bike["color"] = "Green"
#     bike["engine_Size"] = 750

    # for key in bike:
    #     print(key)
    #
    # print('=' * 40)
    #
    # print(bike["engine_Size"])
    # #print(bike["engin_size"])
    # print(bike["color"])



fruit = shelve.open("FruitTest")
fruit["lemon"] = "A small yellow citrus fruit"
fruit["lime"] = " Kinda like a lemon but green"
fruit["apple"] = "A small delicious crispy fruit"
fruit["grape"] = "A round sweet fruit used in wine"
fruit["tomatoe"] = "Not really considered a fruit but it is"


#Sorting the keys into an alphabetical list
orderedKeys = list(fruit.keys())
orderedKeys.sort()

for f in orderedKeys:
    print(f + " - " + fruit[f])
print('=' * 40)
#Listing the items similar to dictionary but a shelve key will only accept a sting
for v in fruit.values():
    print(v)
print(fruit.values())
print('=' * 40)
for f in fruit.items():
    print(f)
print(fruit.items())
print('=' * 40)
while True:
    shelfKey = input("Please Enter a fruit: ")
    if shelfKey == "Q":
        break
    #Using get to return the object in the dictionary
    description = fruit.get(shelfKey)
    print(description)

fruit.close()