
import requests
def getheader():
    resp=requests.post(url='http://ihrm2-test.itheima.net/api/sys/login',json={"mobile":"13800000002","password":"123456"})
    header={"Content-Type":"application/json"}
    str='Bearer '+resp.json().get('data')
    header["Authorization"]=str
    return header

