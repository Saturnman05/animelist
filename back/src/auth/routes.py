from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from .service import AuthService
from users.models import UserCreate

router = APIRouter()


@router.post("/register")
async def register(user: UserCreate):
    return await AuthService.register(user)


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return await AuthService.login(form_data)
