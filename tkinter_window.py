from tkinter import *

window = Tk()
window.title("States Correct")

l = Label(window,text="Enter a state: ",justify='center')
l.grid(row=0,column=0)

e = Entry(window,width=15)
e.grid(row=1,column=0,columnspan=3)

b1 = Button(window,text="Submit")
b1.grid(row=2,column=0)
b2 = Button(window,text="Cancel")
b2.grid(row=2,column=1)

window.mainloop()