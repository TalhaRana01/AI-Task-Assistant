from fastapi import FastAPI
from backend.database import Base, engine
from backend.routers import auth, tasks

app = FastAPI(title="AI Task Assistant")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(tasks.router)
