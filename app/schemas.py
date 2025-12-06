from pydantic import BaseModel, EmailStr
from datetime import datetime




class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserLogin(BaseModel):
    email: str
    password: str


# ----- User Schemas -----
class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True


# ----- Car Schemas -----
class CarBase(BaseModel):
    brand: str
    model: str
    registration_number: str


class CarCreate(CarBase):
    pass


class CarRead(CarBase):
    id: int

    class Config:
        from_attributes = True


# ----- Booking Schemas -----
class BookingBase(BaseModel):
    user_id: int
    car_id: int


class BookingCreate(BookingBase):
    service_date: datetime
    status: str = "Pending"


class BookingRead(BookingBase):
    id: int
    service_date: datetime
    status: str

    class Config:
        from_attributes = True
