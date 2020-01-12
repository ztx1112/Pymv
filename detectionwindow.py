import gxipy,cv2,ROI,Calculation,dwconfig,dialog
import tkinter as tk
import numpy as np
import PIL,PIL.Image,PIL.ImageTk,PIL.ImageOps
from cam import *
import Lib.threading as th



class detectionwindow(tk.Canvas):
    "检测显示窗口"
    def __init__(self,master=None,width=None,height=None,bg=None,config=None,name=None,camsn=None):
        self.image=PIL.ImageTk.PhotoImage(PIL.Image.fromarray(np.zeros((1,1))))
        self.img=self.image
        if config==None:
            self.cam=DHcam(devicesn=camsn)
            self.configure=Configure()
            if camsn!=None:
                self.configure['camsn']=camsn
            if name!=None:
                self.configure['name']=name
        else:
            self.configure=config
            self.cam=DHcam(devicesn=self.configure['camsn'])
            self.width=int(self.configure['width'])
            self.height=int(self.configure['height'])
        super(detectionwindow,self).__init__(master,bg='black',width=self.width,height=self.height)
        self.create_image(0,0,image=self.image,anchor='nw')
        self.ssize=(1,1)
        self.rsize=(1,1)
        self.bindinit()
        self.menu=tk.Menu(self,tearoff=0)
        self.menu.add_command(label='调试模式',command=self.modechange,state='disable')
        self.menu.add_command(label='抓图',command=self.livesignal)
        self.menu.add_command(label='实时开始',command=self.livemultiple)
        self.menu.add_command(label='实时停止',command=self.livestop)
        self.showmode=''
        self.showstatus=0
        self.mode='show'

    def livesignal(self):
        self.showmode='signal'
        self.show()

    def show(self):
        self.showstatus=1
        self.threading=th.Thread(target=self._show)
        self.threading.setDaemon(True)
        self.threading.start()

    def livemultiple(self):
        self.showmode='multiple'
        self.showstatus=1
        self.show()

    def livestop(self):
        self.showstatus=0

    def _show(self,mode=None):
        print('show')
        if self.cam==None:
            print('no cam')
            return
        while self.showstatus:
            data=self.cam.Grabimage()
            self.__show(data)
            if self.showmode=='signal':
                self.showstatus=0

    def __show(self,arrdata):
        self.image=PIL.ImageTk.PhotoImage(PIL.Image.fromarray(arrdata).resize(self.rsize))
        self.create_image(0,0,image=self.image,anchor='nw')
        self.img=self.image

    def resize(self,height,width):
        self.rsize=(width,height)
        print('resize',self.rsize)

    def _destroy(self,event):
        print("dw destroy\n")

    def _resize(self,event):
        print('resize event')
        self.resize(self.winfo_height(),self.winfo_width())

    def bindinit(self):
        self.bind('<Destroy>',self._destroy)
        self.bind('<3>',self.popmenu)
        self.bind('<Configure>',self._resize)
        self.bind('<Activate>',lambda e:print('Activate event'))

    def getconfig(self):
        self.configure['width']=str(self.winfo_width())
        self.configure['height']=str(self.winfo_height())
        return self.configure

    def popmenu(self,event):
        l=self.winfo_toplevel().userlevel
        if self.mode=='show':
            if l==1:
                self.menu.entryconfig("调试模式",state='active')
                return
        self.menu.post(event.x_root,event.y_root)

    def userchange(self,level):
        pass

    def modechange(self):
        if self.mode=='show':
            self.winfo_toplevel().modechange(self.configure['name'])
            return

    def created(self):
        info=self.grid_info()
        self.configure['row']=str(info['row'])
        self.configure['column']=str(info['column'])



def Configure():
    d={}
    d['camsn']=""
    d['modelname']=""
    d['imagetype']=""
    d['deviceclass']=""
    d['camconfigfile']=""
    d['name']=""
    d['row']='0'
    d['col']='0'
    d['height']='0'
    d['width']='0'
    return d





