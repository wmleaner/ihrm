import unittest

from htmltestreport import HTMLTestReport

from ihrm_login import Test_ihrm
import htmltestreport
#创建suite实例
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(Test_ihrm))
#创建htmlreport实例
runner=HTMLTestReport('测试报告2.html')
#调用run()传入suite
runner.run(suite)