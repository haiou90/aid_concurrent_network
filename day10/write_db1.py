"""
数据库写操作演示　2
"""
import pymysql

# 连接数据库 (连接自己计算机可以不写host port)
db = pymysql.connect(host="localhost",
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8'
                     )

# 创建游标 (游标对象负责调用执行sql语句，操作数据，得到结果)
cur = db.cursor()

# 插入多条记录
l = [
    ("Dava",16,'m',77),
    ("Levi",17,'m',67),
    ("Han",18,'w',82)
]

# 对数据库写操作
try:
    sql = "insert into cls (name,age,sex,score) values (%s,%s,%s,%s);"

    # for i in l:
    #     cur.execute(sql,i)

    cur.executemany(sql,l)
    db.commit() # 提交，将sql语句的操作行为提交写入到数据库
except Exception as e:
    print(e)
    db.rollback() # 没有提交到数据库的内容，全部失效


# 关闭游标和数据库
cur.close()
db.close()