from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Task create request schema
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    completed: Optional[bool] = False
    user_id: int  # Task kis user ka hai

# Task response schema
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    completed: bool
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True  # SQLAlchemy models ko response main convert karne ke liye
