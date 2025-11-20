# backend/auth/dependencies.py

from fastapi import Depends
from backend.security import get_current_user
from backend.models.user import User as UserModel


def get_current_active_user(
    current_user: UserModel = Depends(get_current_user),
) -> UserModel:
    # In future you can check is_active here.
    return current_user
