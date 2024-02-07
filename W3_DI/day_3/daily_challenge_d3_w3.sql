CREATE TABLE customer(
    id INT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL
);
CREATE TABLE CustomerProfile (
    id INT PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT false,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customer(id)
);
INSERT INTO Customer (id, first_name, last_name) VALUES
(1, 'John', 'Doe'),
(2, 'Jerome', 'Lalu'),
(3, 'Lea', 'Rive');
INSERT INTO CustomerProfile (id, isLoggedIn, customer_id) VALUES
(1, true, (SELECT id FROM Customer WHERE first_name = 'John')),
(2, false, (SELECT id FROM Customer WHERE first_name = 'Jerome'));
SELECT Customer.first_name
FROM Customer
JOIN CustomerProfile ON Customer.id = CustomerProfile.customer_id
WHERE CustomerProfile.isLoggedIn = true;
SELECT Customer.first_name, COALESCE(CustomerProfile.isLoggedIn, false) AS isLoggedIn
FROM Customer
LEFT JOIN CustomerProfile ON Customer.id = CustomerProfile.customer_id;
SELECT COUNT(*)
FROM Customer
WHERE id NOT IN (SELECT customer_id FROM CustomerProfile WHERE isLoggedIn = true);