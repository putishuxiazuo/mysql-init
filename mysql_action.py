from pymysql import connect

class DB():
    def __init__(self):
        '''连接数据库'''
        self.connect = connect(host = "127.0.0.1",user = "root",password = "951006",db = "test_01",charset = "utf8mb4")

    def clear(self,table_name):
        '''清楚指定表的数据
         table_name:形如字典'''
        clear_sql = "delete from "+table_name+";"
        with  self.connect.cursor() as cursor:
            cursor.execute("set foreign_key_checks=0;")
            cursor.execute(clear_sql)
        self.connect.commit()
        print("清除数据完成")

    def insert(self,table_name,table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        keys = ",".join(table_data.keys())
        values = ",".join(table_data.values())
        insert_sql = "insert into "+table_name+" values "+"("+values+");"
        print(insert_sql)
        with  self.connect.cursor() as cursor:
            cursor.execute("set foreign_key_checks=0;")
            cursor.execute(insert_sql)
        self.connect.commit()
        print("插入数据完成")

    def close(self):
        '''与数据库的连接断开'''
        self.connect.close()
        print("数据库关闭")

if __name__ == "__main__":
    db = DB()
    db.insert("student",{"name":"yzz","snumber":"092414247","age":25})
    db.close()



