from sqlalchemy.orm import Session
from . import models, schemas
from .auth import get_password_hash


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed = get_password_hash(user.password)
    db_obj = models.User(email=user.email, hashed_password=hashed)
    db.add(db_obj); db.commit(); db.refresh(db_obj)
    return db_obj


def create_resource(db: Session, r: schemas.ResourceCreate):
    obj = models.Resource(**r.dict())
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

def list_resources(db: Session, skip: int, limit: int):
    return db.query(models.Resource).offset(skip).limit(limit).all()


def create_appointment(db: Session, appointment: schemas.AppointmentCreate, user_id: int):
    obj = models.Appointment(owner_id=user_id, **appointment.dict())
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

def list_appointments(db: Session, user_id: int, skip: int, limit: int):
    return db.query(models.Appointment).filter(models.Appointment.owner_id==user_id)\
        .offset(skip).limit(limit).all()
