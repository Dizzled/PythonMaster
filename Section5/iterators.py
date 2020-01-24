newList = []
newList.append("This is now in the list")
newList.append("And this is also in the list")
newList.append("Lines of lines")
iterator = iter(newList)
for char in newList:
    print(next(iterator))
