# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

testlist = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","f","w","x","y","z"}
testlist2 = "abcdefghijklmnopqrstufwxyz"
test = set(testlist2)
notVowels = set()
vowels = "a", "e", "i", "o", "u"
vowels2 = "aeiou"
vowelSet = frozenset(vowels2)

notVowels = test.difference(vowelSet)
print(sorted(notVowels))
