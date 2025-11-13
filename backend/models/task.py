


from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(String(500), nullable=True)
    status = Column(String(50), default="pending")  # pending, in-progress, completed
    created_at = Column(DateTime, default=datetime)
    updated_at = Column(DateTime, default=datetime, onupdate=datetime)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref="tasks")

    def __repr__(self):
        return f"<Task(title={self.title}, status={self.status})>"

