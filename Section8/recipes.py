import shelve
# Once it's been written to the file the database for the variables is stored
# Shelve is good as a general database, but it's not really portable and also the files that execute the shelve calls would need to be stored with
# Shelve potentially exposing them to tampering


# blt = ["bacon", "lettuce", "tomato", "bread"]
# beansOnToas = ["beans", "bread"]
# scrambledEggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open("recipe", writeback=True) as recipe:
    # recipe["blt"] = blt
    # recipe["beans on toast"] = beansOnToas
    # recipe["scrambled eggs"] = scrambledEggs
    # recipe["pasta"] = pasta
    # recipe["soup"] = soup

    #To add items to a shelve dictionary you can't just use append because shelf doesn't know that the items have been updated or
    # You can enable writeback in shelve to use the append method
    tempList = recipe["blt"]
    tempList.append("butter")
    recipe["blt"] = tempList

    tempList = recipe["pasta"]
    tempList.append("tomato")
    recipe["pasta"] = tempList

    # Using the append method with writeback to be true
    # The disadvantage of this is it takes more memory and waits to write until the file is closed
    recipe["soup"].append("coutons")

    for snack in recipe:
        print(snack, recipe[snack])