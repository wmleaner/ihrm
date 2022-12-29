import random
#print(random.randint(10,12))
#强化多个条件的逻辑运算
#体会import导入工具包的使用
#需求，从电脑控制台输入出的拳---石头1，剪刀2，布3
print('请出石头剪刀布，石头1，剪刀2，布3')
user_input=int(input('出拳为：'))
comput=random.randint(1,3)
print("comput出拳",comput)
if comput ==user_input:
    print("出拳一样，平局")
elif (comput==1 and user_input==3) or (comput==2 and user_input==1) or (comput==3 and user_input==2):
    print("电脑输了")
else:
    print('电脑赢了')