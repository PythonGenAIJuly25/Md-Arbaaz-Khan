create database practice1;
use practice1;
create table department(departmentid int primary key,name varchar(20));
create table employee(id int primary key,name varchar(20),salary int, departmentid int ,foreign key(departmentid) references department(departmentid));
insert into department values(1,'IT');
insert into department values(2,'Sales');
insert into employee values(1,'joe',70000,1);
insert into employee values(2,'Jim',90000,1);
insert into employee values(3,'Henry',80000,2);
insert into employee values(4,'Sam',60000,2);
insert into employee values(5,'Max',90000,1);
SELECT id, name, salary, department_name
FROM (
    SELECT 
        e.id,
        e.name,
        e.salary,
        d.name AS department_name,
        RANK() OVER (PARTITION BY e.departmentid ORDER BY e.salary DESC) AS rnk
    FROM employee e
    JOIN department d ON e.departmentid = d.departmentid
) ranked
WHERE rnk = 1;



