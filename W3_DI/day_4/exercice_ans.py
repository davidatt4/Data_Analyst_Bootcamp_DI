import psycopg2
from psycopg2 import sql
def connect():
    try:
        connection = psycopg2.connect(
            dbname="user_management",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        )
        return connection
    except psycopg2.Error as e:
        print("Error: Unable to connect to the database.")
        print(e)
        return None
def view_all_users(connection):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users;")
            users = cursor.fetchall()
            for user in users:
                print(user)
    except psycopg2.Error as e:
        print("Error: Unable to fetch users.")
        print(e)
def add_user(connection, username, email, age):
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (username, email, age) VALUES (%s, %s, %s);",
                (username, email, age)
            )
            connection.commit()
            print("User added successfully.")
    except psycopg2.Error as e:
        print("Error: Unable to add user.")
        print(e)
def update_user(connection, user_id, new_username, new_email, new_age):
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE users SET username = %s, email = %s, age = %s WHERE id = %s;",
                (new_username, new_email, new_age, user_id)
            )
            connection.commit()
            print("User updated successfully.")
    except psycopg2.Error as e:
        print("Error: Unable to update user.")
        print(e)
def delete_user(connection, user_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM users WHERE id = %s;",
                (user_id,)
            )
            connection.commit()
            print("User deleted successfully.")
    except psycopg2.Error as e:
        print("Error: Unable to delete user.")
        print(e)
connection = connect()
if connection:
    view_all_users(connection)
    add_user(connection, "NewUser", "newuser@example.com", 25)
    view_all_users(connection)
    update_user(connection, 1, "UpdatedUser", "updateduser@example.com", 30)
    view_all_users(connection)
    delete_user(connection, 2)
    view_all_users(connection)

    connection.close()
