from Common.get_header import getheader
import requests
class addemplyee(object):
    @classmethod
    def add_employee(cls,addData):
        header=getheader()
        resp=requests.post(url='http://ihrm2-test.itheima.net//api/sys/user',headers=header,json=addData)
        print(resp.json())
