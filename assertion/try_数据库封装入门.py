import pymysql
#连接数据库
'''全局属性，使得没有连接等错误情况下cursor.close等不报错'''
conn=None
cursor=None
try:
    conn=pymysql.connect(host="211.103.136.244",port=7061,user="student",password="iHRM_student_2022",database="test_db",charset="utf8")
    #创建游标
    cursor=conn.cursor()
    #执行语句
    cursor.execute('select * from t_book')
    #获取结果

    ret=cursor.fetchall()
    print(ret)
except Exception as err:
    print('查询语句出错',str(err))
#关闭游标和sql连接
finally:
    cursor.close()
    conn.close()
