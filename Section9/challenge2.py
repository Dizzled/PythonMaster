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
# Store the values in an array
result1 = []
result2 = []

flag, ad, di, su, mu = False, False, False, False, False
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

    if flag:
        result2.append(nb.widget['text'])
        outPut.configure(text=nb.widget['text'])
    else:
        result1.append(nb.widget['text'])
        outPut.configure(text=nb.widget['text'])

def add(nb):
    global flag
    global ad
    flag = True
    ad = True

def subtract(nb):
    global flag
    global su
    flag = True
    su = True

def multiply(nb):
    global flag
    global mu
    flag = True
    mu = True

def divide(nb):
    global flag
    global di
    flag = True
    di = True

def equal(nb):
    global result
    global result1
    global result2

    x = int("".join(result1))
    y = int("".join(result2))

    if ad:
        result = x + y
    elif su:
        result = x - y
    elif mu:
        result = x * y
    elif di:
        result = x / y


def clear(nb):

    global ad, su, mu, di, result
    global flag
    flag = False
    result = 0

    del result1[:]
    del result2[:]

    ad = False
    su = False
    mu = False
    di = False

def update(nb):

    nb.configure(text=result)
    clear(nb)

newButton = dict()

column = 0
# Stored buttons in a dictionary so that hashed index position can hopefully be returned by the lambda function call
for x in range(0, 10):
    newButton.update({f'{x}': tkinter.Button(mainWindow, text='{}'.format(x))})
    newButton[f'{x}'].bind("<Button-1>", callback)
    if x >= 7: # Need to be in row 2, column 0, 1 ,2
        newButton.get(f'{x}').grid(row=2, column=column, padx=2)
        column = column + 1
    elif (x >= 4) and (x <= 6): # Need to be in row 3, column 0, 1, 2
        newButton.get(f'{x}').grid(row=3, column=column, padx=2)
        column = column + 1
    elif (x >= 1) and (x <= 3): # Need to be in row 4, column 0, 1, 2
        newButton.get(f'{x}').grid(row=4, column=column, padx=2)
        column = column + 1
    elif x <= 0: # Need to be in row 5, column 0
        newButton.get(f"{x}").grid(row=5, column=column, padx=2)
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

outPut = tkinter.Label(mainWindow, text=result, font=('Arial', 12, 'bold'), justify=tkinter.LEFT, bg='white')
outPut.grid(column=0, row=0, columnspan=4, sticky='nwe')

newButton.update({'=': tkinter.Button(mainWindow, text='=', command=lambda: update(outPut))})
newButton['='].bind("<Button-1>", equal)
newButton.get('=').grid(column=1, row=5, columnspan=2, sticky='we')

newButton.update({'C': tkinter.Button(mainWindow, text='C', command=lambda: update(outPut))})
newButton['C'].bind("<Button-1>", clear)
newButton.get('C').grid(column=0, row=1)

newButton.update({'CE': tkinter.Button(mainWindow, text='CE', command=lambda: update(outPut))})
newButton['CE'].bind("<Button-1>", clear)
newButton.get('CE').grid(column=1, row=1, sticky='we')


mainWindow.mainloop()
