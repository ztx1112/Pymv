from tkinter import *



class ROI():
    def __init__(self):
        self.roi_list=[]
        self.roi_width=1.4
        self.nowdraw=None
        self.nowadd=None
        self.cv=None
        self.event=None

    def add(self):
        self.roi_list.append(RoiDate())
        return
    def starteder(self,event,Canvas):
        self.event=event
        self.cv=Canvas
        self.roi_list[-1].start_x=event.x
        self.roi_list[-1].start_y=event.y
        #self.roi_list[-1].nextstatus="motion"
        return
    def motioner(self,event,Canvas):
        self.event=event
        self.cv=Canvas
        if self.nowdraw is not None:
            self.cv.delete(self.nowdraw)
        self.nowdraw=self.cv.create_rectangle(self.roi_list[-1].start_x,
                                            self.roi_list[-1].start_y,
                                            self.event.x,
                                            self.event.y,
                                            tag="ROI",
                                            width=self.roi_width)
        #self.roi_list[-1].nextstatus="ended"
        return
    def ender(self,event,Canvas):
        self.event=event
        self.cv=Canvas
        self.roi_list[-1].end_x=self.event.x
        self.roi_list[-1].end_y=self.event.y
        #self.roi_list[-1].nextstatus="complex"
        self.nowdraw=None
        return

    def conut(self):
        return len(self.roi_list)




class RoiDate():
    def __init__(self):
        self.name=""
        self.start_x=None
        self.start_y=None
        self.end_x=None
        self.end_y=None
        self.alg_list=[]
        