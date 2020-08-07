"""
数据库写操作演示　１
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

# 对数据库写操作
try:
    # sql = "insert into cls values (5,'Eva',18,'w',86);"
    # cur.execute(sql)

    # 可以执行多次sql语句 依次commit提交
    sql = "update hobby set price=%s where name =%s;"
    cur.execute(sql,[8800,'Joy'])

    sql = "delete from hobby1 where name=%s;"
    cur.execute(sql, ["lily"])
    db.commit() # 提交，将sql语句的操作行为提交写入到数据库
except Exception as e:
    print(e)
    # 注意： 如果是不支持事务的引擎，执行一条语句就会直接写入到数据库内
    # 这样就不能回滚了，但是支持事务的引擎，则可以回滚，因为数据会保留在
    # 事务缓存中。
    db.rollback() # 没有提交到数据库的内容，全部失效


# 关闭游标和数据库
cur.close()
db.close()