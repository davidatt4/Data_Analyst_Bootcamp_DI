SELECT*FROM customer;
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM customer;
SELECT DISTINCT create_date
FROM customer;
SELECT *FROM customer ORDER BY first_name DESC;
SELECT film_id,title,description,release_year,rental_rate FROM film ORDER BY rental_rate ASC;
SELECT a.address, a.phone FROM address a JOIN customer c ON a.address_id = c.address_id WHERE a.district = 'Texas';
SELECT* FROM film WHERE film_id IN(15,150);
SELECT film_id, title, description, length, rental_rate FROM film WHERE title = 'YourFavoriteMovie';
SELECT film_id, title, description, length, rental_rate FROM film WHERE title LIKE 'YourFavoriteMovie%';
SELECT film_id, title, description, length, rental_rate FROM film ORDER BY rental_rate LIMIT 10;
SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY p.staff_id;
SELECT *FROM film WHERE film_id NOT IN (SELECT film_id FROM inventory);
SELECT city, country FROM city JOIN country ON city.country_id = country.country_id;
SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date FROM customer c JOIN payment p ON c.customer_id = p.customer_id ORDER BY p.staff_id;





