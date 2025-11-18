from fastapi import FastAPI

from database import Base, engine
from routers import users  # and auth if you have it
# from routers import auth  # leave this or comment depending on where you’re up to

app = FastAPI(
    title="ClinicQ API",
    version="0.1.0",
)

# Create tables in clinicq.db if they don't exist
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "ClinicQ backend is running with a database!"}

app.include_router(users.router)
# app.include_router(auth.router)   # uncomment when auth is ready

