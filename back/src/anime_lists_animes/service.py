from aiomysql import Error as ConnectionError, DictCursor
from fastapi import HTTPException

from .models import AnimeListsAnimes
from shared.database import Database


class AnimeListsAnimesService:
    @staticmethod
    async def get_all_anime_list_animes(list_id: str | None, anime_id: str | None):
        try:
            async with await Database.get_connection() as con:
                async with con.cursor(DictCursor) as cursor:
                    await cursor.execute(
                        "CALL sp_anime_lists_animes(%s, %s, %s)",
                        (list_id, anime_id, 1),
                    )
                    results = await cursor.fetchall()

                if not results:
                    raise HTTPException(
                        status_code=400, detail="Animes in list not found"
                    )

                return results
        except ConnectionError as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")

    @staticmethod
    async def create_anime_list_animes(anime_lists_animes: AnimeListsAnimes):
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

    @staticmethod
    async def delete_anime_list_anime(anime_lists_animes: AnimeListsAnimes):
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
