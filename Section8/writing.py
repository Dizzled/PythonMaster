towns = ["Fairbanks", "Anchorage", "Juneau", "Kenai", "Soldotna"]

# with open("towns.txt",'w') as fileOut:
#     for town in towns:
#         #No spaces in file=out (a named argument)
#         print(town, file=fileOut)

# cities = []
# with open("towns.txt",'r') as fileIn:
#     for town in towns:
#         cities.append(town.strip('\n'))
# print(cities)
# for city in cities:
#     print(city)
#
#Strip off a portion of the text
print("Fairbanks".strip("F"))

imelda = "Artist", "Title", "Year", {1: "Song One ", 2: "Song Two "}
with open("songFile.txt", 'w') as songFile:
    print(imelda, file=songFile)


# This is a way to readback a tuple using eval to process the data but it's insecure way to use this as
# File contents can be malicious and then executed with eval
with open("songFile.txt", 'r') as songs:
    txt = songs.readline()

contents = eval(txt)
print(contents)
artist, title, year, song = contents
print(artist)
print(title)
print(year)
print(song)
