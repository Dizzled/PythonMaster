even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

#One thing to keep in mind is that in Python the
#numbers sorted method doesn't change the object
print(numbers.sort())

#If you want to sort the list instead use sorted(numbers) to change the object
print(sorted(numbers))

#Both do the same thing to create and empty list
listOne = []
listTwo = list()

#In python lists are iterable and a reference to one is a reference to another
even = [2, 4, 6, 8]
newEven = list(even)
newEven.sort(reverse=True)
even.sort(reverse=True)
print(even)
print(newEven)
#Another thing to keep in mind is using is vs. == (is) checks for the same memory location while (==) checks if lists are the same
if even is newEven:
    print(True)
else:
    print(False)

#Should print True
if even == newEven:
    print(True)
else:
    print(False)
