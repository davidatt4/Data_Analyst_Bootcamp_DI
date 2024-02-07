import psycopg2
import os
from dotenv import load_dotenv

# Load variables from the .env file into the connect
load_dotenv()

# Retrieve database crendetials from env 

# db_name = os.getenv('DB_NAME')
# db_user = os.getenv('DB_USER')
# db_password = os.getenv('DB_PASS')
# db_host = os.getenv('DB_HOST')
# db_port = os.getenv('DB_PORT')

# Establish a connection
conn = psycopg2.connect(
    dbname=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT')
)

# Create a cursur object to execute SQL queries
cur = conn.cursor()

# CRUD  - Create (insert) Read (select) Update (update) Delete (delete)

# Insert query
# insert_query = 'INSERT INTO products (name, price) VALUES (%s, %s)'
# data_to_insert = ('iKey', 750)
# # cur.execute(insert_query, data_to_insert)
# cur.execute('INSERT INTO products (name, price) VALUES (%s, %s)', ('iKey', 750))



# Update query
# update_query = 'UPDATE products SET name=%s, price=%s WHERE id= %s'
# new_value = ('iCar2024', 9999, 8)
# cur.execute(update_query, new_value)

# Delete query
# cur.execute('DELETE FROM products WHERE id=%s', ('5'))


# Commit the transaction
# conn.rollback()



# Execute a SELECT query
cur.execute('SELECT * FROM products')
rows = cur.fetchall()

for row in rows:
    print(row)


# Close the cursur and the connection
cur.close()
conn.close()



























