# 导入第三方库
# import  selenium 会导入工具所有东西

from selenium import webdriver  #从哪里导入什么
from selenium.webdriver.common.by import By
'''selenium是python的工具，有三部分
1）ide:录制脚本----用的少
2）webdriver:库------提供对网页的各种操作，结合语言使用'''
driver=webdriver.Chrome()
driver.get('http://127.0.0.1/Home/user/login.html')
driver.maximize_window()
driver.find_element(by=By.ID,value='username').send_keys('18888888888')
driver.find_element(by=By.ID,value='password').send_keys('123456')
driver.find_element(by=By.ID,value='verify_code').send_keys('8888')
driver.find_element(by=By.NAME,value='sbtbutton').click()


