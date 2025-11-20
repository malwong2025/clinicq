# backend/routers/users.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.user import User as UserModel
from backend.schemas.users import UserCreate, User as UserSchema
from backend.security import get_password_hash

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)) -> UserModel:
    """
    Create a new user.
    """

    # 1) Check if email already exists
    existing = db.query(UserModel).filter(UserModel.email == user.email).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    # 2) Hash the password (MUST be user.password, not user)
    hashed_password = get_password_hash(user.password)

    # 3) Create model instance
    db_user = UserModel(
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password,
        is_active=user.is_active,
    )

    # 4) Save to DB
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
