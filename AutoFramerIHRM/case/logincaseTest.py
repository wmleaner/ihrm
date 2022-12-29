import unittest
from api.loginapi import ihrmlogin
from common.reajsonUtil import read_json
from parameterized import parameterized
from common.assert_util import assertionuse



class Testloginihrm(unittest.TestCase):
    @parameterized.expand(read_json('login_data.json'))
    def test_login(self,desc,login_data,is_succes,code,msg):
        resp=ihrmlogin.loginihrm(login_data)
        print(desc,":",resp.json())
        assertionuse(self,resp,is_succes,code,msg)#
