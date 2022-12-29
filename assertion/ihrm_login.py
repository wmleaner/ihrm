import requests
import parameterized
import htmltestreport
import jsonschema

resp=requests.post(url="http://ihrm2-test.itheima.net/api/sys/login",json={"mobile":"13800000002","password":"123456"})
print(resp.json())
