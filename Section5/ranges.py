# even = list(range(0,100,2))#Create even range
# odd = list(range(0,100,1))#Create odd range
#
# print(even)
# print(odd)

#You can slice an array with slicing and the values can create a new array object
# decimals = range(0, 100)
# print(decimals)
#
# myRange = decimals[3:100:3]
#
# for i in myRange:
#     print(i)
# print("==" * 45)
# print(myRange == decimals[3:100:3])
#
# r = range(0,10)
# for i in r[::-1]:
#     print(i)

o = range(0, 100, 4)
print(o)
p = o[0::5]
print(p)
for i in p:
    print(i)