def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)

#
# def center_text(*args, sep=' ', end='\n', file=None, flush=False):
#
#     text = ""
#     for arg in args:
#         text += str(arg) + " " + sep
#
#     left_margin = (80 - len(text)) // 2
#     print(" " * left_margin, text, end=end, file=file, flush=flush)
#
# with open("centered", mode='w') as centered_file:
# # Call the function
#     center_text("Spam and eggs", file=centered_file)
#     center_text("Spam is more than just eggs", file=centered_file)
#     center_text(112, file=centered_file)
#     center_text("Spam once more is more than just eggs", file=centered_file)


def center_text(*args, sep=' '):

    text = ""
    for arg in args:
        text += str(arg) + " " + sep

    left_margin = (80 - len(text)) // 2
    return " " * left_margin, text

s1 = center_text("Spam and eggs")
print(s1)
s2 = center_text("Spam is more than just eggs")
print(s2)
s3 = center_text(112)
print(s3)
s4 = center_text("Spam once more is more than just eggs", sep=":")
print(s4)


