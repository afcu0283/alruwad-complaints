
from flask import Flask, request, jsonify
import uuid
import datetime

app = Flask(__name__)

complaints = []

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    complaint_id = str(uuid.uuid4())[:8]
    complaints.append({
        "id": complaint_id,
        "name": data.get("name"),
        "phone": data.get("phone"),
        "message": data.get("message"),
        "status": "قيد المراجعة",
        "timestamp": str(datetime.datetime.now())
    })
    return jsonify({"message": "تم استلام الشكوى", "id": complaint_id}), 200

@app.route('/check/<complaint_id>', methods=['GET'])
def check(complaint_id):
    for c in complaints:
        if c["id"] == complaint_id:
            return jsonify(c)
    return jsonify({"error": "الشكوى غير موجودة"}), 404

if __name__ == '__main__':
    app.run(debug=True)
