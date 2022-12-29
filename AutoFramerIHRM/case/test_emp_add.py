import unittest
from api.EmpCURDapi import IhrmEmpCURD
from parameterized import parameterized
from common.DBUitl import DButil
from common.assert_util import assertionuse
from common.getHeader import get_header
from config import tel
class TestEmpAdd(unittest.TestCase):
    #全局手机号
    header=None
    @classmethod
    def setUpClass(cls) -> None:
        cls.header=get_header()

    def setUp(self) -> None:
        #删除手机号
        DButil.add_update_delete(f"DELETE FROM ihrm.bs_user where mobile ='{tel}'")
    def tearDown(self) -> None:
        DButil.add_update_delete(f"DELETE FROM ihrm.bs_user where mobile='%s'"%(tel))#删除手机号
    def test_empAdd(self,json_data,is_success,code,msg):
        resp=IhrmEmpCURD.add_emp(self.header,json_data)
        assertionuse(self,resp,is_success,code,msg)

