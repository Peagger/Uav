双黄列表=[]
while('小猪'not in 双黄列表):
    for 玩家名称 in 双黄列表:
        print(玩家名称+'傻逼',end=' ')
    print('')
    玩家名称=input()
    双黄列表.append(玩家名称)
print(玩家名称+'聪明逼')