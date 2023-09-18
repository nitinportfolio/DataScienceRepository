SELECT * FROM products;


UPDATE products 
SET name='SAMSUNG'
WHERE sku = 100;

# Grants & Revoke Stateemnts

 GRANT ALL ON employees.* to 'test_user'@'localhost';

REVOKE ALL on employees.* FROM 'test_user'@'localhost';









# TCL Transactional Control Language
SELECT * from products;

UPDATE products 
SET qty = 5000
WHERE sku = 100;

SELECT * from products;




