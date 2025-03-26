from aiomysql import Error as ConnectionError, DictCursor

from fastapi import APIRouter, HTTPException, Depends

from .models import GenreCreate, GenreUpdate
from shared.database import Database
from shared.security import get_current_user

router = APIRouter()


@router.get("/")
async def get_genres(genre_name: str | None = None):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute("CALL sp_genres(NULL, %s, %s)", (genre_name, 1))
                results = await cursor.fetchall()

            if not results:
                raise HTTPException(status_code=400, detail="Genres not found")

            return results
    except ConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@router.get("/{genre_id}")
async def get_genre(genre_id: str):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute("CALL sp_genres(%s, NULL, %s)", (genre_id, 2))
                results = await cursor.fetchone()

            if not results:
                raise HTTPException(status_code=400, detail="Genres not found")

            return results
    except ConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@router.post("/")
async def post_genre(genre: GenreCreate, current_user: str = Depends(get_current_user)):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute("CALL sp_genres(NULL, %s, %s)", (genre.name, 3))
            await con.commit()
            return {"message": "Genre created successfully"}
    except ConnectionError as e:
        HTTPException(status_code=500, detail=f"Error: {e}")


@router.put("/")
async def put_genre(genre: GenreUpdate, current_user: str = Depends(get_current_user)):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute(
                    "CALL sp_genres(%s, %s, %s)", (genre.genre_id, genre.name, 4)
                )
            await con.commit()
            return {"message": "Genre updated successfully"}
    except ConnectionError as e:
        HTTPException(status_code=500, detail=f"Error: {e}")


@router.delete("/{genre_id}")
async def delete_genre(genre_id, current_user: str = Depends(get_current_user)):
    try:
        async with await Database.get_connection() as con:
            async with con.cursor(DictCursor) as cursor:
                await cursor.execute("CALL sp_genres(%s, NULL, %s)", (genre_id, 5))
            await con.commit()
            return {"message": "Genre deleted successfully"}
    except ConnectionError as e:
        HTTPException(status_code=500, detail=f"Error: {e}")
