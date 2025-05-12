from aiomysql import Error as ConnectionError, DictCursor
from fastapi import HTTPException

from .models import AnimeListCreate, AnimeListUpdate
from src.shared.database import Database
from src.users.models import User


class AnimeListService:
    @staticmethod
    async def get_all_anime_lists():
        try:
            async with await Database.get_connection() as con:
                async with con.cursor(DictCursor) as cursor:
                    await cursor.execute(
                        "CALL sp_anime_lists(NULL, NULL, NULL, %s)", (1,)
                    )
                    results = await cursor.fetchall()

                if not results:
                    raise HTTPException(status_code=400, detail="Anime lists not found")

                return results
        except ConnectionError as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")

    @staticmethod
    async def get_anime_list_by_id(list_id: str):
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

    @staticmethod
    async def create_anime_list(anime_list: AnimeListCreate, user: User):
        try:
            async with await Database.get_connection() as con:
                async with con.cursor(DictCursor) as cursor:
                    await cursor.execute(
                        "CALL sp_anime_lists(NULL, %s, %s, %s)",
                        (anime_list.list_name, user.user_id, 3),
                    )
                await con.commit()
                return {"message": "Anime list created successfully"}
        except ConnectionError as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")

    @staticmethod
    async def update_anime_list(anime_list: AnimeListUpdate, user: User):
        try:
            async with await Database.get_connection() as con:
                async with con.cursor(DictCursor) as cursor:
                    await cursor.execute(
                        "CALL sp_anime_lists(%s, %s, %s, %s)",
                        (anime_list.list_id, anime_list.name, user.user_id, 4),
                    )
                await con.commit()
                return {"message": "Anime list updated successfully"}
        except ConnectionError as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")

    @staticmethod
    async def delete_anime_list(list_id: str, user: User):
        try:
            async with await Database.get_connection() as con:
                async with con.cursor(DictCursor) as cursor:
                    await cursor.execute(
                        "CALL sp_anime_lists(%s, NULL, %s, %s)",
                        (list_id, user.user_id, 5),
                    )
                await con.commit()
                return {"message": "Anime list deleted successfully"}
        except ConnectionError as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")
