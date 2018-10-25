from tkinter import *

# your code goes between window and window.mainloop
window = Tk()

# function for writing input in first entry box
# insert button's number at the end of the box
def callback(number):
    e1.insert(END, number)

e1_val = StringVar()
e1 = Entry(window, textvariable = e1_val)
e1.grid(row = 0, column = 0, columnspan = 2)

# function for calculating and displaying result
def result():
	# we use eval because we're working with strings
	e2.insert(END, eval(e1_val.get())) 
	
# function for deleting entry boxes
def delete():
	e1.delete(0, 'end')
	e2.delete(0, 'end')

# creating entry boxes and buttons
# I use grid method for easier positioning
e2 = Entry(window)
e2.grid(row = 0, column = 2, columnspan = 2)

b1 = Button(window, text = 7, command = lambda: callback(7), width = 5)
b1.grid(row = 1, column = 0)

b2 = Button(window, text = 8, command = lambda: callback(8), width = 5)
b2.grid(row = 1, column = 1)

b3 = Button(window, text = 9, command = lambda: callback(9), width = 5)
b3.grid(row = 1, column = 2)

b4 = Button(window, text = '/', command = lambda: callback('/'), width = 5)
b4.grid(row = 1, column = 3)

b5 = Button(window, text = 4, command = lambda: callback(4), width = 5)
b5.grid(row = 2, column = 0)

b6 = Button(window, text = 5, command = lambda: callback(5), width = 5)
b6.grid(row = 2, column = 1)

b7 = Button(window, text = 6, command = lambda: callback(6), width = 5)
b7.grid(row = 2, column = 2)

b8 = Button(window, text = '*', command = lambda: callback('*'), width = 5)
b8.grid(row = 2, column = 3)

b9 = Button(window, text = 1, command = lambda: callback(1), width = 5)
b9.grid(row = 3, column = 0)

b10 = Button(window, text = 2, command = lambda: callback(2), width = 5)
b10.grid(row = 3, column = 1)

b11 = Button(window, text = 3, command = lambda: callback(3), width = 5)
b11.grid(row = 3, column = 2)

b12 = Button(window, text = '-', command = lambda: callback('-'), width = 5)
b12.grid(row = 3, column = 3)

b13 = Button(window, text = 0, command = lambda: callback(0), width = 5)
b13.grid(row = 4, column = 0)

b14 = Button(window, text = '.', command = lambda: callback('.'), width = 5)
b14.grid(row = 4, column = 1)

b15 = Button(window, text = '=', command = result, width = 5)
b15.grid(row = 4, column = 2)

b16 = Button(window, text = '+', command = lambda: callback('+'), width = 5)
b16.grid(row = 4, column = 3)

b17 = Button(window, text = 'C', command = delete, width = 5)
b17.grid(row = 5, column = 0)

window.mainloop()
