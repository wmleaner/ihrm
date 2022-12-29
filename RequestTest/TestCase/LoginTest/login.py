import unittest

from parameterized import parameterized
from Common.assertion import assertionuse
from testModul.LoginApi import LoginObj
from Common.readFile import read_json
import requests


'''
    @parameterized 装饰符接受一个由tuples或param(...)组成的列表等：
    导包或文件调用出错：
              1.检查名字是否不复合规范
              2.检查符号是否存在中文
              3.缩进问题-看出错前后语句是否正常缩进，是否该在类里面
              4.查看传参形式，比如传json的login_data,出现‘{"mobile":"13800000002","password":"123456"}’这样的，其实json这样写变成了字符串了
              ctrl+P提示
    设计数据成如下：
                data=[{"req_dody":{"username="xxx","pwd"：”123456“}，”code":1234},
                      {"req_dody":{"username="xxx","pwd"：”123456“}，”code":1234},]是为了在测试多参、少参时直接把数据传过去就行，如果直接把user等拆出来，到时候就要重新封装读参数等
'''


class TestLogincase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session=requests.Session()

    @parameterized.expand(read_json())
    def test_login(cls,desc,username,password,expected):#本来就是cls而已，参数化就要修改为与参数对应
        login_resp=LoginObj.loginapi(cls.session,'http://ihrm2-test.itheima.net/api/sys/login',{"mobile":username,"password":password})
        print(login_resp.json())
        # cls.assertEqual('1000',login_resp.json,'cehng')
        assertionuse(cls,login_resp,expected)#只有True表示真假，true表示字符串


    # def test_login(cls):#本来就是cls而已，参数化就要修改为与参数对应
    #     login_resp=LoginObj.loginapi(cls.session,'http://ihrm2-test.itheima.net/api/sys/login',{"mobile":"13800000002","password":"123456"})
    #     assertionuse(cls,login_resp,True,10000,'操作成功！')#只有True表示真假，true表示字符串




