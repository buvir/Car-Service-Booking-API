from fastapi import FastAPI
from app.routers import auth, cars, bookings
from dotenv import load_dotenv
load_dotenv()


app = FastAPI(
    title="Car Service Booking API",
    version="1.0",
    description="CRUD API for car service bookings with authentication."
)

app.include_router(auth.router)
app.include_router(cars.router)
app.include_router(bookings.router)
