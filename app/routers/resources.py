from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, auth

router = APIRouter(prefix="/resources", tags=["resources"])

@router.post("/", response_model=schemas.ResourceOut)
def create(r: schemas.ResourceCreate, db: Session = Depends(auth.get_db)):
    return crud.create_resource(db, r)

@router.get("/", response_model=list[schemas.ResourceOut])
def list_all(skip: int = 0, limit: int = 10, db: Session = Depends(auth.get_db)):
    return crud.list_resources(db, skip, limit)
