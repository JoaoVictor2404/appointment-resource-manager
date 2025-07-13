from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None


class ResourceBase(BaseModel):
    name: str
    type: str

class ResourceCreate(ResourceBase):
    pass

class ResourceOut(ResourceBase):
    id: int
    class Config:
        orm_mode = True


class AppointmentBase(BaseModel):
    title: str
    start: datetime
    end: datetime

class AppointmentCreate(AppointmentBase):
    resource_id: int

class AppointmentOut(AppointmentBase):
    id: int
    owner: UserOut
    resource: ResourceOut
    class Config:
        orm_mode = True
