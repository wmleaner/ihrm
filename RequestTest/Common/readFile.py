import os
import json
import xlrd




baseUrl=os.path.dirname(os.path.abspath(__file__))#获取当前所在目录=
project_url=os.path.dirname(baseUrl)#获取上一级目录
txt_path=os.path.join(project_url,'data\login_data.txt')#拼接txt测试数据文件名
json_path=os.path.join(project_url,'data\login_data.json')#拼接json测试数据文件名
excel_path=os.path.join(project_url,'data\login_data.xls')
print(excel_path)

'''读取txt文件
1.需要python如何读取文件 
2.需要python操作list
3.需要使用split()对字符串进行分割'''
def read_txt():
    print('----------txt----------')
    with open(txt_path,encoding='utf8') as f:
         txt_line=f.readlines()#readline()只读取文件的一行，返回str类型--------readlines()每次按行读取整个文件内容，将读取到的内容放到一个列表中，返回list类型
         for i in txt_line:#遍历字符串
            i=i.split(',')
            print(i)
         print('----------2txt2----------')
'''读取json文件'''

def read_json():
    with open(json_path,encoding='utf8')as f:
        json_content=json.load(f)
        new_list=[]
        for i in json_content:

            data=tuple(i.values())#参数化的@parameterizd.expend函数只能读取【(),(),(),()】元祖列表，所以需要转化
            new_list.append(data)
            #new_list.append(data[1:])
        print(new_list)
        return new_list




'''读取excel文件,现在的版本不支持xlsx格式了'''
def read_excel():
    open_excel=xlrd.open_workbook(excel_path)
    sheet=open_excel.sheet_by_index(0)
    print(sheet.nrows)
    for i in range(sheet.nrows):
        print(i)



'''读取csv文件'''


'''
------一些目录操作代码-------一些目录操作代码-----一些目录操作代码--------一些目录操作代码------------一些目录操作代码------------------------一些目录操作代码-----------------------一些目录操作代码------------------------------一些目录操作代码------------------------------------------------------------------
print('***获取当前目录***')
print("当前目录是:os.getcwd()
print("当前目录是:os.path.abspath(os.path.dirname(__file__))
 
print('***获取上级目录***')
print("上级目录是:os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print("上级目录是:os.path.abspath(os.path.dirname(os.getcwd()))
print("上级目录是os.path.abspath(os.path.join(os.getcwd(), "..")))                           
 
print('***获取上上级目录***')
print("上上级目录是:os.path.abspath(os.path.join(os.getcwd(), "../..")))






'''



