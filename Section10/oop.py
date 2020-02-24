# a = 12
# # b = 4
# # print(a + b)
# # print(a.__add__(b)) # Each uses the same built in method everything is an object!
class Kettle(object):
    # Self is standard convention and is a reference to the instance of the object
    # The init is the constructor for the function
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switchOn(self):
        self.on = True

kenwood = Kettle("Kenwood", 99)

print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.23
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print(hamilton.make)
print(hamilton.price)

# Objects with their parameters in the specified argument fields
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
"""
print(hamilton.on)
hamilton.switchOn()
print(hamilton.on)
# An alternative way to call the class function
Kettle.switchOn(kenwood)
print(kenwood.on)

# Class objects are mutable and can be changed unlike Class objects in C++ or Java
kenwood.power = 1.5
print(kenwood.power)