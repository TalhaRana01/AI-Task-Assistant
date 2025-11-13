from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Database URL from .env or default SQLite
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")

# SQLAlchemy Engine
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}  # SQLite specific
)

# Session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

