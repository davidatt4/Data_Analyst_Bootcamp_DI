import requests
import sqlite3
import random
def fetch_countries():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    countries_data = response.json()
    return countries_data
def insert_countries_into_db(countries, cursor):
    for _ in range(10):
        random_country = random.choice(countries)
        name = random_country.get("name", {}).get("common", "")
        capital = random_country.get("capital", [])[0] if "capital" in random_country else ""
        flag = random_country.get("flags", {}).get("png", "")
        subregion = random_country.get("subregion", "")
        population = random_country.get("population", 0)
        
        
        cursor.execute(
            "INSERT INTO countries (name, capital, flag, subregion, population) VALUES (?, ?, ?, ?, ?)",
            (name, capital, flag, subregion, population)
        )
conn=sqlite3.connect('your_database.db')
cursor=conn.cursor
cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        capital TEXT,
        flag TEXT,
        subregion TEXT,
        population INTEGER
    )
''')
countries_data = fetch_countries()
insert_countries_into_db(countries_data, cursor)
conn.commit()
conn.close()