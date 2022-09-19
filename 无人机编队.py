
from dis import dis
import random
from turtle import pos
import numpy as np



class Uav():
    '''无人机类'''
    def __init__(self,x,y,z) -> None:
        self.x=x
        self.y=y
        self.z=z            #位置信息
        self.speed=5        #无人机速度
        self.in_place=False
        self.r=0.5     #无人机半径
    
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
    '''编队类'''
    def __init__(self) -> None:
        self.number=0#编队的无人机数量
        uav_list=[]
        self.uav_list=uav_list
    
    def calculateDistance(self,pos1:list,pos2:list,dimension=3):
        '''计算空间距离'''
        distance=0
        for i in range(dimension):
            distance+=(pos1[i]-pos2[i])^2
        return np.sqrt(distance)

    def isCollison(self,u1:Uav,u2:Uav):
        '''判断无人机是否会碰撞,True碰撞,False不碰撞'''
        distance=self.calculateDistance([u1.x,u1.y,u1.z],[u2.x,u2.y,u2.z])
        if (distance>u1.r+u2.r):
            return False
        return True

    def addUav(self,uav:Uav):
        '''将无人机纳入编队'''
        for uav in self.uav_list:
            if(self.isCollison):
                return False
        self.uav_list.append(uav)
        self.number+=1
        return True



if __name__=='__main__':
    uav_list=[]
    for i in range(4):
        x,y,z=random.randint(0,100),random.randint(0,100),random.randint(0,100)
        uav_list.append(Uav(x,y,z))
    for uav in uav_list:
        uav.printPos()
        