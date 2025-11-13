from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# User create request schema
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


# User login request schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str
# User response schema (for API responses)
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True  # SQLAlchemy model ko Pydantic object main convert karne ke liye

# User with tasks schema
class UserWithTasks(UserResponse):
    tasks: Optional[List] = []


