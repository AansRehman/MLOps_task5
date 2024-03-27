from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# MongoDB setup
client = MongoClient("mongodb://localhost:27017")
db = client["MLOps_Task5_webapp"]
collection = db["user_info"]

# Routes
@app.route('/store', methods=['POST'])
def store_data():
    try:
        name = request.form['name']
        email = request.form['email']
        collection.insert_one({"name": name, "email": email})
        return 'Data stored successfully!'
    except Exception as e:
        return str(e), 500

@app.route('/get', methods=['GET'])
def get_data():
    try:
        data = list(collection.find({}, {'_id': 0}))
        return jsonify(data)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
