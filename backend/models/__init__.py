from sqlalchemy import Column, Integer, String
from database import Base  # note: no "backend." here since main.py is in the same package

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)


