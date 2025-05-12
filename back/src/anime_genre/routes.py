from fastapi import APIRouter, Depends

from .models import AnimeGenre
from .service import AnimeGenreService
from src.shared.security import get_current_user

router = APIRouter()


@router.get("/")
async def get_anime_genre(
    anime_id: str | None = None,
    genre_id: str | None = None,
    _: str = Depends(get_current_user),
):
    return await AnimeGenreService.get_all_anime_genres(anime_id, genre_id)


@router.post("/")
async def post_anime_genre(
    anime_genre: AnimeGenre,
    _: str = Depends(get_current_user),
):
    return await AnimeGenreService.create_anime_genre(anime_genre)


@router.delete("/")
async def delete_anime_genre(
    anime_genre: AnimeGenre,
    _: str = Depends(get_current_user),
):
    return await AnimeGenreService.delete_anime_genre(anime_genre)
