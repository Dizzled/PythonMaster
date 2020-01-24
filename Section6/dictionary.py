#An unordered selection .split and .join can't use the index number, but we can use a key
# The dictionary key is hashed so there's no guarantee that the items will iterate in the same manner (see the example at the bottom)

fruit = { "orange": "a sweet, orange, citrus fruit",
          "apple": "good for making cider",
          "lemon": "a sour, yellow citrus fruit",
          "grape": "a small, sweet fruit",
          "lime": "a sour, green citrus fruit"}

print(fruit)
# To access and item select the key as the dictionary is not selectable by index
print(fruit["lemon"])

bike = {"make": "Honda", "model": "250 dream", "color": "red", "engine_size": 250}
print(bike)
bike["year"] = "1981 - 1999"
print(bike)

# To clear the last item vs delete the item
bike.clear()
print(bike)

#del fruit["lime"]
#print(fruit)
#
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if( dict_key == "Q"):
#         break
#     else:
#         print("No " + dict_key)
#     description = fruit.get(dict_key)
#     print(description)

ordered_key = list(fruit.keys())
ordered_key.sort()
# The equivalent thing with one less line of code
ordered_keys = sorted(list(fruit.keys()))
for f in ordered_keys:
    print (f + ' - ' + fruit[f])
# If you aren't using the ordered keys value at the end then you can
# Simplify this
for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])