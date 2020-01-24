# Mac and Linux paths differ Windows being back slashes vs. linux being forward slashes
# Python lets you iterate over the lines of a file without checking for the EOF this is an example of the term Pythonic which are differences between other languages
###############################################
# jabber = open("sample.txt", 'r')
# # Print only the lines that contain "jabberwock" end= prevents the printing of another newline character
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
#
# jabber.close()
##############################################
# You can use the with method so that you don't have to then add .close() this is new in Python3
# with open('sample.txt','r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')
#############################################
# with open('sample.txt','r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()
##############################################
# Returns lines as a list to then be processed later
# with open('sample.txt', 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
# # Process the lines
# for line in lines:
#     print(line, end='')

# Read is takes the file into individual string better for use with binary files
with open('sample.txt', 'r') as jabber:
    lines = jabber.read()

# Process the lines
for line in lines[::-1]:
    print(line, end='')