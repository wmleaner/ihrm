import requests
'''由于token1小时就会变化，所以记得即使更改再运行，不然会一直运行中然后再报错'''
#新增员工
url='http://ihrm2-test.itheima.net/api/sys/user'
headers={"Content-Type":"application/json","Authorization":"Bearer 63ccefcc-de23-410d-8048-fb7817b718a3"}
json_data={
    "username":"新员工0081",
    "mobile":"18976512543",
    "workNumber":"5617"
}
resp=requests.post(url=url,headers=headers,json=json_data)
print("新增员工：",resp.json())
# 查询员工
# surl=' http://ihrm2-test.itheima.net/api/sys/user/1594541009377701888'
# respserarch=requests.get(url=surl,headers=headers)
# print('查询导员信息为：',respserarch.json())
# # 修改员工
# modifyUrl='http://ihrm2-test.itheima.net/api/sys/user/1594540261050953728'
# modifydata={"username":"新员工0081改了",
# "mobile":"18976512543",
#     "workNumber":"5619"
#
#     }
# modify=requests.put(url=modifyUrl,headers=headers,json=modifydata)
# print("修改新增信息",modify.json())
# # 删除员工
# deleteurl='http://ihrm2-test.itheima.net/api/sys/user/1594540261050953728'
# delete=requests.delete(url=deleteurl,headers=headers)
# print(delete.json())

