
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
complaints = []
responses = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_complaint', methods=['POST'])
def submit_complaint():
    name = request.form['name']
    phone = request.form['phone']
    message = request.form['message']
    complaint_id = len(complaints) + 1
    complaints.append({'id': complaint_id, 'name': name, 'phone': phone, 'message': message})
    responses[complaint_id] = "جاري المتابعة"
    return redirect(url_for('home'))

@app.route('/track', methods=['GET'])
def track():
    track_id = request.args.get('track_id', type=int)
    result = responses.get(track_id, "لم يتم العثور على شكوى بهذا الرقم")
    return render_template('track.html', result=result, track_id=track_id)

@app.route('/admin')
def admin():
    return render_template('admin.html', complaints=complaints, responses=responses)

@app.route('/respond/<int:cid>', methods=['POST'])
def respond(cid):
    reply = request.form['reply']
    responses[cid] = reply
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
