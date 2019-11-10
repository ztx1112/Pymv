from tkinter import *
from tkinter.dialog import *
#from tkinter.ttk import *
from ROI import *
import cv2 as cv
from PIL import Image
from PIL import ImageTk
from PIL import ImageOps
from cam import *
from numpy import *
import gxipy as gx
import threading
import time



def GetImage(cvss=None):
    global cam,image,nowimage,cvs
    #data=cam.Grabimage()
    #mat=cv.Mat(date)
    #print(mat)
    #return

    img=Image.fromarray(cam.Grabimage())
    w,h=img.size
    print(w/800)
    print(h/600)
    im=ImageOps.scale(img,0.324)
    im.show()
    print(im)
    image=ImageTk.PhotoImage(im)
    if cvss is None:
        if nowimage!=-1:
            cvs.delete(nowimage)
            print(nowimage)
        nowimage=cvs.create_image(0,0,image=image,anchor=NW)
        print(nowimage)
        return
    if nowimage!=-1:
        cvs.delete(nowimage)
        print("image = ")
        print(nowimage)
    nowimage=cv.create_image(100,100,image=image)
    return


def LiveStart(event=None):
    global status,i,cvs
    status=1
    while status:
        threadLock.acquire()
        GetImage()
        threadLock.release()
        print(i)
        i=i+1
        if i >= 110:
            return


def LiveStop(event=None):
    global status
    status=0

def test():
    global t
    t=threading.Thread(target=LiveStart)
    t.start()

def test_start(event):
    global cvs,s,roi
    roi.add()
    if s:
        roi.starteder(event=event,Canvas=cvs)

def test_end(event):
    global cvs,s,roi
    s=1
    roi.ender(event=event,Canvas=cvs)
    
def test_motion(event):
    global cvs,s,roi
    if ss:
        roi.motioner(event=event,Canvas=cvs)

def Openfile(file=None):
    pass

def Savefile():
    pass



threadLock = threading.Lock()
roi=ROI()
s=1
ss=1
t=None
image=None
im=None
i=100
status=1
nowimage=-1
cam=DHcam()
root=Tk()
root.title("window")
#root.geometry('400x400')
#root.state("zoomed")
menubar=Menu(root,tearoff=0)


filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="打开文件",command=Openfile)
filemenu.add_command(label="保存文件",command=Savefile)

filemenu.add("separator")
filemenu.add_command(label="退出",command=root.quit)
testmenu=Menu(menubar,tearoff=0)
testmenu.add_command(label="抓图",command=GetImage)
#testmenu.add_command(label="实时开始",command=LiveStart)
#testmenu.add_command(label="实时停止",command=LiveStop)
#testmenu.add_command(label="开始",command=test)


menubar.add_cascade(label="文件",menu=filemenu)
menubar.add_cascade(label="测试",menu=testmenu)
root.config(menu = menubar)
cvs=Canvas(root,width=800,height=600)
cvs.pack(side=BOTTOM)
#cvs.bind("<ButtonPress-1>",test_start)
#cvs.bind("<B1-Motion>",test_motion)
#cvs.bind("<ButtonRelease-1>",test_end)

root.mainloop()

cam.Close()




