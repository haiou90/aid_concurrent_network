数据源--大数据处理平台

数据采集--爬虫

数据存储--sql

数据处理 --批量处理引擎 机器学习

服务封装层-- 可视化 统计分析



人工  文件 数据库



字符串--字节

字节串--二进制

b = b"hello"

b ="你好".encode

fb = open(file_name,access_mode="r",buffering =1,encoding=none)



r 只读

w只写  不存在创建，存在覆盖

a追加  文件不存在则创建

r+读写

w+写读

a+追加  偏移在末尾 读的时候可以offset到开头，写时只能在结尾开始写

f = open(file.txt,"r+")

f.read()读全文或给定数量 str

if not data:

​	break

f.readline() 读取文中一行 或一行的部分 str

f.readlines() 每一行作为列表的一个元素[p1,p2,p3,p4,p5,p6]

f.readlines(15) [p1,p2]

for line in f:   
	print(line)

a    innert  word

for line in f:

​	w = line.split(" ",2)   #[生成列表]

​    if w[0] > word:

​		break

​		print(null)

​    Elif w[0]== word:

​		print(line)

​		print(w[-1].strip())

​		break

Else:

​	print("no")

n=f.write("")



l=["hello","world"]

f.writelines(l)

f.close

fr=open("","rb")

fw=open("","wb")



while True:

​	data= fr.read(1024*10)

​	if not data:

​		break

​	fw.write(data)

fr.close()

fw.close()



with open("","rb") as f;

​	data=f.read

​    print(data.decode)

​	f.write(b"hhhh")   

​	f.fllush



```
CREATE TABLE athlete (
  id int primary key AUTO_INCREMENT,
  name varchar(30),
  age tinyint NOT NULL,
  country varchar(30) NOT NULL,
  description varchar(30)
);

CREATE TABLE item (
  id int primary key AUTO_INCREMENT,
  rname varchar(30) NOT NULL
);

CREATE TABLE athlete_item (
   id int primary key auto_increment,
   aid int NOT NULL,
   tid int NOT NULL,
   CONSTRAINT athlete_fk FOREIGN KEY (aid) REFERENCES athlete (id),
   CONSTRAINT item_fk FOREIGN KEY (tid) REFERENCES item (id)
);

 alter table athelete_item add performance tinyint;  #增加成绩字段
```



Import time

f = open('my.log','a+',buffering=1)

n=1

f.seek(0,0)

for i in f:

​	n+=1

while True:

​	time.sleep(2)

​	msg="%d. %s\n" %(n,time.ctime)

​	f.write(msg)

​	n+=1



f.close

Import os

Os.path.getsize()

os.listdir(".")

os.path.exists()

os.path.isfile()

os.remove



Import os

def remove_file(dir)

​	for file in os.listdir(dir)

​		filename="dir+'/'+file"

​		if os.path.isfile(filename) and os.path.getsize(filename) <10:

​			os.remove(filename)

Remove_file()

ab,

 a|b 

. 任意一个

[a-z0-9A-Z] 字符集

[^a-z0-9A-Z] 字符集反集

r"^ a$"

r".*"重复0-n

r".+"重复1-n

r".?"重复0-1

{n}

{m,n}

\d 数字\D匹配任意非数字字符

\w普通字符 数字字母下划线中文  \W非普通字符

\s空字符 \r \n \t  \t  \f

\b 单词边界 \B非单词编辑



re.search(r'(?P<pig>ab)+','abababab').group('pig')  

My.sql -h    -u root -p