import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2
from psycopg2 import sql

# ... (Your existing classes and functions)

# Connect to PostgreSQL (replace with your own database credentials)
conn = psycopg2.connect(
    host="your_host",
    database="your_database",
    user="your_user",
    password="your_password"
)

def save_farmer_details():
    # ... (Your existing code)

    # Insert farmer details into the PostgreSQL database
    with conn, conn.cursor() as cursor:
        cursor.execute(
            sql.SQL("INSERT INTO farmers (first_name, last_name, phone_number, city) VALUES (%s, %s, %s, %s) RETURNING id;"),
            (first_name_entry.get(), last_name_entry.get(), phone_number_entry.get(), city_entry.get())
        )
        farmer_id = cursor.fetchone()[0]

    return Farmer(
        first_name_entry.get(),
        last_name_entry.get(),
        phone_number_entry.get(),
        city_entry.get()
    )

def save_volunteer_details():
    # ... (Your existing code)

    # Insert volunteer details into the PostgreSQL database
    with conn, conn.cursor() as cursor:
        cursor.execute(
            sql.SQL("INSERT INTO volunteers (first_name, last_name, phone_number, city, confirmation) VALUES (%s, %s, %s, %s, %s) RETURNING id;"),
            (first_name_entry.get
