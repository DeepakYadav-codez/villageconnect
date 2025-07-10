from flask import Flask, request, jsonify, render_template, redirect, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "your-secret-key"

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/services", methods=["GET", "POST"])
def services():
    conn = get_db_connection()
    if request.method == "POST":
        name = request.form["name"].strip()
        description = request.form["description"].strip()

        if not name or not description:
            flash("❌ Both fields are required!")
        else:
            conn.execute("INSERT INTO services (name, description) VALUES (?, ?)", (name, description))
            conn.commit()
            flash("✅ Service added successfully!")

    services = conn.execute("SELECT * FROM services").fetchall()
    conn.close()
    return render_template("services.html", services=services)

# ✅ API Endpoint for Postman POST
@app.route("/api/services", methods=["POST"])
def api_add_service():
    data = request.get_json()
    name = data.get("name", "").strip()
    description = data.get("description", "").strip()

    if not name or not description:
        return jsonify({"error": "Name and description are required"}), 400

    conn = get_db_connection()
    conn.execute("INSERT INTO services (name, description) VALUES (?, ?)", (name, description))
    conn.commit()
    conn.close()

    return jsonify({"message": "✅ Service added successfully"}), 201

if __name__ == "__main__":
    app.run(debug=True)
