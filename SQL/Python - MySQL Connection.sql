DROP DATABASE IF EXISTS titanic;
create database if not EXISTS titanic;
use titanic;

drop table titanic_tab;

create  table titanic_tab
( 
Pclass INT ,
Sex BIT ,
Age float,
Fare FLOAT,
Survived BIT 
);
select * from titanic_tab;


