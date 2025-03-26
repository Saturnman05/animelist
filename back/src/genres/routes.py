from fastapi import APIRouter, Depends

from .models import GenreCreate, GenreUpdate
from .service import GenreService
from shared.security import get_current_user

router = APIRouter()


@router.get("/")
async def get_genres(genre_name: str | None = None):
    return await GenreService.get_all_genres(genre_name)


@router.get("/{genre_id}")
async def get_genre(genre_id: str):
    return await GenreService.get_genre_by_id(genre_id)


@router.post("/")
async def post_genre(genre: GenreCreate, _: str = Depends(get_current_user)):
    return await GenreService.create_genre(genre)


@router.put("/")
async def put_genre(genre: GenreUpdate, _: str = Depends(get_current_user)):
    return await GenreService.update_genre(genre)


@router.delete("/{genre_id}")
async def delete_genre(genre_id: str, _: str = Depends(get_current_user)):
    return await GenreService.delete_genre(genre_id)
