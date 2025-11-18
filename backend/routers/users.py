from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import User
from schemas import UserCreate, UserRead

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/", response_model=List[UserRead])
def list_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(
        email=user.email,
        full_name=user.full_name,
        # Temporary fake hashing – just for testing
        hashed_password="fakehashed-" + user.password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
