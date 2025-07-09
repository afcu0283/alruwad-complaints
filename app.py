from flask import Flask, render_template, request
import uuid
import datetime

app = Flask(__name__)
complaints = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    phone = request.form.get('phone')
    message = request.form.get('message')
    complaint_id = f"ruw{str(uuid.uuid4().int)[:4]}"
    complaints[complaint_id] = {
        'name': name,
        'phone': phone,
        'message': message,
        'status': 'قيد المراجعة',
        'time': str(datetime.datetime.now())
    }
    return render_template('submitted.html', complaint_id=complaint_id)

@app.route('/track', methods=['POST'])
def track():
    track_id = request.form.get('track_id')
    complaint = complaints.get(track_id)
    return render_template('track.html', complaint=complaint, track_id=track_id)