import psycopg2
import os
from dotenv import load_dotenv

# Load variables from the .env file into the environment
load_dotenv()

# Function to connect to the PostgreSQL database
def connect_to_db():
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    return conn


# Function to view all users
def view_all_users(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()


# Function to add a new user
def add_user(conn, username, email, age):
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, email, age) VALUES (%s, %s, %s)", (username, email, age))
    conn.commit()
    cur.close()


# Function to update user information
def update_user(conn, user_id, new_username, new_email, new_age):
    cur = conn.cursor()
    cur.execute("UPDATE users SET username = %s, email = %s, age = %s WHERE id = %s",
                (new_username, new_email, new_age, user_id))
    conn.commit()
    cur.close()


# Function to delete a user
def delete_user(conn, user_id):
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    cur.close()


# Example usage:
# conn = connect_to_db()
# view_all_users(conn)
# add_user(conn, "JohnDoe", "john@example.com", 30)
# update_user(conn, 1, "JohnDoeUpdated", "john@example.com", 35)
# delete_user(conn, 1)
# conn.close()


def display_menu():
    print("User Management System")
    print("1. View all users")
    print("2. Add a user")
    print("3. Update a user")
    print("4. Delete a user")
    print("0. Exit")


def get_user_input(prompt):
    return input(prompt)


def main():
    conn = connect_to_db()
    while True:
        display_menu()
        choice = get_user_input("Enter your choice: ")

        if choice == "1":
            print("All Users:")
            view_all_users(conn)
        elif choice == "2":
            print("Add a User:")
            username = get_user_input("Enter username: ")
            email = get_user_input("Enter email: ")
            age = get_user_input("Enter age: ")
            add_user(conn, username, email, age)
            print("User added successfully.")
        elif choice == "3":
            print("Update a User:")
            user_id = get_user_input("Enter user ID to update: ")
            new_username = get_user_input("Enter new username: ")
            new_email = get_user_input("Enter new email: ")
            new_age = get_user_input("Enter new age: ")
            update_user(conn, user_id, new_username, new_email, new_age)
            print("User updated successfully.")
        elif choice == "4":
            print("Delete a User:")
            user_id = get_user_input("Enter user ID to delete: ")
            delete_user(conn, user_id)
            print("User deleted successfully.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()


if __name__ == "__main__":
    main()
