import jsonschema
import  json
import requests
import ihrm_login
login_resp=ihrm_login.resp.json()
token="Bearer "+login_resp["data"]
# token=""+login_resp.get
# modify_url=1
modify_resp=requests.put(url="http://ihrm2-test.itheima.net/api/sys/user/1597534262544838656",
                         headers={"Authorization":token},json={"username":"python好难学1129"})
print(modify_resp.json())