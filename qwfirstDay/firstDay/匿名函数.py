def fun():
    print('------fun()--------')
fun()
print(fun)#函数名其实相当于变量名保存当前函数一个地址，加（）相当于地址


def sum_num(a,b,opt):
    print('a=%d'%a)#打印10
    print('b=%d' % b)#打印20
    print('%d+%d=%d' % (a,b,opt(a,b)))#打印10+20=30
sum_num(10,20,lambda x,y:x+y)
#其中lambda x,y:x+y保存的是一个地址，传给了opt
