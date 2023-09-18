/*
Task 1: Introduction
Introduction to the SQL
Prerequisites for this course
Introduction to the Rhyme interface
Create a sales database
Task 2: Data Definition in SQL
Create a sales table
Create a customers table
Create an items table
Task 3: Data Manipulation in SQL
Insert five (5) records into the sales table
Insert five (5) records into the customers table
Insert five (5) records into the items table
Task 4: Data Manipulation in SQL - Part 2
Upload a CSV file titled companies into the sales database
Create a new table called sales_dup
Insert data into the sales_dup from the sales table
Create a new table called customers_dup
Insert data into the customers_dup from the customers table
Task 5: Alter, rename and update data
Alter the customers_dup table: Add a new column called gender
Add new records to the customers_dup tab
Use Alter: Rename the sales_dup table to sales_data table
Use Alter: Rename the unit_price_usd column to item_price in the items table
Update records of the customers_dup table
Task 6: Drop Vs. Truncate Vs. Delete
Drop the customers_dup table
Truncate the sales_data table
Delete records from the companies table
*/
#########################################

# Data Definition & Data Manipulation Language

#########################################
CREATE DATABASE if not exists salesdb;
# CREATE SCHEMA [if not exists] database_name;


# Below statement will tell system to execute SQL statements in sales database
USE salesdb	;

# Creating sales tables

# alter table sales rename column data_of_purchage to date_of_purchase;

CREATE TABLE sales (
purchase_number  INT  PRIMARY KEY,
date_of_purchase DATE NOT NULL,
customer_id INT NOT NULL,
item_code VARCHAR(10) NOT NULL
);

# Creating the customer Table
CREATE TABLE customers(
customer_id INT PRIMARY KEY,
first_name VARCHAR(255) NOT NULL,
last_name VARCHAR(255) NOT NULL,
email_address 	VARCHAR(255),
number_of_complaints INT	
);

# Creating the item Table
CREATE TABLE items(
item_code VARCHAR(255),
item VARCHAR(255),
unit_price_usd DECIMAL(5,2),
company_id INT,
company_name VARCHAR(255) NOT NULL
);

# Creating a table with atleast one column is requiered
# Syntax

SELECT
  	TABLE_NAME,
COLUMN_NAME
FROM
  	INFORMATION_SCHEMA.COLUMNS;
SELECT
  	TABLE_NAME
FROM
  	INFORMATION_SCHEMA.TABLES;    
    SELECT
	COLUMN_NAME
FROM
  	INFORMATION_SCHEMA.COLUMNS
WHERE
	TABLE_NAME = 'sales';
    
# Inserting data into sales table
insert into sales (purchase_number,date_of_purchase,customer_id, item_code)
VALUES
(101, '2020-01-01', 101, 'SKU101'),
(102, '2020-01-02', 102, 'SKU102'),
(103, '2020-01-13', 101, 'SKU103'),
(104, '2020-01-21', 103, 'SKU104'),
(105, '2020-01-29', 104, 'SKU105');

SELECT 
    *
FROM
    sales;

rollback;

commit;

INSERT INTO customers 
values
(101, 'Saniya','Facello','sv@gmail.com',2),
(102, 'Georgi','Valtorta','gv@gmail.com',7),
(103, 'Chirstian','Koblick','ck@gmail.com',0),
(104, 'Mary','Sluis','ms@gmail.com',9),
(105, 'Elvis','Gates','eg@gmail.com',20);
    
select * from items;
insert into items 
values
(101, 'Lamp', 10, 1, 'Xeon'),
(102, 'Chair', 13, 1, 'Xeon'),
(103, 'Mobile', 160, 2, 'Mobi'),
(101, 'Mobile Cover', 33, 2, 'Mobi'),
(101, 'Screen Gaurd', 100, 2, 'Mobi');

commit;




    
    
    