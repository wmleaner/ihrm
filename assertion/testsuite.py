import unittest
from testcase import Testd1
'''必须要用from导入方法，直接导入文件没有'''
from testcase import Testd2
'''#实例化对象'''
suite=unittest.TestSuite()

suite.addTest(Testd1('test1_1'))
suite.addTest(Testd1('test1_2'))
suite.addTest(Testd2('test2_1'))
suite.addTest(Testd2('test2_2'))
'''实例化 执行对象 unittest.TextTestRunne'''
runner=unittest.TextTestRunner()
runner.run(suite)
