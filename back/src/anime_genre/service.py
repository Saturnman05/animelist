from aiomysql import Error as ConnectionError, DictCursor
from fastapi import APIRouter, Depends, HTTPException

from shared.database import Database
from shared.security import get_current_user
from .models import AnimeGenre


class AnimeGenreService:
    @staticmethod
    async def get_all_anime_genres(anime_id: str | None, genre_id: str | None):
        try:
            async with await Database.get_connection() as con:
                async with con.cursor(DictCursor) as cursor:
                    await cursor.execute(
                        "CALL sp_anime_genres(%s, %s, %s)", (anime_id, genre_id, 1)
                    )
                    results = await cursor.fetchall()

                if not results:
                    raise HTTPException(
                        status_code=400, detail="Anime genres not found"
                    )

                return results
        except ConnectionError as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")

    @staticmethod
    async def create_anime_genre(anime_genre: AnimeGenre):
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

    @staticmethod
    async def delete_anime_genre(anime_genre: AnimeGenre):
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
