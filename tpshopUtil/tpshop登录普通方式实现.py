import  requests
import unittest
from PIL import Image
class TestTpshopLogin(unittest.TestCase):
    def test_loginSuccess(self):
        #创建session实例
        session=requests.Session()#正常是Session()
        #获取验证码
        resp_v=session.get(url='http://demo6.tp-shop.cn/index.php?m=Home&c=User&a=verify&r=0.8062324510316006',headers={"Content-Type":"image/png"})
        with open('vodify.jpg','wb') as vo:
            vo.write(resp_v.content)

        #seesion携带验证码，发送post请求登录
        resp=session.post(url='http://tpshop-test.itheima.net/',data={"username":"1","password":"123456"})

        #对结果进行断言
        self.assertEqual(200,resp.status_code)
        self.assertEqual("登录成功",resp.json().get("msg"))

    def test_phoneNoExists(self):
        # 创建session实例
        session = requests.Session()  # 正常是Session()
        # 获取验证码
        vodify = session.get(url='http://demo6.tp-shop.cn/index.php?m=Home&c=User&a=verify&r=0.8062324510316006',
                             headers={"Content-Type": "image/png"})
        # seesion携带验证码，发送post请求登录
        resp = session.post(url='http://tpshop-test.itheima.net/', data={"username": "1", "password": "123456"})
        print("响应结果=", resp.json())
        # 对结果进行断言
        self.assertEqual(200, resp.status_code)
        self.assertEqual("登录成功", resp.json().get("msg"))
