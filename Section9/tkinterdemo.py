# Pack is a geometry editor that tkinter uses the most basic one


try:
    import tkinter
except ImportError: #python 2
    import Tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)


#tkinter._test()

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
# +8 +400 offsets the window from the screen
mainWindow.geometry('640x480-8-400')

label = tkinter.Label(mainWindow, text="Hello World")
# Using grid instead of pack
label.grid(row=0, column=0)
# label.pack(side='top')
leftFrame = tkinter.Frame(mainWindow)
#leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
# Depending on the expand X vs expand Y the fill needs to be adjusted based off x or y
# canvas.pack(side='left', fill=tkinter.X, expand=True)

#canvas.pack(side='left', anchor='n')
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(mainWindow)
#rightFrame.pack(side='right', anchor='n', expand=True)
rightFrame.grid(row=1, column=2, sticky='n')
button1 = tkinter.Button(rightFrame, text='button1')
button2 = tkinter.Button(rightFrame, text='button2')
button3 = tkinter.Button(rightFrame, text='button3')

# button1.pack(side='top')
# button2.pack(side='top')
# button3.pack(side='top')

button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

#configure the columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky='ew')

mainWindow.mainloop()