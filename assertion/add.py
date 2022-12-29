import os
base_url=os.path.abspath(__file__)
'''D:\pythonProject\assertion\add.py---当前文件路径'''
dir_url=os.path.dirname(base_url)
'''D:\pythonProject\assertion，指定文件的上一级'''
print(dir_url)
a='2b'
print('我要打印%s'%a)