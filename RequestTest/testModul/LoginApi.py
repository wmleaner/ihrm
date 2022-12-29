import requests
'''
导包或文件调用出错：
              1.检查名字是否不复合规范
              2.检查符号是否存在中文
              3.缩进问题-看出错前后语句是否正常缩进，是否该在类里面
              4.查看传参形式，比如传json的login_data,出现‘{"mobile":"13800000002","password":"123456"}’这样的，其实json这样写变成了字符串了'''


class LoginObj(object):

    @classmethod
    def loginapi(cls,session,login_url,login_data):
        resp=session.post(url=login_url,json=login_data)
        return resp

'''
调用时可以不用写cls这些'''
# if __name__ == '__main__':
#     session=requests.Session()
#     h=LoginObj.loginapi(session,'http://ihrm2-test.itheima.net/api/sys/login',{"mobile":"13800000002","password":"123456"})
#     print(h.json())