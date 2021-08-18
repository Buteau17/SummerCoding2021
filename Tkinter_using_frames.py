from tkinter import *

root= Tk()

newframe=Frame(root)
newframe.pack()


otherframe=Frame(root)
otherframe.pack(side=BOTTOM)

button1 = Button(newframe, text="Click here", fg="Red")
button2= Button (otherframe,text="Click here" , fg="Blue")

button1.pack()
button2.pack()



root.mainloop()