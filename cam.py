import gxipy as gx
from numpy import *



class DHcam():
    """大恒相机类"""

    def __init__(self,devicesn):
        self.camstatus=None
        self.devicesn=''
        self.devicesn=devicesn
        self.devicemanager=gx.DeviceManager()
        if len(self.devicesn)>0:
            self.device=self.devicemanager.open_device_by_sn(self.devicesn)
            self.camstatus="on"
            self.device.stream_on()
    def Getimagesize(self):
        """获取图像宽，高
        return height,width"""
        data=self.device.data_stream[0].get_image()
        return  data.get_height(),data.get_width()
    def Close(self):
        if self.camstatus=="on":
            self.device.stream_off()
            self.device.close_device()

    def Grabimage(self):
        """抓取一张图像
        return imagedata of narray"""
        return  self.device.data_stream[0].get_image().get_numpy_array()

def Update_cam():
    """更新相机列表
    return: 相机数量，相机列表"""
    device_manager=gx.DeviceManager()
    return device_manager.update_device_list()