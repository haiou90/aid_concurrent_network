-- 练习1：使用book表
-- 1. 统计每位作家图书的平均价格
select author,avg(price) from book
group by author;

-- 2. 统计每个出版社出版图书的数量
select publication,count(title) from book
group by publication;

-- 3. 统计相同时间出版图书的平均价格
select publication_time,avg(price) from book
group by publication_time ;

-- 4. 查看总共有多少个出版社
select count(distinct publication) from book;

-- 5. 筛选出那些出版过超过50元图书的出版社，并按照其
-- 出版图书的平均价格进行降序排序
select publication,avg(price)
from book
group by publication
having max(price) > 50
order by avg(price) desc;


-- 部门员工表
insert into dept values
(1,"技术部"),
(2,"销售部"),
(3,"市场部"),
(4,"行政部"),
(5,'财务部'),
(6,'总裁办公室');


insert into person values
(1,"Lily",29,'w',20000,'2017-4-3',2),
(2,"Tom",27,'m',16000,'2019-10-3',1),
(3,"Joy",30,'m',28000,'2016-4-3',1),
(4,"Emma",24,'w',8000,'2019-5-8',4),
(5,"Abby",28,'w',17000,'2018-11-3',3),
(6,"Jame",32,'m',22000,'2017-4-7',3);

-- 级联动作
-- 从表关联主表数据，那么主表数据改动从表也随之改动
alter table person add
constraint dept_fk
foreign key (dept_id)
references dept(id)
on delete cascade on update cascade;

-- 从表关联主表数据，那么主表数据改动从表会变为null
alter table person add
constraint dept_fk    --起名字
foreign key (dept_id) --指定外检字段
references dept(id)   --指定主表字段
on delete set null on update set null;