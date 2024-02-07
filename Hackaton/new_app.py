from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farm_volunteer.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Farmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    city = db.Column(db.String(250), nullable=False)
    events = db.relationship('Event', backref='farmer', lazy=True)

class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(250), nullable=False)
    events_attending = db.relationship('Event', secondary='volunteer_event', backref='volunteers', lazy='dynamic')

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100), nullable=False)
    event_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.Text)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'), nullable=True)

# Association table for Volunteer-Event many-to-many relationship
volunteer_event = db.Table('volunteer_event',
    db.Column('volunteer_id', db.Integer, db.ForeignKey('volunteer.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True)
)

# Route to get a list of names with categories (Farmers and Volunteers)
@app.route('/user_list')
def user_list():
    farmers = Farmer.query.all()
    volunteers = Volunteer.query.all()
    return render_template('user_list.html', farmers=farmers, volunteers=volunteers)

# Route to get a combined list of Farmers and Volunteers
@app.route('/combined_list')
def combined_list():
    farmers = Farmer.query.all()
    volunteers = Volunteer.query.all()
    return render_template('combined_list.html', farmers=farmers, volunteers=volunteers)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
