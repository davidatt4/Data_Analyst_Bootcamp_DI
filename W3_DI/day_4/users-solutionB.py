import psycopg2
import os
from dotenv import load_dotenv

# Load variables from the .env file into the environment
load_dotenv()

class UserManagement:
    def __init__(self):
        self.conn = self.connect_to_db()

    def connect_to_db(self):
        return psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )

    def view_all_users(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()

    def add_user(self, username, email, age):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO users (username, email, age) VALUES (%s, %s, %s)", (username, email, age))
        self.conn.commit()
        cur.close()

    def update_user(self, user_id, new_username, new_email, new_age):
        cur = self.conn.cursor()
        cur.execute("UPDATE users SET username = %s, email = %s, age = %s WHERE id = %s",
                    (new_username, new_email, new_age, user_id))
        self.conn.commit()
        cur.close()

    def delete_user(self, user_id):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
        self.conn.commit()
        cur.close()

    def close_connection(self):
        self.conn.close()

    def display_menu(self):
        print("User Management System")
        print("1. View all users")
        print("2. Add a user")
        print("3. Update a user")
        print("4. Delete a user")
        print("0. Exit")

    def get_user_input(self, prompt):
        return input(prompt)

    def start(self):
        while True:
            self.display_menu()
            choice = self.get_user_input("Enter your choice: ")

            if choice == "1":
                print("All Users:")
                self.view_all_users()
            elif choice == "2":
                print("Add a User:")
                username = self.get_user_input("Enter username: ")
                email = self.get_user_input("Enter email: ")
                age = self.get_user_input("Enter age: ")
                self.add_user(username, email, age)
                print("User added successfully.")
            elif choice == "3":
                print("Update a User:")
                user_id = self.get_user_input("Enter user ID to update: ")
                new_username = self.get_user_input("Enter new username: ")
                new_email = self.get_user_input("Enter new email: ")
                new_age = self.get_user_input("Enter new age: ")
                self.update_user(user_id, new_username, new_email, new_age)
                print("User updated successfully.")
            elif choice == "4":
                print("Delete a User:")
                user_id = self.get_user_input("Enter user ID to delete: ")
                self.delete_user(user_id)
                print("User deleted successfully.")
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    user_management = UserManagement()
    user_management.start()
    user_management.close_connection()