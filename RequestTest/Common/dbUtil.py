import pymysql

class DButil(object):
    conn=None
    @classmethod
    def __set_conn(cls):#过程数据且有数据库下、连接等，建议单独封装，且要为私有属性-避免用户查看使用到
        if cls.conn is None:
            cls.conn=pymysql.connect(host='211.103.136.244',port=7061,user='student',passwd='iHRM_student_2022',database='test_db',charset='utf8')
        return cls.conn
    @classmethod
    def __close_conn(cls):
        if  cls.conn is not None:
            cls.conn.close()#关闭连接但是此时conn还是有值，pymysql.connections.Connection object at 0x000001A59A647160
            cls.conn=None

    @classmethod
    def select_one(cls,sql):
        cusor_select=None
        answer=None #在finally里黄色报错所以需要声明为none,又因为该属性不是全局，只是为了搜一条信息而言，所以在select_one里面
        try:
            cls.conn=cls.__set_conn()#获取连接
            cusor_select=cls.conn.cursor()
            cusor_select.execute(sql)
            answer=cusor_select.fetchall()
        except Exception as error:
            print('搜索出错，信息为：',error)
        finally:
            cusor_select.close()
            cls.__close_conn()
            return answer#封装的要被其他调用，所以要返回
    @classmethod
    def add_update_delete(cls,sql):
        cusor_aud=None
        answer_aud=None
        try:
            cls.conn=cls.__set_conn()
            cusor_aud = cls.conn.cursor()
            cusor_aud.execute(sql)
            answer_aud = cusor_aud.fetchall()
            print('影响到的行数',cls.conn.affected_rows())
            cls.conn.commit()
        except Exception as error:
            print('修改出错，信息为：',error)
            cls.conn.rallback()
        finally:
            cusor_aud.close()
            cls.__close_conn()
            return answer_aud
if __name__ == '__main__':
      #  db=DButil()
     # db.add_update_delete()-----使用classmethod装饰器简化代码为1行，使得调用简单
     rd=DButil.add_update_delete("INSERT into test_db.t_book(id, title, pub_date) values (3,'3是奇数','2022-12-06')")#直接可以调用
     print(rd)