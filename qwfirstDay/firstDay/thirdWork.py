# a=[1,2,'6','summer']
# print('i在这个列表里是True是False： '+str('i' in a))
dict_1={"class_id":45,'num':20}
if dict_1.get('num')> 5:
    print(dict_1.get('num'))
else:
    print('人数比5小')
# 第一种手动
# list3=['方方土','七木','荷花鱼','kingo','Amiee','焕蓝']
# dict_list1={'name':'方方土' ,'性别':'' ,'年龄':'' ,'城市':'' }
# dict_list2={'name':'七木' ,'性别':'' ,'年龄':'' ,'城市':'' }
# dict_list3={'name':'荷花鱼' ,'性别':'' ,'年龄':'' ,'城市':'' }
# dict_list4={'name':'kingo' ,'性别':'' ,'年龄':'' ,'城市':'' }
# dict_list5={'name':'Amiee' ,'性别':'' ,'年龄':'' ,'城市':'' }
# dict_list6={'name':'焕蓝' ,'性别':'' ,'年龄':'' ,'城市':'' }
# list_dictfinally=[dict_list1,dict_list2,dict_list3,dict_list4,dict_list5,dict_list6]
# print(list_dictfinally)

# 第二种自动  dict()
list3=['方方土','七木','荷花鱼','kingo','Amiee','焕蓝']
list4=[]
for i in list3:
    nameDict=dict(name=i)
    nameDict.update(性别='',年龄='',城市='')
    listf = []
    listf.append(nameDict)
    list4=list4+listf
print(list4)
print('****************************')
# 第二种参考方式
list3=['方方土','七木','荷花鱼','kingo','Amiee','焕蓝']
list4=[]
list5=[18,19,20,21,22,23]
list6=['男','男','女','男','女','男']
list7=['成都','武汉','北京','重庆','河南','杭州']
for i in range(6):
    dict_2=dict(name=list3[i],年龄=list5[i],性别=list6[i],城市=list7[i])
    list4.append(dict_2)
print(list4)

