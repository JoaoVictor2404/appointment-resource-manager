from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from .. import crud, schemas, auth, notifications

router = APIRouter(prefix="/appointments", tags=["appointments"])

@router.post("/", response_model=schemas.AppointmentOut)
def create(ap: schemas.AppointmentCreate, 
           background_tasks: BackgroundTasks,
           current_user=Depends(auth.get_current_user),
           db: Session = Depends(auth.get_db)):
    # valida resource
    if not crud.list_resources(db, 0, 1):
        raise HTTPException(status_code=404, detail="Recurso não existe")
    obj = crud.create_appointment(db, ap, current_user.id)
    notifications.send_reminder_email(background_tasks, obj)
    return obj

@router.get("/", response_model=list[schemas.AppointmentOut])
def list_all(skip: int = 0, limit: int = 10,
             current_user=Depends(auth.get_current_user),
             db: Session = Depends(auth.get_db)):
    return crud.list_appointments(db, current_user.id, skip, limit)
