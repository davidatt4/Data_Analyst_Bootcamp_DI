import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Farmer(Person):
    def __init__(self, first_name, last_name, phone_number, city):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.city = city

class Volunteer(Person):
    def __init__(self, first_name, last_name, phone_number, city):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.city = city
        self.confirmation = ""

class Event:
    def __init__(self, event_name, event_date, description, farmer):
        self.event_name = event_name
        self.event_date = event_date
        self.description = description
        self.farmer = farmer
        self.volunteers = []

    def add_volunteer(self, volunteer):
        self.volunteers.append(volunteer)

def create_tables():
    connection = sqlite3.connect('central_database.db')
    cursor = connection.cursor()

    # Create a table for volunteers
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

    # Create a table for farmers
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

def save_to_central_database(table_name, person):
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

        save_to_central_database('Volunteer', volunteer)

        return volunteer

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

        save_to_central_database('Farmer', farmer)

        return farmer

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
        for volunteer in volunteers:
            event.add_volunteer(volunteer)

        # Display confirmation window
        display_confirmation_window(event)

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
    confirmation = messagebox.askquestion("Confirmation", f"Do you confirm your arrival, {volunteer}?")
    volunteer.confirmation = "Yes" if confirmation == "yes" else "No"
    if confirmation == "yes":
        messagebox.showinfo("Thanks", "Thanks for your contribution!")

# Main application
root = tk.Tk()
root.title("Event Management Application")

# Check and create tables when the program starts
create_tables()

ttk.Button(root, text="Enter Volunteer Details", command=get_volunteer_details).pack(pady=10)
ttk.Button(root, text="Enter Farmer Details", command=get_farmer_details).pack(pady=10)
ttk.Button(root, text="Create Event", command=lambda: create_event(None, [])).pack(pady=10)

# Additional button for volunteers to confirm arrival
ttk.Button(root, text="Confirm Arrival", command=lambda: confirm_arrival(Volunteer("Sample", "Volunteer", "", ""))).pack(pady=10)

root.mainloop()
