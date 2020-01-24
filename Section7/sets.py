# UNORDERED and doesn't contain duplicates similar to a dictionary in its creation the difference is a set doesn't contain a key
# If you want to create an empty set you need to use the built in set function otherwise it will create a dictionary if you only use the curly braces

farmAnimals = {"sheep", "cow", "hen"}
print(farmAnimals)

for animal in farmAnimals:
    print(animal)

# Keyword built in function
wildAnimals = set(["boar", "tiger", "baboon", "eagle"])
print(wildAnimals)

for wild in wildAnimals:
    print(wild)

farmAnimals.add("horse")
wildAnimals.add("horse")

print(farmAnimals)
print(wildAnimals)
print("++" * 40)
emptySet = set()
#emptySet2 = {}

emptySet.add("pig")
# emptySet2.add("pig")

# Need to use the set constructor to create a set #
even = set(range(0, 40, 2))
print(even)
squaresTuple = (4,6,9,16,25)
squares = set(squaresTuple)
print(squares)
print(len(squares))
# Use the built in union to join sets
print(even.union(squares))
print(len(even.union(squares)))

print(squares.union(even))

print("++" * 40)
# Using the built in intersection to show where the sets contain the same numbers

print(even.intersection(squares))
print(even & squares)
print(squares.intersection(even))
print(squares & even)


# You can use built ins to subtract sets from each other difference
even = set(range(0, 40, 2))
print(sorted(even))
squaresTuple = (4,6,9,16,25)
squaresSet = set(squaresTuple)
print(sorted(squaresSet))

print("even minus squaresSet")
print(sorted(even.difference(squaresSet)))
print(sorted(even - squaresSet))

print("squares minus even")
print(squaresSet.difference(even))
print(squaresSet - even)

newSet = squaresSet.difference(even)
print(newSet)

