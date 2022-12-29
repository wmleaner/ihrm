info='hello.paython.paython.java'#想要替换第二个python，replace只能替换第一个
#倒数的num还是两个都变  info.replace('paython','py',1)
list1=info.split('.')
list1[2]='py'
print('.'.join(list))

info2='hello.py.py.java'
tuple2=info2.rpartition('py')#rpartition元组形式拉开字符串，必须要赋值给其他变量，原先的字符串没有改变
list_info=list(tuple2)#必须要赋值给其他变量，tuple2在list后原先的tuple2还是没有改变
list_info[1]='pppppp'
info2=''.join(list_info)
print(info2)
'''print(info2)#没有变还是hello.py.py'''



