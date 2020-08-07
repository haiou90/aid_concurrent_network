"""
存取二进制数据
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

# 插入图片
# with open('pyt.jpeg','rb') as f:
#     data = f.read()  # 字节串
# sql = "update cls set image=%s where id=2;"
# cur.execute(sql,[data])
# db.commit()

# 提取图片
sql = "select image from cls where id=2;"
cur.execute(sql)
data = cur.fetchone() #(image,)
with open('sg.jpeg','wb') as f:
    f.write(data[0])


# 关闭游标和数据库
cur.close()
db.close()