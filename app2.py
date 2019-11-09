from tkinter import *
from PIL import Image,ImageTk
from ROI import *

def test():
    global roi
    print(roi.conut())
    

def test_start(event):
    global cv,s,roi
    roi.add()
    if s:
        roi.starteder(event=event,Canvas=cv)

def test_end(event):
    global cv,s,roi
    s=1
    roi.ender(event=event,Canvas=cv)
    
def test_motion(event):
    global cv,s,roi
    if ss:
        roi.motioner(event=event,Canvas=cv)


roi=ROI()
s=1
ss=1
start_y=None
start_x=None

win=Tk()
im2=ImageTk.PhotoImage(file="image2.bmp") 
im = ImageTk.PhotoImage(file="image1.bmp") 
win.title('main window')
cv=Canvas(win,width=300,height=300)
cv.create_image(0,0, image=im, anchor=NW)
cv.pack(side=TOP)
bt=Button(win,text='swap')
bt['command']=test
bt.pack(side=BOTTOM)
cv.bind("<ButtonPress-1>",test_start)
cv.bind("<B1-Motion>",test_motion)
cv.bind("<ButtonRelease-1>",test_end)

win.mainloop()