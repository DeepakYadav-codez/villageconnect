from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

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
        name = request.form["name"]
        description = request.form["description"]
        conn.execute("INSERT INTO services (name, description) VALUES (?, ?)", (name, description))
        conn.commit()

    services = conn.execute("SELECT * FROM services").fetchall()
    conn.close()
    return render_template("services.html", services=services)

if __name__ == "__main__":
    app.run(debug=True)
