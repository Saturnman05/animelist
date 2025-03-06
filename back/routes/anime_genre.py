from aiomysql import Error as ConnectionError, DictCursor

from fastapi import APIRouter, Depends, HTTPException

from database import Database
from utils.security import get_current_user
from models.anime_genre import AnimeGenre

router = APIRouter()


@router.get("/")
async def get_api_genre(
    anime_id: str | None = None,
    genre_id: str | None = None,
    current_user: str = Depends(get_current_user),
):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute(
                    "CALL sp_anime_genres(%s, %s, %s)", (anime_id, genre_id, 1)
                )
                results = await cursor.fetchall()

            if not results:
                raise HTTPException(status_code=400, detail="Anime genres not found")

            return results
    except ConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
    finally:
        con.close()


@router.post("/")
async def post_api_genre(
    anime_genre: AnimeGenre,
    current_user: str = Depends(get_current_user),
):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute(
                    "CALL sp_anime_genres(%s, %s, %s)",
                    (anime_genre.anime_id, anime_genre.genre_id, 2),
                )
            await con.commit()

            return {"message": "Genre added to anime succesfully"}
    except ConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


"""
@router.put("/")
async def put_api_genre(
    anime_genre: AnimeGenre,
    current_user: str = Depends(get_current_user),
):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute(
                    "CALL sp_anime_genres(%s, %s, %s)",
                    (anime_genre.anime_id, anime_genre.genre_id, 3),
                )
            await con.commit()

            return {"message": "Genre added to anime succesfully"}
    except ConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
"""


@router.delete("/")
async def delete_api_genre(
    anime_genre: AnimeGenre,
    current_user: str = Depends(get_current_user),
):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute(
                    "CALL sp_anime_genres(%s, %s, %s)",
                    (anime_genre.anime_id, anime_genre.genre_id, 4),
                )
            await con.commit()

            return {"message": "Genre eliminated from anime succesfully"}
    except ConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
