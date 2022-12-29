'''
定义函数获取header
'''
import requests
def get_header():
    url='http://ihrm2-test.itheima.net/api/sys/login'
    data={"mobile":"13800000002","password":"123456"}
    resp=requests.post(url=url,json=data)
    token='Bearer '+resp.json().get('data')
    header={"Content-Type":"application/json",
            "Authorization":token}
    return header
