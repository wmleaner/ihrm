'''
不可变：str\float\int\touple\complex---------原内存空间不可更改，只能重新开辟内存空间
可变：list\dict
'''
str1='sb'
print(str1,id(str1))
str1+='big sb'
print(str1,id(str1))

list1=[10,19.3,'sb',(98,100),{'keyword':'z'}]
print(list1,id(list1))
list1.append('wowwwww')
print(list1,id(list1))
'''
可变类型的数据变化，是通过方法来实现的
如果给一个可变类型的变量赋值了新数据，引用会修改
'''
my_list=[10,20]
print(my_list)