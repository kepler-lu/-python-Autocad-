#隧道横断面
from pyautocad import Autocad, APoint, aDouble
import math
import win32com.client
import pythoncom
from win32com.client import VARIANT


def vtpnt(x, y, z=0):
    """坐标点转化为浮点数"""
    return win32com.client.VARIANT (pythoncom.VT_ARRAY | pythoncom.VT_R8, (x, y, z))


def vtobj(obj):
    """转化为对象数组"""
    return win32com.client.VARIANT (pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, obj)


def vtFloat(list):
    """列表转化为浮点数"""
    return win32com.client.VARIANT (pythoncom.VT_ARRAY | pythoncom.VT_R8, list)


def vtInt(list):
    """列表转化为整数"""
    return win32com.client.VARIANT (pythoncom.VT_ARRAY | pythoncom.VT_I2, list)


def vtVariant(list):
    """列表转化为变体"""
    return win32com.client.VARIANT (pythoncom.VT_ARRAY | pythoncom.VT_VARIANT, list)
#pyacad = Autocad(create_if_not_exists=True)

#origin=[0,0] #圆心坐标
#cross_section=[radius_1,radius_2,radius_3,hight_1,hight_2] #断面参数 分别为单心圆的半径 和 单心圆心与基准线的高度  以及 内边界的最下端与基准线的高度

class one_center_circle():
    def __init__(self,pyacad,origin,cross_section):
        self.plottiong_scale = 10  #比例尺  10毫米表示多少1m
        self.pyacad = pyacad
        self.x0 = origin[0]
        self.y0 = origin[1]
        self.radius_1 = cross_section[0]*self.plottiong_scale
        self.radius_2 = cross_section[1]*self.plottiong_scale
        self.radius_3 = cross_section[2]*self.plottiong_scale
        self.hight_1 = cross_section[3]*self.plottiong_scale #单心圆心与基准线的高度
        self.hight_2 = cross_section[4]*self.plottiong_scale #内边界的最下端与基准线的高度



    def draw(self,pyacad):
        center = APoint (self.x0, self.y0)  # 圆心
        radius = self.radius_1  # 半径
        nei_lunkuo_1 = pyacad.model.AddArc(center, radius, math.radians(0), math.radians(90))
        nei_lunkuo_1.update
        #v = VARIANT (pythoncom.VT_BYREF | pythoncom.VT_ARRAY | pythoncom.VT_R8,nei_lunkuo_1)
        #nei_lunkuo_2 = v.offset(-0.50)
        nei_lunkuo_2 = nei_lunkuo_1.offset (-0.50)


        nei_lunkuo_2.update

        print(nei_lunkuo_2.radius)
        nei_lunkuo_1.update







