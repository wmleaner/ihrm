import requests
#员工管理模块的 接口对象层次
class IhrmEmpCURD(object):
    #添加员工
    @classmethod
    def add_emp(cls,header,json_data):
        url = 'http://ihrm2-test.itheima.net/api/sys/user'
        resp = requests.post(url=url, headers=header, json=json_data)
        return resp
    #查询员工
    @classmethod
    def query_emp(cls,emp_id,header):
        surl = ' http://ihrm2-test.itheima.net/api/sys/user/'+emp_id
        resp_serarch = requests.get(url=surl, headers=header)
        return resp_serarch
    #修改员工
    @classmethod
    def modify_emp(cls,emp_id,header,modifydata):
        modifyUrl = 'http://ihrm2-test.itheima.net/api/sys/user/'+emp_id
        resp_modify = requests.put(url=modifyUrl, headers=header, json=modifydata)
        return  resp_modify
    #删除员工
    @classmethod
    def delete_emo(cls,emp_id,header):
        deleteurl='http://ihrm2-test.itheima.net/api/sys/user/'+emp_id
        resp_delete=requests.delete(url=deleteurl,headers=header)
        return  resp_delete

