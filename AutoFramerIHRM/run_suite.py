import unittest
from case.logincaseTest import Testloginihrm
from htmltestreport import HTMLTestReport

#创建套件实例
suite=unittest.TestSuite()
#添加测试累
suite.addTest(unittest.makeSuite(Testloginihrm))
#创建HTmlTestReport类实例-Runner
loginrepoter=HTMLTestReport('./report/login.html',description='描述',title='标题')
#runner()调用run(),传入suite
loginrepoter.run(suite)