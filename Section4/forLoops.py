# for s in ["some thing", "has happened", "to me", "and I'm trying to avoid it"]:
#     print("Jerry " + s)
#
# #for k in range(0,50,5):
#     for j in range (0,10):
#         print(f"{k} times {j} = {k * j}", end="\n")
#
# quote = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?
# """
# for char in quote:
#     if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         print(char)
#
# for i in range(0, 101):
#     remainder = i % 7
#     if remainder is 0:
#         print(i)
#
# remainder = 0
# for i in range(0,100):
#     remainder = i % 11
#     print(i)
#     if remainder == 0 and i != 0:
#         break

#print all the numbers in the range 0 - 20 that aren't divisible by 5
for i in range(0,20):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)
