--2. 练习book表
-- 将book表拆分成3个表：图书  作家  出版社
-- 字段及类型自己设计，关系自定义
-- 建立三张表及表关系
create table 作家(
id int primary key auto_increment,
name varchar(30),
sex char,
remark text
);

create table 出版社(
id int primary key auto_increment,
pname varchar(30),
address text,
phone char(16)
);

create table 图书(
id int primary key auto_increment,
bname varchar(30),
price float,
a_id int,
p_id int,
foreign key (a_id) references 作家(id),
foreign key (p_id) references 出版社(id)
);

create table 作家_出版社(
id int primary key auto_increment,
签约时间 date,
aid int,
pid int,
foreign key (aid) references 作家(id),
foreign key (pid) references 出版社(id)
);


--3. 编写一个函数，传入两个学生的ID，返回
-- 这两个学生成绩之差
create function score(uid1 int,uid2 int)
returns float
begin
declare s1 float;
declare s2 float;
select score from cls where id=uid1 into s1;
select score from cls where id=uid2 into s2;
return s1-s2;
end $$


-- 编写一个存储过程，传入一个学生姓名
-- 在外部得到这个学生的成绩
create procedure get_score(inout uname varchar(30))
begin
set uname=(select score from cls where name=uname);
end $$

set @n="Lily";
call get_score(@n)