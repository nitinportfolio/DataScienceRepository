# Creating Database or Schema


# CREATE DATABASE [if not exists] database_name;

# CREATE SCHEMA [if not exists] database_name;

CREATE DATABASE IF NOT EXISTS sales;

CREATE SCHEMA IF NOT EXISTS retailsales;

# Below statement will tell system to execute SQL statements in sales database
USE sales;

# Creating a table with atleast one column is requiered
# Syntax
/*
CREATE TABLE TABLE_NAME
(
column_1    data_type    constraints,
column_2    data_type    constraints,
.
.
.
column_n   data_type    constrains
);
*/
 CREATE TABLE sales
(
	purchase_number  INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    date_of_purchase DATE NOT NULL,
    customer_id INT,
    item_code VARCHAR(10) NOT NULL
);

CREATE TABLE customers                                                 
(
    customer_id INT,
    first_name varchar(255),
    last_name varchar(255),
    email_address varchar(255),
    number_of_complaints int

);

drop table sales;

 CREATE TABLE sales
(
	purchase_number  INT NOT NULL  AUTO_INCREMENT,
    date_of_purchase DATE NOT NULL,
    customer_id INT,
    item_code VARCHAR(10) NOT NULL,
PRIMARY KEY (purchase_number),
FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

/*ALTER TABLE sales
ADD FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE;
*/
commit;


DROP TABLE customers;


CREATE TABLE customers                                                    
(  
    customer_id INT,  
    first_name varchar(255),  
    last_name varchar(255),  
    email_address varchar(255),   
    number_of_complaints int ,   
primary key (customer_id)  , 
unique key (email_address)
);  


ALTER TABLE customers
CHANGE COLUMN number_of_complaints number_of_complaints INT DEFAULT 0; 

ALTER TABLE customers
ALTER COLUMN number_of_complaints DROP DEFAULT;






# Deleting foreign key 
/*ALTER TABLE sales
DROP FOREIGN KEY sales_ibfk_1;
*/


/*ALTER TABLE customers
ADD UNIQUE KEY (email_address);
*/

# Droping an Index
ALTER TABLE customers
DROP INDEX 	email_address;



select getdate();

   

CREATE TABLE items                                                                                                                              
(  
    item_code varchar(255),   
    item varchar(255),   
    unit_price numeric(10,2),   
    company_id varchar(255),
primary key (item_code)   
);  
DROP TABLE companies;
    CREATE  TABLE companies   
(
    company_id varchar(255),   
    company_name varchar(255),  
    headquarters_phone_number int,   
primary key (company_id)   

);






















