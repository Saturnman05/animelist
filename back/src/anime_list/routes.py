from aiomysql import Error as ConnectionError, DictCursor
from fastapi import APIRouter, Depends, HTTPException

from .models import AnimeListCreate, AnimeListUpdate
from shared.database import Database
from shared.security import get_current_user

router = APIRouter()


@router.get("/")
async def get_anime_lists():
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute("CALL sp_anime_lists(NULL, NULL, NULL, %s)", (1,))
                results = await cursor.fetchall()

            if not results:
                raise HTTPException(status_code=400, detail="Anime lists not found")

            return results
    except ConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@router.get("/{list_id}")
async def get_anime_list(list_id: str):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute(
                    "CALL sp_anime_lists(%s, NULL, NULL, %s)", (list_id, 2)
                )
                result = await cursor.fetchone()

            if not result:
                raise HTTPException(status_code=400, detail="Anime list not found")

            return result
    except ConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@router.post("/")
async def post_anime_list(
    anime_list: AnimeListCreate, current_user: str = Depends(get_current_user)
):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute(
                    "CALL sp_anime_lists(NULL, %s, %s, %s)",
                    (anime_list.list_name, current_user.user_id, 3),
                )
            await con.commit()
            return {"message": "Anime list created successfully"}
    except ConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@router.put("/")
async def put_anime_list(
    anime_list: AnimeListUpdate, current_user: str = Depends(get_current_user)
):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute(
                    "CALL sp_anime_lists(%s, %s, %s, %s)",
                    (anime_list.list_id, anime_list.name, current_user.user_id, 4),
                )
            await con.commit()
            return {"message": "Anime list updated successfully"}
    except ConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@router.delete("/{list_id}")
async def delete_anime_list(
    list_id: str, current_user: str = Depends(get_current_user)
):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute(
                    "CALL sp_anime_lists(%s, NULL, %s, %s)",
                    (list_id, current_user.user_id, 5),
                )
            await con.commit()
            return {"message": "Anime list deleted successfully"}
    except ConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
