import os
import json
#获取data文件目录，这里设置的是项目文件名下data目录直接存放数据文件汇总
def getURL(file):
    projectURL=os.path.dirname(os.getcwd())
    data_url=os.path.join(projectURL,'data')
    fileURL=os.path.join(data_url,file)
    return fileURL
#读取data文件，文件格式为json类型
def build_data(file):
   with open(getURL(file),mode='r',encoding='utf8') as f:#with open 用完时打开的文件会被自动回收
       new_list = []
       json_content=json.load(f)
       for i in json_content:#使用json.load(f)后i是dict类型的，属于1行行读取的json数据。不使用这个读出来是str类型
           new_list.append(tuple(i.values()))

       return new_list


build_data('logindata.json')