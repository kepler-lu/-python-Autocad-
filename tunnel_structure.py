# -*- coding: utf-8 -*-
from pyautocad import Autocad, APoint, aDouble
import math
import numpy as np
import cross_section as cs

pyacad = Autocad(create_if_not_exists=True)
"""
#设置图层
"""
#修改图层属性
def Layers_property(pyacad,name,clr_num,linetyper,line_weight):
    #pyacad:cad工程名称 #name图层名称 #clr_num 图层颜色 #linetyer 线型  #line_weight线宽

    #设置图层颜色
    ClrNum = clr_num
    name.color = ClrNum
    # ClrNum为颜色索引号，其取值范围为[0,256]；
    # 标准颜色的颜色索引号指定如下：：1 红、2 黄、3 绿、4 青、5 蓝、6 洋红、7 白/黑；
    # 0 ByBlock、256 ByLayer；
    # 其他颜色索引号见 https://wenku.baidu.com/view/9d458b70195f312b3069a505.html。

    #设置图层线型
    #linetyper="ACAD_ISO08W100"
    try:
        pyacad.ActiveDocument.Linetypes.Load (linetyper, "acadiso.lin")
    except:
        print("线型已加载")
    # 加载线型，"ACAD_ISO05W100"为线型名称，详细信息见CAD帮助文档；
    # "acadiso.lin"为用于公制单位的线型定义文件，详细信息见CAD帮助文档；
    # 为图层指定线型前，需先加载相关线型；
    # 注意：不能重复加载，否则报错——'记录名重复'；
    # 可利用try...except...finally...机制，处理此类报错

    name.Linetype = "ACAD_ISO08W100"
    # 设置图层线型；
    # 指定线型前，若不想以Load方式加载线型，也可在CAD程序中点击线型>其他>加载，加载全部所用线型；
    # 若既没采用Load方式也没有在CAD程序中手动加载线型，则程序会报错——'未找到主键'。

    #设置线宽
    name.Lineweight = line_weight
    # 13表示线宽为0.01mm的13倍，即0.13mm；
    # 线宽值∈{0,5,9,13,15,18,20,25,30,35,40,50,53,60,70,80,90,100,106,120,140,158,200,211}；
    # 线宽值在上述集合中选取，含义为0.01mm的整数倍；其他数值非系统默认；
    # 可以修改现有线宽，但不能添加或删除线宽，修改在CAD程序中进行。

#定义图层
#1.结构图层
jiegou = pyacad.ActiveDocument.Layers.Add ("结构")
Layers_property(pyacad,jiegou,1,"ACAD_ISO08W100",200)

#################################绘图

####外框

def retangle(origin,L,H):
    x0=origin[0]
    y0=origin[1]
    pnts = [APoint(x0,y0), APoint(x0+L,y0), APoint(x0+L,y0+H),APoint(x0,y0+H),APoint(x0,y0)]
    pnts = [j for i in pnts for j in i]  # 将各点坐标顺序变换为行数据
    pnts = aDouble (pnts)  # 转化为双精度浮点数
    plineObj = pyacad.model.AddPolyLine (pnts)
    plineObj.Closed = True  # 闭合多段线

#1.绘制边框
pyacad.ActiveDocument.ActiveLayer = jiegou   # 激活图层 设置为当前图层
origin=np.array([0,0])
retangle(origin,420,297)


#2.绘制隧道结构 cross_section

origin=origin+np.array([100,200]) #圆心坐标
print(origin)
cross_section=[5.75,1,15,1.4,-1.5] #断面参数 分别为单心圆的半径 和 单心圆心与基准线的高度  以及 内边界的最下端与基准线的高度
Cs=cs.one_center_circle(pyacad,origin,cross_section)
Cs.draw(pyacad)



