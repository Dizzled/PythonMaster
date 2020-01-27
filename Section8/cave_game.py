import shelve

vocab = shelve.open('vocabulary')
location = shelve.open('locations')

locations = location['locations']
vocabulary = vocab['vocabulary']

print(vocabulary, locations)
loc = 1

while True:
    #Since now there's a master dictionary the location keys
    availableExits = ", ".join(locations[loc]["exits"].keys())
    print(locations[loc]["desc"])

    if loc == 0:
        break
    else:
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["namedExits"])

    direction = input("Available exits are " + availableExits).upper()
    print()

    # Parse the user input, using our vocabulary dictionary if necessary
    if len(direction) > 1:  # more than 1 letter, so check vocab
        words = direction.split()
        for word in words:
            if word in vocabulary:  # does it contain a word we know?
                direction = vocabulary[word]
                break

    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go in that direction")

vocabulary.close()
locations.close()
