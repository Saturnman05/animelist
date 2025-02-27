from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    username: str
    email: str
    password: str


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserUpdate(BaseModel):
    user_id: str
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str
