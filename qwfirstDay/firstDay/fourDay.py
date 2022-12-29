# 1 把字符串转成列表-------这里面会把字符串的每一项目变成列表
# str='qwertyuiop'
# print (list(str))
# 把字符串转成列表-------这里面会把字符串作为一个整体弄成列表
# str2='qwertyuiop'
# print (str2.split())
# 定义函数来弄
# m=input('请输入一串字符: ')
# def listStr():
#     print(list(m))
# listStr()

#  2.完成任意整数序列的相加│   -生成一个整数序列，里面全是数字。求里面所有数字的和
# n=input('请输入一个整数序列: ')
# def sumrange():
#     sum = 0
#     for i in n:
#         m=int(i)
#         sum+=m
#     print('d序列号数字之和是:%d'%(sum))
#     print('format序列号数字之和是:{}'.format(sum))
#     print('直接拼接序列号数字之和是:'+str(sum))  #直接+sum会分不清是拼接还是数值想加，所以要转换类型
# sumrange()
#2的第二种方式，直接传参数
def sumrange(n):
    sum = 0
    for i in n:
        m=int(i)
        sum+=m
    print('d序列号数字之和是:%d'%(sum))
    print('format序列号数字之和是:{}'.format(sum))
    print('直接拼接序列号数字之和是:'+str(sum))  #直接+sum会分不清是拼接还是数值想加，所以要转换类型
sumrange('123456')

# 3.判断一个对象（列表，字典，字符串）的长度是不是大于5，如果大于5输出true
