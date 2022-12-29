
# 1.定义一个函数my_func(),函数执行结果为输出10行”hello world”
def my_func():
    print('hello world\n'*10)
    print('*'*50)
    i=0
    while i<10:
        print('hello world')
        i+=1
my_func()
# 2.定义一个函数my_sub(a, b), a和b为整数, 调用函数, 执行结果为显示a - b的差
# def my_sub(a,b):
#     if isinstance(a,int) and isinstance(b,int):
#             c=a-b
#             print(c)
#     else:
#         print('a,b必须为整数，请重新输入')
# my_sub(-1.2,2.2)


# 3.定义一个函数my_sub(a, b), a和b为整数, 调用函数, 函数的返回值为a - b的差
def my_sub(a,b):
    if isinstance(a,int) and isinstance(b,int):
            return a-b
    else:
        print('a,b必须为整数，请重新输入')
my_sub(-1.2,2.2)
#
# 4.定义一个函数my_num(a)，有一个参数，判断参数为奇数还是偶数,奇数函数返回False,偶数函数返回True
def my_num(a):
    if a%2==0:
        return True
    elif a%2==1:
        return False
    else:
        print('参数有误')

# my_num(11)
# 5.定义一个全局变量num1 = 0, 定义一个函数my_num(),在函数内部修改全局变量num1的值为10
num1=0
def my_num2():
    global num1
    num1=10
my_num2()

#
# # 6.定义一个函数my_sum1, 有四个参数（a, b, c, d） 函数返回值为四个参数相加的和
def my_sum2(a,b,c,d):
    if  (isinstance(a,int) or isinstance(a,float)) and (isinstance(b,int) or isinstance(b,float)) and (isinstance(c,int) or isinstance(c,float)) and (isinstance(d,int) or isinstance(d,float)):
        sum = a + b + c + d
        print(sum)
        return sum
    else:
        print('a,b,c,d只能是int或float')
my_sum2('p',2.2,3,6.0)
# 7.定义一个lambda函数,有1个参数,返回值是参数乘以
# lambda a: a*10







