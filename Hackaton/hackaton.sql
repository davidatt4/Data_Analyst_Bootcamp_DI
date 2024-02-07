-- CREATE TABLE Farmers (
--     FirstName VARCHAR(50) NOT NULL,
--     LastName VARCHAR(50) NOT NULL,
--     Email VARCHAR(100) UNIQUE NOT NULL,
--     Password VARCHAR(255) NOT NULL -- You should hash the passwords in a real-world scenario
-- );

--INSERT INTO Farmers(FirstName,LastName,PhoneNumber,City)
--VALUES('David','Attal','0123456789','Jerusalem')
--CREATE TABLE Volunteers (
 --VolunteerID INT PRIMARY KEY,
    --FirstName VARCHAR(250) NOT NULL,
    --LastName VARCHAR(250) NOT NULL,
	--PhoneNumber VARCHAR(20) NOT NULL,
	--City VARCHAR(250) NOT NULL
--);
--INSERT INTO  Volunteers(FirstName,LastName,PhoneNumber,City)
--VALUES('Moshe','Levy','0987654321','Haifa')
--CREATE TABLE Events (
    --EventID INT PRIMARY KEY,
    --EventName VARCHAR(100) NOT NULL,
    --EventDate DATE NOT NULL,
    --Description TEXT,
    --FOREIGN KEY (FarmerID) REFERENCES Farmers(FarmerID)
--);
-- Get a list of names with categories (Farmers and Volunteers)
-- Get a list of names with categories (Farmers and Volunteers)
-- Get a combined list of Farmers and Volunteers

SELECT 
    'Farmer' AS UserType,
    FirstName,
    LastName,
    PhoneNumber,
    City
FROM Farmers

UNION

SELECT 
'Volunteer' AS UserType,
FirstName,
LastName,
PhoneNumber,
    City
FROM Volunteers