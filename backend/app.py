from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import sys
from flask_cors import CORS  # Import CORS


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Attempt to connect to MongoDB
try:
    client = MongoClient("mongodb://localhost:27017")
    db = client["MLOps_Task5_webapp"]
    collection = db["user_info"]
    print("Connected to MongoDB")
except ConnectionFailure as e:
    print("Failed to connect to MongoDB:", e)
    sys.exit(1)  # Exit the application with exit code 1 if MongoDB connection fails

@app.route('/store', methods=['POST'])
def store_data():
    try:
        name = request.form['name']
        email = request.form['email']
    except KeyError as e:
        return f'Missing form field: {e.args[0]}', 400

    # Store data in MongoDB
    collection.insert_one({"name": name, "email": email})
    return 'Data stored successfully!'

@app.route('/get', methods=['GET'])
def get_data():
    # Retrieve data from MongoDB
    data = list(collection.find({}, {'_id': 0}))
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
