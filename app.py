from tkinter import *
from tkinter.ttk import *

import cv2 as cv
from PIL import Image
from PIL import ImageTk
from cam import *
from numpy import *
import gxipy as gx

def GetImage():
    global lb,root,cam,image
    img=Image.fromarray(cam.Grabimage())
    image=ImageTk.PhotoImage(img)
    lb['image']=image
    root.update()

def LiveStart():
    global status
    status=1
    while status:
        GetImage()


def LiveStop():
    global lb,root,cam,image,status
    status=0


status=1
#cam=DHcam()
root=Tk()
root.title("window")
root.geometry('400x400')
root.state("zoomed")
menubar=Menu(root,tearoff=0)


filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="打开文件")
filemenu.add("separator")
filemenu.add_command(label="退出",command=root.quit)
testmenu=Menu(menubar,tearoff=0)
testmenu.add_command(label="抓图",command=GetImage)
testmenu.add_command(label="实时开始",command=LiveStart)
testmenu.add_command(label="实时停止",command=LiveStop)

menubar.add_cascade(label="文件",menu=filemenu)
menubar.add_cascade(label="测试",menu=testmenu)
root.config(menu = menubar)

#lb=Label(root,padx=0,pady=0)
#lb.pack()
root.mainloop()

#cam.Close()




