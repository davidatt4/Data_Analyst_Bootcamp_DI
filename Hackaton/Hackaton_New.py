from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config = 'postgres://ddlmjmnp:***@ella.db.elephantsql.com/ddlmjmnp '
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secret key

db = SQLAlchemy(app)
socketio = SocketIO(app)

class Farmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    events = db.relationship('Event', backref='farmer', lazy=True)

class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(50), nullable=False)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'), nullable=False)@app.route('/api/farmers', methods=['POST'])
def register_farmer():
    data = request.get_json()
    new_farmer = Farmer(name=data['name'], phone_number=data['phone_number'], city=data['city'])
    db.session.add(new_farmer)
    db.session.commit()
    return jsonify({"message": "Farmer registered successfully"}), 201

@app.route('/api/volunteers', methods=['POST'])
def register_volunteer():
    data = request.get_json()
    new_volunteer = Volunteer(name=data['name'], phone_number=data['phone_number'], city=data['city'])
    db.session.add(new_volunteer)
    db.session.commit()
    return jsonify({"message": "Volunteer registered successfully"}), 201

@app.route('/api/events', methods=['POST'])
def create_event():
    data = request.get_json()
    farmer_id = data.get('farmer_id')

    farmer = Farmer.query.get(farmer_id)
    if not farmer:
        return jsonify({"error": "Farmer not found"}), 404

    new_event = Event(description=data['description'], farmer_id=farmer_id)
    db.session.add(new_event)
    db.session.commit()

    event_data = {
        'farmer_id': farmer_id,
        'event_id': new_event.id,
        'description': new_event.description,
    }
    socketio.emit('new_event', event_data, namespace='/')

    return jsonify({"message": "Event created successfully"}), 201

@socketio.on('connect', namespace='/')
def handle_connect():
    print('Client connected')

if __name__ == '__main__':
    socketio.run(app, debug=True)
