from tkinter import *

root=Tk()

label1= Label(root, text="First", bg="Red", fg="White")
label1.pack(fill=X)

label2= Label(root, text="Second", bg="Blue", fg="Green")
label2.pack(side=LEFT,fill=Y)

root.mainloop()