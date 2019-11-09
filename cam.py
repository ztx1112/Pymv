import gxipy as gx
import tkinter as tk
from numpy import *
from PIL import Image
from PIL import ImageTk
import threading



class DHcam():
    """DHcam class"""

    def __init__(self):
        self.device_manager=gx.DeviceManager()
        self.device_num,self.device_list=self.device_manager.update_device_list()
        self.device=self.Open(1)
        self.device.stream_on()


    def Open(self,index):
        print(self.device_list[index-1].get("sn"))
        return self.device_manager.open_device_by_index(index)
    def Close(self):
        self.device.stream_off()
        self.device.close_device()

    def Grabimage(self):
        imagedata=self.device.data_stream[0].get_image()
        return imagedata.get_numpy_array()


