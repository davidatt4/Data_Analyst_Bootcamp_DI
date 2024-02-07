CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
);
SELECT COUNT(*) FROM actors;
INSERT INTO actors (first_name, last_name) VALUES ('John', '');
