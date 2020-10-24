#import gxipy as gx
import threading as th
import time
import tkinter as tk
import cv2
import numpy as np
from PIL import ImageOps, ImageTk
import PIL
from ROI import *
from cam import *
#import detectionwindow as dw


def GetImage():
    global cam,image,lb,rsize,root,imagedata
    data=cam.GetImage()
    
    im=cv2.cvtColor(data,cv2.COLOR_BGR2RGB)
    imagedata=im.copy()
    img=PIL.Image.fromarray(imagedata).resize(rsize)
    image=ImageTk.PhotoImage(img)
    lb.config(image=image)
    lb.image=image
    #root.update()
    return


def LiveStart(event=None):
    global status
    status=1
    new=th.Thread(target=live)
    new.setDaemon(True)
    new.start()
    time.sleep(0.02)

def live():
    global status
    while status:
        GetImage()
        
def LiveStop(event=None):
    global status
    status=0

def Openfile(file=None):
    pass

def Savefile():
    pass

def test():
    global lb,root
    #print(root.winfo_width)
    #lb.resize(root.winfo_width(),root.winfo_height())


#threadLock = threading.Lock()
imagedata=None
rsize=(600,600)
roi=ROI()
lb=None
image=None
status=0

cam=NormalCam()

cam.OpenDevice()

root=tk.Tk()
root.title("window")
#root.geometry('1000x800')
root.state("zoomed")
menubar=tk.Menu(root,tearoff=0)
filemenu=tk.Menu(menubar,tearoff=0)
filemenu.add_command(label="打开文件",command=Openfile)
filemenu.add_command(label="保存文件",command=Savefile)
filemenu.add("separator")
filemenu.add_command(label="退出",command=root.quit)
testmenu=tk.Menu(menubar,tearoff=0)
testmenu.add_command(label="抓图",command=GetImage)
testmenu.add_command(label="实时开始",command=LiveStart)
testmenu.add_command(label="实时停止",command=LiveStop)
testmenu.add_command(label="resize",command=test)


menubar.add_cascade(label="文件",menu=filemenu)
menubar.add_cascade(label="测试",menu=testmenu)
root.config(menu = menubar)
lb=tk.Label(root)
lb.pack()
# cvs=Canvas(root,width=800,height=600)
# cvs.pack(side=BOTTOM)
#cvs.bind("<ButtonPress-1>",test_start)
#cvs.bind("<B1-Motion>",test_motion)
#cvs.bind("<ButtonRelease-1>",test_end)

root.mainloop()

#cam.Close()
