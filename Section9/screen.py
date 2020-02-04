try:
    import tkinter
except ImportError: # Python 2
    import Tkinter as tkinter

# To import the list of directories
# It's a good idea to draw the rows and columns as a grid so your layout is clear

import os
mainWindow = tkinter.Tk()

mainWindow.title("Grid Demo")
mainWindow.geometry('640x480-8-200')

label = tkinter.Label(mainWindow, text='Tkinter Grid Demo')
label.grid(row=0, column=0, columnspan=3)


# The weights really only come into play when you're resizing the window frame
mainWindow.columnconfigure(0, weight=100)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1000)
mainWindow.columnconfigure(3, weight=600)
mainWindow.columnconfigure(4, weight=1000)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

mainWindow['padx'] = 10

fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')

for zone in os.listdir('/Windows/System32'):
    fileList.insert(tkinter.END, zone)

# Actions are set by the commands
listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview) # Changes the vertical position
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = listScroll.set # Needed to link the listScroll to the scroll bar

# frame for the radio buttons
optionFrame = tkinter.LabelFrame(mainWindow, text='File Details')
optionFrame.grid(row=1, column=2, sticky='ne')

# Create three radio buttons that share the same variable
rbValue = tkinter.IntVar()
# Sets the default radio button set
rbValue.set(3)

# Radio buttons
radio1 = tkinter.Radiobutton(optionFrame, text="Filename", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text="Path", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text="Timestamp", value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# Adding the result in the main window
# Display the result
resultLabel = tkinter.Label(mainWindow, text="Result")
resultLabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

# Frame for the time spinners
timeFrame = tkinter.LabelFrame(mainWindow, text="Time")
timeFrame.grid(row=3, column=0, sticky='new')
#Time spinners two ways to set the range either tuples or using the from_ to:
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)

hourSpinner.grid(row=0, column=0)
minuteSpinner.grid(row=0, column=2)
secondSpinner.grid(row=0, column=4)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)

# Built in padding command
timeFrame['padx'] = 36

# Frame for the date spinners
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')
#Date Labels
dayLabel = tkinter.Label(dateFrame, text='Day')
monthLabel = tkinter.Label(dateFrame, text='Month')
yearLabel = tkinter.Label(dateFrame, text='Year')

dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')
# Date Spinners
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpin = tkinter.Spinbox(dateFrame, values=("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"))
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2999)

daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)

# Buttons
okButton = tkinter.Button(mainWindow, text="OK")
cancelButton = tkinter.Button(mainWindow, text="Cancel", command=mainWindow.destroy) # Using Destroy instead of quit is easier and ends the mainloop return value is assigned to command
# Dont use destory() because we don't want the function to be called we want the command to be assigned to destroy when clicked

cancelButton.grid(row=4, column=3, sticky='e')
okButton.grid(row=4, column=3, sticky='w')
okButton['padx'] = 15



tkinter.mainloop()

# Returns the value of the radio button selected
print(rbValue.get())