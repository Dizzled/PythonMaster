#The {0:2} the 2 value indicates the field width and the first value is the placeholder for i (variable)

for i in range(1,13):
    print("Number {0:2} squared is {1:4} cubed is {2:4}".format(i,i**2,i**3))

#If you want the values to be left aligned you can use the < symbol
for i in range(1, 13):
    print("Number {0:<2} squared is {1:<4} cubed is {2:<4}".format(i,i**2,i**3))



#You can use the f idiom for floating point values. The precision of python generally only goes up to 52 digits
print("PI is approximately {0:2}".format(22/7))
print("PI is approximately {0:2f}".format(22/7))
print("PI is approximately {0:12.50f}".format(22/7)) #In this case python cared more about precision than about proper field width
print("PI is approximately {0:52.50f}".format(22/7))
print("PI is approximately {0:62.50f}".format(22/7))

#You can also omit the actual values and just include the field width and python will still produce an output
for i in range(1, 13):
    print("Number {} squared is {} cubed is {:4}".format(i,i**2,i**3))

#Now in Python version 3.6 you can use f-strings, but it's not backwards compatible with versions prior to this. It's very similar
#To a replacement field the only difference is that you don't have to use the .format() at the end

age = 23

print(f"Number {age}")

print(f"pi is equal {22/7:12.50f}")

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[:-1:5])

flower = "blue violet"
print('blue' in flower)
