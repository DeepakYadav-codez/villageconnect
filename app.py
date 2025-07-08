from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Connect to DB helper
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# ✅ Home route
@app.route('/')
def home():
    return "Welcome to VillageConnect 🌾"

# ✅ GET all services
@app.route('/api/services', methods=['GET'])
def get_services():
    conn = get_db_connection()
    services = conn.execute('SELECT * FROM services').fetchall()
    conn.close()

    service_list = []
    for service in services:
        service_list.append({
            "id": service["id"],
            "name": service["name"],
            "description": service["description"]
        })
    return jsonify(service_list)

# ✅ POST a new service
@app.route('/api/services', methods=['POST'])
def add_service():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")

    if not name:
        return jsonify({"error": "Service name is required"}), 400

    conn = get_db_connection()
    conn.execute('INSERT INTO services (name, description) VALUES (?, ?)', (name, description))
    conn.commit()
    conn.close()

    return jsonify({"message": "✅ Service added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
