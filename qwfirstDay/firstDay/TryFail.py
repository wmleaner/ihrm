# try:
#     #当try里面有无数个bug,只会执行第一个异常捕获---即nameError
#     print(x)
#     n=2/0
#     m=[1,2]
#     m[3]=0
# except NameError as ret:#变量未定义异常
#    # try出现异常，except一定执行。try没有异常，except就不会报错
#     print('变量未定义：%s'%ret)
# except ValueError as exp:#值错误异常
#     print('值错误异常：%s'%exp)
# except ZeroDivisionError as zro:#除数为0异常
#     print('除数为0错误：%s'%zro)
# except IndexError as index:#序列错误异常
#     print('序列错误：%s'%index)
#
#
# # 一次捕获多异常----出现错误处理结果一样
# try:
#     open('22.txt','r')
#     def ab(a,b):#会打印漏网之鱼，因为既不是name也不是ile错误
#         c=a+b
#     ab()
# except (NameError,FileExistsError):#不是说处理所有异常，而是说总会出现except中的一种
#     print('资源未找到')
# except Exception:
#     print('漏网之鱼，可以捕获任意异常')

#异常完整语法
try:
    #当try里面有无数个bug,只会执行第一个异常捕获---即nameError
    file=open('22.txt', 'w')
    file.write([1,2,3,4])
    print('报错，只能字符串')
    file.close()
    print('看到我文件才关闭')
except NameError as ret:#变量未定义异常
   # try出现异常，except一定执行。try没有异常，except就不会报错
    print('变量未定义：%s'%ret)
except ValueError as exp:#值错误异常
    print('值错误异常：%s'%exp)
except ZeroDivisionError as zro:#除数为0异常
    print('除数为0错误：%s'%zro)
except IndexError as index:#序列错误异常
    print('序列错误：%s'%index)
except Exception as exc:
    print('可以捕获任意异常%s'%exc)
else:
    print('try部分没有异常，else一定会执行')
finally:
    print('无论有没有异常，都会执行')
    file.close()
    print('看到我，---因为finally----文件才关闭')



