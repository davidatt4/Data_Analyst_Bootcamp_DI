SELECT * FROM language;
SELECT film.title, film.description, language FROM film LEFT JOIN language ON film.language_id = language.language_id;
SELECT film.title, film.description, language FROM language LEFT JOIN film ON film.language_id = language.language_id;
CREATE TABLE new_film (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);
INSERT INTO new_film (id,name) VALUES
    (1,'Titanic'),
    (2,'Harry Potter');
CREATE TABLE customer_review (
    review_id INT PRIMARY KEY,
    film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INT REFERENCES language(language_id),
    title VARCHAR(255),
    score INT CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES
    (1, 1, 'Great Movie', 9, 'This movie was amazing!'),
    (2, 2, 'Nice Film', 7, 'Enjoyed watching it.');
DELETE FROM new_film WHERE id = 1;

UPDATE film
SET language_id = (SELECT language_id FROM language WHERE language_name = 'NewLanguage')
WHERE film_id IN (1, 2, 3); 
DROP TABLE customer_review;
SELECT COUNT(*) AS outstanding_rentals FROM rental WHERE return_date IS NULL;
-- 30 most expensive outstanding movies
SELECT film.title, film.rental_rate
FROM film
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
WHERE rental.return_date IS NULL
ORDER BY film.rental_rate DESC
LIMIT 30;
SELECT title FROM film WHERE description LIKE '%sumo%' AND film_id IN (SELECT film_id FROM film_actor WHERE actor_id IN (SELECT actor_id FROM actor WHERE first_name = 'Penelope' AND last_name = 'Monroe'));
SELECT title FROM film WHERE length < 60 AND rating = 'R';
SELECT title FROM film WHERE film_id IN (SELECT film_id FROM rental WHERE customer_id IN (SELECT customer_id FROM customer WHERE first_name = 'Matthew' AND last_name = 'Mahan') AND rental_rate > 4.00 AND return_date BETWEEN '2005-07-28' AND '2005-08-01');
SELECT title FROM film WHERE (title LIKE '%boat%' OR description LIKE '%boat%') AND film_id IN (SELECT film_id FROM inventory WHERE replacement_cost > 50.00);




