from flask import Flask, render_template, request, redirect

app = Flask(__name__)
complaints = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    phone = request.form['phone']
    complaint = request.form['complaint']
    complaints.append({'name': name, 'phone': phone, 'complaint': complaint})
    return render_template('thanks.html', name=name)

@app.route('/track', methods=['GET'])
def track():
    phone = request.args.get('phone')
    found = [c for c in complaints if c['phone'] == phone]
    return render_template('track.html', found=found, phone=phone)

@app.route('/admin')
def admin():
    return render_template('admin.html', complaints=complaints)

if __name__ == '__main__':
    app.run(debug=True)
