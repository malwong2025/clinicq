from fastapi import FastAPI

from database import Base, engine
from routers import router as users_router

# Create tables (including User)
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "ClinicQ backend is running with a database!"}


# Add the /users endpoints
app.include_router(users_router)
