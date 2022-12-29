
import requests


class department(object):
#部门增加
    @classmethod
    def department_add(cls,header,jsondata):
        URL='http://ihrm2-test.itheima.net/api/company/department'
        resp=requests.post(url=URL,headers=header,json=jsondata)
        return resp

#部门查询
    @classmethod
    def department_query(cls,department_id,header):
        URL = 'http://ihrm2-test.itheima.net/api/company/department/'+department_id
        respquery = requests.get(url=URL, headers=header)
        return respquery

#部门修改

    @classmethod
    def department_modify(cls,department_id,header,jsondata):
        URL = 'http://ihrm2-test.itheima.net/api/company/department/'+department_id
        respmodify = requests.put(url=URL, headers=header, json=jsondata)
        return respmodify


#部门删除
    @classmethod
    def department_delete(cls,department_id,header):
        URL = 'http://ihrm2-test.itheima.net/api/company/department/'+department_id
        resp = requests.delete(url=URL, headers=header)
        return resp

