import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Create a SQLite database and connect to it
connection = sqlite3.connect("event_management.db")
cursor = connection.cursor()

# Create tables if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS farmers (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        phone_number TEXT,
        city TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS volunteers (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        phone_number TEXT,
        city TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY,
        event_name TEXT,
        event_date TEXT,
        description TEXT,
        farmer_id INTEGER,
        FOREIGN KEY (farmer_id) REFERENCES farmers (id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS volunteer_confirmations (
        id INTEGER PRIMARY KEY,
        event_id INTEGER,
        volunteer_id INTEGER,
        confirmation TEXT,
        FOREIGN KEY (event_id) REFERENCES events (id),
        FOREIGN KEY (volunteer_id) REFERENCES volunteers (id)
    )
''')

connection.commit()

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Farmer(Person):
    def __init__(self, first_name, last_name, phone_number, city):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.city = city

    def save_to_database(self):
        cursor.execute('''
            INSERT INTO farmers (first_name, last_name, phone_number, city)
            VALUES (?, ?, ?, ?)
        ''', (self.first_name, self.last_name, self.phone_number, self.city))
        connection.commit()

class Volunteer(Person):
    def __init__(self, first_name, last_name, phone_number, city):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.city = city
        self.confirmation = ""

    def save_to_database(self):
        cursor.execute('''
            INSERT INTO volunteers (first_name, last_name, phone_number, city)
            VALUES (?, ?, ?, ?)
        ''', (self.first_name, self.last_name, self.phone_number, self.city))
        connection.commit()

class Event:
    def __init__(self, event_name, event_date, description, farmer):
        self.event_name = event_name
        self.event_date = event_date
        self.description = description
        self.farmer = farmer
        self.volunteers = []

    def add_volunteer(self, volunteer):
        self.volunteers.append(volunteer)

    def save_to_database(self):
        cursor.execute('''
            INSERT INTO events (event_name, event_date, description, farmer_id)
            VALUES (?, ?, ?, ?)
        ''', (self.event_name, self.event_date, self.description, self.farmer.id))
        connection.commit()
        event_id = cursor.lastrowid

        for volunteer in self.volunteers:
            volunteer.save_to_database()
            cursor.execute('''
                INSERT INTO volunteer_confirmations (event_id, volunteer_id, confirmation)
                VALUES (?, ?, ?)
            ''', (event_id, volunteer.id, volunteer.confirmation))
            connection.commit()

def get_volunteer_details():
    volunteer_window = tk.Toplevel(root)
    volunteer_window.title("Volunteer Details")

    ttk.Label(volunteer_window, text="Enter Volunteer Details:").grid(row=0, column=0, columnspan=2, pady=10)

    ttk.Label(volunteer_window, text="First Name:").grid(row=1, column=0, pady=5)
    first_name_entry = ttk.Entry(volunteer_window)
    first_name_entry.grid(row=1, column=1, pady=5)

    ttk.Label(volunteer_window, text="Last Name:").grid(row=2, column=0, pady=5)
    last_name_entry = ttk.Entry(volunteer_window)
    last_name_entry.grid(row=2, column=1, pady=5)

    ttk.Label(volunteer_window, text="Phone Number:").grid(row=3, column=0, pady=5)
    phone_number_entry = ttk.Entry(volunteer_window)
    phone_number_entry.grid(row=3, column=1, pady=5)

    ttk.Label(volunteer_window, text="City:").grid(row=4, column=0, pady=5)
    city_entry = ttk.Entry(volunteer_window)
    city_entry.grid(row=4, column=1, pady=5)

    def save_volunteer_details():
        volunteer_window.destroy()
        volunteer = Volunteer(
            first_name_entry.get(),
            last_name_entry.get(),
            phone_number_entry.get(),
            city_entry.get()
        )
        volunteer.save_to_database()
        volunteers.append(volunteer)

    ttk.Button(volunteer_window, text="Save", command=save_volunteer_details).grid(row=5, column=0, columnspan=2, pady=10)

def get_farmer_details():
    farmer_window = tk.Toplevel(root)
    farmer_window.title("Farmer Details")

    ttk.Label(farmer_window, text="Enter Farmer Details:").grid(row=0, column=0, columnspan=2, pady=10)

    ttk.Label(farmer_window, text="First Name:").grid(row=1, column=0, pady=5)
    first_name_entry = ttk.Entry(farmer_window)
    first_name_entry.grid(row=1, column=1, pady=5)

    ttk.Label(farmer_window, text="Last Name:").grid(row=2, column=0, pady=5)
    last_name_entry = ttk.Entry(farmer_window)
    last_name_entry.grid(row=2, column=1, pady=5)

    ttk.Label(farmer_window, text="Phone Number:").grid(row=3, column=0, pady=5)
    phone_number_entry = ttk.Entry(farmer_window)
    phone_number_entry.grid(row=3, column=1, pady=5)

    ttk.Label(farmer_window, text="City:").grid(row=4, column=0, pady=5)
    city_entry = ttk.Entry(farmer_window)
    city_entry.grid(row=4, column=1, pady=5)

    def save_farmer_details():
        farmer_window.destroy()
        farmer = Farmer(
            first_name_entry.get(),
            last_name_entry.get(),
            phone_number_entry.get(),
            city_entry.get()
        )
        farmer.save_to_database()
        farmers.append(farmer)

    ttk.Button(farmer_window, text="Save", command=save_farmer_details).grid(row=5, column=0, columnspan=2, pady=10)

def create_event(farmer, volunteers):
    event_window = tk.Toplevel(root)
    event_window.title("Event Details")

    ttk.Label(event_window, text="Enter Event Details:").grid(row=0, column=0, columnspan=2, pady=10)

    ttk.Label(event_window, text="Event Name:").grid(row=1, column=0, pady=5)
    event_name_entry = ttk.Entry(event_window)
    event_name_entry.grid(row=1, column=1, pady=5)

    ttk.Label(event_window, text="Event Date:").grid(row=2, column=0, pady=5)
    event_date_entry = ttk.Entry(event_window)
    event_date_entry.grid(row=2, column=1, pady=5)

    ttk.Label(event_window, text="Event Description:").grid(row=3, column=0, pady=5)
    description_entry = ttk.Entry(event_window)
    description_entry.grid(row=3, column=1, pady=5)

    def save_event_details():
        event_window.destroy()
        event = Event(
            event_name_entry.get(),
            event_date_entry.get(),
            description_entry.get(),
            farmer
        )
        event.save_to_database()
        messagebox.showinfo("Success", "Event and volunteer confirmations saved successfully.")

    ttk.Button(event_window, text="Save", command=save_event_details).grid(row=4, column=0, columnspan=2, pady=10)

def display_confirmation_window(event):
    confirmation_window = tk.Toplevel(root)
    confirmation_window.title("Volunteer Confirmations")

    ttk.Label(confirmation_window, text=f"Volunteer Confirmations for Event '{event.event_name}':").grid(row=0, column=0, columnspan=2, pady=10)

    for i, volunteer in enumerate(event.volunteers, start=1):
        ttk.Label(confirmation_window, text=f"{i}. {volunteer.first_name} {volunteer.last_name}:", anchor="e").grid(row=i, column=0, padx=5, pady=5)
        ttk.Entry(confirmation_window, textvariable=tk.StringVar(value=volunteer.confirmation), state="readonly", width=10, justify="center").grid(row=i, column=1, padx=5, pady=5)

    ttk.Button(confirmation_window, text="Close", command=confirmation_window.destroy).grid(row=len(event.volunteers) + 1, column=0, columnspan=2, pady=10)

def confirm_arrival(volunteer):
    confirmation = messagebox.askquestion("Confirmation", f"Do you confirm your arrival, {volunteer.first_name}?")
    volunteer.confirmation = "Yes" if confirmation == "yes" else "No"

# Main application
root = tk.Tk()
root.title("Event Management Application")

# Load existing farmers and volunteers from the database
cursor.execute('SELECT * FROM farmers')
farmers = [Farmer(*row) for row in cursor.fetchall()]

cursor.execute('SELECT * FROM volunteers')
volunteers = [Volunteer(*row) for row in cursor.fetchall()]

# Additional button for volunteers to confirm arrival
ttk.Button(root, text="Enter Volunteer Details", command=get_volunteer_details).pack(pady=10)
ttk.Button(root, text="Enter Farmer Details", command=get_farmer_details).pack(pady=10)
ttk.Button(root, text="Create Event", command=lambda: create_event(farmers[0], volunteers)).pack(pady=10)
ttk.Button(root, text="Confirm Arrival", command=lambda: confirm_arrival(volunteers[0])).pack(pady=10)

root.mainloop()

# Close the database connection
connection.close()
