import shelve

# The with statement will automatically close the shelve file upon completion
# If you want to change the opening and closing of it to manually do it see the next example
# with shelve.open('ShelfTest') as fruit:
#     fruit['orange'] = "A sweet, orange citrus fruit"
#     fruit['grape'] = "A sweet small round fruit"
#     fruit['tomatoe'] = "Not a fruit"
#     fruit['lime'] = "Kinda like a lemon"
#     fruit['apple'] = "A sweet, crispy succulent fruit"
#
#     print(fruit['apple'])
#     print(fruit['lime'])

#Open shelf manually and then close it manually
#with shelve.open('ShelfTest') as fruit:
fruit = shelve.open('Shelftest')
fruit['orange'] = "A sweet, orange citrus fruit"
fruit['grape'] = "A sweet small round fruit"
fruit['tomatoe'] = "Not a fruit"
fruit['lime'] = "Kinda like a lemon"
fruit['apple'] = "A sweet, crispy succulent fruit"
fruit.close()

print(fruit['apple'])
print(fruit['lime'])