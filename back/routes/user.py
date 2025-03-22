from aiomysql import Error as ConectionError, DictCursor
from fastapi import APIRouter, HTTPException, Depends

from database import Database
from models.user import User, UserCreate, UserUpdate, UserChangePassword
from utils import hash_password
from utils.security import get_current_user

router = APIRouter()


# POST
@router.post("/")
async def crear_usuario(
    user: UserCreate, current_user: User = Depends(get_current_user)
):
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


# GET ALL
@router.get("/")
async def get_usuarios(current_user: User = Depends(get_current_user)):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute("CALL sp_users(NULL, NULL, NULL, NULL, %s)", (1,))
                results = await cursor.fetchall()

        if not results:
            raise HTTPException(status_code=400, detail="Usuarios no encontrados")
        return results
    except ConectionError as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


# GET my user
@router.get("/my_user")
async def get_my_user(current_user: User = Depends(get_current_user)):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute(
                    "CALL sp_users(%s, NULL, NULL, NULL , %s)",
                    (current_user.user_id, 2),
                )
                user = await cursor.fetchone()

        if not user:
            raise HTTPException(status_code=400, detail="Usuario no encontrado")

        return user
    except ConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


# GET single
@router.get("/{user_id}")
async def obtener_usuario(user_id: str, current_user: User = Depends(get_current_user)):
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


# PUT
@router.put("/")
async def actualizar_usuario(
    user: UserUpdate, current_user: User = Depends(get_current_user)
):
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


# DELETE
@router.delete("/{user_id}")
async def eliminar_usuario(
    user_id: str, current_user: User = Depends(get_current_user)
):
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


# PUT change password
@router.put("/change_password")
async def change_password(
    user: UserChangePassword, current_user: User = Depends(get_current_user)
):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute(
                    "CALL sp_users(%s, NULL, NULL, %s, %s)",
                    (current_user.user_id, hash_password(user.password), 6),
                )
            await con.commit()
        return {"message": "Contraseña acutalizada"}
    except ConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@router.post("/recover_password")
async def recover_password(email: str):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute(
                    "CALL sp_users(NULL, NULL, %s, NULL, %s)", (email, 7)
                )
            await con.commit()
        return {"message": "Contrseña cambiada"}
    except ConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
