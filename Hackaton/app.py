from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
from psycopg2 import OperationalError, Error
from dotenv import load_dotenv
from pyfcm import FCMNotification
import os

app = Flask(__name__)
CORS(app) 

load_dotenv()
def create_connection():
    try:
        connection = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        return connection
    except OperationalError as e:
        print(f"Error: {e}")
        return None

fcm = FCMNotification(api_key=os.getenv('FCM_API_KEY'))

@app.route('/create_event', methods=['POST'])
def create_event():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        data = request.get_json()
        farmer_id = data.get('farmer_id')
        event_name = data.get('event_name')
        event_description = data.get('event_description')
        query = f"INSERT INTO events (farmer_id, event_name, event_description) VALUES ({farmer_id}, '{event_name}', '{event_description}') RETURNING id;"
        cursor.execute(query)
        event_id = cursor.fetchone()[0]
        connection.commit()
        notify_volunteers(event_name, event_description)

        return jsonify({"success": True, "event_id": event_id})
    except Error as e:
        print(f"Error creating event: {e}")
        return jsonify({"success": False, "error": str(e)})
    finally:
        cursor.close()
        connection.close()

def notify_volunteers(event_name, event_description):
    volunteer_tokens_query = "SELECT token FROM volunteers;"
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(volunteer_tokens_query)
    volunteer_tokens = [row[0] for row in cursor.fetchall()]

    message = {
        'body': f'New Event: {event_name}\nDescription: {event_description}',
        'title': 'New Event',
        'sound': 'default'
    }
    result = fcm.notify_multiple_devices(registrationids=volunteer_tokens, message_body=message)

if __name__ == '__main__':
    app.run(debug=True)
    
