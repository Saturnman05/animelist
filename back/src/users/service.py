from aiomysql import Error as ConectionError, DictCursor
from fastapi import HTTPException

from .models import User, UserCreate, UserUpdate, UserChangePassword
from src.shared.database import Database
from src.shared.hash_password import hash_password


class UserService:
    @staticmethod
    async def create_user(user: UserCreate):
        try:
            async with await Database.get_connection() as con:
                async with con.cursor(DictCursor) as cursor:
                    await cursor.execute(
                        "CALL sp_users(NULL, %s, %s, %s, %s)",
                        (user.username, user.email, user.password, 3),
                    )
                await con.commit()
            return {"message": "Usuario creado correctamente"}
        except ConectionError as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")

    @staticmethod
    async def get_all_users():
        try:
            async with await Database.get_connection() as con:
                async with con.cursor(DictCursor) as cursor:
                    await cursor.execute(
                        "CALL sp_users(NULL, NULL, NULL, NULL, %s)", (1,)
                    )
                    results = await cursor.fetchall()

            if not results:
                raise HTTPException(status_code=400, detail="Usuarios no encontrados")
            return results
        except ConectionError as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")

    @staticmethod
    async def get_my_user(user: User):
        try:
            async with await Database.get_connection() as con:
                async with con.cursor(DictCursor) as cursor:
                    await cursor.execute(
                        "CALL sp_users(%s, NULL, NULL, NULL , %s)",
                        (user.user_id, 2),
                    )
                    user = await cursor.fetchone()

            if not user:
                raise HTTPException(status_code=400, detail="Usuario no encontrado")

            return user
        except ConnectionError as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")

    @staticmethod
    async def get_user_by_id(user_id: str):
        try:
            async with await Database.get_connection() as con:
                async with con.cursor(DictCursor) as cursor:
                    await cursor.execute(
                        "CALL sp_users(%s, NULL, NULL, NULL, %s)", (user_id, 2)
                    )
                    user = await cursor.fetchone()

            if not user:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")

            return user
        except ConnectionError as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")

    @staticmethod
    async def update_user(user: UserUpdate):
        try:
            async with await Database.get_connection() as con:
                async with con.cursor(DictCursor) as cursor:
                    await cursor.execute(
                        "CALL sp_users(%s, %s, %s, %s, %s)",
                        (user.user_id, user.username, user.email, user.password, 4),
                    )
                await con.commit()
            return {"message": "Usuario editado correctamente"}
        except ConectionError as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")

    @staticmethod
    async def change_password(user: UserChangePassword):
        try:
            async with await Database.get_connection() as con:
                async with con.cursor(DictCursor) as cursor:
                    await cursor.execute(
                        "CALL sp_users(%s, NULL, NULL, %s, %s)",
                        (user.user_id, hash_password(user.password), 6),
                    )
                await con.commit()
            return {"message": "Contraseña acutalizada"}
        except ConnectionError as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")

    @staticmethod
    async def delete_user(user_id: str):
        try:
            async with await Database.get_connection() as con:
                async with con.cursor(DictCursor) as cursor:
                    await cursor.execute(
                        "CALL sp_users(%s, NULL, NULL, NULL, %s)",
                        (user_id, 5),
                    )
                await con.commit()
            return {"message": "Usuario eliminado correctamente"}
        except ConectionError as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")
