from aiomysql import Error as ConnectionError, DictCursor

from fastapi import APIRouter, Depends, HTTPException

from database import Database
from utils.security import get_current_user
from models.anime import AnimeCreate, AnimeUpdate

router = APIRouter()


@router.get("/")
async def get_animes(
    name: str | None = None,
    amount_episodes: int | None = None,
    author: str | None = None,
):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute(
                    "CALL sp_animes(NULL, %s, %s, %s, %s)",
                    (name, amount_episodes, author, 1),
                )
                results = await cursor.fetchall()

            if not results:
                raise HTTPException(status_code=400, detail="Animes not found")

            return results
    except ConnectionError as e:
        HTTPException(status_code=500, detail=f"Error: {e}")


@router.get("/{anime_id}")
async def get_anime(anime_id: str):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute(
                    "CALL sp_animes(%s, NULL, NULL, NULL, %s)", (anime_id, 2)
                )
                result = await cursor.fetchone()

            if not result:
                raise HTTPException(status_code=400, detail="Anime not found")

            return result
    except ConnectionError as e:
        HTTPException(status_code=500, detail=f"Error: {e}")


@router.post("/")
async def post_anime(anime: AnimeCreate, current_user: str = Depends(get_current_user)):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute(
                    "CALL sp_animes(NULL, %s, %s, %s, %s)",
                    (anime.name, anime.amount_episodes, anime.author, 3),
                )
            await con.commit()
        return {"message": "Anime created successfully"}
    except ConnectionError as e:
        HTTPException(status_code=500, detail=f"Error: {e}")


@router.put("/")
async def put_anime(anime: AnimeUpdate, current_user: str = Depends(get_current_user)):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute(
                    "CALL sp_animes(%s, %s, %s, %s, %s)",
                    (
                        anime.anime_id,
                        anime.name,
                        anime.amount_episodes,
                        anime.author,
                        4,
                    ),
                )
            await con.commit()
            return {"message": "Anime updated successfully"}
    except ConnectionError as e:
        HTTPException(status_code=500, detail=f"Error: {e}")


@router.delete("/{anime_id}")
async def delete_anime(anime_id: str, current_user: str = Depends(get_current_user)):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute(
                    "CALL sp_animes(%s, NULL, NULL, NULL, %s)",
                    (anime_id, 5),
                )
            await con.commit()
            return {"message": "Anime deleted successfully"}
    except ConnectionError as e:
        HTTPException(status_code=500, detail=f"Error: {e}")
