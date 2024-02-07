--CREATE TABLE students(
	--id serial PRIMARY KEY,
	--last_name VARCHAR(255)UNIQUE NOT NULL,
	--first_name VARCHAR(255)UNIQUE NOT NULL,
	--birth_date DATE
--);
--ALTER TABLE students
--DROP CONSTRAINT IF EXISTS students_first_name_key;
--INSERT INTO students(id,last_name,first_name,birth_date)VALUES
--(1,'Marc','Benichou','1998-11-02'),
--(2,'Yoan',	'Cohen','2010-12-03'),
--(3,	'Lea',	'Benichou',	'1987-07-27'),
--(4,	'Amelia',	'Dux',	'1996-04-07'),
--(5,	'David',	'Grez',	'2003-06-14'),
--(6,	'Omer',	'Simpson'	,'1980-10-03')

SELECT * FROM students;
SELECT first_name, last_name FROM students;
SELECT first_name, last_name FROM students WHERE id = 2;
SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc';
SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc';
SELECT first_name, last_name FROM students WHERE first_name LIKE '%a%';
SELECT first_name, last_name FROM students WHERE first_name LIKE '%a';
SELECT first_name, last_name FROM students WHERE SUBSTRING(first_name, LENGTH(first_name)-1, 1) = 'a';
SELECT first_name, last_name FROM students WHERE id IN (1, 3);
SELECT * FROM students WHERE birth_date >= '2000-01-01';
