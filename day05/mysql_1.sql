create table `hobby`(
    `id` int primary key auto_increment,
    `name` varchar(30) not null,
    `hobby` set('sing','dance','draw'),
    `level` char(2),
    `price` decimal(7,2),
    `remark` text
);

--插入数据
insert into class_1 values
(1,"Lily",18,'w',92),
(2,"Tom",17,'m',76);

insert into class_1 (name,age,sex,score)
values
("Abby",17,'w',87),
("Baron",19,'m',93);

insert into class_1 (name,age)
values
("Lucy",18),
("Alex",19);

insert into class_1 (age,score)
values
(18,90),
(19,88);

insert into hobby (name,hobby,level,price,remark)
values
("Joy",'sing',"A",15800,"天籁之音"),
("Lily",'sing,dance',"B",66800.888,"骨骼惊奇");






