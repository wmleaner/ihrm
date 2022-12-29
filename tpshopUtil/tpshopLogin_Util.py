#主要封装tpshop的登录方法
import requests
from PIL import Image

import pytesseract
class tpshoplogin(object):
    @classmethod
    def vifoy(cls,session,vorify_url):
        resp_v=session.get(url=vorify_url, headers={"Content-Type": "image/png"})
        with open('vodify.jpg','wb') as f:
            f.write(resp_v.content)
            f.flush()
            f.close()
        v_string=input("请输入vodify.jpg显示的验证码文字：")
        return v_string


    @classmethod
    def login(cls,session,login_url,login_data):
        resp=session.post(url=login_url,data=login_data)
        return resp


