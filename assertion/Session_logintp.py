#session登录tpshop，里面有动态图片验证码
import requests
import jsonschema
import time
import pytesseract
#创建seesion实例
session=requests.Session()
#使用seesion实例调用get发送验证码请求——————————不使用cookie
resp_v=session.get(url="http://www.cunzheer.com/index.php?m=Home&c=User&a=verify&r=0.4084225809860249")
fp = open('code.jpg', "wb") #以字节流的形式写入并保存
fp.write(resp_v.content)
fp.flush()# 强制刷新
fp.close()

time.sleep(3)
st=input("验证码：")
#使用seesion实例调用post请求，发送登录请求
resp=session.post(url="http://www.cunzheer.com/index.php?m=Home&c=User&a=do_login&t=0.8003711663583042",headers={"Content-Type":"application/x-www-form-urlencoded","charset":"UTF-8"},
             data={"username":"2863463318@qq.com","password":"123456","verify_code":st})
print(resp.json())
#使用同一个seesion查看订单页面
resp_0=session.get(url="http://www.cunzheer.com/Home/Order/order_list.html")
print(resp_0.text)