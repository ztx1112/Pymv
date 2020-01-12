import tkinter as tk
import cam
from tkinter.simpledialog import askstring, askinteger, askfloat

class Addwindow(tk.Toplevel):
    '''添加检测窗口'''
    def __init__(self):
        super().__init__()
        self.title('添加一个检测窗口')
        self.wm_attributes('-topmost',1)
        self.grab_set()
        self.resizable(width=False, height=False)
        #self.overrideredirect(True)
        self.cam_num=None
        self.cam_list=None
        self.cam_num,self.cam_list = cam.Update_cam()
        if self.cam_num<1:
            return
        self.sn=tk.StringVar()
        self.name=tk.StringVar(value='CCD')
        self.initui()
        self.result=[]
    def initui(self):
        '''初始化UI'''
        l2=tk.Label(self,text='当前连接相机').grid(row=0,column=0)
        self.csn=[]
        for s in self.cam_list:
            self.csn.append(s['sn'])
        ccsn=tk.StringVar(value=self.csn)
        lb=tk.Listbox(self,height=10,listvariable=ccsn)
        lb.bind('<<ListboxSelect>>', self.selectevent)
        lb.selection_set(0)
        lb.grid(row=1,column=0,rowspan=2)
        l3=tk.Label(self,text='新窗口名字:').grid(row=0,column=2,columnspan=2)
        e1=tk.Entry(self,textvariable=self.name).grid(row=1,column=2,columnspan=2)
        self.sn.set(self.csn[0])
        b1=tk.Button(self,command=self.ok,text='确认').grid(row=5,column=2)
        b2=tk.Button(self,command=self.cancel,text='取消').grid(row=5,column=3)
    def selectevent(self,event):
        i=event.widget.curselection()
        if len(i)<1:
            return
        self.sn.set(self.csn[i[0]])
    def ok(self):
        self.result.append(self.name.get())
        self.result.append(self.sn.get())
        self.destroy()
    def cancel(self):
        self.destroy()


def sign_in():
    return askstring("用户","输入密码：")




class preference_panel(tk.Frame):
    '''调试界面参数设置面板'''
    def __init__(self,master,width=None,height=None):
        super(preference_panel,self).__init__(master,width=200,height=200,borderwidth=2,relief='raised')
        
        l1=tk.Label(self,text='检测设置页面').grid(row=0,column=0)
        l1=tk.Label(self,text='11233').grid(row=1,column=0)
        b1=tk.Button(self,text='click').grid(row=2,column=0)













if __name__=='__main__':
    root=tk.Tk()
    root.title('main')
    #root.geometry('200x200')
    f1=preference_panel(root).grid(column=0,row=0)
    l1=tk.Label(root,text='412').grid(row=0,column=1)
    #f1=tk.Frame(root,width=100,height=100,borderwidth=5,relief='sunken').grid(row=1,column=0)
    root.mainloop()