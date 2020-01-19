name = input("Please Enter Name\n")
age = int(input("Please enter Age\n"))

if (age > 18) and (age < 31):
    print(f"{name} Welcome to holiday")
else:
    print(f"""Sorry {name} you aren't the correct age""")
