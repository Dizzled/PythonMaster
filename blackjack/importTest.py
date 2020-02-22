import blackjack

# print(blackjack)
# print(__name__)
# # Starting a name with an underscore means it should not be changed ie. private
# if __name__ == '__main__':
#     blackjack.play()

# g = sorted(globals())
# for x in g:
#     print(x)
#
# # Functions that start with an underscore won't be imported as they're private
# blackjack._dealCard()
#
# blackjack.play()

personal_details = ("dustin", 37, "Alaska")


# Underscore values as a variable are just unused values that are to be thrown away
name, _, state = personal_details
print(name, state)
print(_)