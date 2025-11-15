from fastapi import FastAPI

from database import Base, engine  # new import

app = FastAPI()

# This will create tables later once we define models
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "ClinicQ backend is running with a database!"}
