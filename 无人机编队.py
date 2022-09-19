
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
    
    def move(self,dir):
        '''向给定方向向量移动无人机'''
        self.x+=self.speed*dir[0]
        self.y+=self.speed*dir[1]
        self.z+=self.speed*dir[2]

    
    def printPos(self):
        '''报告自身位置'''
        print('x坐标:{:3}'.format(self.x),end=',')
        print('y坐标:{:3}'.format(self.y),end=',')
        print('z坐标:{:3}'.format(self.z),end='\n')


class Formation():
    '''编队类'''
    def __init__(self) -> None:
        self.number=0           #编队的无人机数量
        self.uav_list=[]        #无人机对象列表
    
    def calculateDistance(self,pos1:list,pos2:list):
        '''计算空间距离'''
        distance=0
        for i in range(3):
            distance+=(pos1[i]-pos2[i])**2
        return np.sqrt(distance)
    
    def calculateAngel(self,pos1:list,pos2:list):
        '''计算方向向量  pos1指向pos2'''
        dir=np.array([pos2[0]-pos1[0],pos2[1]-pos1[1],pos2[2]-pos1[2]])
        length=np.sqrt(dir.dot(dir))
        dir=dir/length
        return dir

    def isCollison(self,u1:Uav,u2:Uav):
        '''判断无人机是否会碰撞,True碰撞,False不碰撞'''
        distance=self.calculateDistance([u1.x,u1.y,u1.z],[u2.x,u2.y,u2.z])
        if (distance>u1.r+u2.r):
            return False
        return True

    def addUav(self,u:Uav):
        '''将无人机纳入编队'''
        for uav in self.uav_list:
            if(self.isCollison(uav,u)):
                return False
        self.uav_list.append(u)
        self.number+=1
        return True

    def autoRandomAdd(self,n,x1=0,x2=100,y1=0,y2=100,z1=0,z2=100):
        '''随机生成编队'''
        while(self.number<n):
            x,y,z=random.randint(x1,x2),random.randint(y1,y2),random.randint(z1,z2)
            self.addUav(Uav(x,y,z))
    
    def showUav(self):
        '''显示编队信息'''
        print('共{}架无人机'.format(self.number))
        for uav in self.uav_list:
            uav.printPos()



if __name__=='__main__':
    f=Formation()
    # f.autoRandomAdd(10)
    # f.showUav()
    res=f.calculateAngel([0,0,0],[3,4,0])
    print(res)