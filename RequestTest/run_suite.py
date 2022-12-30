import unittest
from htmltestreport import HTMLTestReport
import os
from Common.readFile import project_url
from TestCase.LoginTest.test_login_params import TestLogincase
from Common.readFile import read_json
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogincase))
login_report=os.path.join(project_url, 'result\loginre.html')
login_rep=HTMLTestReport(login_report,title='登录测试报告2',description='登录')
login_rep.run(suite)#提示'HTMLTestReport' object has no attribute 'passrate'可能是测试类里面没有测试case,如test_login写成teat_login

