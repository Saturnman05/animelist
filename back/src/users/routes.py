from fastapi import APIRouter, Depends

from .models import User, UserCreate, UserUpdate, UserChangePassword
from .service import UserService
from shared.security import get_current_user

router = APIRouter()


@router.post("/")
async def crear_usuario(
    user: UserCreate, current_user: User = Depends(get_current_user)
):
    return await UserService.create_user(user)


@router.get("/")
async def get_usuarios(current_user: User = Depends(get_current_user)):
    return await UserService.get_all_users()


@router.get("/my_user")
async def get_my_user(current_user: User = Depends(get_current_user)):
    return await UserService.get_my_user(current_user)


@router.get("/{user_id}")
async def obtener_usuario(user_id: str, current_user: User = Depends(get_current_user)):
    return await UserService.get_user_by_id(user_id)


@router.put("/")
async def actualizar_usuario(
    user: UserUpdate, current_user: User = Depends(get_current_user)
):
    return await UserService.update_user(user)


@router.delete("/{user_id}")
async def eliminar_usuario(
    user_id: str, current_user: User = Depends(get_current_user)
):
    return await UserService.delete_user(user_id)


@router.put("/change_password")
async def change_password(
    user: UserChangePassword, current_user: User = Depends(get_current_user)
):
    user.user_id = current_user.user_id
    return await UserService.change_password(user)


"""
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
"""
