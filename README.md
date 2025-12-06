# Car-Service-Booking-API
FastAPI + PostgreSQL + CRUD + Auth + Swagger UI

🚗 Car Service Booking API

A FastAPI-based backend for managing car service workshop operations — including user registration, vehicle management, service booking, and real-time status updates.

explnation:

This is a Car Service Booking API built using FastAPI, PostgreSQL, SQLAlchemy, and Alembic.
The goal is to provide a complete backend solution for a car workshop where users can register, log in, book service slots, track service status, and manage vehicle details.

I designed a relational database schema handling users, vehicles, service bookings, and mechanics.

I implemented:

JWT authentication for secure login

CRUD APIs for all core entities

Alembic migrations for version-controlled DB changes

PostgreSQL as the production database

I structured the project following clean architecture:

app/
├── models       → Database schema
├── routers      → API endpoints
├── database     → DB connection & session management
└── main         → App entry


This API is scalable: new roles like workshop admin or payments can be added easily.

I built this to showcase real-world backend engineering skills including authentication, DB migrations, dependency injection, and code modularity.

✨ Features
Feature	Description
🔐 JWT Authentication	Secure login & access control
🚙 Vehicle Management	Add, view, update customer vehicle details
🧾 Service Booking	Create bookings for servicing
🛠 Service Status Tracking	Mechanic/workshop can update status
🗄 PostgreSQL + Alembic	Production-ready database with migrations
🧩 Modular Architecture	Easy to extend and maintain

🏛 Tech Stack
Layer	Technology
Backend Framework	FastAPI
Database	PostgreSQL
ORM	SQLAlchemy
Migrations	Alembic
Auth	JWT Tokens
Server	Uvicorn
📂 Project Structure
Car-Service-Booking-API/
│
├── alembic/                # Migration scripts
├── app/
│   ├── routers/            # API endpoints
│   ├── models.py           # SQLAlchemy models
│   ├── database.py         # DB connection config
│   ├── auth.py             # JWT login
│   └── main.py             # FastAPI entry
│
├── alembic.ini
├── requirements.txt
└── README.md

⚙️ Installation & Setup
Clone & Move into Project
git clone https://github.com/Yourusername/Car-Service-Booking-API.git
cd Car-Service-Booking-API

Create Virtual Environment
python -m venv venv
source venv/bin/activate     # Mac / Linux
venv\Scripts\activate        # Windows

Install Requirements
pip install -r requirements.txt

Update DB URL (PostgreSQL example)
# app/database.py
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:YOURPASSWORD@localhost/car_db"

Run Alembic migrations
alembic upgrade head

▶️ Start the Server
uvicorn app.main:app --reload

🧪 API Testing

Open Swagger UI after running the server:
👉 http://127.0.0.1:8000/docs

🚀 Future Enhancements

✔ Payment integration
✔ Admin dashboard
✔ Mechanic role-based access
✔ SMS/Email notifications

📌 Status

Currently in active development. Core booking features are implemented.





```
car-service-booking-api/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── auth.py
│   ├── routers/
│   │   ├── users.py
│   │   ├── cars.py
│   │   ├── bookings.py
│
├── requirements.txt
├── README.md

```

Create and activate virtual environment
```
python -m venv venv
venv\Scripts\activate
```
Install all dependencies
```
pip install -r requirements.txt

```

Confirm installation success

```
uvicorn --version
fastapi --help

```
Test DB connection (optional check)
```
python -c "from app.database import engine; print(engine)"
```
create DB
```
python create_db.py
```


Generate first migration
```
alembic revision --autogenerate -m "create tables"

```
Apply migration — Create tables in PostgreSQL 🎯
```

```
