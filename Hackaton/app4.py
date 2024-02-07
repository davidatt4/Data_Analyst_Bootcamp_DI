import tkinter as tk
from tkinter import ttk, messagebox
import json


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
        self.confirmation = "Pending"


class Event:
    def __init__(self, event_name, event_date, description, farmers, volunteers):
        self.event_name = event_name
        self.event_date = event_date
        self.description = description
        self.farmers = farmers
        self.volunteers = volunteers

    def add_farmer(self, farmer):
        self.farmers.append(farmer)

    def add_volunteer(self, volunteer):
        self.volunteers.append(volunteer)

    def get_volunteer_status(self):
        return {f"{volunteer.first_name} {volunteer.last_name}": volunteer.confirmation for volunteer in self.volunteers}


def save_data(events):
    with open("event_data.json", "w") as file:
        data = {
            "events": [
                {
                    "event_name": event.event_name,
                    "event_date": event.event_date,
                    "description": event.description,
                    "farmers": [
                        {"first_name": farmer.first_name, "last_name": farmer.last_name,
                         "phone_number": farmer.phone_number, "city": farmer.city}
                        for farmer in event.farmers
                    ],
                    "volunteers": [
                        {"first_name": volunteer.first_name, "last_name": volunteer.last_name,
                         "phone_number": volunteer.phone_number, "city": volunteer.city,
                         "confirmation": volunteer.confirmation}
                        for volunteer in event.volunteers
                    ]
                }
                for event in events
            ]
        }
        json.dump(data, file)


def load_data():
    try:
        with open("event_data.json", "r") as file:
            data = json.load(file)
            events = []
            for event_data in data.get("events", []):
                farmers = [Farmer(**farmer) for farmer in event_data.get("farmers", [])]
                volunteers = [Volunteer(**volunteer) for volunteer in event_data.get("volunteers", [])]
                events.append(Event(event_data["event_name"], event_data["event_date"], event_data["description"],
                                    farmers, volunteers))
            return events
    except FileNotFoundError:
        return []


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
        return Volunteer(
            first_name_entry.get(),
            last_name_entry.get(),
            phone_number_entry.get(),
            city_entry.get()
        )

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
        return Farmer(
            first_name_entry.get(),
            last_name_entry.get(),
            phone_number_entry.get(),
            city_entry.get()
        )

    ttk.Button(farmer_window, text="Save", command=save_farmer_details).grid(row=5, column=0, columnspan=2, pady=10)


def create_event():
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

    farmers = []
    volunteers = []

    def add_farmer():
        farmer = get_farmer_details()
        farmers.append(farmer)
        ttk.Label(event_window, text=f"Farmer: {farmer.first_name} {farmer.last_name} added").grid(row=len(farmers) + 4, column=0, columnspan=2, pady=5)

    def add_volunteer():
        volunteer = get_volunteer_details()
        volunteers.append(volunteer)
        ttk.Label(event_window, text=f"Volunteer: {volunteer.first_name} {volunteer.last_name} added").grid(row=len(volunteers) + 4, column=0, columnspan=2, pady=5)

    def save_event_details():
        event_window.destroy()
        event = Event(
            event_name_entry.get(),
            event_date_entry.get(),
            description_entry.get(),
            farmers,
            volunteers
        )
        display_confirmation_window(event)

    ttk.Button(event_window, text="Add Farmer", command=add_farmer).grid(row=4, column=0, pady=10)
    ttk.Button(event_window, text="Add Volunteer", command=add_volunteer).grid(row=4, column=1, pady=10)
    ttk.Button(event_window, text="Save", command=save_event_details).grid(row=5, column=0, columnspan=2, pady=10)


def display_confirmation_window(event):
    confirmation_window = tk.Toplevel(root)
    confirmation_window.title("Volunteer Confirmations")

    ttk.Label(confirmation_window, text=f"Volunteer Confirmations for Event '{event.event_name}':").grid(row=0, column=0, columnspan=2, pady=10)

    for i, farmer in enumerate(event.farmers, start=1):
        ttk.Label(confirmation_window, text=f"Farmer: {farmer.first_name} {farmer.last_name}", anchor="e").grid(row=i, column=0, padx=5, pady=5)

    for i, volunteer in enumerate(event.volunteers, start=len(event.farmers)+1):
        ttk.Label(confirmation_window, text=f"{i}. Volunteer: {volunteer.first_name} {volunteer.last_name}:", anchor="e").grid(row=i, column=0, padx=5, pady=5)
        ttk.Entry(confirmation_window, textvariable=tk.StringVar(value=volunteer.confirmation), state="readonly", width=10, justify="center").grid(row=i, column=1, padx=5, pady=5)

    ttk.Button(confirmation_window, text="Approve Arrival", command=lambda: approve_arrival_window(event)).grid(row=len(event.volunteers) + len(event.farmers) + 1, column=0, columnspan=2, pady=10)


def send_message_to_farmer(event):
    farmer_messages = [f"Farmer: {farmer.first_name} {farmer.last_name} has confirmed the event." for farmer in event.farmers]
    confirmed_volunteers = [volunteer for volunteer in event.volunteers if volunteer.confirmation.lower() == "yes"]

    if confirmed_volunteers:
        message = f"Confirmed arrivals for event '{event.event_name}':\n"
        for volunteer in confirmed_volunteers:
            message += f"{volunteer.first_name} {volunteer.last_name}\n"
            send_confirmation_message_to_farmer(volunteer)

        messagebox.showinfo("Confirmed Arrivals", message)
    else:
        messagebox.showinfo("No Confirmations", "No volunteers confirmed their arrival for the event.")


def send_confirmation_message_to_farmer(volunteer):
    farmer_message = f"{volunteer.first_name} {volunteer.last_name} has confirmed his presence."
    messagebox.showinfo("Volunteer Confirmation", farmer_message)


def approve_arrival_window(event):
    approval_window = tk.Toplevel(root)
    approval_window.title("Approve Arrival")

    ttk.Label(approval_window, text="Approve arrival for volunteers?").grid(row=0, column=0, columnspan=3, pady=10)

response_var = tk.StringVar(value="Yes")  # Default choice is "Yes"
response_combobox = ttk.Combobox( textvariable=response_var, values=["Yes", "No"])
response_combobox.grid(row=1, column=0, columnspan=3, pady=5)

for i, volunteer in enumerate(Event.volunteers, start=1):
  response_var = tk.StringVar(value="Yes")  # Default choice is "Yes"
response_combobox = ttk.Combobox( textvariable=response_var, values=["Yes", "No"])
response_combobox.grid(row=0, column=0, columnspan=3, pady=10)

ttk.Button( text="Finish").grid(row=len(Event.volunteers) + 1, column=0, columnspan=3, pady=10)

def approve_arrival(event, approval_status):
    for volunteer in event.volunteers:
        if approval_status:
            volunteer.confirmation = "Yes"
            send_message_to_farmer(Event)
            messagebox.showinfo("Arrival Approved", f"Arrival approved for {volunteer.first_name} {volunteer.last_name}")
            save_data(events)
        else:
            messagebox.showinfo("Arrival Denied", f"Arrival denied for volunteers in {event.event_name}")
            break


root = tk.Tk()
root.title("Event Management Application")

events = load_data()

ttk.Button(root, text="Enter Volunteer Details", command=get_volunteer_details).pack(pady=10)
ttk.Button(root, text="Enter Farmer Details", command=get_farmer_details).pack(pady=10)
ttk.Button(root, text="Create Event", command=create_event).pack(pady=10)
ttk.Button(root, text="Approve Arrivals", command=lambda: approve_arrival_window(events)).pack(pady=10)


root.mainloop()
