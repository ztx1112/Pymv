import tkinter.ttk as ttk
import tkinter as tk
from detectionwindow import *
import Lib.configparser as cp
import os,sys
import cam,dialog


class Mainwindow(tk.Tk):
    def __init__(self):
        super(Mainwindow,self).__init__()
        self.state("zoomed")
        self.initUI()
        self.winmanage=[]
        self.eventinit()
        self.update()
        self.configure=cp.ConfigParser()
        self.configlist=[]
        self.cam_num=None
        self.cam_list=None
        self.updatacam()
        self.loadfile('config.ini')
        if len(self.configlist)>0:
            self.initwin()
        self.userlevel=0        #0:user  1:admin
        self.password='112233'

    def initUI(self):
        '''UI初始化'''
        self.menubar=tk.Menu(self,tearoff=0)
        self.filemenu=tk.Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label="打开文件",command=self.openfile)
        self.filemenu.add_command(label="保存文件",command=self.savefile)
        self.filemenu.add("separator")
        self.filemenu.add_command(label="退出",command=self.destroy)
        self.testmenu=tk.Menu(self,tearoff=0)
        self.testmenu.add_command(label="添加窗口",command=self.addwin)
        self.testmenu.add_command(label="01")
        self.cammenu=tk.Menu(self,tearoff=0)
        self.cammenu.add_command(label="更新相机列表",command=self.updatacam)
        self.usermenu=tk.Menu(self,tearoff=0)
        self.usermenu.add_command(label="切换权限",command=self.userchange)
        self.menubar.add_cascade(label="文件",menu=self.filemenu)
        self.menubar.add_cascade(label="测试",menu=self.testmenu)
        self.menubar.add_cascade(label="相机",menu=self.cammenu)
        self.menubar.add_cascade(label="用户",menu=self.usermenu)
        self.config(menu = self.menubar)

        

    def initwin(self):
        '''程序打开时初始化窗口'''
        for con in self.configlist:
            self.addwin(config=self.configure[con])

    def addwin(self,config=None):
        if self.cam_num==0:
            return
        a=None
        if config==None:
            win=dialog.Addwindow()
            self.wait_window(win)
            name=win.result[0]
            sn=win.result[1]
            l=len(self.winmanage)+1
            width=self.winfo_width()
            height=self.winfo_height()
            a=detectionwindow(self,width=width,height=height,name=name,camsn=sn)
            a.grid()
            ii=self.configure.has_section('root')
            if ii==False:
                self.configure.add_section('root')
            self.configure['root']['num']=str(l)
        else:
            a=detectionwindow(self,config=config)
            r=int(config['row'])
            c=int(config['col'])
            a.grid(row=r,column=c)
            a.created()
        self.winmanage.append(a)


    def savefile(self):
        i=1
        self.configure['root']['password']=self.password
        for win in self.winmanage:
            s='detectionwindow '+str(i)
            i+=1
            if self.configure.has_section(s):
                pass
            else:
                self.configure.add_section(s)
            con=win.getconfig()
            for name in con:
                self.configure[s][name]=str(con[name])
        with open('config.ini','w') as cfile:
            self.configure.write(cfile)

    def openfile(self,path):
        rootpath=os.getcwd()
        i=0
        for root,dirs,names in os.walk(rootpath):
            i=names.count('config.ini')
        if i>0:
            self.configure.read('config.ini')
    def loadfile(self,file=None):
        isfile=False
        if file!=None:
            cwdpath=os.getcwd()
            for a,b,c in os.walk(cwdpath):
                for f in c:
                    if f==file:
                        isfile=True
            if isfile:
                self.configure.read(file)
                for sec in self.configure.sections():
                    if sec[0:15]=='detectionwindow':
                        print(sec)
                        self.configlist.append(sec)
    def resizeevent(self,event):
        for win in self.winmanage:
            #win.resize()
            pass
    def _destroy(self,event):
        print(self.userlevel)

    def eventinit(self):
        self.bind('<Configure>',self.resizeevent)
        self.bind('<Destroy>',self._destroy)

    def updatacam(self):
        self.cam_num,self.cam_list=cam.Update_cam()
        print(self.cam_num,self.cam_list)

    def userchange(self):
        if self.userlevel==0:
            password=dialog.sign_in()
            if password==self.password:
                self.userlevel=1
                tk.messagebox.showinfo('提示','用户已切换为管理员')
                return
        if self.userlevel==1:
            self.userlevel=0
            tk.messagebox.showinfo('提示','用户已切换为操作员')

    def modechange(self,name=None):
        twin=None
        for win in self.winmanage:
            if win.configure['name']==name:
                twin=win
            win.grid_forget()
        
        





















if __name__=="__main__":
    win=Mainwindow()
    print('\n')
    win.mainloop()


