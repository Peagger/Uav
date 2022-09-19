import random
import os
root_dir=os.path.dirname(__file__)
def printNum(i):
    for k in range(i):
        print(random.randint(0,9),end='')
def roleid(strlist):
    print('11',end='')
    printNum(6)
    print(':[',end='')
    print('"'+strlist[0]+'"',end='')
    if(len(strlist)>=2):
        for i in range(1,len(strlist)):
            if(' ' in strlist[i]):
                for str in strlist[i].split(' '):
                    if(str!=''):
                        print(',"'+str+'"',end='')
            else:
                if(strlist[i]!=''):
                    print(',"'+strlist[i]+'"',end='')
    print('],')
with open(os.path.join(root_dir,'1.txt'),'r',encoding='utf-8') as f:
    dict=f.read().split('\n')
    for str in dict:
        roleid(str.split(',')[1:])

