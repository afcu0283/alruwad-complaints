from flask import Flask, render_template, request, redirect, url_for
import uuid
import datetime

app = Flask(__name__)
complaints = {}
admin_username = 'admin'
admin_password = '123456'

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
        'time': str(datetime.datetime.now()),
        'reply': ''
    }
    return render_template('submitted.html', complaint_id=complaint_id)

@app.route('/track', methods=['POST'])
def track():
    track_id = request.form.get('track_id')
    complaint = complaints.get(track_id)
    return render_template('track.html', complaint=complaint, track_id=track_id)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == admin_username and password == admin_password:
            return render_template('dashboard.html', complaints=complaints)
        else:
            return "بيانات الدخول غير صحيحة"
    return render_template('admin_login.html')

@app.route('/reply/<complaint_id>', methods=['POST'])
def reply(complaint_id):
    reply_message = request.form.get('reply')
    if complaint_id in complaints:
        complaints[complaint_id]['reply'] = reply_message
        complaints[complaint_id]['status'] = 'تم الرد'
    return redirect(url_for('admin'))