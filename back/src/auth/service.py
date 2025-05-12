from aiomysql import Error as ConnectionError, DictCursor
from datetime import timedelta
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from .models import Token
from src.shared.database import Database
from src.shared.hash_password import hash_password, verify_password
from src.shared.security import create_access_token
from src.users.models import UserCreate


class AuthService:
    @staticmethod
    async def register(user: UserCreate):
        try:
            async with await Database.get_connection() as con:
                async with con.cursor(DictCursor) as cursor:
                    await cursor.execute(
                        "CALL sp_register(%s, %s, %s)",
                        (user.username, user.email, hash_password(user.password)),
                    )
                await con.commit()
                return {"message": "Usuario registrado correctamente"}
        except ConnectionError as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")

    @staticmethod
    async def login(form_data: OAuth2PasswordRequestForm):
        try:
            async with await Database.get_connection() as con:
                async with con.cursor(DictCursor) as cursor:
                    await cursor.execute("CALL sp_login(%s)", (form_data.username,))
                    user_result = await cursor.fetchone()

                if not user_result or not verify_password(
                    form_data.password, user_result["password"]
                ):
                    raise HTTPException(
                        status_code=400, detail="Credenciales incorrectas"
                    )

                access_token = create_access_token(
                    data={"sub": user_result["user_id"]},
                    expires_delta=timedelta(minutes=30),
                )

                return Token(access_token=access_token, token_type="bearer")
        except ConnectionError as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")
