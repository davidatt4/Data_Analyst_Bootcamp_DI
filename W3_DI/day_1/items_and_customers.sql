-- Create the Items Table if it doesn't exist
CREATE TABLE IF NOT EXISTS items (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(255),
    price INT
);

-- Create the Customers Table if it doesn't exist
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

INSERT INTO items(item_id, item_name, price) VALUES
    (1, 'Small Desk', 100),
    (2, 'Large Desk', 300),
    (3, 'Fan', 80);

INSERT INTO customers(customers_id,first_name,last_name)VALUES
(1,'Greg','Jones'),
(2,'Sandra','Jones'),
(3,'Scott','Scott'),
(4,'Trevor','Green'),
(5,'Melanie','Johnson');
SELECT * FROM items;
SELECT * FROM items WHERE price>80;
SELECT *FROM items WHERE price<=300;
SELECT *FROM customers WHERE last_name='Smith';
SELECT *FROM customers WHERE last_name='Jones';
SELECT FROM customers WHERE first_name!='Scott'