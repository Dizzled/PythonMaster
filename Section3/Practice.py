thing = "My Name is Steve"
number = "9,223,372:456;456 487,807"


letters = "abcdefghijklmnopqrstuvwxyz"

#Print starting index 16 to index 13 in reverse
print(letters[16:13:-1])

#Print all the letters in steps of one
print(letters[::1])

#Print the first two letters
print(letters[:2])

#Print letters in Reverse
print(letters[::-1])

#Idiom if string is empty using print(index[0]) will crash
print(letters[:1]) # Does not crash if string is empty