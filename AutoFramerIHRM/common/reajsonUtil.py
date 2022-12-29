import json
import os


def read_json(filename):
    baseUrl = os.path.dirname(os.path.abspath(__file__))  # 获取当前所在目录=
    project_url = os.path.dirname(baseUrl) # 获取上一级目录
    finally_url=os.path.join(project_url,'data',filename)
    # json_path = os.path.join(project_url, 'data\login_data.json')  # 拼接json测试数据文件名
    with open(finally_url,'r',encoding='utf8')as f:
        json_content=json.load(f)
        new_list=[]
        for i in json_content:
            data=tuple(i.values())#参数化的@parameterizd.expend函数只能读取【(),(),(),()】元祖列表，所以需要转化
            new_list.append(data)
            #new_list.append(data[1:])
        return new_list



