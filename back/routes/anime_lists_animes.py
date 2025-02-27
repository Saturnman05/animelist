from aiomysql import Error as ConnectionError, DictCursor

from fastapi import APIRouter, Depends, HTTPException

from ..database import Database
from ..utils.security import get_current_user
from ..models.anime_lists_animes import AnimeListsAnimes
from ..models.user import User

router = APIRouter()


@router.get("/")
async def get_anime_lists_animes(
    list_id: str | None = None,
    anime_id: str | None = None,
    current_user: User = Depends(get_current_user),
):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute(
                    "CALL sp_anime_lists_animes(%s, %s, %s)", (list_id, anime_id, 1)
                )
                results = await cursor.fetchall()

            if not results:
                raise HTTPException(status_code=400, detail="Animes in list not found")

            return results
    except ConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@router.post("/")
async def post_anime_lists_animes(
    anime_lists_animes: AnimeListsAnimes, current_user: User = Depends(get_current_user)
):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute(
                    "CALL sp_anime_lists_animes(%s, %s, %s)",
                    (anime_lists_animes.list_id, anime_lists_animes.anime_id, 2),
                )
            await con.commit()
            return {"message": "Post succesfully"}
    except ConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


"""
@router.put("/")
async def put_anime_lists_animes(
    anime_lists_animes: AnimeListsAnimes, current_user: User = Depends(get_current_user)
):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute(
                    "CALL sp_anime_lists_animes(%s, %s, %s)",
                    (anime_lists_animes.list_id, anime_lists_animes.anime_id, 3),
                )
            await con.commit()
            return {"message": "Put succesfully"}
    except ConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
"""


@router.delete("/")
async def delete_anime_lists_animes(
    anime_lists_animes: AnimeListsAnimes, current_user: User = Depends(get_current_user)
):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute(
                    "CALL sp_anime_lists_animes(%s, %s, %s)",
                    (anime_lists_animes.list_id, anime_lists_animes.anime_id, 4),
                )
            await con.commit()
            return {"message": "Delete succesfully"}
    except ConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
