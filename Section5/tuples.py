t = "a", "b", "c"
print(t)
z = 'a', 'b','c'
print(z)
# You need a double parenthesis to remove the quotations when printing tuples
# Also tuples are immutable but you can change with indexing or slicing
print("a","b","c")
print (("a", "b", "c"))

welcome = "Welcome to my nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company",  1974

print(welcome)
print(welcome[0])

# Can't change the tuple object it's immutable
# Welcome[0] = "Trying to change a tuple"

welcome = welcome[0], "Jimmy Buffet", welcome[2]
# The above will work to change the tuple it's important to note that
# The object itself is immutable, but the variable is changeable difference between a list and a tuple
# A list is contained in the brackets of an array whereas a tuple is just the assignment with quotations

# list: Are intended to hold items of the same type
# Tuples: Are intended to hold items of different types but are constant
ruby = ["Dog", "Labrador", 9]
ruby2 = "Dog", "Labrador", 9
print(ruby)
print(ruby2)

# Unpacking the tuple
animal, breed, age = ruby2
print(animal, breed, age)

# The append function can only be used with a list item
ruby.append("90lbs")
print(ruby)

# Will return an error because there's 4 items in the list that need  assignment
#animal, breed, age = ruby

#You can store a list inside a tuple which then in turn makes the tuple listm modifyable

imelda = "More Mayhem", "Imelda May", 2011, [(1, "Pulling the Rug"), (2, "Psyco"), (3, "Mayhem"), (4, "Kentish Town Waltz")]
imelda[3].append((5, "Stuck"))

#Or you can append the tuple item in this way
albut, artist, year, track = imelda
track.append()

print(imelda)
