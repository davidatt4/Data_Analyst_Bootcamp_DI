CREATE TABLE items(
	item_id SERIAL PRIMARY KEY,
	product_name VARCHAR(255)NOT NULL,
	price DECIMAL(10,2)NOT NULL
);
CREATE TABLE product_orders(
	order_id SERIAL PRIMARY KEY,
	order_date DATE NOT NULL,
	customer_name VARCHAR(255)NOT NULL
);
CREATE TABLE order_items(
	order_id INT,
	item_id INT,
	quantity INT NOT NULL,
	PRIMARY KEY (order_id, item_id),
    FOREIGN KEY (order_id) REFERENCES product_orders(order_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);
CREATE TABLE users(
	user_id SERIAL PRIMARY KEY,
	username VARCHAR(255)NOT NULL,
	email VARCHAR(255)NOT NULL
);
ALTER TABLE product_orders
ADD COLUMN user_id INT,
ADD FOREIGN KEY(user_id)REFERENCES users(user_id);
CREATE OR REPLACE FUNCTION calculate_order_total(user_id INT, order_id INT)
RETURNS DECIMAL(10, 2) AS $$
DECLARE
    total_price DECIMAL(10, 2);
BEGIN
    SELECT COALESCE(SUM(items.price * order_items.quantity), 0)
    INTO total_price
    FROM order_items
    JOIN items ON order_items.item_id = items.item_id
    JOIN product_orders ON order_items.order_id = product_orders.order_id
    WHERE product_orders.user_id = calculate_order_total.user_id
        AND order_items.order_id = calculate_order_total.order_id;

    RETURN total_price;
END;
$$ LANGUAGE plpgsql;
	