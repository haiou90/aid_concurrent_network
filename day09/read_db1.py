"""
数据库查询操作 2
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
name = input("Name:")
# 确保sql语句正确
# sql = "select name,age,score from cls where name='%s';"%name
# print(sql)
# cur.execute(sql)  # 执行sql

# 利用execute参数列表解决
sql = "select name,age,score from cls where name=%s or score>%s;"
cur.execute(sql,[name,80])  # 执行sql,列表不能传递关键字，符号，表名，字段名

# # 获取一条记录   没有结果返回None
row = cur.fetchall()
print(row)

# 关闭游标和数据库
cur.close()
db.close()