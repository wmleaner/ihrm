import os
import  shutil
# x=os.listdir()
# x2=x=os.listdir('.')
# print(x,x2)
#
# os.mkdir('C:\\Users\\Administrator\\Desktop\\python')
# file=open('C:\\Users\\Administrator\\Desktop\\python\\py.py','w')
# shutil.rmtree('C:\\Users\\Administrator\\Desktop\\python')
# print(os.getcwd())
# os.chdir('D:\\pythonProject\\qwfirstDay\\card_system')
# print(os.getcwd())
# print(os.path.isdir('D:\\pythonProject\\qwfirstDay\\firstDay\\info4.txt'))
# print(os.path.exists('D:\\pythonProject\\qwfirstDay\\firstDay'))
# for i in range(10):
#     file=open('D:\\pythonProject\\qwfirstDay\\firstDay\\pl\\%d.txt'%i,'w')
def createfiles():
    os.getcwd()
    print('查看当前目录看是否存在pl2',os.getcwd())
    name=['qw.txt','er.c','ty.py','ui.html','op.txt']
    if os.path.exists('./pl2'):
        print('pl2存在，正在准备删掉11111111111')
        shutil.rmtree('./pl2')
        print('pl2已经执行删除操作')
        '''本来需要else来设置当文件夹不存在时也执行重新新建的
            但是利用python的缩进关系，把新建的代码放到if外面，那么无论if是真是假都要执行'''
    os.mkdir('./pl2')
    os.chdir('./pl2')
    for i in name:
        open('%s'%i,'w')
createfiles()