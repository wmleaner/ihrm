import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from parameterized import parameterized
import htmltestreport
import ddt


def write_data():
    with open('./login_data.txt', 'r') as f:
        datalist = f.readlines()
        data = []
        for i in datalist:
            i = i.strip('\n').split(',')
            data.append(i)
        return data


'''试自动化登陆---------参数化-加断言'''
@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:#初始化浏览器
        cls.driver=webdriver.Chrome()
        print('浏览器已打开，执行测试用例')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)

    def setUp(self) -> None:
        self.driver.get('http://ihrm2-test.itheima.net/')
        time.sleep(10)
    def tearDown(self) -> None:
        self.driver.close()

    @parameterized.expand(write_data())
    def test_login(self,username_key,password_key):
        username=self.driver.find_element(by=By.XPATH,value='''//input[@tabindex='1']''')#找到元素再发送数值
        username.clear()

        username.send_keys(username_key)
        password=self.driver.find_element(by=By.XPATH,value='''//input[@tabindex='2']''')
        password.clear()

        password.send_keys(password_key)
        bu_login=self.driver.find_element(by=By.XPATH,value="//button")
        bu_login.click()
        time.sleep(120)


    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(10)
        print('开始关闭浏览器')
        cls.driver.quit()
    def test_readData(self):
        print()

