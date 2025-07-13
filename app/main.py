from fastapi import FastAPI
from .database import engine, Base
from .auth import get_db, authenticate_user, create_access_token
from .routers import users, resources, appointments
from fastapi.security import OAuth2PasswordRequestForm

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Gestão de Agendamentos", version="2.0")

app.include_router(users.router)
app.include_router(resources.router)
app.include_router(appointments.router)

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Credenciais incorretas")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
