
import random
import numpy as np



class Uav():
    def __init__(self,x,y,z) -> None:
        self.x=x
        self.y=y
        self.z=z    #位置信息
        self.speed=5    #无人机速度
        self.in_place=False
    
    def move(self,angel_x,angel_y,angel_z):
        '''向给定角度移动无人机'''
        self.x+=self.speed*np.cos(angel_x)
        self.y+=self.speed*np.cos(angel_y)
        self.z+=self.speed*np.cos(angel_z)

    
    def printPos(self):
        '''报告自身位置'''
        print('x坐标:{:3}'.format(self.x),end=',')
        print('y坐标:{:3}'.format(self.y),end=',')
        print('z坐标:{:3}'.format(self.z),end='\n')


class Formation():
    def __init__(self,n) -> None:
        self.number=n#编队的无人机数量
        uav_list=[]
        for i in range(n):
            x,y,z=random.randint(0,100),random.randint(0,100),random.randint(0,100)
            uav_list.append(Uav(x,y,z))
        self.uav_list=uav_list



if __name__=='__main__':
    uav_list=[]
    for i in range(4):
        x,y,z=random.randint(0,100),random.randint(0,100),random.randint(0,100)
        uav_list.append(Uav(x,y,z))
    for uav in uav_list:
        uav.printPos()
        