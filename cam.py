#import gxipy as gx
import numpy as np
import cv2

class CamCase():
    """ 相机基类    """
    def __init__(self):
        self.__devicestate=None
        self.devicesn=''
        self.__image_heigh=0
        self.__image_width=0
        self.__device=None

    def OpenDevice(self,index=0):
        """打开设备"""
        self.__device=cv2.VideoCapture(index,cv2.CAP_DSHOW)
        if self.__device.isOpened():
            self.__devicestate="opened"

    def Getimagesize(self):
        """ 获取图像宽，高
            return height,width
            """
        pass

    def GetImage(self):
        """ 抓取一张图像
            return imagedata of narray
            """
        if not self.__devicestate=="opened":
            return None
        else:
            retvl,image=self.__device.read()
            return image

    def Getstate(self):
        """ 获取相机状态
            return camera state
            """
        return self.__devicestate


class NormalCam(CamCase):
    """ 一般相机类  """
    def __init__(self):
        CamCase.__init__(self)


class DHcam(CamCase):
    """大恒相机类"""

    def __init__(self,devicesn):
        self.__devicestate=None
        self.devicesn=''
        self.devicesn=devicesn
        self.devicemanager=gx.DeviceManager()
        if len(self.devicesn)>0:
            self.device=self.devicemanager.open_device_by_sn(self.devicesn)
            self.__devicestate="on"
            self.device.stream_on()
    def Getimagesize(self):
        """获取图像宽，高
        return height,width"""
        data=self.device.data_stream[0].get_image()
        return  data.get_height(),data.get_width()
    def Close(self):
        if self.__devicestate=="on":
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