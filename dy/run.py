import re

#打开1.txt读取文件
with open('应用文写作.txt','r',encoding='utf-8') as f:
    txt=f.readlines()


    list=[]
    str=''
    list1 = []
    list2 = []
    dict={}

    for i in txt:
        str=str+i
    x=re.split('\d+、',str)
    for m in x:
        if not m is None:
            list.append(m)
    xiugai=set(list)
    for i in xiugai:
        with open('应用文写作修改.txt','a',encoding='utf-8') as f:
            f.write(i)






#使用strip按照序号分离
#分别存在不同的list序列中
#set去重复