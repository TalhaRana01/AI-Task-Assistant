# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database import Base, engine  # relative import
from backend.routers import auth, tasks

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Task Assistant",
    description="An AI-powered task management app using FastAPI, Streamlit, and LangChain",
    version="1.0.0"
)

# CORS
origins = [
    "http://localhost",
    "http://localhost:8501",  # Streamlit default
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Task Assistant!"}
