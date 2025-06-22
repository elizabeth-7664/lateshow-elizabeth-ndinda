# 🎬 Late Show API

A Flask-based RESTful API to manage episodes, guests, and appearances on a fictional late-night show.

---

## 🚀 Features

- View all episodes
- View episode details (with guest appearances)
- View all guests
- Add a new appearance (with rating validation)

---

## 🛠️ Technologies Used

- Python 3
- Flask
- Flask SQLAlchemy
- Flask Migrate
- Python-dotenv
- SQLite
- Postman (for testing)

---

## 🧱 Project Structure

lateshow-firstname-lastname/
├── app.py
├── models.py
├── config.py
├── extensions.py
├── routes/
│ ├── episodes.py
│ ├── guests.py
│ └── appearances.py
├── seed.py
├── data/
│ └── seed.csv
├── requirements.txt
├── .env
└── .gitignore


---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone <your-private-repo-url>
cd lateshow-firstname-lastname

2. Create Virtual Environment

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Set up .env file

DATABASE_URL=sqlite:///db.sqlite3

5. Run Migrations and Seed the DB

flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python seed.py

6. Run the App

python app.py

📬 API Endpoints
Method	Endpoint	Description
GET	/episodes	List all episodes
GET	/episodes/<id>	Get one episode + appearances
GET	/guests	List all guests
POST	/appearances	Add a guest appearance to an episode
📥 Sample POST /appearances JSON

{
  "rating": 5,
  "episode_id": 2,
  "guest_id": 3
}

    Rating must be between 1 and 5.

    On success, you’ll get a full appearance with guest and episode info.

    On failure, you’ll get:

{
  "errors": ["validation errors"]
}

📎 Notes

    Cascade delete is enabled for appearances.

    You can use Postman or browser to test the endpoints.

    Ensure db.sqlite3 is added to .gitignore.

