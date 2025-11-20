# backend/main.py

from fastapi import FastAPI

from backend.database import Base, engine
from backend.routers import users, auth

# Create the DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ClinicQ API", version="0.1.0")

# Register routers
app.include_router(users.router)
app.include_router(auth.router)
