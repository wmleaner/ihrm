import unittest
from testcase import Testd1
'''必须要用from导入方法，直接导入文件没有'''
from testcase import Testd2
'''#实例化对象'''
suite=unittest.TestSuite()
'''添加整个测试类
suite.addTest(unittest.makeSuite(测试类名))----在不同python中可能不会有提示
'''
suite.addTest(unittest.makeSuite(Testd1))
suite.addTest(unittest.makeSuite(Testd2))
'''实例化 执行对象 unittest.TextTestRunne'''
runner=unittest.TextTestRunner()
runner.run(suite)
