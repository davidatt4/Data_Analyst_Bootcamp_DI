import tkinter as tk
from tkinter import ttk,messagebox
from plyer import notification

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
class Farmer(Person):
    def __init__(self, first_name, last_name, phone_number, city):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.city = city

    def can_create_event(self):
        return True

    def notify_new_event(self, event_name):
        messagebox.showinfo("New Event Created", f"Farmer {self.first_name} {self.last_name} has created a new event: {event_name}. Do you want to participate?")

class Volunteer(Person):
    def __init__(self, first_name, last_name, phone_number, city):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.city = city
        self.confirmation = ""

    def can_create_event(self):
        return False

    def receive_notification(self, event_name):
        response = messagebox.askquestion("New Event Notification", f"The farmer has created a new event: {event_name}. Do you want to participate?")
        return response.lower() == 'yes'

    def notify_participation_approval(self):
        messagebox.showinfo("Participation Approval", f"{self.first_name} {self.last_name} has approved participation in the event.")

class Event:
    def __init__(self, event_name, event_date, description, farmers, volunteers):
        self.event_name = event_name
        self.event_date = event_date
        self.description = description
        self.farmers = farmers
        self.volunteers = volunteers

    def add_farmer(self, farmer):
        self.farmers.append(farmer)
        for volunteer in self.volunteers:
            if volunteer.receive_notification(self.event_name):
                volunteer.confirmation = 'yes'
                volunteer.notify_participation_approval()

    def add_volunteer(self, volunteer):
        self.volunteers.append(volunteer)

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
        for farmer in farmers:
            farmer.notify_new_event(event.event_name)
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

    ttk.Button(confirmation_window, text="Approve Arrival", command=lambda: confirm_arrival(event)).grid(row=len(event.volunteers) + len(event.farmers) + 1, column=0, columnspan=2, pady=10)

def send_message_to_farmer(event):
    farmer_messages = [f"Farmer: {farmer.first_name} {farmer.last_name} has confirmed the event." for farmer in event.farmers]
    confirmed_volunteers = [volunteer for volunteer in event.volunteers if volunteer.confirmation.lower() == "yes"]

    if confirmed_volunteers:
        message = f"Confirmed arrivals for event '{event.event_name}':\n"
        for volunteer in confirmed_volunteers:
            message += f"{volunteer.first_name} {volunteer.last_name}\n"

            # Send a message to the farmer for each confirmed volunteer
            send_confirmation_message_to_farmer(volunteer)

        messagebox.showinfo("Confirmed Arrivals", message)
    else:
        messagebox.showinfo("No Confirmations", "No volunteers confirmed their arrival for the event.")

# ... (autres parties du code)

def send_confirmation_message_to_farmer(volunteer):
    farmer_message = f"{volunteer.first_name} {volunteer.last_name} a confirmé sa présence."
    notification.notify(
        title="Confirmation du volontaire",
        message=f"Le volontaire {volunteer.first_name} {volunteer.last_name} a confirmé sa participation.",
    )
    # Vous pouvez remplacer la ligne suivante par la méthode que vous préférez pour informer le fermier
    messagebox.showinfo("Confirmation du volontaire", farmer_message)

def confirm_arrival(event):
    confirmation_window = tk.Toplevel(root)
    confirmation_window.title("Confirmer l'arrivée")

    ttk.Label(confirmation_window, text="Confirm the arrival for the volunteers?").grid(row=0, column=0, columnspan=2, pady=10)



def set_confirmation(value):
    for volunteer in Event.volunteers:
        volunteer.confirmation = value
    if value.lower() == "yes":
        for farmer in Event.farmers:
            farmer_name = f"{volunteer.first_name} {volunteer.last_name}"
            message = f"{farmer_name} approves his arrival"
            notification.notify(
                title="Arrival Approvation",
                message=message,
            )
            messagebox.showinfo("Confirmation", message)
            send_confirmation_message_to_farmer(volunteer)

    send_message_to_farmer(Event)



    ttk.Button( text="Yes", command=lambda: set_confirmation("Yes")).grid(row=1, column=0, pady=10)
    ttk.Button( text="No", command=lambda: set_confirmation("no")).grid(row=1, column=1, pady=10)

    ttk.Button(text="Yes", command=lambda: set_confirmation("yes")).grid(row=1, column=0, pady=10)
    ttk.Button( text="No", command=lambda: set_confirmation("no")).grid(row=1, column=1, pady=10)




# Main application
root = tk.Tk()
root.title("Event Management Application")

# Create a Farmer instance for testing
person = Farmer("John", "Doe", "123456789", "Cityville")

ttk.Button(root, text="Enter Volunteer Details", command=get_volunteer_details).pack(pady=10)
ttk.Button(root, text="Enter Farmer Details", command=get_farmer_details).pack(pady=10)
ttk.Button(root, text="Create Event", command=create_event).pack(pady=10)
ttk.Button(root, text="Confirm Arrivals", command=lambda: confirm_arrival(None)).pack(pady=10)

root.mainloop()
