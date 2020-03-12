from mysql_init.mysql_action import DB
#准备测试数据

form_datas = {"student":[{"name":"张三","snumber":"092414247","age":25},
                    {"name":"李四","snumber":"092414246","age":26}]}

def data_init(form_datas):
    db = DB()
    for table,datas in form_datas.items():
        db.clear(table)
        for data in datas:
            db.insert(table,data)
    db.close()


if __name__ == "__main__":
    data_init(form_datas)