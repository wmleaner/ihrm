import requests
class ihrmlogin(object):
    @classmethod
    def loginihrm(cls,login_data):
        url='http://ihrm2-test.itheima.net/api/sys/login'
        headers={"Content-Type":"application/json"}
        resp=requests.post(url=url,headers=headers,json=login_data)
        return resp
'''       
 'str' object has no attribute 'items'是说有一个参数传成错误的了，变成了字符串，这时候就要检验穿进去的json等是不是不经意加了引号,是绿色的字典才对
'''

