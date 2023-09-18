# Querying the Employee table
# * means all or everything

use employees;

# Querying a data from a table in a database
select * from employees;

# Querying only required columns data from a table
select emp_no, First_name, Last_name from employees;

# Where Clause
# Querying data based on condition

select * from employees
where gender = 'M';

select * from employees
where birth_date>'1955-01-01';

select * from employees
where first_name = 'Saniya';

# Using AND we can have more than one condition
select * from employees
where first_name = 'Saniya'
and gender ='F';

# Using OR condition - satisfy any of the conditions
select * from employees
where first_name = 'Saniya'
or last_name = 'Valtorta';

# Understanding precedence in AND & OR
select * from employees
where first_name = 'Saniya'
AND gender = 'M' OR gender = 'F' ;

select * from employees
where (first_name = 'Saniya'
AND gender = 'M') OR (gender = 'F') ;

# Use parenthesis to decide the order
select * from employees
where (first_name = 'Saniya')
AND (gender = 'M' OR gender = 'F');


# IN & NOT IN
# If we have same condition on a single columns
select * from employees
where first_name in ( 'Saniya','Parto','Genin');

select * from employees
where first_name in ( 'Saniya','Parto','Genin');

select * from employees
where first_name not in ( 'Saniya','Parto','Genin')
AND gender = 'M' ;

# LIKE & NOT LIKE
# When you want to query based on some pattern
# % should be used to indicate the pattern
# % is used as a substitute for sequence of characters
# _ is used as a substitute for single character

select * from employees
where first_name like ('Ge%');

select * from employees
where first_name like ('%Ge');

select * from employees
where first_name like ('%Ge%');

select * from employees
where emp_no like ('%1');

select * from employees
where hire_date like ('1986-01%');

select * from employees
where hire_date like ('1986-01%')
and emp_no not like ('100%');

select * from employees
where first_name like ('Mar_');


# BETWEEN & NOT BETWEEN operator is used to Query data
# based on some interval
# Always used with AND operator

# Find out all employees hired between any date range
select * from employees
where hire_date 
between '1985-01-01' and '1985-12-31';

select * from employees
where emp_no 
between '10000' and '11000';

select * from employees
where emp_no 
not between '20000' and '31000'
and 
hire_date between '1985-01-01' and '1985-12-31';

# name>='A' and name<='C'
select * from employees
where first_name between 'A' and 'C'
and emp_no between 10000 and 10010;

/*select * from employees
where
substr(first_name,1,1) between 'A' and 'c'
and emp_no between 10000 and 10010;
*/

# IS NOT NULL
# Extracts values that are not NULL
select * from employees
where emp_no is NULL;

# Comarison Operators
# = < > >= <= <> !=
select * from employees
where first_name = 'Mark'
and gender <> 'M';

select * from employees
where first_name = 'Mark'
and gender != 'M';

select * from employees
where 
hire_date >='2000-01-01';

# SELECT DISTINCT
# Querying only unique calues
select distinct first_name from employees;

select distinct gender from employees;

select distinct first_name, gender from employees
where first_name like 'Mark';

select  first_name, gender from employees
where first_name like 'Mark';

# Aggregate Funcitons
# Applied on multiple row of a column of a table
# and returns a single output

# COUNT - Number of rows
select count(emp_no) from employees;

select count(*) from employees
where first_name = 'MARK';

select count(gender) from employees;

select count(distinct gender) from employees;

select count(distinct first_name) from employees;

# ORDER BY defaut sorting is ASC ascending 
# DESC for descending 
select * from employees
order by first_name;

select * from employees
order by first_name ASC;

select * from employees
order by first_name DESC;

select * from employees
order by first_name, last_name;

# GROUP BY
# Getting result by grouping specific field or fields
# Used with aggregate functions
# Senior management are more interested in
# summarised data hence we use aggregate functions
# Just above the order by clause
# ALwyas use the field you group by with
# Getting the count of distinct names
select first_name, count(first_name) from employees
group by first_name;

select first_name,last_name, count(first_name) from employees
group by first_name
order by last_name desc;

# Aliases AS
# Used to rename the selected from the query
select first_name,last_name, count(first_name) as name_count from employees
group by first_name
order by last_name desc;

# HAVING
# The  HAVING clause is used in the SELECT statement 
# to specify filter conditions for a group of rows or aggregates.

# The HAVING clause is often used with the GROUP BY clause 
# to filter groups based on a specified condition. 
# If the GROUP BY clause is omitted, the HAVING clause 
# behaves like the WHERE clause.
select first_name,last_name, count(first_name) as name_count from employees
group by first_name
having count(first_name)>250
order by last_name desc;


# SELECT - FROM - WHERE - GROUP BY - HAVING - ORDER BY# 
# Having is like a where clause but for group by clause
# Can't use aggregate in where clause

select count(*) from employees;

# How much money company spend on salaries

select sum(salary) from salaries;


SELECT * from salaries;
# who earns the maximum & the minimum salaries
select max(salary) from salaries;


select min(salary) from salaries;


select max(salary) from salaries;
select * from salaries
order by salary desc;

# Avg will average all not null values
select avg(salary) from salaries;

# Round funciton
select round(avg(salary)) as Sal from salaries;

select round(avg(salary),2) as Sal from salaries;


# Joins - Inner Join
# Joining more than one tables
select * from departments;
select * from dept_manager;

SELECT 
    m.dept_no, m.emp_no, d.dept_name
FROM
    dept_manager m
        INNER JOIN
    departments d ON m.dept_no = d.dept_no
ORDER BY m.dept_no;


SELECT 
    m.dept_no, m.emp_no, d.dept_name
FROM
    dept_manager m
         inner JOIN
    departments d ON m.dept_no = d.dept_no
            where m.emp_no > 111000
            order by m.dept_no;

# Joining more than two tables
select 
e.first_name,e.last_name, e.hire_date, 
m.from_date,
d.dept_name
from
employees e
join
dept_manager m on e.emp_no = m.emp_no
join
departments d on m.dept_no = d.dept_no;


# SUB QUERIESwith IN  in where clause
# Query inside another query
select * from employees
where
emp_no in (select emp_no from dept_manager);


select * from employees
where
emp_no in (select emp_no from dept_manager
where emp_no = 110022);

# Exists
select * from employees
where
 exists(select emp_no from dept_manager
where emp_no = 110022);

# Views 

select emp_no, from_date, to_date, count(emp_no) as Num
 from dept_emp
 group by emp_no
 having num >1;
 
 create or replace view v_dept_emp_latest_date as 
 select 
 emp_no, max(from_date) as from_date, max(to_date) as to_date
 from dept_emp
 group by emp_no;
 
 select * from v_dept_emp_latest_date;
