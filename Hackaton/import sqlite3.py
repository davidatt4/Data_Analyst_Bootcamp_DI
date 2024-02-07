import sqlite3

connection = sqlite3.connect('Final_Version_Hackaton.py')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Volunteer (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        phone_number TEXT,
        city TEXT,
        confirmation TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Farmer (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        phone_number TEXT,
        city TEXT
    )
''')

connection.commit()
connection.close()
def save_volunteer_details():
    volunteer = Volunteer(
        first_name_entry.get(),
        last_name_entry.get(),
        phone_number_entry.get(),
        city_entry.get()
    )
    save_person_to_database('Volunteer', volunteer)

    return volunteer

def save_farmer_details():
    farmer = Farmer(
    first_name_entry.get(),
    last_name_entry.get(),
    phone_number_entry.get(),
    city_entry.get()
    )

    save_person_to_database('Farmer', farmer)

    return farmer

def save_person_to_database(table_name, person):
    connection = sqlite3.connect('central_database.db')
    cursor = connection.cursor()

    if table_name == 'Volunteer':
        cursor.execute('''
            INSERT INTO Volunteer (first_name, last_name, phone_number, city, confirmation)
            VALUES (?, ?, ?, ?, ?)
        ''', (person.first_name, person.last_name, person.phone_number, person.city, person.confirmation))
    elif table_name == 'Farmer':
        cursor.execute('''
            INSERT INTO Farmer (first_name, last_name, phone_number, city)
            VALUES (?, ?, ?, ?)
        ''', (person.first_name, person.last_name, person.phone_number, person.city))
    connection.commit()
    connection.close()
