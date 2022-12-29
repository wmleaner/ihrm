import unittest
import requests
from tpshopLogin_Util import tpshoplogin
'''想从类导入里面的方法会报错-因为要从文件名先找到类，总不能import类.方法吧
    测试登陆成功的断言，因为返回值不一样，所以设置不一样的测试用例
    可以封装通用断言文件----一般单独封装，不存在测试里面'''
def comm_ass(self,resp,code,status,msg):
    self.assertEqual(code,resp.status_code)
    self.assertEqual(status,resp.json().get('status'))
    self.assertEqual(msg,resp.json().get('msg'))


class TestshopUtil(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.Session()
    def setUp(self) -> None:
        self.string= tpshoplogin.vifoy(self.session,
                                   'http://www.cunzheer.com/index.php?m=Home&c=User&a=verify&r=0.4084225809860249')
    def test_loginOK(self):
        #调用自己封装的方法然后断言借口调用返回的数据
        resp=tpshoplogin.login(self.session,'http://www.cunzheer.com/index.php?m=Home&c=User&a=do_login&t=0.8003711663583042',{"username":"1","password":"123456","verify_code":self.string})
        print(resp.json())
        comm_ass(self,resp,200,-1,'账号不存在')
