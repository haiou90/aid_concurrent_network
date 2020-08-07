"""
数据库查询操作 1
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

# 查询数据库
sql = "select name,age,score from cls;"
cur.execute(sql)  # 执行sql

# # 获取一条记录   没有结果返回None
# row = cur.fetchone()
# print(row)
#
# # 多个结果  没有结果返回()
# row = cur.fetchmany(2)
# print(row)
#
# # 所有结果 没有结果返回()
# row = cur.fetchall()
# print(row)

# cur 在查询后可以迭代取值
for row in cur:
    print(row)

# 关闭游标和数据库
cur.close()
db.close()