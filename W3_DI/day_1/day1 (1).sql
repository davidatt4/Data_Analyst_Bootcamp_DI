-- CREATE TABLE syntax
-- CREATE TABLE [IF NOT EXISTS] table_name (
--    column1 datatype(length) column_contraint,
--    column2 datatype(length) column_contraint,
--    column3 datatype(length) column_contraint,
--    table_constraints
-- );

-- Constraints
-- NOT NULL – ensures that values in a column cannot be NULL.
-- UNIQUE – ensures the values in a column unique .
-- PRIMARY KEY – a primary key column uniquely identify rows in a table. A table can have one and only one primary key. 
-- FOREIGN KEY – ensures values in a column or a group of columns from a table exists in a column or group of columns in another table. 

CREATE TABLE accounts (
	user_id serial PRIMARY KEY,
	username VARCHAR ( 50 ) UNIQUE NOT NULL,
	password VARCHAR ( 50 ) NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
    last_login TIMESTAMP 
);


CREATE TABLE products (
	id serial PRIMARY KEY,
	name VARCHAR ( 50 )  NOT NULL,
	price integer NOT NULL,
	description VARCHAR ( 1000 )
);

-- INSERT statement
-- INSERT INTO table_name(column1, column2, …)
-- VALUES (value1, value2, …);

-- Inserting a single row into a table
INSERT INTO products (price, name)
VALUES(700, 'iPad');

-- Inserting multiple rows example
INSERT INTO 
    products (price, name)
VALUES
    (800,'iPhone'),
    (600,'iWatch'),
    (900,'iCar');

-- SELECT statement syntax
-- SELECT
--    select_list
-- FROM
--    table_name;

SELECT * FROM products;

SELECT price, name FROM products;

SELECT id, price, name, description FROM products;


-- column aliases

SELECT price || ' ' || name as name_and_price FROM products;

SELECT price  as product_price FROM products;


-- ORDER BY clause
SELECT * FROM products ORDER BY name ASC; -- ascending order:

SELECT * FROM products ORDER BY name DESC; -- descending order



-- WHERE clause
-- SELECT select_list
-- FROM table_name
-- WHERE condition
-- ORDER BY sort_expression

SELECT * FROM products WHERE id = 1 

-- Operator	Description
-- =			Equal
-- >			Greater than
-- <			Less than
-- >=			Greater than or equal
-- <=			Less than or equal
-- <> or !=		Not equal
-- AND			Logical operator AND
-- OR			Logical operator OR
-- IN			Return true if a value matches any value in a list
-- BETWEEN		Return true if a value is between a range of values
-- LIKE			Return true if a value matches a pattern
-- IS NULL		Return true if a value is NULL
-- NOT			Negate the result of other operators

SELECT * FROM products WHERE id in (1 ,3);
SELECT * FROM products WHERE name LIKE 'iP%';
SELECT * FROM products WHERE name LIKE 'iP%' AND price <> 600;


-- UPDATE statement
-- UPDATE table_name
-- SET column1 = value1,
--     column2 = value2,
--     ...
-- WHERE condition;

UPDATE products SET name = 'iPhone15' WHERE id = 2;
UPDATE products SET name = 'iPhone13', price=1000 WHERE id = 2;

-- DELETE statement
-- DELETE FROM table_name
-- WHERE condition;

DELETE FROM products WHERE id = 2;


