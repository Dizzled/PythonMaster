imelda = "More Mayhem", "Imelda May", 2011, ((1, "Pulling the Rug"), (2, "Psyco"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

for items in imelda:
    if(imelda.index(items) >= 3):
        print('\t', items)
    else:
        print(items)

# Unpacking the tuple in this case gives us
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)

for track in tracks:
    print('\t', track)

# Or to unpack it further you can
print("==="*20)
for track in tracks:
    number, song = track
    print('\t', number, song)

even = range(0, 20, 2)

for number in even[::-1]:
    print(number, end=', ')
