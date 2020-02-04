# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.
import tkinter
import math
result = 0
mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry('640x480')

icon = tkinter.PhotoImage(file='icon.png')
# label = tkinter.Label(mainWindow, text='Calculator', bg='green')
# label.grid(row=0, column=0, columnspan=3)

mainWindow.iconphoto(False, icon)
#
# mainWindow.columnconfigure(0, weight=10)
# mainWindow.columnconfigure(1, weight=1)
# mainWindow.columnconfigure(2, weight=1)
# mainWindow.columnconfigure(3, weight=1)
# mainWindow.columnconfigure(4, weight=1)
#
# mainWindow.rowconfigure(0, weight=10)
# mainWindow.rowconfigure(1, weight=1)
# mainWindow.rowconfigure(2, weight=1)
# mainWindow.rowconfigure(3, weight=1)
# mainWindow.rowconfigure(4, weight=1)
# mainWindow.rowconfigure(5, weight=1)
# mainWindow.rowconfigure(6, weight=1)

# outputWindow = tkinter.Text(mainWindow, bg='grey')
# outputWindow.grid(row=1, column=0, sticky='nsew', rowspan=1)
# outputWindow.tag_add('output', '1.0')
def callback(nb):
    result = int(nb.widget['text'])

def add(nb):
    result = int(nb.widget['text'])

def subtract(nb):
    result = int(nb.widget['text'])

def multiply(nb):
    result = int(nb.widget['text'])

def divide(nb):
    result = int(nb.widget['text'])

newButton = dict()

column = 0
# Stored buttons in a dictionary so that hashed index position can hopefully be returned by the lambda function call
for x in range(0, 10):
    newButton.update({f'{x}': tkinter.Button(mainWindow, text='{}'.format(x))})
    newButton[f'{x}'].bind("<Button-1>", callback)
    if x >= 7: # Need to be in row 2, column 0, 1 ,2
        newButton.get(f'{x}').grid(row=2, column=column, padx=1)
        column = column + 1
    elif (x >= 4) and (x <= 6): # Need to be in row 3, column 0, 1, 2
        newButton.get(f'{x}').grid(row=3, column=column, padx=1)
        column = column + 1
    elif (x >= 1) and (x <= 3): # Need to be in row 4, column 0, 1, 2
        newButton.get(f'{x}').grid(row=4, column=column, padx=1)
        column = column + 1
    elif x <= 0: # Need to be in row 5, column 0
        newButton.get(f"{x}").grid(row=5, column=column, padx=1)
    if column > 2:
        column = 0


newButton.update({'+': tkinter.Button(mainWindow, text='+')})
newButton['+'].bind("<Button-1>", add)
newButton.get('+').grid(column=3, row=2)

newButton.update({'-': tkinter.Button(mainWindow, text='-')})
newButton['-'].bind("<Button-1>", subtract)
newButton.get('-').grid(column=3, row=3)

newButton.update({'*': tkinter.Button(mainWindow, text='*')})
newButton['*'].bind("<Button-1>", multiply)
newButton.get('*').grid(column=3, row=4)

newButton.update({'/': tkinter.Button(mainWindow, text='/')})
newButton['/'].bind("<Button-1>", divide)
newButton.get('/').grid(column=3, row=5)

newButton.update({'=': tkinter.Button(mainWindow, text='=')})
newButton['='].bind("<Button-1>", divide)
newButton.get('=').grid(column=1, row=5, columnspan=2, sticky='we')

mainWindow.mainloop()
