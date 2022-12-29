import unittest
import htmltestreport
# '''定义测试类,只需要继承unittest.testcase类就是测试类'''
# class Testcase(unittest.TestCase):
#      '''书写测试方法 方法中的代码就是真正用例代码，方法名必须要以test开头'''
#      def test_method1(self):
#          print("测试方法1")
#      def test_method2(self):
#         print("测试方法2")
# '''执行
# 4.1在类名后右键运行-----------执行所有
# 4.2在方法名后右键运行----------执行该方法
# 4.3在主程序使用unittest.man()来运行'''
# if __name__=='_main_':
#     unittest.main()
class Testd1(unittest.TestCase):
    def test1_1(self):
        print("1-1")
    def test1_2(self):
        print("1-2")
class Testd2(unittest.TestCase):
    def test2_1(self):
        print("2-1")
    def test2_2(self):
        print("2-2")
