from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter(prefix="/cars", tags=["Cars"])


@router.post("/", response_model=schemas.CarRead)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    return crud.create_car(db, car)


@router.get("/", response_model=list[schemas.CarRead])
def list_cars(db: Session = Depends(get_db)):
    return crud.get_cars(db)
