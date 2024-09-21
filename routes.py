# routes.py

from flask import app, render_template, request, redirect, url_for, session, jsonify
from chatbot import process_message
# from __init__ import app
from models import User, store_conversation, book_appointment_in_db
from werkzeug.security import check_password_hash

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('options'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        return redirect(url_for('options'))
    return "Invalid credentials", 401

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/options')
def options():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    return render_template('options.html')

@app.route('/chat')
def chat():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    return render_template('chat.html')

@app.route('/appointment')
def appointment():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    return render_template('appointment.html')

@app.route('/process', methods=['POST'])
def process():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    user_input = request.json.get('message')
    user_id = session.get('user_id')
    response = process_message(user_input)
    store_conversation(user_id, user_input, response)
    return jsonify({'response': response})

@app.route('/book', methods=['POST'])
def book_appointment():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    data = request.form
    data['user_id'] = session.get('user_id')
    booking_status = book_appointment_in_db(data)
    return jsonify({'status': 'success', 'message': 'Appointment booked!'} if booking_status else {'status': 'failure'})