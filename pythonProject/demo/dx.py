n='123qwe'#6位数
#直接切片
print('直接切片方法')
print(n[::-1])
#转化成列表后再聚合成字符串；join()将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串；
list_n=list(n)#得到['1','2','3','q','w','e']
list_n.reverse()#reverse()是列表的内置方法，字典，字符串或者元组中没有这个内置方法的，其作用是反向列表中元素
print('reverse函数方法')
print(''.join(list_n))#拼接到一起
#新建一个列表，从后往前添加元素
str1_list = []
for i in range(len(list(n))-1,-1,-1):#遍历，从最后一个数依次倒数取
    print(i)#543210
    str1_list.append(n[i])
print('新建列表apend方法')
print(''.join(str1_list))
#5递归实现
def rec(n):#定义函数
    if len(n) != 1:
        rec(n[1:])
    print(n[0], end='')
rec(n)
