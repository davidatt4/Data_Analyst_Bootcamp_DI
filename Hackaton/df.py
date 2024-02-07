import psycopg2
from psycopg2 import OperationalError, Error
from dotenv import load_dotenv
import os

def create_connection():
    try:
        connection = psycopg2.connect(
            dbname='Hackaton_Project',
            user='ddlmjmnp',
            password='idvbZddDEhwrSPAchEXxH6hk-39HEpC2',
            host='ella.db.elephantsql.com',
            port='5432'
        )
        return connection
    except OperationalError as e:
        print(f"Error: {e}")
        return None

load_dotenv()

connection = create_connection()
if connection is not None:
    try:
        cursor = connection.cursor()
        query = 'SELECT * FROM farmer'
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error executing query: {e}")
    finally:
        cursor.close()
        connection.close()
else:
    print("Connection failed.")
    
    
