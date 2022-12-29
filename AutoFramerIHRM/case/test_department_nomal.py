import unittest
import pymysql
from api.departmentapi import department
from parameterized import parameterized
from common.DBUitl import DButil
from common.assert_util import assertionuse
class TestDepartmentContol(unittest.TestCase):


    def test_departmentAdd(self):
        header={"Content-Type":"application/json","Authorization":"Bearer 33c6003e-f5a8-4abd-a555-800f6589367b"}
        json_data={"name":"1213日测试数据","code":"15630"}
        resp=department.department_add(header,json_data)
        print(resp.json())
        assertionuse(self,resp,True,10000,"操作成功！")
    def test_departmentQuery(self):
        resp_s=department.department_query('1602520587954155520',{"Content-Type":"application/json","Authorization":"Bearer 33c6003e-f5a8-4abd-a555-800f6589367b"})
        assertionuse(self, resp_s, True, 10000, "操作成功！")
        print(resp_s.json())
    def test_departmentModify(self):
        resp_m=department.department_modify('1602520587954155520',{"Content-Type":"application/json","Authorization":"Bearer 33c6003e-f5a8-4abd-a555-800f6589367b"},{"name":"1213日测试数据1213"})
        assertionuse(self, resp_m, True, 10000, "操作成功！")
        print(resp_m.json())
    # def test_departmentDelete(self):
    #     department.department_delete()