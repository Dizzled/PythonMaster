even = set(range(0, 40, 2))

squaresTuple = (4,6,9,16,25)
squares = set(squaresTuple)

print(sorted(even))
print(squares)

# Even difference_update acts on the even set
# even.difference_update(squares)
# print(sorted(even))

# Symmetric difference is the opposite of intersection
# print("Symmetric even minus squares\n")
# print(sorted(even.symmetric_difference(squares)))
#
# # This will print out a sorted squares even though sorted wasn't called on this is unreliable and a quark
# print("Symmetric squares minus even \n")
# print(squares.symmetric_difference(even))

squares.discard(4)
squares.remove(16)
squares.discard(8) # No error both remove and discard have same behavior but remove will have error if item is not present
try:
    squares.remove(8) # Error if using then error check prior
except KeyError:
    print("The item 8 is not in the set")

# Issubset vs. Issuperset
if squares.issubset(even):
    print("Squares is a subset of even")
if even.issuperset(squares)
    print("Even is superset of squares")
