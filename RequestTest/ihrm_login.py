import unittest
import requests
class Test_ihrm(unittest.TestCase):

    def test_login(self):
        url = 'http://ihrm2-test.itheima.net/api/sys/login'
        headers = {"Content-Type": "application/json"}
        login_data = {"mobile": "138000000002", "password": "123456"}
        resp=requests.post(url=url,headers=headers,json=login_data)
        result= resp.json()
        #return result.get('message')获取返回的值{'success': False, 'code': 20001, 'message': '用户名或密码错误', 'data': None}
        self.assertEqual('用户名或密码错误',result.get('message'))
        self.assertEqual(20001, result.get('code'))
        self.assertEqual(False, result.get('success'))



