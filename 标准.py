# from turtle import position

import copy
import random
import numpy as np
# 双黄列表=[]
# while('小猪'not in 双黄列表):
#     for 玩家名称 in 双黄列表:
#         print(玩家名称+'傻逼',end=' ')
#     print('')
#     玩家名称=input()
#     双黄列表.append(玩家名称)
# print(玩家名称+'聪明逼')


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
        for i in self.position:
            print(i,end=',')
        print('\n')


if __name__=='__main__':
    position=[]
    for i in range(4):
        x,y,z=random.randint(0,100),random.randint(0,100),random.randint(0,100)
        print(x,y,z)
        