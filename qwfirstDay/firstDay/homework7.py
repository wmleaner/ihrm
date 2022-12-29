# 1.
# 定义一个程序员类(coder) ，有两个方法, 分别为工作(work)
# 方法，睡觉(sleep)
class Progranmmer():
    def __init__(self):
        self.name='张三'
        self.sex='男'
        self.age=30
    def work(self):
        print('程序员正在写代码')
    def sleep(self):
        print('程序员终于能睡觉了')
    def __del__(self):
        print('再见程序员')
w=Progranmmer()
print(w.name)
print(w.age)
print(w.sex)
w.work()
w.sleep()










# 2.
# 定义一个程序员类, 有__init__方法,
# 在__init__方法中添加name, age, sex属性;
# 其中name属性的值为”张三”;
# sex属性的值为”男”;
# age属性的值为30;
#
# 3.
# 为程序员类提供__del__方法, 在程序员类的实例对象销毁时, 输出”再见程序员”