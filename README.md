# 🌾 VillageConnect – Day 16 (Internship Project)

This is the initial setup for the **VillageConnect** web application as part of my Python Developer Internship.

The goal of this project is to help villagers connect with essential services like electricity, healthcare, water supply, etc. using a simple web platform.

---

## ✅ Day 16 Tasks Completed

- 🔹 Set up basic Flask web application (`app.py`)
- 🔹 Created SQLite database (`database.db`)
- 🔹 Built two tables:
  - `services` → Stores service names and descriptions
  - `users` → Stores user details and roles (villager, official)

---

## 🛠️ Project Files

| File         | Description                          |
|--------------|--------------------------------------|
| `app.py`     | Starts the Flask server              |
| `init_db.py` | Creates `services` and `users` tables |
| `database.db`| SQLite database file                 |

---

## 🚀 How to Run Locally

1. Install Flask (if not already):
   ```bash
   pip install flask
   
Create the database and tables:
python init_db.py

Start the Flask app:
python app.py

Open in browser:
http://127.0.0.1:5000/


## ✅ Day 17 - VillageConnect API (GET & POST)

Today, I created a RESTful API using Flask and SQLite for the VillageConnect project. It includes:

- `GET /api/services` – to fetch all services
- `POST /api/services` – to add new services

Tested both endpoints using Postman.

### Sample POST JSON:
```json
{
  "name": "Electricity",
  "description": "Village electricity service"
}

## ✅ Day 18 – HTML Templates & CSS Styling

On Day 18, I added a user interface to the VillageConnect project:

- Created `home.html` and `services.html` under the `templates/` directory.
- Set up a `static/style.css` file for clean and centered UI styling using Flexbox.
- Home page shows a welcome message and a link to view services.
- Services page displays a list of all services and includes a form to add new services.
- Ensured the layout is mobile-friendly and responsive.
- Fully tested via browser at `http://127.0.0.1:5000/`

### 📂 Project Structure (Updated)
Villageconnect/
├── app.py
├── init_db.py
├── database.db
├── static/
│ └── style.css
├── templates/
│ ├── home.html
│ └── services.html
└── README.md

👨‍💻 Created by
Deepak Yadav
Intern @ Python Developer Internship


