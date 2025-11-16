from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    full_name: str | None = None


class UserRead(BaseModel):
    id: int
    email: str
    full_name: str | None = None

    class Config:
        orm_mode = True
