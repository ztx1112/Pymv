from tkinter import *
from tkinter.dialog import *
from tkinter.filedialog import *


root=Tk()
bt=Button(root,text="111")
bt.pack()
dialog=LoadFileDialog(root)

root.mainloop()