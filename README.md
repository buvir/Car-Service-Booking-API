# Car-Service-Booking-API
FastAPI + PostgreSQL + CRUD + Auth + Swagger UI







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
