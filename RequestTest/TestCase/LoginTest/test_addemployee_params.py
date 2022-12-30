import unittest
from parameterized import parameterized
from api.addEnp import addemplyee
from Common.readFile import read_json
from Common.assertion import assertionuse
'''由于新建员工需要反复测试，但是一点运行手机就注册掉了，所以引入数据库对手机号进行及时删除数据
'''
class TestaddEmployee(unittest.TestCase):
    @parameterized.expand(read_json('addeEmp.json'))
    def test_addemployee(self,desc,json,is_success,code,msg):
        resp=addemplyee.add_employee(json)
        # assertionuse(self,resp,is_success,code,msg)