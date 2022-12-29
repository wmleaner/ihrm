import requests

resp=requests.get(url="https://www.baidu.com/")
print(resp.text)