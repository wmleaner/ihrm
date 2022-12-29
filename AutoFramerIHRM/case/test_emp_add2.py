import unittest
from api.EmpCURDapi import IhrmEmpCURD
from parameterized import parameterized
from common.DBUitl import DButil
from common.getHeader import get_header
from common.reajsonUtil import read_json
from common.assert_util import assertionuse
from config import tel
'''参数化后




'''

class TestEmpAddParams(unittest.TestCase):
    header=None
    #全局手机号
    @classmethod
    def setUpClass(cls) -> None:
        cls.header=get_header()#要是不写cls就不是同一个变量

    def setUp(self) -> None:
        #删除手机号
        DButil.add_update_delete(f"DELETE FROM ihrm.bs_user where mobile ='{tel}'")
    def tearDown(self) -> None:
        DButil.add_update_delete("DELETE FROM ihrm.bs_user where mobile='{tel}'")


    @parameterized.expand(read_json('empAdd.json'))
    def test_empAdd(self,desc,json_data,is_success,code,msg):
        resp = IhrmEmpCURD.add_emp(self.header, json_data)
        print(desc,":",resp.json())
        assertionuse(self,resp,is_success,code,msg)
